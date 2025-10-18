#streamlit run app.py
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Curso de Costos - DeciCost",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión
def initialize_session_state():
    if 'current_section' not in st.session_state:
        st.session_state.current_section = "Inicio"
    if 'current_lesson' not in st.session_state:
        st.session_state.current_lesson = None
    if 'lesson_progress' not in st.session_state:
        st.session_state.lesson_progress = {
            "Lección 1": 0,
            "Lección 2": 0,
            "Lección 3": 0,
            "Lección 4": 0,
            "Lección 5": 0
        }
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            "nombre": "",
            "email": "",
            "institucion": "",
            "experiencia": "Principiante",
            "notificaciones": True,
            "progreso_detallado": True,
            "meta_estudio": 5
        }
    if 'exercise_answers' not in st.session_state:
        st.session_state.exercise_answers = {}
    if 'exercise_results' not in st.session_state:
        st.session_state.exercise_results = {}
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False

initialize_session_state()

# Datos del curso
course_data = {
    "Lección 1": {
        "title": "Fundamentos de Costos",
        "description": "Introducción a los conceptos básicos de costos para la toma de decisiones",
        "content": {
            "introduccion": """
            # Lección 1: Fundamentos de Costos
            
            En esta lección aprenderás los conceptos fundamentales de los costos y su importancia 
            en la toma de decisiones empresariales. Comprenderás cómo los costos afectan la 
            rentabilidad de una organización y cómo utilizarlos para mejorar la gestión financiera.
            
            ## Objetivos de aprendizaje:
            - Identificar los elementos del balance y estado de resultados
            - Diferenciar entre costos fijos y variables
            - Calcular la contribución marginal
            - Determinar el punto de equilibrio
            """,
            "teoria": [
                {
                    "titulo": "Elementos del Balance y Estado de Resultados",
                    "contenido": """
                    ### Elementos del Balance y Estado de Resultados
                    
                    El balance general y el estado de resultados son herramientas fundamentales 
                    para comprender la situación financiera de una empresa.
                    
                    **Balance General:**
                    - Activos: Lo que la empresa posee
                    - Pasivos: Lo que la empresa debe
                    - Capital: La inversión de los propietarios
                    
                    **Estado de Resultados:**
                    - Ingresos: Lo que la empresa gana
                    - Costos y Gastos: Lo que la empresa gasta
                    - Utilidad o Pérdida: El resultado de las operaciones
                    
                    Estos documentos financieros son esenciales para analizar la salud financiera 
                    de una organización y tomar decisiones informadas.
                    """,
                    "video": "https://www.youtube.com/watch?v=LPGIgRqMpOs"
                },
                {
                    "titulo": "Costos Fijos y Variables",
                    "contenido": """
                    ### Costos Fijos y Variables
                    
                    **Costos Fijos:** Son aquellos que no cambian con el volumen de producción.
                    Ejemplos: alquiler, salarios administrativos, seguros.
                    
                    **Costos Variables:** Cambian proporcionalmente con el volumen de producción.
                    Ejemplos: materias primas, comisiones por ventas, empaques.
                    
                    **Contribución Marginal:** Es la diferencia entre el precio de venta y 
                    los costos variables unitarios. Representa cuánto contribuye cada unidad 
                    vendida a cubrir los costos fijos y generar utilidad.
                    
                    Fórmula: Contribución Marginal = Precio de Venta - Costo Variable Unitario
                    """,
                    "video": "https://www.youtube.com/watch?v=evboZvaG8iI"
                },
                {
                    "titulo": "Punto de Equilibrio",
                    "contenido": """
                    ### Punto de Equilibrio
                    
                    El punto de equilibrio es el nivel de ventas en el que los ingresos totales 
                    igualan a los costos totales, resultando en una utilidad de cero.
                    
                    **Fórmula:**
                    Punto de Equilibrio (unidades) = Costos Fijos / (Precio de Venta - Costo Variable Unitario)
                    
                    **Análisis Marginal:** Técnica que estudia cómo cambian los costos e ingresos 
                    cuando se toman decisiones sobre producción y ventas.
                    
                    El punto de equilibrio es una herramienta fundamental para la planificación 
                    financiera y la toma de decisiones sobre precios y volúmenes de producción.
                    """,
                    "video": "https://www.youtube.com/watch?v=MBMIN21lrYI"
                }
            ],
            "ejercicios": [
                {
                    "pregunta": "¿Cuál de los siguientes es un ejemplo de costo fijo?",
                    "opciones": ["Materia prima", "Alquiler de la fábrica", "Comisiones por ventas", "Material de empaque"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "La contribución marginal se calcula como:",
                    "opciones": [
                        "Precio de venta - Costos fijos",
                        "Precio de venta - Costos variables unitarios", 
                        "Ingresos totales - Costos totales",
                        "Costos fijos / Costos variables"
                    ],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "El punto de equilibrio ocurre cuando:",
                    "opciones": [
                        "Los ingresos son máximos",
                        "Los costos variables son mínimos",
                        "Los ingresos totales igualan a los costos totales",
                        "Se vende la primera unidad"
                    ],
                    "respuesta_correcta": 2
                }
            ]
        }
    },
    "Lección 2": {
        "title": "Análisis e Interpretación de Información Financiera",
        "description": "Métodos para analizar e interpretar estados financieros",
        "content": {
            "introduccion": """
            # Lección 2: Análisis e Interpretación de Información Financiera
            
            En esta lección aprenderás a analizar e interpretar la información financiera 
            para tomar decisiones empresariales informadas.
            
            ## Temas que cubriremos:
            - Estados financieros básicos
            - Métodos de análisis financiero
            - Razones financieras de liquidez y solvencia
            - Razones de rentabilidad y modelo DuPont
            
            *Contenido en desarrollo...*
            """
        }
    },
    "Lección 3": {
        "title": "Administración de Capital de Trabajo",
        "description": "Gestión eficiente del capital de trabajo en la organización",
        "content": {
            "introduccion": """
            # Lección 3: Administración de Capital de Trabajo
            
            Esta lección cubre los elementos necesarios para una buena administración 
            del capital de trabajo en una organización.
            
            ## Temas que cubriremos:
            - Administración de efectivo e inversiones
            - Estado de cambios en la situación financiera
            - Administración de cuentas por cobrar
            - Administración de inventarios
            - Administración de pasivos de corto plazo
            
            *Contenido en desarrollo...*
            """
        }
    },
    "Lección 4": {
        "title": "Planeación y Presupuestos",
        "description": "Desarrollo de presupuestos y planeación financiera",
        "content": {
            "introduccion": """
            # Lección 4: Planeación y Presupuestos
            
            Aprenderás a desarrollar un presupuesto maestro detallado que parta del 
            pronóstico de ingresos.
            
            ## Temas que cubriremos:
            - Evaluación de antecedentes y plan de negocios
            - Pronóstico de ingresos
            - Estructuración del estado de resultados
            - Presupuesto maestro
            
            *Contenido en desarrollo...*
            """
        }
    },
    "Lección 5": {
        "title": "Evaluación de Proyectos de Inversión",
        "description": "Herramientas para evaluar la viabilidad de proyectos de inversión",
        "content": {
            "introduccion": """
            # Lección 5: Evaluación de Proyectos de Inversión
            
            Esta lección te enseñará herramientas financieras para reconocer el valor 
            del dinero en el tiempo y evaluar proyectos de inversión.
            
            ## Temas que cubriremos:
            - Estudios previos (mercado, operación, técnico)
            - Definición de flujos de efectivo
            - Valor del dinero en el tiempo (VPN y TIR)
            - Evaluación financiera
            - Costo ponderado de capital (WACC) y valor económico agregado (EVA)
            
            *Contenido en desarrollo...*
            """
        }
    }
}

# Barra lateral simplificada
with st.sidebar:
    st.title("📊 Curso de Costos")
    
    # Navegación principal
    st.header("Navegación")
    
    # Botones de navegación principal
    if st.button("🏠 Inicio"):
        st.session_state.current_section = "Inicio"
        st.session_state.current_lesson = None
        st.rerun()
    
    if st.button("📚 Lecciones"):
        st.session_state.current_section = "Lecciones"
        st.session_state.current_lesson = None
        st.rerun()
    
    if st.button("📈 Mi Progreso"):
        st.session_state.current_section = "Mi Progreso"
        st.session_state.current_lesson = None
        st.rerun()
    
    if st.button("👤 Mi Perfil"):
        st.session_state.current_section = "Mi Perfil"
        st.session_state.current_lesson = None
        st.rerun()
    
    # Mostrar lección actual si estamos en una lección
    if st.session_state.current_lesson:
        st.info(f"Lección actual: {st.session_state.current_lesson}")

# Función para mostrar página de inicio
def show_home():
    st.title("Curso de Costos para la Toma de Decisiones")
    st.subheader("DeciCost")
    
    st.markdown("""
    ## Bienvenido al curso
    
    Este curso te proporcionará las herramientas necesarias para comprender y 
    aplicar los conceptos de costos en la toma de decisiones empresariales.
    
    ### ¿Cómo funciona el curso?
    
    1. **Navega por las lecciones** usando el menú de la izquierda
    2. **Estudia el contenido teórico** en cada lección
    3. **Completa los ejercicios** para reforzar tu aprendizaje
    4. **Revisa tu progreso** en la sección "Mi Progreso"
    
    ### Temario del curso:
    """)
    
    for leccion, info in course_data.items():
        st.write(f"**{leccion}:** {info['title']} - {info['description']}")
    
    st.info("💡 **Consejo:** Comienza con la Lección 1 para familiarizarte con los conceptos básicos.")

# Función para mostrar lista de lecciones
def show_lessons_list():
    st.title("Lecciones del Curso")
    st.write("Selecciona una lección para comenzar a aprender:")
    
    for i, (leccion, info) in enumerate(course_data.items(), 1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(f"{leccion}: {info['title']}")
            st.write(info['description'])
            progreso = st.session_state.lesson_progress[leccion]
            st.progress(progreso / 100)
            st.write(f"Progreso: {progreso}%")
        with col2:
            if st.button(f"Estudiar ▶️", key=f"btn_{leccion}"):
                st.session_state.current_lesson = leccion
                st.session_state.current_section = "Lección Detalle"
                st.rerun()
        
        if i < len(course_data):
            st.markdown("---")

# Función para mostrar perfil
def show_profile():
    st.title("Mi Perfil")
    
    with st.form("profile_form"):
        st.subheader("Información Personal")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nombre = st.text_input("Nombre completo", value=st.session_state.user_profile["nombre"])
            email = st.text_input("Correo electrónico", value=st.session_state.user_profile["email"])
            institucion = st.text_input("Institución/Empresa", value=st.session_state.user_profile["institucion"])
            
        with col2:
            experiencia = st.selectbox(
                "Nivel de experiencia", 
                ["Principiante", "Intermedio", "Avanzado"],
                index=["Principiante", "Intermedio", "Avanzado"].index(st.session_state.user_profile["experiencia"])
            )
        
        st.subheader("Preferencias")
        notificaciones = st.checkbox("Recibir notificaciones por correo", value=st.session_state.user_profile["notificaciones"])
        progreso_detallado = st.checkbox("Mostrar progreso detallado", value=st.session_state.user_profile["progreso_detallado"])
        meta_estudio = st.slider("Meta de estudio semanal (horas)", 1, 20, st.session_state.user_profile["meta_estudio"])
        
        # Botón para guardar
        guardar_cambios = st.form_submit_button("Guardar cambios")
        
        if guardar_cambios:
            # Actualizar perfil en session_state
            st.session_state.user_profile = {
                "nombre": nombre,
                "email": email,
                "institucion": institucion,
                "experiencia": experiencia,
                "notificaciones": notificaciones,
                "progreso_detallado": progreso_detallado,
                "meta_estudio": meta_estudio
            }
            st.success("¡Perfil actualizado correctamente!")

# Función para mostrar avance
def show_progress():
    st.title("Mi Progreso")
    
    # Mostrar progreso general
    st.subheader("Progreso General del Curso")
    total_lecciones = len(st.session_state.lesson_progress)
    lecciones_completadas = sum(1 for prog in st.session_state.lesson_progress.values() if prog > 0)
    progreso_general = (lecciones_completadas / total_lecciones) * 100
    
    st.progress(progreso_general / 100)
    st.write(f"**{lecciones_completadas} de {total_lecciones} lecciones iniciadas** ({progreso_general:.1f}%)")
    
    # Mostrar progreso por lección
    st.subheader("Progreso por Lección")
    for leccion, progreso in st.session_state.lesson_progress.items():
        col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
        with col1:
            st.write(f"**{leccion}** - {course_data[leccion]['title']}")
        with col2:
            st.progress(progreso / 100)
        with col3:
            st.write(f"{progreso}%")
        with col4:
            if st.button("Ver", key=f"ver_{leccion}"):
                st.session_state.current_lesson = leccion
                st.session_state.current_section = "Lección Detalle"
                st.rerun()
    
    st.info("📈 Tu progreso se actualizará automáticamente conforme completes las lecciones y ejercicios.")

# Función para mostrar lecciones
def show_lesson(lesson_name):
    leccion = course_data[lesson_name]
    
    # Botón para volver a la lista de lecciones
    if st.button("← Volver a la lista de lecciones"):
        st.session_state.current_section = "Lecciones"
        st.session_state.current_lesson = None
        st.rerun()
    
    st.title(leccion["title"])
    st.write(leccion["description"])
    
    # Para la Lección 1, mostrar contenido completo
    if lesson_name == "Lección 1":
        # Introducción
        st.markdown(leccion["content"]["introduccion"])
        
        # Teoría con videos
        st.header("Contenido Teórico")
        for i, seccion in enumerate(leccion["content"]["teoria"]):
            st.subheader(seccion["titulo"])
            st.markdown(seccion["contenido"])
            
            # Mostrar video si está disponible
            if seccion.get("video"):
                st.video(seccion["video"])
            
            if i < len(leccion["content"]["teoria"]) - 1:
                st.markdown("---")
        
        # Ejercicios
        st.header("Ejercicios de Práctica")
        st.info("Responde las siguientes preguntas para verificar tu comprensión del tema.")
        
        # Inicializar respuestas si no existen
        if lesson_name not in st.session_state.exercise_answers:
            st.session_state.exercise_answers[lesson_name] = [None] * len(leccion["content"]["ejercicios"])
        
        # Mostrar preguntas
        respuestas_usuario = []
        for i, ejercicio in enumerate(leccion["content"]["ejercicios"]):
            st.subheader(f"Pregunta {i+1}")
            st.write(ejercicio["pregunta"])
            
            # Usar key única para cada pregunta
            respuesta = st.radio(
                f"Selecciona tu respuesta:",
                ejercicio["opciones"],
                key=f"{lesson_name}_pregunta_{i}",
                index=st.session_state.exercise_answers[lesson_name][i] if st.session_state.exercise_answers[lesson_name][i] is not None else 0
            )
            
            # Guardar respuesta
            if respuesta:
                respuesta_index = ejercicio["opciones"].index(respuesta)
                st.session_state.exercise_answers[lesson_name][i] = respuesta_index
                respuestas_usuario.append(respuesta_index)
            
            if i < len(leccion["content"]["ejercicios"]) - 1:
                st.markdown("---")
        
        # Botón para calcular resultado
        if st.button("Calcular mi resultado", key="calcular_resultado"):
            respuestas_correctas = 0
            resultados = []
            
            for i, (ejercicio, respuesta_index) in enumerate(zip(leccion["content"]["ejercicios"], respuestas_usuario)):
                # Verificar respuesta
                es_correcta = respuesta_index == ejercicio["respuesta_correcta"]
                if es_correcta:
                    respuestas_correctas += 1
                
                resultados.append({
                    "pregunta": ejercicio["pregunta"],
                    "respuesta_usuario": ejercicio["opciones"][respuesta_index] if respuesta_index is not None else "No respondida",
                    "respuesta_correcta": ejercicio["opciones"][ejercicio["respuesta_correcta"]],
                    "es_correcta": es_correcta
                })
            
            # Guardar resultados
            st.session_state.exercise_results[lesson_name] = resultados
            st.session_state.show_results = True
            
            # Mostrar resultado
            porcentaje = (respuestas_correctas / len(leccion["content"]["ejercicios"])) * 100
            st.subheader("Resultado")
            st.write(f"Has respondido correctamente {respuestas_correctas} de {len(leccion['content']['ejercicios'])} preguntas ({porcentaje:.1f}%)")
            
            # Mostrar retroalimentación detallada
            st.subheader("Retroalimentación:")
            for i, resultado in enumerate(resultados):
                st.write(f"**Pregunta {i+1}:** {resultado['pregunta']}")
                if resultado['es_correcta']:
                    st.success(f"✅ Tu respuesta: '{resultado['respuesta_usuario']}' - Correcta")
                else:
                    st.error(f"❌ Tu respuesta: '{resultado['respuesta_usuario']}' - La respuesta correcta es: '{resultado['respuesta_correcta']}'")
                st.write("---")
            
            # Actualizar progreso en la sesión
            if porcentaje > st.session_state.lesson_progress[lesson_name]:
                st.session_state.lesson_progress[lesson_name] = porcentaje
                st.balloons()
                st.success("¡Felicidades! Tu progreso ha sido actualizado.")
    
    else:
        # Para otras lecciones, solo mostrar introducción
        st.markdown(leccion["content"]["introduccion"])
        st.info("El contenido completo de esta lección estará disponible próximamente.")

# Navegación principal basada en estado actual
if st.session_state.current_section == "Inicio":
    show_home()
elif st.session_state.current_section == "Lecciones":
    if st.session_state.current_lesson:
        show_lesson(st.session_state.current_lesson)
    else:
        show_lessons_list()
elif st.session_state.current_section == "Lección Detalle":
    if st.session_state.current_lesson:
        show_lesson(st.session_state.current_lesson)
    else:
        st.warning("No hay lección seleccionada. Por favor, selecciona una lección.")
        show_lessons_list()
elif st.session_state.current_section == "Mi Progreso":
    show_progress()
elif st.session_state.current_section == "Mi Perfil":
    show_profile()

# Pie de página
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Curso de Costos para la Toma de Decisiones - DeciCost</div>", 
    unsafe_allow_html=True
)