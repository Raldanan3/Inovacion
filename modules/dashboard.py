# modules/dashboard.py
import streamlit as st
from user_manager import UserManager
from content_manager import CONTENIDO_CURSO

def dashboard_page():
    st.title("🏠 Dashboard de Cálculo Diferencial")
    
    user_manager = UserManager()
    usuario_actual = user_manager.get_current_user()
    progreso = st.session_state.user_progress.get(usuario_actual, {})
    
    # Mostrar progreso general
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bloques_completados = len(progreso.get("bloques_completados", []))
        st.metric("Lecciones Completadas", f"{bloques_completados}/5")
    
    with col2:
        ejercicios_resueltos = sum(len(ej) for ej in progreso.get("ejercicios_resueltos", {}).values())
        st.metric("Ejercicios Resueltos", ejercicios_resueltos)
    
    with col3:
        puntaje_total = progreso.get("puntaje_total", 0)
        st.metric("Puntaje Total", puntaje_total)
    
    with col4:
        porcentaje_total = (bloques_completados / 5) * 100 if bloques_completados > 0 else 0
        st.metric("Progreso Total", f"{porcentaje_total:.1f}%")
    
    # Mostrar lecciones del curso
    st.subheader("📖 Lecciones del Curso")
    
    for leccion_id, leccion_info in CONTENIDO_CURSO.items():
        with st.expander(f"Lección {leccion_id}: {leccion_info['titulo']}", expanded=True):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write("**Subtemas:**")
                for subtema_id, subtema_info in leccion_info['subtemas'].items():
                    st.write(f"- {subtema_id}: {subtema_info['nombre']}")
                
                st.write("**Ejercicios:**")
                for ej_id, ej_info in leccion_info['ejercicios'].items():
                    estado = "✅" if ej_id in progreso.get("ejercicios_resueltos", {}).get(leccion_id, []) else "⏳"
                    st.write(f"- {estado} {ej_info['pregunta']} ({ej_info['puntaje']} pts)")
            
            with col2:
                leccion_completada = leccion_id in progreso.get("bloques_completados", [])
                if leccion_completada:
                    st.success("✅ Completada")
                else:
                    progreso_leccion = len(progreso.get("ejercicios_resueltos", {}).get(leccion_id, []))
                    total_ejercicios = len(leccion_info['ejercicios'])
                    st.progress(progreso_leccion / total_ejercicios if total_ejercicios > 0 else 0)
                    st.write(f"Progreso: {progreso_leccion}/{total_ejercicios}")
                
                # Botón para estudiar la lección - ESTE ES EL QUE DEBE FUNCIONAR
                if st.button("📖 Estudiar Lección", key=f"btn_{leccion_id}"):
                    st.session_state.current_bloque = leccion_id
                    st.rerun()