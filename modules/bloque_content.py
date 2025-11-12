# modules/bloque_content.py
import streamlit as st
from user_manager import UserManager
from content_manager import CONTENIDO_CURSO
from math_tools import MathTools

def bloque_content_page():
    leccion_id = st.session_state.get('current_bloque', '1')  # Por defecto Lección 1
    leccion_info = CONTENIDO_CURSO[leccion_id]
    
    st.title(f"Lección {leccion_id}: {leccion_info['titulo']}")
    
    # Botón para volver al dashboard
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Volver al Dashboard"):
            if 'current_bloque' in st.session_state:
                del st.session_state.current_bloque
            st.rerun()
    
    # Mostrar subtemas
    st.header("📚 Teoría y Conceptos")
    for subtema_id, subtema_info in leccion_info['subtemas'].items():
        with st.expander(f"{subtema_id}: {subtema_info['nombre']}"):
            st.markdown(subtema_info['contenido'])
            
            # Ejemplos interactivos
            if st.checkbox(f"Mostrar ejemplos interactivos - {subtema_id}", key=f"ej_{subtema_id}"):
                if leccion_id == "1" and "1.3" in subtema_id:  # Lección 1, subtema 1.3
                    st.subheader("Ejemplo: Modelo Lineal")
                    st.write("Función lineal: f(x) = mx + b")
                    col1, col2 = st.columns(2)
                    with col1:
                        m = st.slider("Pendiente (m)", -5.0, 5.0, 2.0, key=f"m_{subtema_id}")
                        b = st.slider("Intercepto (b)", -5.0, 5.0, 1.0, key=f"b_{subtema_id}")
                    with col2:
                        funcion_str = f"{m}*x + {b}"
                        math_tools = MathTools()
                        fig = math_tools.graficar_funcion(funcion_str, (-10, 10))
                        if fig:
                            st.plotly_chart(fig, use_container_width=True)
    
    # Ejercicios prácticos
    st.header("💪 Ejercicios Prácticos")
    user_manager = UserManager()
    usuario_actual = user_manager.get_current_user()
    progreso = st.session_state.user_progress.get(usuario_actual, {})
    
    for ej_id, ej_info in leccion_info['ejercicios'].items():
        with st.container():
            st.subheader(f"Ejercicio {ej_id}")
            st.write(f"**{ej_info['pregunta']}**")
            st.write(f"*Puntaje: {ej_info['puntaje']} puntos*")
            
            # Verificar si ya está resuelto
            ya_resuelto = ej_id in progreso.get("ejercicios_resueltos", {}).get(leccion_id, [])
            
            if ya_resuelto:
                st.success("✅ Ejercicio completado")
                if st.button(f"Ver solución nuevamente - {ej_id}", key=f"ver_sol_{ej_id}"):
                    st.info(f"**Solución:** {ej_info['solucion']}")
            else:
                # Campo para respuesta del estudiante
                respuesta = st.text_area(f"Tu respuesta para {ej_id}", key=f"resp_{leccion_id}_{ej_id}")
                
                col1, col2, col3 = st.columns([1, 1, 2])
                with col1:
                    if st.button("Enviar respuesta", key=f"btn_{leccion_id}_{ej_id}"):
                        # Simulación de verificación de respuesta
                        user_manager.update_progress(usuario_actual, leccion_id, ej_id, ej_info['puntaje'])
                        st.success("¡Respuesta enviada correctamente!")
                        st.rerun()
                
                with col2:
                    if st.button("Ver solución", key=f"sol_{leccion_id}_{ej_id}"):
                        st.info(f"**Solución:** {ej_info['solucion']}")
                
                with col3:
                    # Herramienta para ayudar a resolver
                    if st.button("Herramienta de ayuda", key=f"ayuda_{leccion_id}_{ej_id}"):
                        if "deriva" in ej_info['pregunta'].lower():
                            st.info("💡 Usa la calculadora de derivadas en la pestaña de Herramientas")
                        elif "gráfica" in ej_info['pregunta'].lower() or "grafica" in ej_info['pregunta'].lower():
                            st.info("💡 Usa el graficador en la pestaña de Herramientas")
                        elif "límite" in ej_info['pregunta'].lower() or "limite" in ej_info['pregunta'].lower():
                            st.info("💡 Usa la calculadora de límites en la pestaña de Herramientas")