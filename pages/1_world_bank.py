import dash
from dash import html
import polars as pl
from components.bank_pib import returned_bank_pib_component
from components.bank_etario import returned_etario_component
from components.bank_burbuja import returned_bank_burbuja_component

df = pl.read_csv("data/01_data_bank.csv")
df = df.with_columns(
    Inv_Extranjera_Poblacion=pl.col("Inv_Extranjera") / pl.col("Total Poblacion") * 1000
)
df_burbuja = df[
    "Zona", "INB_ATLAS_PC", "Porcentaje Activo", "Inv_Extranjera_Poblacion", "hoover"
]

dash.register_page(__name__, path="/bank", name="🏦 Banco Mundial")


layout = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [returned_bank_pib_component(df["Zona", "INB_ATLAS_PC"])],
                        id="bank-pib-container",
                        className="bank-left",
                    ),
                ],
                id="bank-left-container",
            ),
            html.Div(
                [
                    html.Div(
                        returned_bank_burbuja_component(df_burbuja),
                        id="bank-burbuja-container",
                        className="bank-right",
                    ),
                    html.Div(
                        [returned_etario_component(df[:, 4:])],
                        id="bank-etario-container",
                        className="bank-right",
                    ),
                ],
                id="bank-right-container",
            ),
        ],
        id="bank-container",
    ),
    className="work-container",
)
