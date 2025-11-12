#streamlit run main.py

# main.py
import streamlit as st
from user_manager import UserManager

# Configuración de la página
st.set_page_config(
    page_title="Plataforma de Cálculo Diferencial",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None  # Esto desactiva el menú superior
)

def main_app():
    user_manager = UserManager()
    
    # Solo un menú lateral
    st.sidebar.title("📚 Plataforma de Cálculo")
    
    # Información del usuario
    st.sidebar.write(f"**Usuario:** {user_manager.get_current_user()}")
    st.sidebar.write(f"**Rol:** {'Profesor' if user_manager.is_admin() else 'Estudiante'}")
    
    # Navegación principal - SOLO UN MENÚ
    if user_manager.is_admin():
        app_mode = st.sidebar.selectbox(
            "Navegación",
            ["Dashboard", "Contenido", "Herramientas", "Progreso", "Gestión"]
        )
    else:
        app_mode = st.sidebar.selectbox(
            "Navegación",
            ["Dashboard", "Contenido", "Herramientas", "Progreso"]
        )
    
    # Información rápida del progreso en sidebar (solo estudiantes)
    if not user_manager.is_admin():
        usuario_actual = user_manager.get_current_user()
        progreso = st.session_state.user_progress.get(usuario_actual, {})
        bloques_completados = len(progreso.get("bloques_completados", []))
        st.sidebar.progress(bloques_completados / 5)
        st.sidebar.write(f"**Progreso:** {bloques_completados}/5 bloques")
    
    # Botón de cerrar sesión
    if st.sidebar.button("🚪 Cerrar Sesión"):
        user_manager.logout()
        st.rerun()
    
    # Navegación basada en la selección del menú lateral
    if app_mode == "Dashboard":
        from modules.dashboard import dashboard_page
        dashboard_page()
    elif app_mode == "Contenido":
        if 'current_bloque' in st.session_state:
            from modules.bloque_content import bloque_content_page
            bloque_content_page()
        else:
            from modules.dashboard import dashboard_page
            st.info("Selecciona un bloque desde el Dashboard para ver su contenido")
            dashboard_page()
    elif app_mode == "Herramientas":
        from modules.tools import tools_page
        tools_page()
    elif app_mode == "Progreso":
        from modules.progress import progress_page
        progress_page()
    elif app_mode == "Gestión" and user_manager.is_admin():
        from modules.management import management_page
        management_page()

def main():
    user_manager = UserManager()
    if user_manager.get_current_user() is None:
        from modules.login import login_page
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()