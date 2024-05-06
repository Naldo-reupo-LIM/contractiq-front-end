import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, dcc, html

import api_requests

modal_buttons = dbc.Row(
    children=[
        dbc.Col(
            dbc.Button(
                "Cancel",
                id="close",
                className="ms-auto",
                n_clicks=0,
                color="secondary",
                style={"width": "120px"},
            ),
        ),
        dbc.Col(
            dbc.Button(
                "Create",
                id="create-workspace-button",
                className="",
                n_clicks=0,
                color="primary",
                style={"width": "120px"},
            ),
        ),
    ],
    justify="end",
)

modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.CardHeader(
                    "Create new workspace",
                    style={
                        "padding": "10px 10px 0px 30px",
                        "fontSize": "30px",
                        "fontWeight": "600",
                    },
                ),
                dbc.CardHeader(
                    "Workspace Details", style={"padding": "0px 10px 0px 30px"}
                ),
                dbc.ModalBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Name *"),
                                        dbc.Input(
                                            id="workspace-name",
                                            type="text",
                                            placeholder="Name",
                                            className="search-input",
                                        ),
                                    ],
                                    width=6,
                                ),
                                dbc.Col(
                                    [
                                        html.Label("Charge Code *"),
                                        dbc.Input(
                                            id="workspace-code",
                                            type="text",
                                            placeholder="Enter Charge Code",
                                            className="search-input",
                                        ),
                                    ],
                                    width=6,
                                ),
                            ],
                            className="mt-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Document Type*"),
                                        dbc.Input(
                                            id="document-type",
                                            type="text",
                                            placeholder="Document Type*",
                                            className="search-input",
                                        ),
                                    ],
                                    width=4,
                                ),
                                dbc.Col(
                                    [
                                        html.Label("Client Name"),
                                        dbc.Input(
                                            id="client-name",
                                            type="text",
                                            placeholder="Client ID",
                                            className="search-input",
                                        ),
                                    ],
                                    width=4,
                                    style={"padding-left": "120px"},
                                ),
                            ],
                            className="mt-4",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Add Teams"),
                                        dcc.Dropdown(
                                            id="project-members",  # Replace with the actual identifier
                                            options=[
                                                {"label": "Team 1", "value": "Team 1"},
                                                {"label": "Team 2", "value": "Team 2"},
                                                {"label": "Team 3", "value": "Team 3"},
                                            ],
                                            placeholder="Team names",
                                            clearable=True,
                                            style={"width": "100%"},
                                        ),
                                    ]
                                ),
                            ],
                            className="mt-4",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Project Description"),
                                        dbc.Textarea(
                                            id="project-description",
                                            placeholder="Add project description",
                                            className="search-input",
                                        ),
                                    ]
                                ),  # Specify width of 6 for half of the row
                            ],
                            className="mt-4",
                        ),
                    ],
                    style={"padding": "3rem 5rem"},
                ),
                dbc.ModalFooter(modal_buttons, style={"borderTop": "none"}),
            ],
            id="modal",
            is_open=False,
            size="lg",
        ),
    ],
)





