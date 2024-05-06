import dash_bootstrap_components as dbc
from dash import callback, callback_context, dcc, html
from dash.dependencies import Input, Output, State

import api_requests

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

login_form = dbc.Card(
    [
        dcc.Store(id="jwt-token", storage_type="local"),
        dbc.CardBody(
            [
                dbc.Form(
                    [
                        dbc.Label("Username"),
                        dbc.Input(
                            type="text",
                            id="login-username-input",
                            placeholder="Enter username",
                            style={"margin-bottom": "10px"},  # Added margin-bottom
                        ),
                    ]
                ),
                dbc.Form(
                    [
                        dbc.Label("Password"),
                        dbc.Input(
                            type="password",
                            id="login-password-input",
                            placeholder="Enter password",
                            style={"margin-bottom": "10px"},  # Added margin-bottom
                        ),
                    ]
                ),
                html.Div(
                    id="login-error", style={"color": "red", "margin-bottom": "10px"}
                ),  # Adjusted color and added margin-bottom
                dbc.Button(
                    "Login",
                    id="login-button",
                    color="primary",
                    style={"width": "100%"},
                ),
                dbc.NavLink(
                    "Create an account",
                    href="/register_user",
                    active="exact",
                    style={
                        "color": "#0d6efd",
                        "margin-top": "10px",
                    },
                ),
                dcc.Location(id="login-success-url", refresh=True),
            ],
            style={
                "padding": "20px",
                "border-radius": "10px",
                "box-shadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
            },  # Added box shadow
        ),
    ],
    id="login-card",
    style={
        "width": "25%",
        "margin-left": "auto",
        "margin-right": "auto",
    },  # Removed background color
    className="login_card",
)

layout = html.Div(
    children=[
        html.H1(
            "Contracts IQ",
            style={
                "text-align": "center",
                "margin-bottom": "20px",
                "margin-top": "20px",
            },
        ),  # Added "Contracts IQ" as a heading
        login_form,
    ],
    style={
        "display": "flex",
        "flex-direction": "column",  # Added flex-direction column
        "align-items": "center",
        "justify-content": "center",
        "background-color": "#EBEBF6",  # Added background color
        "height": "100vh",  # Set height to full viewport height
    },
)


@callback(
    Output("login-error", "children"),
    Output("jwt-token", "data"),
    Output("login-success-url", "pathname"),
    [Input("login-button", "n_clicks")],
    [State("login-username-input", "value"), State("login-password-input", "value")],
    running=[
        (Output("login-button", "disabled"), True, False),
    ],
)
def authenticate_user_callback(login_clicks, username, password):
    ctx = callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    else:
        button_id = None

    if button_id == "login-button" and login_clicks:
        # Make a POST request to authenticate user
        response = api_requests.authenticate_user(username, password)
        success = response.json().get("success")
        if response.status_code == 200 and success:
            access_token = response.json().get("data", {}).get("access_token")
            return "", access_token, "workspaces"  # Return success message and token
        else:
            return (
                "Invalid username or password",
                None,
                None,
            )
            # Return error message and None for token
    elif "jwt-token" in ctx.states:
        token = ctx.states["jwt-token"]["data"]
        if token:
            return "", token, "workspaces"
    else:
        return "", None, None
























































