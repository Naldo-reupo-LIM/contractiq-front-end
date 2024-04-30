from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import dash,api_requests

modal_buttons2 = dbc.Row(
    children=[
        dbc.Col(
            dbc.Button(
                "Finish",
                id="close",
                className="ms-auto",
                n_clicks=0,
                color="secondary",
                style={"width": "120px"},
            ),
        ),
    ],
    justify="end",
)

steps_header2 = dbc.Row(
    [
        dbc.Col(html.H4("Upload", className="text-center"), width=3),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center",style = {"color":'black'}),
        dbc.Col(html.H4("Review", className="text-center"), width=3),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center"),
        dbc.Col(html.H4("Import", className="text-center"), width=3,style={"color":"blue"}),
    ],
    
    className="align-items-center",
)

modal2 = html.Div(
    [
        dbc.Modal(
            [   dbc.ModalHeader(steps_header2),
                dbc.ModalBody(
                    dbc.Container(  # Use a Container for proper padding and spacing
                        [   dbc.Row(
                                dbc.Col(
                                    html.Div(
                                        [
                                        html.I(className="fa fa-check-circle fa-5x",style = {"color":"green"}), html.H1("Import Complete"),], # 'fa-5x' is for large size
                                        
                                        className="d-flex justify-content-center align-items-center"
                                    ),
                                    width={"size": 12, "offset": 0},
                                    style = {"paddingTop":"15rem"}
                                ),
                                className="mb-4"
                            )
                        ],
                        style = {"TextAlign":"center","width":"100px","height":"670px"},
                        fluid=True,
                    ),
                    style={"padding": "2rem","textAlign":"center"},
                    className="d-flex justify-content-between",
                ),
                dbc.ModalFooter(modal_buttons2, style={"borderTop": "none"}),
            ],
            id="modal2",
            is_open=False,
            size="lg",
        ),
    ]
    
)

