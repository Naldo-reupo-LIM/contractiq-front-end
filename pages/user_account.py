from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
from pages.add_new_team import modal

def generate_table(data):
    table_headers = [
        '',
        "Team Name",
        "Team Members",
    ]
    table_data =  [
        [
            'Leading Team A',
            'test@abc.com,test2@abc.com',
            
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


layout = html.Div(
    [
        html.Div(
            id="sidebar-user_account",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-user_account",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-user_account",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-user_account"),
                html.Div(
                    id="sidebar-content-user_account",
                    children=[
                        html.P(html.A("Workspaces", href="/")),
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
                    id="sidebar-content-user_account-2",
                    children=[
                        html.P(html.A("Accounts", href="#")),
                        html.P(html.A("Send us a feedback", href="/user_account",style = {"color":"blue"})),
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
            id="user_account-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                
                html.P(
                    "Account",
                    id="user_account-heading",
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
            [
                dbc.Col(
                    [
                        html.Label("User Name"),
                        dbc.Input(
                            id="workspace-name",
                            type="text",
                            placeholder="User Name",
                            className="search-input",
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Email"),
                        dbc.Input(
                            id="workspace-code",
                            type="text",
                            placeholder="Email",
                            className="search-input",
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Member since"),
                        dbc.Input(
                            id="workspace-code",
                            type="text",
                            placeholder="Date",
                            className="search-input",
                        ),
                    ],
                    width=3,
                ),
            ],
            className="mt-3",
            style={"paddingLeft": "25rem", "overflow": "hidden"},
        ),
        dbc.Row(
                    id="button-container",
                    children=[
                        dbc.Col(
                            html.Div(
                                [
                                    dbc.Button(
                                        "add a New Team",
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
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div([
                                    
                                    html.Div(id='table-container', children=generate_table('test'))  # Replace with actual data
                                ]), width=5, className="content-col"),  # Adjust the width as needed
                            ],
                            className="g-0"  # No gutters
                        )
                    ],
                    className="container-fluid main-container",
                    style = {"paddingLeft": "30rem"}
                ),
    ]
)


@callback(
    Output("sidebar-user_account", "className"),
    Output("sidebar-toggle-button-container-user_account", "style"),
    Output("sidebar-toggle-button-container-user_account", "children"),
    Output("sidebar-content-user_account", "style"),
    Output("sidebar-content-user_account-2", "style"),
    Output("contract-heading-user_account", "style"),
    Output("user_account-heading", "style"),
    Output("user_account-content", "style"),
    Input("sidebar-toggle-button-container-user_account", "n_clicks"),
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
