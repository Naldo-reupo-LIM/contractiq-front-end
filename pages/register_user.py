import re

import dash_bootstrap_components as dbc
from dash import callback, callback_context, dcc, html
from dash.dependencies import Input, Output, State

import api_requests

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

register_user_form = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Form(
                    [
                        dbc.Label("Username"),
                        dbc.Input(
                            type="text",
                            id="username-input",
                            placeholder="Enter username",
                            style={"margin-bottom": "10px"},
                            required=True,
                        ),
                    ]
                ),
                dbc.Form(
                    [
                        dbc.Label("Email"),
                        dbc.Input(
                            type="email",
                            id="email-input",
                            placeholder="Enter email",
                            style={"margin-bottom": "10px"},
                            required=True,
                        ),
                    ]
                ),
                dbc.Form(
                    [
                        dbc.Label("Password"),
                        dbc.Input(
                            type="password",
                            id="password-input",
                            placeholder="Enter password",
                            style={"margin-bottom": "10px"},
                            required=True,
                        ),
                    ]
                ),
                dbc.Form(
                    [
                        dbc.Label("Confirm password"),
                        dbc.Input(
                            type="password",
                            id="password-confirm-input",
                            placeholder="Confirm password",
                            style={"margin-bottom": "10px"},
                            required=True,
                        ),
                    ]
                ),
                html.Div(
                    id="register-user-error",
                    style={"color": "red", "margin-bottom": "10px"},
                ),  # Adjusted color and added margin-bottom
                dbc.Button(
                    "Save",
                    id="save-button",
                    disabled=False,
                    color="primary",
                    style={"width": "100%"},
                ),
            ],
            style={
                "padding": "20px",
                "border-radius": "10px",
                "box-shadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
            },  # Added box shadow
        ),
    ],
    id="register-card",
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
            "Register user",
            style={
                "text-align": "center",
                "margin-bottom": "20px",
                "margin-top": "20px",
            },
        ),  # Added "Contracts IQ" as a heading
        register_user_form,
        dcc.Location(id="success-url", refresh=True),
        dbc.Alert(
            "User register successfully", id="alert-auto", is_open=True, duration=4000
        ),
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
    [
        Output("register-user-error", "children"),
        Output("alert-auto", "is_open"),
        Output("success-url", "pathname"),
    ],
    [Input("save-button", "n_clicks")],
    [
        State("username-input", "value"),
        State("email-input", "value"),
        State("password-input", "value"),
        State("password-confirm-input", "value"),
    ],
    running=[
        (Output("save-button", "disabled"), True, False),
    ],
)
def register_user_callback(login_clicks, username, email, password, passwordConfirm):

    ctx = callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    else:
        button_id = None

    if button_id == "save-button" and login_clicks:

        if not username or not email or not password or not passwordConfirm:
            return "Please complete all fields", False, None

        regex = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
        if not re.fullmatch(regex, email):
            return "Invalid email", False, None

        if password != passwordConfirm:
            return "Passwords do NOT match", False, None

        response = api_requests.register_user(username, email, password)
        if response.status_code == 200:
            message = response.json().get("message")
            success = response.json().get("success")
            if bool(success):
                return "", True, "/"
            else:
                return message, False, None

    return "", False, None





























































































































































