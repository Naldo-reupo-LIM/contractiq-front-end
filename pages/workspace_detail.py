from dash import html, callback, Input, Output, dcc, callback_context, State
import dash_bootstrap_components as dbc
import dash


def generate_table(data):
    table_headers = [
        '',
        "Document Name",
        "# of Pages",
        "Document Types",
        "Uploaded By",
        "Date Uploaded",
    ]
    table_data =  [
        [
            'Document 1',
            '24',
            'contract',
            'Varuem Shama',
            '3/10/2021',
            
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

modal_buttons_update = dbc.Row(
    children=[
        dbc.Col(
            dbc.Button(
                "Close",
                id="close-update",
                className="ms-auto",
                n_clicks=0,
                color="secondary",
                style={"width": "120px"},
            ),
        ),
        dbc.Col(
            dbc.Button(
                "Update",
                id="update",
                className="",
                n_clicks=0,
                color="primary",
                style={"width": "120px"},
            ),
        ),
    ],
    justify="end",
)

modal_update = html.Div(
    [
        dbc.Modal(
            [
                dbc.CardHeader(
                    "Update workspace",
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
                                            id="workspace-name-update",
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
                                            id="workspace-code-update",
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
                        # Add more input fields as needed
                    ],
                    style={"padding": "3rem 5rem"},
                ),
                dbc.ModalFooter(modal_buttons_update, style={"borderTop": "none"}),
            ],
            id="modal-update",
            is_open=False,
            size="lg",
        ),
    ],
)


layout = html.Div(
    [
        html.Div(
            id="sidebar-worksapce-detail",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-worksapce-detail",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-worksapce-detail",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-worksapce-detail"),
                html.Div(
                    id="button-container-worksapce-detail",
                    children=[
                        dbc.Button(
                            "Start new DocuChat",
                            color="primary",
                            className="sidebar-button",
                            id="worksapce-detail-button-worksapce-detail",
                        )
                    ],
                    style={"padding": "4rem 3rem 3rem 3rem"},
                ),
                html.Div(
                    id="sidebar-content-worksapce-detail",
                    children=[
                        html.P(html.A("Workspaces", href="/", style = {"color":"blue"})),
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
                    id="sidebar-content-worksapce-detail-2",
                    children=[
                        html.P(html.A("Accounts", href="#")),
                        html.P(html.A("Send us a feedback", href="/feedback")),
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
            id="worksapce-detail-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                html.P(
                    "Workspaces > Workspace Detail ",
                    id="worksapce-detail-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                html.P(id="worksapce-detail-text"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Table(
                                    [
                                        html.Tr(
                                            [
                                                html.Th(
                                                    "Workspace Name",
                                                    style={
                                                        "padding-right": "10rem",
                                                        "color": "#949494",
                                                    },
                                                ),
                                                html.Th(
                                                    "# of documents",
                                                    style={
                                                        "padding-right": "10rem",
                                                        "color": "#949494",
                                                    },
                                                ),
                                                html.Th(
                                                    "Document Type",
                                                    style={"padding-right": "10rem","color": "#949494"},
                                                ),
                                                html.Th(
                                                    "Client Name",
                                                    style={"padding-right": "10rem","color": "#949494"},
                                                ),
                                                html.Th(
                                                    "Charge code",
                                                    style={"color": "#949494"},
                                                )
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td("Contract Analysis"),
                                                html.Td("24"),
                                                html.Td("pd,docx"),
                                                html.Td("052839C"),
                                                html.Td("Company ABC"),
                                            ]
                                        ),
                                    ]
                                ),
                                
                            ],
                            style={"padding": "2rem"},
                        ),
                        
                    ],
                    className="mainbox",
                ),
                html.Div(
                    className="d-flex justify-content-between",
                    style={"padding": "2rem"},
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
                                html.Div(
                                    className="filter-container",
                                    children=[
                                        "Filter",
                                        html.Span(
                                            className="fa-solid fa-caret-down filter-icon",
                                            style={"cursor": "pointer"},
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
                                ]), width=10, className="content-col"),  # Adjust the width as needed
                            ],
                            className="g-0"  # No gutters
                        )
                    ],
                    className="container-fluid main-container"
                ),
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


@callback(
    Output("sidebar-worksapce-detail", "className"),
    Output("sidebar-toggle-button-container-worksapce-detail", "style"),
    Output("sidebar-toggle-button-container-worksapce-detail", "children"),
    Output("sidebar-content-worksapce-detail", "style"),
    Output("sidebar-content-worksapce-detail-2", "style"),
    Output("contract-heading-worksapce-detail", "style"),
    Output("worksapce-detail-heading", "style"),
    Output("worksapce-detail-text", "style"),
    Output("worksapce-detail-content", "style"),
    Input("sidebar-toggle-button-container-worksapce-detail", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_sidebar(n):
    if n and n % 2 != 0:
        return (
            "sidebar collapsed",
            {"display": "flex", "justifyContent": "center"},
            html.Span(
                className="fa-solid fa-chevron-right toggle-icon",
                id="sidebar-toggle-button-worksapce-detail",
            ),
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {},
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
                id="sidebar-toggle-button-worksapce-detail",
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
            {},
            {"paddingLeft": "20rem", "overflow": "hidden"},
        )


@callback(
    Output("url-worksapce-detail", "pathname"),
    Input("worksapce-detail-button-", "n_clicks"),
    prevent_initial_call=True,
)
def navigate_to_docu_chat(n_clicks):
    if n_clicks:
        return "/docu_chat"
    return "/"


