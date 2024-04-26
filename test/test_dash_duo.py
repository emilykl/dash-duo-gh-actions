# Set up simple Pytest test using dash_duo

import dash
from dash import html, dcc


def test_app(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div([html.P(id="output", children="Hello, Dash!")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#output", timeout=4)
    assert dash_duo.find_element("#output").text == "Hello, Dash!"
