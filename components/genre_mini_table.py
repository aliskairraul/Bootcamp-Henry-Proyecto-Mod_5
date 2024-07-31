from dash import html, dcc
import dash_ag_grid as dag
import polars as pl
import pandas as pd

columns = ["Ranking", "Titulo", "Cantidad Reviews"]


def returned_mini_table_component(data: pl.DataFrame, title: str) -> html.Div:
    """returned_mini_table_component: Tabla con el Top 5 de Titulos del Genero seleccionado

    Args:
        data (pl.DataFrame): DataFrame de libreria Polars con la informacin necesaria

    Returns:
        html.Div: Componente con la Tabla
    """
    df = data[columns].to_pandas()
    mini_table_component = html.Div(
        [
            html.Div(html.Label(title), id="minitable-title"),
            html.Br(),
            dag.AgGrid(
                id="minitable",
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                className="ag-theme-balham",
                columnSize="sizeToFit",
                style={
                    "height": "22vh",
                    "width": "31vw",
                },
            ),
        ],
        id="genre-minitable-container",
    )
    return mini_table_component
