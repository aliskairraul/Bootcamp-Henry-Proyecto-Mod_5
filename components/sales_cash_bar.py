from dash import html, dcc
import plotly.graph_objects as go
import polars as pl


def returned_cash_bar_component(
    data: pl.DataFrame, column: str, title: str
) -> html.Div:
    """returned_cash_bar_component: Grafico de Barras de la pagina Ventas o Sales
                                    donde se muestran las ventas por los distintos generos
                                    de los cuales se tiene data

    Args:
        data (pl.DataFrame): Dataframe con la Informacion a graficar
        column (str): columna del Dataframe que tiene los valores
        title (str): titulo del grafico

    Returns:
        html.Div: Componente con el grafico de Barras
    """
    fig = go.Figure(
        data=[
            go.Bar(
                y=data[column],
                x=data["GENERO"],
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
        xaxis_title="Generos con Data de Ventas",
        yaxis_title="Ventas en MM $",
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

    bar_component = html.Div(
        [
            html.Label(title, id="cash-title-bar"),
            dcc.Graph(
                id="graph-cash-bar",
                figure=fig,
                style={
                    "width": "38vw",
                    "height": "69vh",
                    # "margin-top": "1 em",
                    "margin-left": "0.3em",
                    "margin-boton": "0.5em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="in-bar-cash-container",
    )
    return bar_component
