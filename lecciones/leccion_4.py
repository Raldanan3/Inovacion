# lecciones/leccion_4.py
LECCION_4 = {
    "titulo": "FUNCIONES LOGARÍTMICAS + FUNCIONES IMPLÍCITAS + APLICACIONES DE LA DERIVADA",
    "subtemas": {
        "4.1": {
            "nombre": "Modelos logarítmicos en problemas aplicados",
            "contenido": """
            **Función logarítmica**: f(x) = log_b(x)
            - Inversa de la función exponencial
            - Propiedades: log(ab) = log(a) + log(b)
            - Aplicaciones: pH, escala Richter, decibelios
            """
        },
        "4.2": {
            "nombre": "Derivada de inversas trigonométricas y de funciones hiperbólicas",
            "contenido": """
            **Derivadas de inversas trigonométricas**:
            - d/dx[arcsin(x)] = 1/√(1-x²)
            - d/dx[arctan(x)] = 1/(1+x²)
            """
        },
        "4.3": {
            "nombre": "Derivación implícita",
            "contenido": """
            Técnica para derivar funciones definidas implícitamente.
            
            **Ejemplo**: x² + y² = 1 → 2x + 2y·dy/dx = 0 → dy/dx = -x/y
            """
        },
        "4.4": {
            "nombre": "Estudio de puntos críticos y concavidad",
            "contenido": """
            **Puntos críticos**: donde f'(x) = 0 o f'(x) no existe
            **Concavidad**: 
            - Cóncava arriba: f''(x) > 0
            - Cóncava abajo: f''(x) < 0
            **Puntos de inflexión**: donde cambia la concavidad
            """
        },
        "4.5": {
            "nombre": "Derivación gráfica",
            "contenido": """
            Análisis de la derivada a partir de la gráfica de la función:
            - Pendiente positiva → derivada positiva
            - Pendiente negativa → derivada negativa
            - Máximos/mínimos → derivada cero
            """
        },
        "4.6": {
            "nombre": "Razones de cambio relacionadas",
            "contenido": """
            Problemas donde múltiples variables cambian con el tiempo y están relacionadas.
            
            **Estrategia**:
            1. Identificar variables y sus razones de cambio
            2. Encontrar relación entre variables
            3. Derivar implícitamente respecto al tiempo
            4. Sustituir valores conocidos
            """
        }
    },
    "ejercicios": {
        "ej1": {
            "pregunta": "Deriva f(x) = ln(x² + 1)",
            "puntaje": 15,
            "solucion": "f'(x) = (2x)/(x² + 1)"
        },
        "ej2": {
            "pregunta": "Encuentra los puntos críticos de f(x) = x³ - 3x",
            "puntaje": 20,
            "solucion": "f'(x) = 3x² - 3 = 3(x-1)(x+1) → puntos críticos: x = -1, 1"
        },
        "ej3": {
            "pregunta": "Usa derivación implícita para encontrar dy/dx de x² + y² = 25",
            "puntaje": 15,
            "solucion": "2x + 2y·dy/dx = 0 → dy/dx = -x/y"
        }
    }
}