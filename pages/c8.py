from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import dash,api_requests
from pages.d8 import modal2

modal_buttons1 = dbc.Row(
    id = "button-container",
    children=[
        
        dbc.Col(
            html.Div(
                                [
                                    dbc.Button(
                                        "Import",
                                        color="primary",
                                        className="sidebar-button",
                                        id="next-button-2",
                                        style={"width": "204px"},
                                    ),
                                    modal2,
                                ]
                            ),
                            className="d-flex justify-content-end",
        ),
        
    ],
    justify="end",
)

steps_header1 = dbc.Row(
    [
        dbc.Col(html.H4("Upload", className="text-center"), width=3),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center",style = {"color":'black'}),
        dbc.Col(html.H4("Review", className="text-center"), width=3,style={"color":"blue"}),
        dbc.Col(html.I(className="bi bi-arrow-right-circle-fill"), width=1, className="text-center"),
        dbc.Col(html.H4("Import", className="text-center"), width=3),
    ],
    
    className="align-items-center",
)

# Function to create a form input row with an icon
def form_input_row(placeholder_text):
    return dbc.Row(
        [
            
            dbc.Col(
                dbc.Input(placeholder=placeholder_text, type="text"),
                width=11
            ),
            dbc.Col(
                html.Div(
                    className="dustbin-container",
                    children=[
                        html.Span(
                            className="fa fa-trash-alt dustbin-icon"  # Adjust the class name if needed
                        )
                    ],
                ),
                width={"size": 1, "offset": 0},  # Adjust size and offset as needed
                className="d-flex justify-content-center align-items-center"
            )
        ],
        style = {"padding":"2rem"},
        className="mb-3",
    )

modal1 = html.Div(
    [
        dbc.Modal(
            [   dbc.ModalHeader(steps_header1),
                dbc.ModalBody(
                    dbc.Container(  # Use a Container for proper padding and spacing
                        [   dbc.Row(
                            "Review and edit data from [FileName]"
                        ),                            form_input_row("What is the client name?"),
                            form_input_row("What is the start date?"),
                            form_input_row("Who are the key stakeholders?"),
                            form_input_row("When is the end date?"),
                            form_input_row("What is the proposal?"),
                        ],
                        style = {"TextAlign":"center"},
                        fluid=True,
                    ),
                    style={"padding": "2rem","textAlign":"center"},
                    className="d-flex justify-content-between",
                ),
                dbc.ModalFooter(modal_buttons1, style={"borderTop": "none"}),
            ],
            id="modal1",
            is_open=False,
            size="lg",
        ),
    ]
    
)

