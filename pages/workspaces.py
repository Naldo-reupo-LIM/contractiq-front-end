from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import dash,api_requests
from pages.workspaces_set_up import modal
######## TABLE #########
# Define table data
# def generate_table(data):
#     table_headers = [
#         "Workspace Name",
#         "# of Documents",
#         "Document Types",
#         "Created By",
#         "Date Created",
#         "Client Name",
#         "Charge Code",
#     ]
#     table_data = [table_headers] + [
#         [
#             project['project_name'],
#             "0",
#             project['document_type'],
#             "ABC",
#             project['created_at'],
#             project['client_name'],
#             project['client_code']
#         ]
#         for project in data
#     ]

#     table_rows = [html.Tr([html.Td(cell) for cell in row]) for row in table_data]

#     return html.Table(
#         [html.Thead(html.Tr([html.Th(header) for header in table_headers])), html.Tbody(table_rows)],
#         className="custom-table",
#     )

def generate_table(data):
    table_headers = [
        '',
        "Workspace Name",
        "# of Documents",
        "Document Types",
        "Created By",
        "Date Created",
        "Client Name",
        "Charge Code",
    ]
    table_data =  [
        [
            'Contract analysis',
            '24',
            'contract',
            'Varun Sharma',
            '3/10/2024',
            'ABC Company LLC',
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
                dbc.NavLink("Workspaces", href="/workspaces", active="exact",style = {"color":"green"}),
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
                        html.P(html.A("Worksapces", href="/",style = {"color":"blue"})),
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
                    "Workspaces",
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
                                        "Create a New Workspace",
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
                html.P(
                    "Workspaces", style={"paddingLeft": "2rem", "fontSize": "1.25rem"}
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
                html.Div(id="table-container", className="table-container"),
                dcc.Interval(id='interval-component', interval=30000, n_intervals=0)
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


@callback(
    Output(
        "sidebar",
        "className",
    ),
    Output("sidebar-toggle-button-container", "style"),
    Output("sidebar-toggle-button-container", "children"),
    Output("sidebar-content", "style"),
    Output("sidebar-content-2", "style"),
    Output("contract-heading", "style"),
    Output("main-content-heading", "style"),
    Output("main-content-text", "style"),
    Output("content", "style"),
    Input("sidebar-toggle-button-container", "n_clicks"),
    prevent_initial_call=True,
    allow_duplicates=True,
)
def toggle_sidebar(n):
    if n and n % 2 != 0:
        return (
            "sidebar collapsed",
            {"display": "flex", "justifyContent": "center"},
            html.Span(
                className="fa-solid fa-chevron-right toggle-icon",
                id="sidebar-toggle-button",
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
                id="sidebar-toggle-button",
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
    Output("url", "pathname"),
    Input("docu-chat-button", "n_clicks"),
    prevent_initial_call=True,
)
def navigate_to_docu_chat(n_clicks):
    if n_clicks:
        return "/docu_chat"
    return "/"


@callback(
    Output("modal", "is_open"),
    [Input("create-workspace-button", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open



@callback(
    Output("modal", "is_open",allow_duplicate=True),
    [Input("create-workspace-button", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open"),
     State("workspace-name", "value"),
     State("workspace-code", "value"),
     State("document-type", "value"),
     State("client-id", "value"),
     State("client-name", "value"),
     State("project-members", "value"),
     State("project-description", "value")],
      prevent_initial_call=True,
)
def toggle_modal_and_create_workspace(n_create_clicks, n_close_clicks, is_open, project_name,client_code, document_type, client_id,client_name, project_members, project_description):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if triggered_id == "create-workspace-button" and n_create_clicks:
        # Send the request to create the workspace
        response = api_requests.create_workspace(project_name,client_code, document_type, client_id,client_name, project_members, project_description)
        if response.status_code == 200:
            return False

    elif triggered_id == "close":
        return False

    return is_open

@callback(
    Output("table-container", "children"),
    Input("content", "children")  # Triggers when content is loaded
)
def update_table(_):
    projects_data = api_requests.get_projects()
    if projects_data:
        return generate_table(projects_data)
    else:
        return "Failed to fetch projects data"
