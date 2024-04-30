from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc


layout = html.Div(
    [
        html.Div(
            id="sidebar-feedback",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-feedback",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-feedback",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-feedback"),
                html.Div(
                    id="sidebar-content-feedback",
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
                    id="sidebar-content-feedback-2",
                    children=[
                        html.P(html.A("Accounts", href="#")),
                        html.P(html.A("Send us a feedback", href="/feedback",style = {"color":"blue"})),
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
            id="feedback-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                
                html.P(
                    "Feedback",
                    id="feedback-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                
                html.Div(
                    children=[
                        html.H4(
                            "Thank you for your interest in ContractIQ.Please fill out the form below to ",
                         
                        ),
                        html.H4("ask question or report a technical problem."),
                        html.P(
                            "Required fields are marked with asterisk (*)",
                            style={"paddingTop": "2rem"},
                        ),
                    ],
                    style={"padding": "2rem"},
                ),
                html.Div(
                    [
                        dbc.Form(
                            [
                                dbc.Label("Name", html_for="name-input"),
                                dbc.Input(
                                    id="name-input",
                                    type="text",
                                    placeholder="Enter your name",
                                ),
                            ], style={"width":"50%"},
                        ),
                        dbc.Form(
                            [
                                dbc.Label("Email Address", html_for="email-input"),
                                dbc.Input(
                                    id="email-input",
                                    type="email",
                                    placeholder="Enter your email address",
                                ),
                            ],className="mt-3",style={"width":"50%"},
                        ),
                        dbc.Form(
                            [
                                dbc.Label("Subject", html_for="subject-input"),
                                dbc.Input(
                                    id="subject-input",
                                    type="text",
                                    placeholder="Enter the subject",
                                ),
                            ],className="mt-3", 
                        ),
                        dbc.Form(
                            [
                                dbc.Label("Message", html_for="message-textarea"),
                                dbc.Textarea(
                                    id="message-textarea",
                                    placeholder="Enter your message",
                                    style={"height": "100px"},
                                ),
                            ],className="mt-3",  
                        ),
                        dbc.Button("Submit", color="primary", className="mt-3"),
                    ],
                    style={"padding": "0 4rem"},
                ),
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


@callback(
    Output("sidebar-feedback", "className"),
    Output("sidebar-toggle-button-container-feedback", "style"),
    Output("sidebar-toggle-button-container-feedback", "children"),
    Output("sidebar-content-feedback", "style"),
    Output("sidebar-content-feedback-2", "style"),
    Output("contract-heading-feedback", "style"),
    Output("feedback-heading", "style"),
    Output("feedback-content", "style"),
    Input("sidebar-toggle-button-container-feedback", "n_clicks"),
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
