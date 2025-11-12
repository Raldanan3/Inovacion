# pages/tools.py
import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from math_tools import MathTools

def tools_page():
    st.title("🛠️ Herramientas Matemáticas")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Calculadora de Derivadas", "Graficador", "Calculadora de Límites", "Resolvedor de Ecuaciones", "Calculadora Algebraica"])
    
    with tab1:
        st.subheader("Calculadora de Derivadas")
        funcion = st.text_input("Ingresa la función (usa 'x' como variable):", "x**2 + 3*x + 1", key="derivada_func")
        variable = st.selectbox("Variable:", ['x', 'y', 't'], key="derivada_var")
        
        if st.button("Calcular Derivada", key="btn_derivada"):
            math_tools = MathTools()
            resultado, derivada = math_tools.calcular_derivada(funcion, variable)
            st.write("**Resultado:**")
            st.latex(resultado)
            
            if derivada is not None:
                st.write("**Gráfica de la función y su derivada:**")
                col1, col2 = st.columns(2)
                with col1:
                    fig_func = math_tools.graficar_funcion(funcion)
                    if fig_func:
                        st.plotly_chart(fig_func, use_container_width=True)
                with col2:
                    fig_deriv = math_tools.graficar_funcion(str(derivada))
                    if fig_deriv:
                        st.plotly_chart(fig_deriv, use_container_width=True)
    
    with tab2:
        st.subheader("Graficador de Funciones")
        funcion_graf = st.text_input("Función a graficar:", "sin(x)", key="graf_func")
        col1, col2 = st.columns(2)
        with col1:
            x_min = st.number_input("x mínimo:", value=-10.0, key="x_min")
        with col2:
            x_max = st.number_input("x máximo:", value=10.0, key="x_max")
        
        # Múltiples funciones
        st.write("**Funciones adicionales (opcional):**")
        funcion2 = st.text_input("Segunda función:", "", key="func2")
        funcion3 = st.text_input("Tercera función:", "", key="func3")
        
        if st.button("Generar Gráfica", key="btn_graf"):
            math_tools = MathTools()
            fig = math_tools.graficar_funcion(funcion_graf, (x_min, x_max))
            if fig:
                # Agregar funciones adicionales si existen
                if funcion2:
                    try:
                        x = sp.symbols('x')
                        f2 = sp.lambdify(x, sp.sympify(funcion2), 'numpy')
                        x_vals = np.linspace(x_min, x_max, 400)
                        y_vals2 = f2(x_vals)
                        fig.add_trace(go.Scatter(x=x_vals, y=y_vals2, mode='lines', name=f'g(x) = {funcion2}'))
                    except:
                        st.error(f"Error al graficar: {funcion2}")
                
                if funcion3:
                    try:
                        x = sp.symbols('x')
                        f3 = sp.lambdify(x, sp.sympify(funcion3), 'numpy')
                        x_vals = np.linspace(x_min, x_max, 400)
                        y_vals3 = f3(x_vals)
                        fig.add_trace(go.Scatter(x=x_vals, y=y_vals3, mode='lines', name=f'h(x) = {funcion3}'))
                    except:
                        st.error(f"Error al graficar: {funcion3}")
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Error al generar la gráfica. Verifica la función.")
    
    with tab3:
        st.subheader("Calculadora de Límites")
        funcion_lim = st.text_input("Función para el límite:", "sin(x)/x", key="lim_func")
        punto = st.number_input("Punto donde calcular el límite:", value=0.0, key="lim_punto")
        direccion = st.selectbox("Dirección del límite:", ["ambos", "+", "-"], key="lim_dir")
        
        if st.button("Calcular Límite", key="btn_lim"):
            math_tools = MathTools()
            if direccion == "ambos":
                resultado, limite = math_tools.calcular_limite(funcion_lim, punto)
            else:
                resultado, limite = math_tools.calcular_limite(funcion_lim, punto, direccion=direccion)
            
            st.write("**Resultado:**")
            st.latex(resultado)
            
            # Gráfica cerca del punto
            if limite is not None and str(limite) not in ['zoo', 'NaN']:
                radio = 2.0
                fig = math_tools.graficar_funcion(funcion_lim, (punto-radio, punto+radio))
                if fig:
                    # Agregar punto del límite
                    if str(limite) != '0':
                        fig.add_trace(go.Scatter(
                            x=[punto], y=[limite], 
                            mode='markers', 
                            marker=dict(size=10, color='red'),
                            name=f'Límite: {limite}'
                        ))
                    st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.subheader("Resolvedor de Ecuaciones")
        ecuacion = st.text_input("Ingresa la ecuación (ej: x**2 - 4 = 0):", "x**2 - 4", key="ecuacion")
        variable = st.selectbox("Variable a resolver:", ['x', 'y', 't'], key="ecuacion_var")
        
        if st.button("Resolver Ecuación", key="btn_ecuacion"):
            math_tools = MathTools()
            # Asegurar que la ecuación tenga = 0
            if '=' in ecuacion:
                partes = ecuacion.split('=')
                ecuacion_str = f"({partes[0]}) - ({partes[1]})"
            else:
                ecuacion_str = ecuacion
            
            resultado, soluciones = math_tools.resolver_ecuacion(ecuacion_str, variable)
            st.write("**Resultado:**")
            st.write(resultado)
            
            if soluciones:
                st.write("**Gráfica de la función:**")
                fig = math_tools.graficar_funcion(ecuacion_str)
                if fig:
                    # Marcar soluciones en la gráfica
                    for sol in soluciones:
                        if sol.is_real:
                            fig.add_trace(go.Scatter(
                                x=[float(sol)], y=[0], 
                                mode='markers', 
                                marker=dict(size=10, color='red'),
                                name=f'Solución: {float(sol):.2f}'
                            ))
                    st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("Calculadora Algebraica")
        expresion = st.text_input("Ingresa la expresión algebraica:", "(x + 1)**2", key="algebra")
        operacion = st.selectbox("Operación:", ["Expandir", "Simplificar", "Factorizar"], key="algebra_op")
        variable = st.selectbox("Variable principal:", ['x', 'y', 't'], key="algebra_var")
        
        if st.button("Calcular", key="btn_algebra"):
            math_tools = MathTools()
            if operacion == "Expandir":
                resultado, resultado_exp = math_tools.expandir_expresion(expresion, variable)
                st.write("**Resultado:**")
                st.latex(resultado)
            elif operacion == "Simplificar":
                try:
                    x = sp.symbols(variable)
                    expr = sp.sympify(expresion)
                    simplificado = sp.simplify(expr)
                    st.write("**Resultado:**")
                    st.latex(f"Simplificación de {expr}: {simplificado}")
                except:
                    st.error("Error al simplificar la expresión")
            elif operacion == "Factorizar":
                try:
                    x = sp.symbols(variable)
                    expr = sp.sympify(expresion)
                    factorizado = sp.factor(expr)
                    st.write("**Resultado:**")
                    st.latex(f"Factorización de {expr}: {factorizado}")
                except:
                    st.error("Error al factorizar la expresión")