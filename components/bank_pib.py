from dash import html, dcc
import plotly.graph_objects as go
import polars as pl

colores = [
    "rgb(86, 85, 215)",
    "rgb(174, 68, 217)",
    "rgb(33, 150, 243)",
    "rgb(140, 255, 159)",
]


def returned_bank_pib_component(data: pl.DataFrame) -> html.Div:
    """returned_bank_pib_component: Grafica de Barras que muestra el INB
                                    percapita de las Zonas en esturio de la pagina
                                    del Banco Mundial

    Args:
        data (pl.DataFrame): _description_

    Returns:
        html.Div: _description_
    """
    fig = go.Figure(
        data=[
            go.Bar(
                y=data["INB_ATLAS_PC"],
                x=data["Zona"],
                # marker_color="rgb(86, 85, 215)",
                marker=dict(color=colores),
                width=0.7,
                hovertemplate=None,
                showlegend=False,
            ),
        ]
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(
        # xaxis_title="Zonas",
        yaxis_title="INB ATLAS PC $",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="rgb(0, 0, 0)"),
        margin=dict(t=0, b=0, l=0, r=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
    )

    pib_component = html.Div(
        [
            html.Label("INB Percapita Método ATLAS", className="bank-titles"),
            dcc.Graph(
                id="graph-bank-pib",
                figure=fig,
                style={
                    "width": "34vw",
                    "height": "70vh",
                    "margin-left": "0.3em",
                    "margin-boton": "1em",
                },
                config={"displayModeBar": False},
            ),
        ],
        id="in-pib-bank-container",
    )
    return pib_component
