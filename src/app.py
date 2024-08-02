from dash import Dash, _dash_renderer
import dash_bootstrap_components as dbc

from pages.site_wrapper import SiteWrapper

_dash_renderer._set_react_version("18.2.0")

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # suppress_callback_exceptions=True,
)
sever = app.server

site_wrapper = SiteWrapper()
app.layout = site_wrapper.serve_layout()


if __name__ == "__main__":
    app.run(debug=True)
