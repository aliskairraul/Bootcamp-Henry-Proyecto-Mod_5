from dash import html, dcc
from dash import dash_table
import polars as pl
import pandas as pd

columns = ["Ranking", "Titulo", "Windows", "Mac", "Linux"]


def returned_table_component(data: pl.DataFrame) -> html.Div:
    """returned_table_component: retorna la Tabla con el listado de titulos Disponibles
                                 de Titulos por Genero Seleccionado en la Plataforma Steam
                                 ordenados segun el Ranking de Ventas (informacion obtenida
                                 de la pagina web de Steam)

    Args:
        drop_options (pl.DataFrame): Dataframe con la informacion

    Returns:
        dcc.Dropdown: Componente Tabla
    """
    df = data.to_pandas()
    table_component = html.Div(
        [
            dash_table.DataTable(
                id="dash_table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
                editable=False,
                filter_action="native",
                sort_action="native",
                page_size=10,
                fixed_rows={"headers": True},
                row_selectable="single",  # Permitir la selección de una sola fila
                selected_rows=[],
                # page_action="none",
                style_table={
                    "width": "100%",
                    "height": "80%",
                    # "height": "30vh",
                    # "overflowY": "auto",
                },
                # style_cell={"textAlign": "left"},
                style_data_conditional=[
                    {
                        "if": {"column_id": "Ranking"},
                        "textAlign": "center",
                        "width": "12%",
                    },
                    {
                        "if": {"column_id": "Titulo"},
                        "textAlign": "left",
                        "width": "52%",
                    },
                    {
                        "if": {"column_id": "Windows"},
                        "textAlign": "center",
                        "width": "12%",
                    },
                    {"if": {"column_id": "Mac"}, "textAlign": "center", "width": "12%"},
                    {
                        "if": {"column_id": "Linux"},
                        "textAlign": "center",
                        "width": "12%",
                    },
                ],
                style_cell={
                    "height": "2em",  # Altura de la fila en unidades em
                    # 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                    "overflow": "hidden",
                    "textOverflow": "ellipsis",
                },
                style_header={
                    "backgroundColor": "rgb(230, 230, 230)",
                    "fontWeight": "bold",
                    "textAlign": "center",
                },
            ),
        ],
        id="table-table-container",
    )
    return table_component


"""
ag-theme-alpine
ag-theme-balham
ag-theme-balham-dark
ag-theme-material
ag-theme-fresh
ag-theme-dark
ag-theme-blue



@app.callback(
    Output('table', 'page_size'),
    Input('table-height', 'value')
)
def update_page_size(height):
    row_height = 35  # Altura aproximada de cada fila en píxeles
    page_size = max(1, height // row_height)  # Calcula el número de filas que caben en la altura
    return page_size


"""
