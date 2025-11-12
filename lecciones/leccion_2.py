# lecciones/leccion_2.py
LECCION_2 = {
    "titulo": "FUNCIONES TRIGONOMÉTRICAS + LÍMITES Y CONTINUIDAD",
    "subtemas": {
        "2.1": {
            "nombre": "Modelos trigonométricos y sus inversas",
            "contenido": """
            **Funciones trigonométricas**:
            - sen(x), cos(x), tan(x)
            - Periodo: 2π para seno y coseno, π para tangente
            
            **Funciones inversas**:
            - arcsen(x), arccos(x), arctan(x)
            - Dominios restringidos
            """
        },
        "2.2": {
            "nombre": "Concepto de límite + derivadas sencillas",
            "contenido": """
            **Límite**: lim(x→a) f(x) = L significa que f(x) se acerca a L cuando x se acerca a a.
            
            **Derivada por definición**:
            f'(x) = lim(h→0) [f(x+h) - f(x)]/h
            """
        },
        "2.3": {
            "nombre": "Continuidad de una función",
            "contenido": """
            Una función es **continua** en x = a si:
            1. f(a) existe
            2. lim(x→a) f(x) existe
            3. lim(x→a) f(x) = f(a)
            """
        },
        "2.4": {
            "nombre": "Límites infinitos y asíntotas verticales",
            "contenido": """
            **Límite infinito**: lim(x→a) f(x) = ∞
            **Asíntota vertical**: x = a es una asíntota vertical si lim(x→a) f(x) = ±∞
            """
        },
        "2.5": {
            "nombre": "Límites en el infinito y asíntotas horizontales",
            "contenido": """
            **Límite en infinito**: lim(x→∞) f(x) = L
            **Asíntota horizontal**: y = L es una asíntota horizontal si lim(x→∞) f(x) = L
            """
        }
    },
    "ejercicios": {
        "ej1": {
            "pregunta": "Calcula lim(x→0) sin(x)/x",
            "puntaje": 15,
            "solucion": "El límite es 1 (límite trigonométrico fundamental)"
        },
        "ej2": {
            "pregunta": "Determina las asíntotas de f(x) = 1/(x²-4)",
            "puntaje": 20,
            "solucion": "Asíntotas verticales: x = 2, x = -2; Asíntota horizontal: y = 0"
        },
        "ej3": {
            "pregunta": "Calcula la derivada de f(x) = 3x² - 2x + 1 usando la definición",
            "puntaje": 25,
            "solucion": "f'(x) = 6x - 2"
        }
    }
}