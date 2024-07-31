import dash
from dash import html, callback, Input, Output
import polars as pl
from components.table_drop_component import returned_drop_component
from components.table_table_component import returned_table_component


df = pl.read_csv("data/julio_2024_rank_steam_con_generos.csv")
drop_options = pl.read_csv("data/2024_steam_titulos_generos.csv", columns="genero")

dash.register_page(
    __name__, path="/grid", name="📋 Tabla", suppress_callback_exceptions=True
)


layout = html.Div(
    [
        html.Div(
            [
                html.Div([returned_drop_component(drop_options)], id="drop"),
                html.Div([], id="table"),
            ],
            id="grid-left-container",
        ),
        html.Div([], id="grid-right-container"),
    ],
    id="tables-container",
)


@callback(
    Output("table", "children"),
    [Input("drop-down", "value")],
    prevent_initial_call=False,
)
def refresh_table(value: str) -> html.Div:
    """refresh_table: Se encarga de Actualizar la Tabla que muestra
                      los titulos del genero seleccionado

    Args:
        value (str): Genero selecionado por el usuario

    Returns:
        _type_: Tabla con los Titulos correspondientes a los generos seleccionados
    """
    data = df.filter(df[value] == 1)["Ranking", "Titulo", "Windows", "Mac", "Linux"]

    component = returned_table_component(data=data)
    return component


@callback(
    Output("grid-right-container", "children"),
    [Input("dash_table", "selected_rows"), Input("dash_table", "derived_virtual_data")],
)
def display_selected_row(selected_rows: int, derived_vritual_data: list):
    """display_selected_row: Se encarga de mostrar la información disponible del
                             titulo seleccionado

    Args:
        selected_rows (int): indice que indica la fila seleccionada
        derived_vritual_data (list): Toda la Informacion de la Tabla vaciada
                                     en una lista de diccionarios donde cada
                                     diccionario representa una row

    Returns:
        _type_: Informacion disponible del registro seleccinado
    """
    if selected_rows is None or len(selected_rows) == 0:
        return []

    ranking = derived_vritual_data[selected_rows[0]]["Ranking"]
    data = (
        df.filter(df["Ranking"] == ranking)
        .drop("Aprobacion")
        .drop("Critica Categorica")
        .drop("Fecha Ingles")
        .drop("Fecha")
    )

    return html.Div(
        [
            html.P(f"{data[:,j].name}: {data[0,j]}")
            for j in range(len(data.columns))
            if data[0, j] != 0
        ],
        id="descripcion",
    )
