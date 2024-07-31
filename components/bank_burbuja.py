from dash import html, dcc
import plotly.graph_objects as go
import polars as pl

colores = [
    "rgb(86, 85, 215)",
    "rgb(174, 68, 217)",
    "rgb(33, 150, 243)",
    "rgb(140, 255, 159)",
]


def returned_bank_burbuja_component(df: pl.DataFrame) -> html.Div:
    """returned_bank_burbuja_component: Despliega el Grafico de Burbuja de
                                        la pagina Banco Mundial

    Args:
        df (pl.DataFrame): DataFrame de la libreria Polars con la in-
                           formacion necesaria para desplegar el grafico

    Returns:
        html.Div: componente con el grafico de Burbujas
    """
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Inv_Extranjera_Poblacion"],
            y=df["Porcentaje Activo"],
            mode="markers",
            marker=dict(
                size=df["INB_ATLAS_PC"] / 150,
                sizemode="diameter",
                sizeref=8,
                color=colores,
                opacity=1,
            ),
            hovertext=df["hoover"],
            hoverinfo="text",
        )
    )
    fig.update_xaxes(showgrid=False, zeroline=True, showline=True, linecolor="black")
    fig.update_layout(
        yaxis_title="% Poblacion Activa",
        xaxis_title="Inversion Extranjera presente por cada 1000 Hab ($)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        margin=dict(t=20, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        annotations=[
            dict(
                text="Poblacion Activa vs Pib vs Inversion Extranjera",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.87,
                y=1.1,
                align="right",
                font=dict(color="rgb(0, 0, 0)", size=14),
            )
        ],
    )
    burbuja_component = html.Div(
        [
            dcc.Graph(
                figure=fig,
                style={
                    "width": "37vw",
                    "height": "36vh",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="bank-burbuja-container",
    )
    return burbuja_component
