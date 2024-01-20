"""
    Aqui es donde se hace uso de Flask como el servidor web para ejecutar mi aplicación Dash. 
"""
import os
from flask import Flask, render_template
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px


def create_app():
    """ Configuration """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'database', 'clients.xlsx')
    print(file_path)
    df = pd.read_excel(file_path)
    app_flask = Flask(__name__)
    app_dash = Dash(__name__, server=app_flask)

    fig = px.bar(df, x='Nombre', y='Sueldo', color="Pais", barmode="group")

    # App layout
    app_dash.layout = html.Div([
        html.Div(children=[html.H1(
            children="Datos de Clientes",
            className="title"
        )]),
        html.H2(children="Lista de Clientes"),
        dash_table.DataTable(data=df.to_dict('records'), page_size=10),
        html.H2(
            children="Grafico del promedio de Sueldos en los Paises de los Clientes"
        ),
        dcc.Graph(figure=px.histogram(
            df, x='Pais', y='Sueldo', histfunc='avg')
        ),
        html.H2(
            children="Grafico de los Sueldos de los trabajadores de los diferentes paises representados en colores"
        ),
        dcc.Graph(
            className='grafico',
            figure=fig
        )
    ])

    return app_flask
