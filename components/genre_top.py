from dash import html, dcc
import plotly.graph_objects as go
import polars as pl


def returned_genre_top_component(data: pl.DataFrame) -> html.Div:
    """returned_genre_top_component: Grafico de Barras Principal de la pagina Generos
                                     donde se muestran las ventas de titulos en la pla-
                                     taforma Steam de los 10 principales Generos de Juegos

    Args:
        data (pl.DataFrame): DataFrame de la libreria Polars con la informacion
                             necesaria

    Returns:
        html.Div: Componente con el grafico de Barras
    """
    fig = go.Figure(
        data=[
            go.Bar(
                y=data["cantidad"],
                x=data["genero"],
                marker_color="rgb(86, 85, 215)",
                width=0.7,
                hovertemplate=None,
                showlegend=False,
            ),
        ]
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(
        yaxis_title="Cantidad de Titulos Vendidos",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        showlegend=False,
    )

    top_component = html.Div(
        [
            html.Label(
                "TOP 10 Generos con Videojuegos mas vendidos en Steam", id="gen-top-bar"
            ),
            dcc.Graph(
                id="graph-gen-top",
                figure=fig,
                style={"width": "38vw", "height": "66vh", "margin-left": "0.3em"},
                config={"displayModeBar": False},
            ),
        ],
        id="in-top-genre-container",
    )
    return top_component
