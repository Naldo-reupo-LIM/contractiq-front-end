from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import dash,api_requests
from pages.c8 import modal1

modal_buttons = dbc.Row(
    id = "button-container",
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
            html.Div(
                                [
                                    dbc.Button(
                                        "Next",
                                        color="primary",
                                        className="sidebar-button",
                                        id="next-button",
                                        style={"width": "204px"},
                                    ),
                                    modal1,
                                ]
                            ),
                            className="d-flex justify-content-end",
        ),
        
    ],
    justify="end",
)

steps_header = dbc.Row(
    [
        dbc.Col(html.H4("Upload", className="text-center"), width=3,style={"color":"blue"}),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center",style = {"color":'black'}),
        dbc.Col(html.H4("Review", className="text-center"), width=3),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center"),
        dbc.Col(html.H4("Import", className="text-center"), width=3),
    ],
    
    className="align-items-center",
)


modal = html.Div(
    [
        dbc.Modal(
            [   dbc.ModalHeader(steps_header),
                dbc.ModalBody(
                    [
                        dbc.Row(
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.Row(
                                                dbc.Col(
                                                    html.H5("Drag and drop file", className="text-center"),
                                                    width={"size": 6, "offset": 3},
                                                )
                                            ),
                                            dbc.Row(
                                                dbc.Col(
                                                    dbc.Button("Select files", color="primary", className="mb-3"),
                                                    width={"size": 6, "offset": 3},
                                                ),
                                            ),
                                            dbc.Row(
                                                dbc.Col(
                                                    [
                                                        html.P("Max file size: 200 MB"),
                                                        html.P("Upload Limit: 2 Left"),
                                                        html.P("File types allowed: .xlsx, .csv"),
                                                    ],
                                                    width={"size": 6, "offset": 3},
                                                ),
                                            ),
                                        ]
                                    ),
                                    className="mb-4",
                                    style={"textAlign": "center"},
                                ),
                                width=12,
                            ),
                        ),
                        dbc.Row(
                            dbc.Col(
                                dbc.Alert(
                                    "ObligationList5.csv uploaded successfully", color="success", dismissable=True
                                ),
                                width={"size": 6, "offset": 3},
                            ),
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
    ]
    
)

