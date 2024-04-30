from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc

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
                id="create",
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
                    "Create new team",
                    style={
                        "padding": "10px 10px 0px 30px",
                        "fontSize": "30px",
                        "fontWeight": "600",
                    },
                ),
                dbc.CardHeader(
                    "Team Details", style={"padding": "0px 10px 0px 30px"}
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
                            ],
                            className="mt-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label("Add email adress"),
                                        dbc.Input(
                                            id="document-type",
                                            type="text",
                                            placeholder="Email Adress",
                                            className="search-input",
                                        ),
                                    ],
                                    width=10,
                                ),
                                
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

