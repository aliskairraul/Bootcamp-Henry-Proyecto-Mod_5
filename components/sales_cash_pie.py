from dash import html, dcc
import plotly.graph_objects as go
import polars as pl


def returned_cash_pie_component(data: pl.DataFrame, title: str) -> html.Div:
    """returned_cash_pie_component: Grafico tipo Pie de la pagina Ventas o Sales
                                    donde se muestran las ventas por las distintas
                                    regiones del mundo

    Args:
        data (pl.DataFrame): Dataframe con la Informacion a graficar
        title (str): titulo del grafico

    Returns:
        html.Div: Componente con el grafico tipo Pie
    """
    transpuesta = data.transpose(include_header=True)
    transpuesta.columns = ["Locaciones", "Valores"]
    colors = {
        "N_America": "rgb(86, 85, 215)",
        "Otros": "rgb(140, 255, 159)",
        "Europa": "rgb(174, 68, 217)",
        "Japon": "rgb(33, 150, 243)",
    }

    labels = ["N_America", "Japon", "Europa", "Otros"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=transpuesta["Valores"],
                # hole=0.4,
                marker=dict(colors=[colors[label] for label in labels]),
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
        font=dict(color="rgb(0, 0, 0)"),  # size=13
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(x=0.7, y=1.3),
    )

    pie_component = html.Div(
        [
            html.Label(title, id="cash-title-pie"),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id="graph-cash-pie",
                figure=fig,
                style={"width": "42vw", "height": "60vh", "margin-top": "0.5em"},
                config={"displayModeBar": False},
            ),
        ],
        id="in-bar-cash-container",
    )
    return pie_component


"""
        "N_America": "rgb(86, 85, 215)",
        "Otros": "rgb(74, 189, 232)",
        "Europa": "rgb(154, 89, 181)",
        "Japon": "rgb(140, 255, 144)",
"""
