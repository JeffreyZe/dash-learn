from dash import html, register_page
import dash_mantine_components as dmc


register_page(__name__,
              path="/home",
              title="Home")

layout = dmc.MantineProvider(
    children=[
        html.Div(
            html.H1("Home Page")
        )
    ]
)