from dash import html, dcc
import plotly.graph_objects as go
import polars as pl


def returned_critic_pie_component(data: pl.DataFrame, title: str) -> html.Div:
    """returned_critic_pie_component: Retorna una grafica tipo `Donuts` con los
                                    porcentajes de Calificaciones Positivas, Negativas
                                    y Neutras del Genero seleccionado

    Args:
        data (pl.DataFrame): DataFrame de la libreria Polars con la informacion necesaria
        title (str): Titulo de la Grafica, que debe variar según el Genero

    Returns:
        html.Div: Componente con el grafic Donut
    """
    colors = {
        "Positivas": "rgb(140, 255, 159)",
        "Negativas": "rgb(255, 76, 61)",
        "Neutras": "rgb(174, 68, 217)",
    }

    labels = ["Positivas", "Negativas", "Neutras"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=data["column_0"],
                hole=0.4,
                marker=dict(colors=[colors[label] for label in labels]),
                textinfo="label+percent",
                showlegend=False,
                textposition="outside",
            )
        ]
    )
    fig.update_traces(
        textfont=dict(color="rgb(0, 0, 0)"),  # size=13
        hoverinfo="label+percent",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        margin=dict(t=0, b=0, l=0, r=0),
    )

    pie_critic_component = html.Div(
        [
            html.Label(title, className="top-pies"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id="graph_critic_pie",
                figure=fig,
                style={
                    "width": "17vw",
                    "height": "32vh",
                },
            ),
        ],
        id="in-bar-cash-container",
    )
    return pie_critic_component
