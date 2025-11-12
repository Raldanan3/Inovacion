# lecciones/leccion_1.py
LECCION_1 = {
    "titulo": "RELACIONES FUNCIONALES + MODELOS LINEALES Y CUADRÁTICOS",
    "subtemas": {
        "1.1": {
            "nombre": "Relaciones que son funciones (relaciones funcionales)",
            "contenido": """
            Una **función** es una relación entre dos conjuntos donde cada elemento del primer conjunto (dominio) 
            se relaciona con exactamente un elemento del segundo conjunto (rango).
            
            **Ejemplo**: f(x) = x² es una función porque para cada x hay exactamente un x².
            **No función**: x² + y² = 1 (círculo) no es función porque para un x puede haber dos valores de y.
            """
        },
        "1.2": {
            "nombre": "Cálculo analítico del dominio de una función",
            "contenido": """
            El **dominio** de una función son todos los valores de x para los cuales la función está definida.
            
            **Reglas**:
            - Polinomios: Dominio = ℝ (todos los reales)
            - Fracciones: Denominador ≠ 0
            - Raíces pares: Radicando ≥ 0
            - Logaritmos: Argumento > 0
            
            **Ejemplo**: f(x) = 1/(x-2) → Dominio: ℝ - {2}
            """
        },
        "1.3": {
            "nombre": "Modelos lineales en problemas aplicados",
            "contenido": """
            **Función lineal**: f(x) = mx + b
            - m: pendiente (tasa de cambio)
            - b: intercepto con el eje y
            
            **Aplicaciones**:
            - Costos fijos y variables
            - Movimiento uniforme
            - Proporcionalidad directa
            """
        },
        "1.4": {
            "nombre": "Modelos cuadráticos en problemas aplicados",
            "contenido": """
            **Función cuadrática**: f(x) = ax² + bx + c
            - Gráfica: Parábola
            - Vértice: x = -b/(2a)
            - Aplicaciones: Movimiento parabólico, optimización
            """
        },
        "1.5": {
            "nombre": "Modelos a trozos",
            "contenido": """
            Funciones definidas por diferentes expresiones en diferentes intervalos.
            
            **Ejemplo**:
            ```
            f(x) = { x² si x < 0
                   { 2x si x ≥ 0
            ```
            """
        },
        "1.6": {
            "nombre": "Movimiento de gráficas",
            "contenido": """
            **Traslaciones**:
            - f(x) + k: desplazamiento vertical
            - f(x + h): desplazamiento horizontal
            - -f(x): reflexión en eje x
            - f(-x): reflexión en eje y
            """
        },
        "1.7": {
            "nombre": "Operaciones con funciones",
            "contenido": """
            **Suma**: (f + g)(x) = f(x) + g(x)
            **Resta**: (f - g)(x) = f(x) - g(x)
            **Multiplicación**: (f · g)(x) = f(x) · g(x)
            **División**: (f/g)(x) = f(x)/g(x), g(x) ≠ 0
            **Composición**: (f ∘ g)(x) = f(g(x))
            """
        }
    },
    "ejercicios": {
        "ej1": {
            "pregunta": "Determina si la relación y = x² + 1 es una función",
            "puntaje": 10,
            "solucion": "Sí es función porque para cada x hay exactamente un valor de y"
        },
        "ej2": {
            "pregunta": "Encuentra el dominio de f(x) = 1/(x-2)",
            "puntaje": 15,
            "solucion": "Dominio: ℝ - {2} (todos los reales excepto 2)"
        },
        "ej3": {
            "pregunta": "Resuelve el modelo lineal: 2x + 3 = 7",
            "puntaje": 10,
            "solucion": "2x = 4 → x = 2"
        },
        "ej4": {
            "pregunta": "Encuentra el vértice de f(x) = x² - 4x + 3",
            "puntaje": 15,
            "solucion": "Vértice en x = -(-4)/(2*1) = 2, f(2) = -1 → V(2, -1)"
        }
    }
}