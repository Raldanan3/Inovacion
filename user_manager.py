# user_manager.py
import streamlit as st
from datetime import datetime

class UserManager:
    def __init__(self):
        if 'users' not in st.session_state:
            st.session_state.users = {}
        if 'current_user' not in st.session_state:
            st.session_state.current_user = None
        if 'user_roles' not in st.session_state:
            st.session_state.user_roles = {}
        if 'user_progress' not in st.session_state:
            st.session_state.user_progress = {}
        if 'user_scores' not in st.session_state:
            st.session_state.user_scores = {}
    
    def create_user(self, username, password, is_admin=False):
        if username in st.session_state.users:
            return False, "El usuario ya existe"
        
        st.session_state.users[username] = password
        st.session_state.user_roles[username] = "admin" if is_admin else "student"
        st.session_state.user_progress[username] = {
            "bloques_completados": [],
            "ejercicios_resueltos": {},
            "puntaje_total": 0
        }
        st.session_state.user_scores[username] = {
            "quices": {},
            "tareas": {},
            "examenes": {}
        }
        return True, "Usuario creado exitosamente"
    
    def login(self, username, password):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.current_user = username
            return True
        return False
    
    def logout(self):
        st.session_state.current_user = None
    
    def is_admin(self, username=None):
        if username is None:
            username = st.session_state.current_user
        return st.session_state.user_roles.get(username) == "admin"
    
    def get_current_user(self):
        return st.session_state.current_user
    
    def update_progress(self, username, bloque, ejercicio, puntaje):
        if username not in st.session_state.user_progress:
            st.session_state.user_progress[username] = {
                "bloques_completados": [],
                "ejercicios_resueltos": {},
                "puntaje_total": 0
            }
        
        if bloque not in st.session_state.user_progress[username]["ejercicios_resueltos"]:
            st.session_state.user_progress[username]["ejercicios_resueltos"][bloque] = []
        
        if ejercicio not in st.session_state.user_progress[username]["ejercicios_resueltos"][bloque]:
            st.session_state.user_progress[username]["ejercicios_resueltos"][bloque].append(ejercicio)
            st.session_state.user_progress[username]["puntaje_total"] += puntaje
            
            # Verificar si se completó el bloque
            from content_manager import CONTENIDO_CURSO
            ejercicios_bloque = CONTENIDO_CURSO[bloque]["ejercicios"]
            if len(st.session_state.user_progress[username]["ejercicios_resueltos"][bloque]) == len(ejercicios_bloque):
                if bloque not in st.session_state.user_progress[username]["bloques_completados"]:
                    st.session_state.user_progress[username]["bloques_completados"].append(bloque)
    
    def add_score(self, username, tipo, nombre, puntaje, max_puntaje=100):
        if username not in st.session_state.user_scores:
            st.session_state.user_scores[username] = {"quices": {}, "tareas": {}, "examenes": {}}
        
        st.session_state.user_scores[username][tipo][nombre] = {
            "puntaje": puntaje,
            "max_puntaje": max_puntaje,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        }