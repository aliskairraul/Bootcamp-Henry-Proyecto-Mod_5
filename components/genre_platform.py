from dash import html, dcc
import plotly.graph_objects as go
import polars as pl


def returned_platform_component(data: pl.DataFrame, title: str) -> html.Div:
    """returned_platform_component: Retorna un Grafico de Barras con la cantidad de Juegos
                                    disponibles en las distintas plataformas según el Genero
                                    seleccionado

    Args:
        data (pl.DataFrame): DataFrame de la libreria polars con la informacin necesaria
        title (str): Titulo de la Grafica que varia dependiendo del genero

    Returns:
        html.Div: componente con el grafico de barras
    """
    fig = go.Figure(
        data=[
            go.Bar(
                y=data["column_0"],
                x=data["column"],
                marker_color="rgb(86, 85, 215)",
                width=0.4,
                hovertemplate=None,
                showlegend=False,
            ),
        ]
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(
        yaxis_title="Titulos Plataforma",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        xaxis=dict(
            tickmode="linear",
            dtick=1,
        ),
        margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        showlegend=False,
    )

    platform_component = html.Div(
        [
            html.Label(title, className="top-pies"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                # id="graph-cash-bar",
                figure=fig,
                style={
                    "width": "17vw",
                    "height": "32vh",
                    "margin-left": "0.5em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="in-platforms-container",
    )
    return platform_component
