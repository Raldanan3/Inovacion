# lecciones/leccion_3.py
LECCION_3 = {
    "titulo": "FUNCIONES EXPONENCIALES + DERIVADAS",
    "subtemas": {
        "3.1": {
            "nombre": "Modelos exponenciales en problemas aplicados",
            "contenido": """
            **Función exponencial**: f(x) = a·b^x
            - Crecimiento exponencial: b > 1
            - Decaimiento exponencial: 0 < b < 1
            - Aplicaciones: interés compuesto, crecimiento poblacional
            """
        },
        "3.2": {
            "nombre": "Concepto de derivada, notación y reglas",
            "contenido": """
            **Notaciones**: f'(x), dy/dx, Df(x)
            
            **Reglas básicas**:
            - Constante: d/dx[c] = 0
            - Potencia: d/dx[x^n] = n·x^(n-1)
            - Suma: d/dx[f + g] = f' + g'
            - Producto: d/dx[f·g] = f'g + fg'
            - Cociente: d/dx[f/g] = (f'g - fg')/g²
            """
        },
        "3.3": {
            "nombre": "Problemas aplicados de razones de cambio",
            "contenido": """
            La derivada representa la **razón de cambio instantánea**.
            
            **Aplicaciones**:
            - Velocidad (derivada de posición)
            - Aceleración (derivada de velocidad)
            - Tasa de crecimiento
            """
        },
        "3.4": {
            "nombre": "Regla de la cadena y funciones compuestas",
            "contenido": """
            **Regla de la cadena**: d/dx[f(g(x))] = f'(g(x)) · g'(x)
            
            **Ejemplo**: d/dx[sin(x²)] = cos(x²) · 2x
            """
        }
    },
    "ejercicios": {
        "ej1": {
            "pregunta": "Deriva f(x) = e^(2x) + 3^x",
            "puntaje": 15,
            "solucion": "f'(x) = 2e^(2x) + 3^x·ln(3)"
        },
        "ej2": {
            "pregunta": "Aplica la regla de la cadena en f(x) = sin(x²)",
            "puntaje": 20,
            "solucion": "f'(x) = cos(x²) · 2x"
        },
        "ej3": {
            "pregunta": "Encuentra la razón de cambio instantánea de f(x) = x³ en x=2",
            "puntaje": 15,
            "solucion": "f'(x) = 3x², f'(2) = 12"
        }
    }
}