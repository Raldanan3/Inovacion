# math_tools.py
import sympy as sp
import numpy as np
import plotly.graph_objects as go

class MathTools:
    @staticmethod
    def calcular_derivada(funcion_str, variable='x'):
        """Calcula la derivada de una función"""
        try:
            x = sp.symbols(variable)
            funcion = sp.sympify(funcion_str)
            derivada = sp.diff(funcion, x)
            return f"d/d{x} ({funcion}) = {derivada}", derivada
        except:
            return "Error: Función no válida", None
    
    @staticmethod
    def graficar_funcion(funcion_str, x_range=(-10, 10), puntos=None):
        """Genera gráfica de una función"""
        try:
            x = sp.symbols('x')
            funcion = sp.sympify(funcion_str)
            
            # Convertir a función numérica
            f = sp.lambdify(x, funcion, 'numpy')
            
            # Crear array de valores x
            x_vals = np.linspace(x_range[0], x_range[1], 400)
            y_vals = f(x_vals)
            
            # Crear gráfica
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f'f(x) = {funcion_str}'))
            
            # Agregar puntos si se especifican
            if puntos:
                for punto in puntos:
                    fig.add_trace(go.Scatter(
                        x=[punto[0]], y=[punto[1]], 
                        mode='markers', 
                        marker=dict(size=10, color='red'),
                        name=f'Punto ({punto[0]}, {punto[1]})'
                    ))
            
            fig.update_layout(
                title=f'Gráfica de f(x) = {funcion_str}',
                xaxis_title='x',
                yaxis_title='f(x)',
                height=400
            )
            return fig
        except:
            return None
    
    @staticmethod
    def calcular_limite(funcion_str, punto, variable='x', direccion='+'):
        """Calcula el límite de una función"""
        try:
            x = sp.symbols(variable)
            funcion = sp.sympify(funcion_str)
            
            if direccion == '+':
                limite = sp.limit(funcion, x, punto, dir='+')
            elif direccion == '-':
                limite = sp.limit(funcion, x, punto, dir='-')
            else:
                limite = sp.limit(funcion, x, punto)
            
            return f"lim(x→{punto}) {funcion} = {limite}", limite
        except:
            return "Error: No se pudo calcular el límite", None
    
    @staticmethod
    def resolver_ecuacion(ecuacion_str, variable='x'):
        """Resuelve una ecuación"""
        try:
            x = sp.symbols(variable)
            ecuacion = sp.sympify(ecuacion_str)
            soluciones = sp.solve(ecuacion, x)
            return f"Soluciones de {ecuacion} = 0: {soluciones}", soluciones
        except:
            return "Error: No se pudo resolver la ecuación", None
    
    @staticmethod
    def expandir_expresion(expresion_str, variable='x'):
        """Expande una expresión algebraica"""
        try:
            x = sp.symbols(variable)
            expresion = sp.sympify(expresion_str)
            expandida = sp.expand(expresion)
            return f"Expansión de {expresion}: {expandida}", expandida
        except:
            return "Error: No se pudo expandir la expresión", None