from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc

######## TABLE #########
# Define table data
table_data = [
    ["", "Topic" , "Question", "Answer", "Workspace Name", "Document", "Date", "Client Name"],
    [
        dcc.Checklist(options=[{"label": "", "value": 1}]),
        'Topic 1',
        "What is the client name?",
        "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Contract Analysis",
        "Contract_1,pg 2",
        "2024-10-03",
        "ABC Company LLC",
    ],
    [
        dcc.Checklist(options=[{"label": "", "value": 2}]),
        'Topic 2',
        "What is the start date?",
        "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Contract Analysis",
        "Contract_5,pg 2",
        "2024-10-03",
        "ABC Company LLC",
    ],
    [
        dcc.Checklist(options=[{"label": "", "value": 3}]),
        'Topic 2',
        "Who are the key stakeholders?",
        "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "LOP Obligation",
        "LoP_33,pg 2",
        "2024-10-03",
        "ABC Company LLC",
    ],
    [
        dcc.Checklist(options=[{"label": "", "value": 4}]),
        'Topic 3',
        "When is the end date?",
        "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "SOW Obligations",
        "SOW_4,pg 2",
        "2024-10-03",
        "ABC Company LLC",
    ],
]

# Define table headers and rows
table_headers = [html.Th(header) for header in table_data[0]]
table_rows = [[html.Td(cell) for cell in row] for row in table_data[1:]]

# Create table
table = html.Table(
    [
        html.Thead(html.Tr(table_headers)),
        html.Tbody([html.Tr(row) for row in table_rows]),
    ],
    className="custom-table",
)


layout = html.Div(
    [
        html.Div(
            id="sidebar-chat-history",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-chat-history",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-chat-history",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-chat-history"),
                html.Div(
                    id="sidebar-content-chat-history",
                    children=[
                        html.P(html.A("Workspaces", href="/")),
                        html.P(html.A("Chat History", href="/chat_history",style = {"color":"blue"})),
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
                    id="sidebar-content-chat-history-2",
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
            id="chat-history-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                
                html.P(
                    "Chat History",
                    id="chat-history-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                
                html.P(id="chat-history-text"),
                dbc.Row(
                    id="chat-history-button-container",  # Unique ID
                    children=[
                        dbc.Col(
                            dbc.Button(
                                "Export",
                                color="primary",
                                className="sidebar-button",
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
                    "Questions", style={"paddingLeft": "2rem", "fontSize": "1.25rem"}
                ),
                html.Div(table, className="table-container"),
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


@callback(
    Output("sidebar-chat-history", "className"),
    Output("sidebar-toggle-button-container-chat-history", "style"),
    Output("sidebar-toggle-button-container-chat-history", "children"),
    Output("sidebar-content-chat-history", "style"),
    Output("sidebar-content-chat-history-2", "style"),
    Output("contract-heading-chat-history", "style"),
    Output("chat-history-heading", "style"),
    Output("chat-history-text", "style"),
    Output("chat-history-content", "style"),
    Input("sidebar-toggle-button-container-chat-history", "n_clicks"),
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
            {},
            {"paddingLeft": "20rem", "overflow": "hidden"},
        )
@callback(
    Output("url-chat-history", "pathname"),
    Input("docu-chat-button-chat-history", "n_clicks"),
    prevent_initial_call=True,
)
def navigate_to_docu_chat(n_clicks):
    if n_clicks:
        return "/docu_chat"
    return "/"
