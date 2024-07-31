import dash
from dash import html

dash.register_page(__name__, path="/", name="🏠 Home")


layout = html.Div(
    html.Div(
        [
            html.Div(
                html.Label(
                    "Proyecto Integrador Modulo 5 Data-PT10 Grupo 1",
                    id="work-title",
                )
            ),
            html.Div(
                html.Img(src="assets/videojuegos-2.png"),
                style={"width": "100%", "height": "30vh"},
                id="image",
            ),
        ],
        id="home-container",
    ),
    id="work-home",
)
