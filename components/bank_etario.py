from dash import html, dcc
import plotly.graph_objects as go
import polars as pl

rangos = ["0 - 14", "15 - 64", "65 o mas"]


def returned_etario_component(df: pl.DataFrame) -> html.Div:
    """returned_etario_component: Retorna un grafico de Barras apiladas con
                                  la informacion de las proporciones de los grupos
                                  de edades según las Zonas del mundo

    Args:
        df (pl.DataFrame): Dataframe de la Libreria Polars con la informacion
                           necesaria para desplegar el gráfico

    Returns:
        html.Div: Componente Grafico de Barras apiladas
    """
    fig = go.Figure(
        data=[
            go.Bar(
                name="0-14 Años",
                y=df["Porcentaje 0-14"],
                x=df["Zona"],
                width=0.25,
                hovertemplate=None,
                showlegend=True,
            ),
            go.Bar(
                name="15-64 Años",
                y=df["Porcentaje 15-64"],
                x=df["Zona"],
                # marker_color="rgb(255, 21, 110)",
                width=0.25,
                hovertemplate=None,
                showlegend=True,
            ),
            go.Bar(
                name="65 Años o mas",
                y=df["Porcentaje 65 o mas"],
                x=df["Zona"],
                # marker_color="rgb(255, 21, 110)",
                width=0.25,
                hovertemplate=None,
                showlegend=True,
            ),
        ]
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(
        barmode="group",
        yaxis_title="% de Habitantes",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        # xaxis=dict(
        #     tickmode="linear",
        #     dtick=1,
        # ),
        margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        # showlegend=True,
        legend=dict(x=0.9, y=1),
    )

    etario_component = html.Div(
        [
            html.Label(
                "Distribucion de Edades en la Población", className="bank-titles"
            ),
            dcc.Graph(
                id="graph-eta-pib",
                figure=fig,
                style={
                    "width": "41vw",
                    "height": "32vh",
                    # "margin-top": "1 em",
                    "margin-left": "0.3em",
                    "margin-boton": "1.5em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="in-eta-bank-container",
    )
    return etario_component
