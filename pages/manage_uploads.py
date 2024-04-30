from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import dash,api_requests
from pages.workspaces import toggle_modal
from pages.b8 import modal

def generate_table(data):
    table_headers = [
        '',
        'File Name       ',
        '',
        '',
        'Date Created',
        ''
    ]
    table_data =  [
        [
            'file_name.xlsx',
            '',
            '',
            '3/10/2024',
            ''
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
######## MODELS #########




# Update the sidebar with the relevant links and styling
sidebar_table = html.Div(
    [
        html.H2("ContractIQ", className="sidebar_table-title"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Workspaces", href="/workspaces", active="exact"),
                dbc.NavLink("Chat History", href="/chat-history", active="exact"),
                dbc.NavLink("Manage Uploads", href="/manage-uploads", active="exact"),
                dbc.NavLink("Account", href="/account", active="exact"),
                dbc.NavLink("Send us a feedback", href="/feedback", active="exact"),
            ],
            vertical=True,
            pills=True,
            className="flex-column"
        ),
    ],
    className="sidebar_table"
)

layout = html.Div(
    [
        html.Div(
            id="sidebar",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading"),
                
                html.Div(
                    id="sidebar-content",
                    children=[
                        html.P(html.A("Workspaces", href="/")),
                        html.P(html.A("Chat History", href="/chat_history")),
                        html.P(html.A("Manage Uploads", href="#",style = {"color":"blue"})),
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
                    id="sidebar-content-2",
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
            id="content",
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
                    id="main-content-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                
                html.P(id="main-content-text"),
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
                                        id="download-button",
                                        style={"width": "204px", "background-color": "#FFFFFF","border": "1px solid #000","color":"#000"},
                                    ),
                                    
                                    
                                ]
                            ),
                            className="d-flex justify-content-end",
                            
                        ),
                    ],
                    
                    className="col-flex",
                ),
                html.Div(
                    className="d-flex justify-content-between",
                    style={"paddingLeft": "3rem","paddingDown":"30rem"},
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
                    style = {"paddingLeft": "3rem"}
                ),
                
                html.Div(id="table-container", className="table-container"),
                dcc.Interval(id='interval-component', interval=30000, n_intervals=0)
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


@callback(
    Output("modal1", "is_open"),
    [Input("next-button", "n_clicks"), Input("close", "n_clicks")],
    [State("modal1", "is_open")],
)
def toggle_modal1(n1, n2, is_open):
    toggle_modal(True,True,True)
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("modal1", "is_open",allow_duplicate=True),
    [Input("next-button", "n_clicks"), Input("close", "n_clicks")],
    [State("modal1", "is_open")],
      prevent_initial_call=True,
)
def toggle_modal1_and_create_upload(n_create_clicks, n_close_clicks, is_open, project_name,client_code, document_type, client_id,client_name, project_members, project_description):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if triggered_id == "next-button" and n_create_clicks:
        # Send the request to create the upload
        response = api_requests.create_next()
        if response.status_code == 200:
            return False

    elif triggered_id == "close":
        return False
    toggle_modal(True,True,True)
    return is_open


@callback(
    Output("modal2", "is_open"),
    [Input("next-button-2", "n_clicks"), Input("close", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal2(n1, n2, is_open):
    toggle_modal1(True,True,True)
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("modal2", "is_open",allow_duplicate=True),
    [Input("next-button-2", "n_clicks"), Input("close", "n_clicks")],
    [State("modal2", "is_open")],
      prevent_initial_call=True,
)
def toggle_modal2_and_create_upload(n_create_clicks, n_close_clicks, is_open, project_name,client_code, document_type, client_id,client_name, project_members, project_description):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if triggered_id == "next-button" and n_create_clicks:
        # Send the request to create the upload
        response = api_requests.create_next()
        if response.status_code == 200:
            return False

    elif triggered_id == "close":
        return False
    toggle_modal2(True,True,True)
    return is_open