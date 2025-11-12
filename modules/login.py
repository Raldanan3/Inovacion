# pages/login.py
import streamlit as st
from user_manager import UserManager

def login_page():
    st.title("📚 Plataforma de Cálculo Diferencial")
    
    tab1, tab2 = st.tabs(["Iniciar Sesión", "Registrarse"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            login_button = st.form_submit_button("Iniciar Sesión")
            
            if login_button:
                user_manager = UserManager()
                if user_manager.login(username, password):
                    st.success(f"¡Bienvenido, {username}!")
                    st.rerun()
                else:
                    st.error("Usuario o contraseña incorrectos")
    
    with tab2:
        with st.form("register_form"):
            new_username = st.text_input("Nuevo Usuario")
            new_password = st.text_input("Nueva Contraseña", type="password")
            confirm_password = st.text_input("Confirmar Contraseña", type="password")
            is_admin = st.checkbox("Es profesor")
            register_button = st.form_submit_button("Registrarse")
            
            if register_button:
                if new_password != confirm_password:
                    st.error("Las contraseñas no coinciden")
                else:
                    user_manager = UserManager()
                    success, message = user_manager.create_user(new_username, new_password, is_admin)
                    if success:
                        st.success(message)
                    else:
                        st.error(message)