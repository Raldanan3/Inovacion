# progress.py
import streamlit as st
import plotly.express as px
from user_manager import UserManager
from content_manager import CONTENIDO_CURSO

def progress_page():
    st.title("📊 Progreso y Reportes")
    
    user_manager = UserManager()
    usuario_actual = user_manager.get_current_user()
    progreso = st.session_state.user_progress.get(usuario_actual, {})
    puntuaciones = st.session_state.user_scores.get(usuario_actual, {})
    
    # Gráfico de progreso por bloques
    st.subheader("Progreso por Lecciones")
    bloques = list(CONTENIDO_CURSO.keys())
    bloque_nombres = [f"Lección {b}" for b in bloques]
    progreso_porcentaje = []
    
    for bloque in bloques:
        ejercicios_resueltos = len(progreso.get("ejercicios_resueltos", {}).get(bloque, []))
        total_ejercicios = len(CONTENIDO_CURSO[bloque]["ejercicios"])
        progreso_porcentaje.append(ejercicios_resueltos / total_ejercicios if total_ejercicios > 0 else 0)
    
    fig = px.bar(
        x=bloque_nombres,
        y=progreso_porcentaje,
        title="Progreso por Lección",
        labels={'x': 'Lecciones', 'y': 'Porcentaje de Completación'},
        color=progreso_porcentaje,
        color_continuous_scale=["red", "yellow", "green"]
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Detalle del progreso
    st.subheader("Detalle por Lección")
    for bloque_id, bloque_info in CONTENIDO_CURSO.items():
        with st.expander(f"Lección {bloque_id}: {bloque_info['titulo']}"):
            ejercicios_resueltos = len(progreso.get("ejercicios_resueltos", {}).get(bloque_id, []))
            total_ejercicios = len(bloque_info['ejercicios'])
            porcentaje = (ejercicios_resueltos / total_ejercicios) * 100 if total_ejercicios > 0 else 0
            
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**Ejercicios completados:** {ejercicios_resueltos}/{total_ejercicios}")
                st.progress(porcentaje / 100)
            with col2:
                st.write(f"**Porcentaje:** {porcentaje:.1f}%")
            with col3:
                if bloque_id in progreso.get("bloques_completados", []):
                    st.success("✅ Completado")
                else:
                    st.warning("⏳ En progreso")
            
            # Lista de ejercicios
            st.write("**Ejercicios:**")
            for ej_id, ej_info in bloque_info['ejercicios'].items():
                estado = "✅" if ej_id in progreso.get("ejercicios_resueltos", {}).get(bloque_id, []) else "❌"
                st.write(f"{estado} {ej_info['pregunta']} - {ej_info['puntaje']} pts")
    
    # Puntuaciones de evaluaciones
    if puntuaciones.get("quices") or puntuaciones.get("tareas") or puntuaciones.get("examenes"):
        st.subheader("Calificaciones")
        
        # Quices
        if puntuaciones.get("quices"):
            st.write("**Quices:**")
            for quiz, info in puntuaciones["quices"].items():
                st.write(f"- {quiz}: {info['puntaje']}/{info['max_puntaje']} ({info['fecha']})")
        
        # Tareas
        if puntuaciones.get("tareas"):
            st.write("**Tareas:**")
            for tarea, info in puntuaciones["tareas"].items():
                st.write(f"- {tarea}: {info['puntaje']}/{info['max_puntaje']} ({info['fecha']})")
        
        # Exámenes
        if puntuaciones.get("examenes"):
            st.write("**Exámenes:**")
            for examen, info in puntuaciones["examenes"].items():
                st.write(f"- {examen}: {info['puntaje']}/{info['max_puntaje']} ({info['fecha']})")