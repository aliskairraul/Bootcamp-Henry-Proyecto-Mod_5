import dash
from dash import html, Input, Output, callback
import polars as pl
from components.sales_cash_bar import returned_cash_bar_component
from components.sales_cash_pie import returned_cash_pie_component

##################################### CARGA DE DATOS
df = pl.read_csv("data/04_ventas_juegos_genero_consolas.csv")
df = df.filter(~df["GENERO"].is_null())
totales = {
    "N_America": df["N_America"].sum(),
    "Europa": df["Europa"].sum(),
    "Japon": df["Japon"].sum(),
    "Otros": df["Otros"].sum(),
}

dash.register_page(
    __name__, path="/sales", name="💵 Ventas Cash", suppress_callback_exceptions=True
)

layout = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            returned_cash_bar_component(
                                data=df, column="Total", title="Generos"
                            )
                        ],
                        id="sales-bar",
                    ),
                    html.Div([], id="sales-pie"),
                ],
                id="sales-bar-pie",
            ),
        ],
        id="cash-container",
    ),
    className="work-container",
)


@callback(
    Output("sales-pie", "children"),
    Input("graph-cash-bar", "clickData"),
    prevent_initial_call=False,
)
def refresh_cash_pie(clickData: dict) -> html.Div:
    """refresh_cash_pie: Se encarga de actualizar el Grafico tipo Pie de
                         la pagina de Sales

    Args:
        clickData (dict): Diccionario con la Informacion de la Barra
                          donde el usuario hizo click

    Returns:
        html.Div: Componente con Grafico tipo Torta con la Informacion
                  de ventas de las distntas regiones del Genero de Juego
                  seleccionado por el usuario
    """
    if clickData:
        selected_gen = clickData["points"][0]["x"]
        df_genero = df.filter(df["GENERO"] == selected_gen)
        genre = df_genero.drop("Total").drop("GENERO")
        title = f"Ventas por Región del Genero {selected_gen}"
    else:
        genre = pl.DataFrame(data=totales)
        title = "Ventas por Región"

    component = returned_cash_pie_component(data=genre, title=title)
    return component


@callback(
    Output("sales-bar", "children"),
    Input("graph-cash-pie", "clickData"),
    prevent_initial_call=False,
)
def refresh_cash_bar(clickData: dict) -> html.Div:
    """refresh_cash_bar: Se encarga de actualizar el grafico de barras
                         de la pagina Sales

    Args:
        clickData (dict): Diccionario con la Informacion de la Region
                          el el grafico tipo `pie` donde el usuario
                          hizo click

    Returns:
        html.Div: Componente con Grafico tipo Grafico de Barras con la
                  Informacion de ventas de los distntos Generos de Juegos
                  en la Region seleccionada por el usuario
    """
    if clickData:
        column = clickData["points"][0]["label"]
        title = f"Ventas por Género en la Región {column}"
    else:
        title = "Ventas por Género"
        column = "Total"

    component = returned_cash_bar_component(data=df, column=column, title=title)
    return component
