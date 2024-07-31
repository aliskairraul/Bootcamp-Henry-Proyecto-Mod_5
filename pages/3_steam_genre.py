import dash
from dash import html, Input, Output, callback
import polars as pl
from components.genre_top import returned_genre_top_component
from components.genre_pie_critic import returned_critic_pie_component
from components.genre_platform import returned_platform_component
from components.genre_mini_table import returned_mini_table_component

######################## CARGA DE DATOS
df_top = (
    pl.read_csv("data/2024_steam_titulos_generos.csv")
    .sort("cantidad", descending=True)
    .head(10)
)
df_ranking = pl.read_csv("data/julio_2024_rank_steam_con_generos.csv")


dash.register_page(__name__, path="/genres", name="📊 Generos")


layout = html.Div(
    html.Div(
        [
            html.Div([returned_genre_top_component(df_top)], id="genre-left-container"),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [],
                                id="genre_pie_critic",
                                className="genre-pies-containers",
                            ),
                            html.Div(
                                [],
                                id="genre-platforms",
                                className="genre-pies-containers",
                            ),
                        ],
                        id="genre-right-up-container",
                    ),
                    html.Div([], id="genre-mini-table-container"),
                ],
                id="genre-right-container",
            ),
        ],
        id="gen-container",
    ),
    className="work-container",
)


@callback(
    Output("genre_pie_critic", "children"),
    Input("graph-gen-top", "clickData"),
    prevent_initial_call=False,
)
def refresh_critic_pie(clickData: dict) -> html.Div:
    """refresh_critic_pie: Se encarga de Actualizar el Grafico tipo Pie
                           de la pagina Generos

    Args:
        clickData (dict): Diccionario con la Informacion de la Barra
                          (Genero seleccionado) donde el usuario hizo click

    Returns:
        html.Div: Grafico tipo Pie con los porcentajes con respecto a las
                  criticas del Genero Seleccionado
    """
    if clickData:
        selected_gen = clickData["points"][0]["x"]
        title = f"Criticas {selected_gen}"
    else:
        selected_gen = "Accion"
        title = "Criticas Accion"

    data = df_top.filter(df_top["genero"] == selected_gen)
    data = data["Suma Positiva", "Suma Negativa", "Variadas"]
    data = data.transpose(include_header=True)

    component = returned_critic_pie_component(data=data, title=title)
    return component


@callback(
    Output("genre-platforms", "children"),
    Input("graph-gen-top", "clickData"),
    prevent_initial_call=False,
)
def refresh_platforms(clickData: dict) -> html.Div:
    """refresh_platforms: Se encarga de actualizar el grafico de barras que
                          muestra las plataformas de la pagina Generos

    Args:
        clickData (dict): Diccionario con la Informacion de la Barra
                          (Genero seleccionado) donde el usuario hizo click

    Returns:
        html.Div: Numero de Juegos disponibles por plataforma de Sistema
                  Operativo
    """
    if clickData:
        selected_gen = clickData["points"][0]["x"]
        title = f"Plataformas {selected_gen}"
    else:
        selected_gen = "Accion"
        title = "Plataformas Accion"

    data = df_top.filter(df_top["genero"] == selected_gen)[:, 2:5]
    data = data.transpose(include_header=True)

    component = returned_platform_component(data=data, title=title)
    return component


@callback(
    Output("genre-mini-table-container", "children"),
    Input("graph-gen-top", "clickData"),
    prevent_initial_call=False,
)
def refresh_top5(clickData: dict) -> html.Div:
    """refresh_top5: Se encarga de actualizar la lista de los 5 titulos
                     mas vendidos segun el genero seleccionado

    Args:
        clickData (dict): Diccionario con la Informacion de la Barra
                          (Genero seleccionado) donde el usuario hizo click

    Returns:
        html.Div: Tabla con los 5 Titulos con mas Ventas en Steam del Genero
                  seleccionado por el usuario
    """
    if clickData:
        selected_gen = clickData["points"][0]["x"]
        title = f"Top 5 Titulos {selected_gen}"
    else:
        selected_gen = "Accion"
        title = "Top 5 Titulos Accion"

    data = df_ranking.filter(df_ranking[selected_gen] == 1).head(5)

    component = returned_mini_table_component(data=data, title=title)
    return component
