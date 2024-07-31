from dash import html, dcc
import polars as pl


def returned_drop_component(drop_options: pl.DataFrame) -> dcc.Dropdown:
    """returned_drop_component: retorna el componente Dropdown de la pagina Tabla

    Args:
        drop_options (pl.DataFrame): Dataframe con la informacion

    Returns:
        dcc.Dropdown: Componente Dropdwon
    """
    options = [drop_options[i, 0] for i in range(len(drop_options))]
    drop_component = html.Div(
        [
            dcc.Dropdown(
                options=options,
                value=options[0],
                placeholder="Seleccione una Categoria",
                style={
                    "backgroundColor": "rgb(255, 255, 255)",
                    "fontSize": 14,
                    "color": "black",
                    # "fontFamily": "Arial",
                },
                id="drop-down",
            ),
        ]
    )
    return drop_component
