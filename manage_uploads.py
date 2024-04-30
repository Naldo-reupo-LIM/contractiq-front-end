from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc


def generate_table(data):
    table_headers = [
        '',
        "Bluck Upload Files",
        "Date",
    ]
    table_data =  [
        [
            'ObligationList.csv',
            '03/12/2024',
            
        ]
        for project in data
    ]

    table_rows =[html.Tr([html.Td( dcc.Checklist(
                options=[
                    {"label": "", "value": '1323'}  # Assuming each project has a unique 'id'
                ],
                value=[],
                id={'type': 'select-checkbox', 'index': '1323'},
                className='workspace-checkbox'
            ))] + [html.Td(cell) for cell in row]) for row in table_data]

    return html.Table(
        [html.Thead(html.Tr([html.Th(header) for header in table_headers])), html.Tbody(table_rows)],
        className="custom-table",
    )

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
                "Next",
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

# Header with the steps and arrow icons
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

layout = html.Div(
    [
        html.Div(
            id="sidebar-manage_uploads",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-manage_uploads",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-manage_uploads",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-manage_uploads"),
                html.Div(
                    id="sidebar-content-manage_uploads",
                    children=[
                        html.P(html.A("Worksapces", href="/")),
                        html.P(html.A("Chat History", href="/chat_history")),
                        html.P(html.A("Manage Uploads", href="#")),
                    ],
                    style={
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "alignItems": "stretch",
                        "paddingTop": "2rem",
                        "cursor": "pointer",
                        "gap": "1rem",
                    },
                    className="sidebar-content",
                ),
                html.Div(
                    id="sidebar-content-manage_uploads-2",
                    children=[
                        html.P(html.A("Accounts", href="#")),
                        html.P(html.A("Send us a feedback", href="/manage_uploads")),
                    ],
                    style={
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "alignItems": "stretch",
                        "paddingTop": "7rem",
                        "cursor": "pointer",
                        "gap": "1rem",
                    },
                    className="sidebar-content",
                ),
            ],
        ),
        html.Div(
            id="manage_uploads-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                
                html.P(
                    "Manage Uploads",
                    id="manage_uploads-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                
                
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
        
        dbc.Row(
                    id="button-container",
                    children=[
                        dbc.Col(
                            html.Div(
                                [
                                    dbc.Button(
                                        "Upload",
                                        color="primary",
                                        className="sidebar-button",
                                        id="create-workspace-button",
                                        style={"width": "204px"},
                                    ),
                                    modal,
                                ]
                            ),
                            className="d-flex justify-content-end",
                        ),
                    ],
                    className="col-flex",
                ),
        dbc.Row(
            id="button-container",
            children=[
                dbc.Col(
                    html.Div(
                        [
                            dbc.Button(
                                "Download Template",
                                color="primary",
                                className="sidebar-button",
                                id="create-workspace-button",
                                style={"width": "204px", "background-color": "#FFFFFF","border": "1px solid #000","color":"#000"},
                            ),
                            modal,
                            
                        ]
                    ),
                    className="d-flex justify-content-end",
                    
                ),
            ],
            
            className="col-flex",
            ),
        html.Div(
                    className="d-flex justify-content-between",
                    style={"paddingLeft": "30rem","paddingDown":"30rem"},
                    children=[
                        html.Div(
                            className="search-filter-container",
                            children=[
                                # Search Container
                                html.Div(
                                    className="search-container",
                                    style={"position": "relative"},
                                    children=[
                                        dbc.Input(
                                            type="text",
                                            placeholder="Search...",
                                            className="search-input",
                                            style={
                                                "border": "2px solid #CCCCCC",
                                                "borderRadius": "5px",
                                                "paddingRight": "12rem",
                                            },
                                        ),
                                        html.Span(
                                            className="fa-solid fa-search search-icon",
                                            style={
                                                "position": "absolute",
                                                "right": "10px",
                                                "top": "50%",
                                                "transform": "translateY(-50%)",
                                                "cursor": "pointer",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="dustbin-container",
                            
                            children=[
                                html.Span(
                                    className="fa-solid fa-trash-alt dustbin-icon"
                                )
                            ],
                        ),
                    ],
                    
                ),    
        html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div([
                                    
                                    html.Div(id='table-container', children=generate_table('test'))  # Replace with actual data
                                ]), width=5, className="content-col"),  # Adjust the width as needed
                            ],
                            style = {"padding":"3rem"},
                            className="g-0"  # No gutters
                        )
                    ],
                    className="container-fluid main-container",
                    style = {"paddingLeft": "30rem"}
                ),
        
    ]
)


@callback(
    Output("sidebar-manage_uploads", "className"),
    Output("sidebar-toggle-button-container-manage_uploads", "style"),
    Output("sidebar-toggle-button-container-manage_uploads", "children"),
    Output("sidebar-content-manage_uploads", "style"),
    Output("sidebar-content-manage_uploads-2", "style"),
    Output("contract-heading-manage_uploads", "style"),
    Output("manage_uploads-heading", "style"),
    Output("manage_uploads-content", "style"),
    Input("sidebar-toggle-button-container-manage_uploads", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_sidebar(n):
    if n and n % 2 != 0:
        return (
            "sidebar collapsed",
            {"display": "flex", "justifyContent": "center"},
            html.Span(
                className="fa-solid fa-chevron-right toggle-icon",
                id="sidebar-toggle-button-chat-history",
            ),
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {},
            {"paddingLeft": "4rem", "overflow": "hidden"},
        )
    else:
        return (
            "sidebar",
            {
                "display": "flex",
                "alignContent": "center",
                "justifyContent": "flex-end",
                "alignItems": "center",
            },
            html.Span(
                className="fa-solid fa-chevron-left toggle-icon",
                id="sidebar-toggle-button-chat-history",
            ),
            {
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "center",
                "alignItems": "stretch",
                "paddingTop": "2rem",
                "cursor": "pointer",
                "gap": "1rem",
            },
            {
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "center",
                "alignItems": "stretch",
                "paddingTop": "7rem",
                "cursor": "pointer",
                "gap": "1rem",
            },
            {"display": "flex", "flexDirection": "column"},
            {},
            {"paddingLeft": "20rem", "overflow": "hidden"},
        )
