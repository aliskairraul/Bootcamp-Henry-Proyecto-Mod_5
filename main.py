import dash
from dash import Dash, html, dcc
import pandas as pd


app = Dash(
    __name__, pages_folder="pages", use_pages=True, suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        html.Div(
            children=[
                dcc.Link(
                    page["name"],
                    href=page["relative_path"],
                    className="links-pages",
                    refresh=True,
                )
                for page in dash.page_registry.values()
            ],
            id="links-container",
        ),
        dash.page_container,
    ],
    id="general-container",
)

if __name__ == "__main__":
    app.run_server(debug=True)
