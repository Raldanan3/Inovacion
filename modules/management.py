# management.py
import streamlit as st
import plotly.express as px
from user_manager import UserManager
from content_manager import CONTENIDO_CURSO

def management_page():
    st.title("👨‍🏫 Panel de Gestión - Profesor")
    
    user_manager = UserManager()
    if not user_manager.is_admin():
        st.error("Acceso denegado. Solo los profesores pueden acceder a esta sección.")
        return
    
    tab1, tab2, tab3, tab4 = st.tabs(["Gestión de Estudiantes", "Asignar Calificaciones", "Estadísticas del Curso", "Configuración"])
    
    with tab1:
        st.subheader("Gestión de Estudiantes")
        
        if st.session_state.users:
            st.write("**Estudiantes registrados:**")
            for username, password in st.session_state.users.items():
                if st.session_state.user_roles[username] == "student":
                    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
                    with col1:
                        st.write(f"**{username}**")
                    with col2:
                        progreso = st.session_state.user_progress.get(username, {})
                        bloques_comp = len(progreso.get("bloques_completados", []))
                        st.write(f"Lecciones completadas: {bloques_comp}/5")
                    with col3:
                        if st.button("Ver progreso", key=f"ver_{username}"):
                            st.session_state.estudiante_seleccionado = username
                    with col4:
                        if st.button("Eliminar", key=f"del_{username}"):
                            del st.session_state.users[username]
                            del st.session_state.user_roles[username]
                            if username in st.session_state.user_progress:
                                del st.session_state.user_progress[username]
                            st.success(f"Estudiante {username} eliminado")
                            st.rerun()
        else:
            st.info("No hay estudiantes registrados")
    
    with tab2:
        st.subheader("Asignar Calificaciones")
        
        if st.session_state.users:
            estudiantes = [u for u in st.session_state.users.keys() if st.session_state.user_roles[u] == "student"]
            if estudiantes:
                estudiante = st.selectbox("Seleccionar estudiante:", estudiantes)
                tipo_eval = st.selectbox("Tipo de evaluación:", ["quices", "tareas", "examenes"])
                nombre_eval = st.text_input("Nombre de la evaluación:")
                puntaje = st.number_input("Puntaje obtenido:", min_value=0, max_value=100, value=80)
                max_puntaje = st.number_input("Puntaje máximo:", min_value=1, max_value=100, value=100)
                
                if st.button("Asignar Calificación"):
                    user_manager.add_score(estudiante, tipo_eval, nombre_eval, puntaje, max_puntaje)
                    st.success(f"Calificación asignada a {estudiante}")
            else:
                st.info("No hay estudiantes para asignar calificaciones")
        else:
            st.info("No hay estudiantes para asignar calificaciones")
    
    with tab3:
        st.subheader("Estadísticas del Curso")
        
        if st.session_state.users:
            estudiantes = [u for u in st.session_state.users.keys() if st.session_state.user_roles[u] == "student"]
            
            if estudiantes:
                # Estadísticas de progreso
                progreso_promedio = []
                for estudiante in estudiantes:
                    progreso = st.session_state.user_progress.get(estudiante, {})
                    bloques_comp = len(progreso.get("bloques_completados", []))
                    progreso_promedio.append((bloques_comp / 5) * 100)
                
                if progreso_promedio:
                    promedio = sum(progreso_promedio) / len(progreso_promedio)
                    st.metric("Progreso Promedio", f"{promedio:.1f}%")
                    
                    # Gráfico de distribución
                    fig = px.histogram(x=progreso_promedio, 
                                     title="Distribución del Progreso de Estudiantes",
                                     labels={'x': 'Porcentaje de Progreso', 'y': 'Número de Estudiantes'})
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No hay estudiantes en el curso")
        else:
            st.info("No hay usuarios registrados")
    
    with tab4:
        st.subheader("Configuración del Curso")
        
        st.write("**Lecciones del curso:**")
        for bloque_id, bloque_info in CONTENIDO_CURSO.items():
            if st.button(f"Editar Lección {bloque_id}", key=f"edit_{bloque_id}"):
                st.info("Funcionalidad de edición en desarrollo")
        
        st.write("**Configuración general:**")
        if st.button("Restablecer Progreso del Curso"):
            for username in st.session_state.users:
                if st.session_state.user_roles[username] == "student":
                    st.session_state.user_progress[username] = {
                        "bloques_completados": [],
                        "ejercicios_resueltos": {},
                        "puntaje_total": 0
                    }
            st.success("Progreso del curso restablecido")