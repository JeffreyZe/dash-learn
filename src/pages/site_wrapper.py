from dash import dcc, page_registry, page_container
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


class SiteWrapper:
    def __init__(self) -> None:
        self.navbar = self.create_navbar()

    def create_navbar(self):
        return dbc.NavbarSimple(
            dbc.Nav(
                [
                    dbc.NavLink(page["name"], href=page["path"])
                    for page in page_registry.values()
                ],
            ),
            brand="Xuze testing page",
            brand_href="/",
            color="primary",
            dark=True,
            className="mb-2",
        )

    def serve_layout(self):
        return dmc.MantineProvider(
            children=[
                dcc.Location(id="url", refresh=False),
                dcc.Store(id="global-data", storage_type="session"),
                dmc.Container(
                    fluid=True,
                    children=[
                        self.navbar,
                        page_container,
                        # TODO: footer
                    ],
                    style={"padding": "0px", "backgroundColor": "#e9ecef"},
                ),
            ]
        )
