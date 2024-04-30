from dash import html, callback, Input, Output, dcc, callback_context, State
import dash_bootstrap_components as dbc
import dash



input_group = dbc.InputGroup(
    [
        dbc.Input(placeholder="Ask a question..."),
        dbc.Button("Send", color="primary", className="me-1"),  # "me-1" for margin-end
        dbc.DropdownMenu(
            label="Select a file",
            children=[
                dbc.DropdownMenuItem("Item 1"),
                dbc.DropdownMenuItem("Item 2"),
                dbc.DropdownMenuItem("Item 3"),
            ],
            color="info",
            className="me-1",  # "me-1" for margin-end
        ),
    ],
    className="mb-3",
)

layout = html.Div(
    [
        html.Div(
            id="sidebar-docu-chat",
            className="sidebar",
            children=[
                html.Div(
                    id="sidebar-toggle-button-container-docu-chat",
                    className="toggle-button",
                    children=html.Span(
                        className="fa-solid fa-chevron-left toggle-icon",
                        id="sidebar-toggle-button-docu-chat",
                        style={
                            "display": "flex",
                            "alignContent": "center",
                            "justifyContent": "flex-end",
                            "alignItems": "center",
                        },
                    ),
                ),
                html.H2("ContractIQ", id="contract-heading-docu-chat"),
                html.Div(
                    id="sidebar-content-docu-chat",
                    children=[
                        html.P(html.A("Workspaces", href="/",style = {"color":"blue"})),
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
                    id="sidebar-content-docu-chat-2",
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
            id="docu-chat-content",
            children=[
                html.Div(
                    className="d-flex justify-content-end align-items-center",
                    style={"paddingRight": "10px"},
                    children=[
                        html.Div(className="circle", children="AS"),
                    ],
                ),
                
                html.P(
                    "Workspaces > Workspaces Detail > DocuChat ",
                    id="docu-chat-heading",
                    className="main-content-heading",
                    style={
                        'backgroundColor': '#EFEFEF', # Replace with the color you want
                        'width': '100%',
                        'padding': '10px 0', # Adjust the padding as needed
                        'textAlign': 'left',
                        
                    }
                ),
                
                html.P(id="docu-chat-text"),
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
                                                    style={"color": "#949494","padding-right": "10rem"},
                                                ),
                                                html.Th(
                                                    "Client Name",
                                                    style={
                                                        "padding-right": "12.5rem",
                                                        "color": "#949494",
                                                    },
                                                ),
                                                html.Th(
                                                    "Charge Code",
                                                    style={"color": "#949494","padding-right": "10rem",},
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td("Contract Analysis"),
                                                html.Td("contract analysis"),
                                                html.Td("pd/docx"),
                                                html.Td("Company ABC"), 
                                                html.Td("9893993")
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

                    style={
                        "padding": "10px",
                        "backgroundColor": "#333333",
                        "color": "white",
                        'display' : 'flex',
                    },
                    children=[
                        html.Div(
                            [html.I(
                                className="fas fa-file-pdf", style={"marginRight": "5px"}
                            ),
                            "Document_Contract_1.pdf"],
                            className='col s12 m6',
                        ),#
                        html.Div(
                                [html.I(
                                    className="fa-solid fa-grip-lines-vertical", style={"marginRight": "5px",'paddingRight':'1rem',"color":"#add8e6"}
                                ),
                                html.I(
                                className="fa-solid fa-arrow-left", style={"marginRight": "5px",'paddingRight':'1rem',"color":"#add8e6"}
                            ),
                            "Document 1 of 5",
                            html.I(
                                className="fa-solid fa-arrow-right", style={"marginRight": "5px",'paddingLeft':'1rem',"color":"#add8e6"}
                            ),],
                            className='col s12 m6',
                        ),
                    ],
                ),
                
                html.Div(
                    style={"position": "relative"},
                    children=[
                        html.Div(
                            [html.Div(
                                style={
                                    "background-color": "#EBEBF5",
                                    "display": "flex",
                                    "align-items": "center",
                                    "padding": "2px",
                                    "justify-content": "space-between",
                                },
                                children=[
                                    html.Div(
                                        children=[
                                            html.I(
                                                id="up-icon",
                                                className="fa-solid fa-angle-up",
                                                style={
                                                    "marginRight": "5px",
                                                    "cursor": "pointer",
                                                },
                                            ),
                                            html.Div(id="number", children="1/100"),
                                            html.I(
                                                id="down-icon",
                                                className="fa-solid fa-angle-down",
                                                style={
                                                    "marginLeft": "5px",
                                                    "cursor": "pointer",
                                                },
                                            ),
                                        ],
                                        className="d-flex justify-content-evenly align-items-center",
                                    ),
                                    html.Div(
                                        children=[
                                            html.I(
                                                id="plus-icon",
                                                className="fa-solid fa-magnifying-glass",
                                                style={
                                                    "marginRight": "5px",
                                                    "cursor": "pointer",
                                                },
                                            ),
                                            html.Div(
                                                id="percent",
                                                children=[
                                                    "100%",
                                                    html.I(
                                                        className="fa-solid fa-caret-down",
                                                        style={"cursor": "pointer"},
                                                    ),
                                                ],
                                            ),
                                            html.I(
                                                id="minus-icon",
                                                className="fa-solid fa-magnifying-glass",
                                                style={
                                                    "marginLeft": "5px",
                                                    "cursor": "pointer",
                                                },
                                            ),
                                        ],
                                        className="d-flex justify-content-evenly align-items-center",
                                    ),
                                    html.Div(
                                        children=[
                                            html.I(
                                                id="inbox",
                                                className="fa-solid fa-inbox",
                                                style={
                                                    "cursor": "pointer",
                                                    "marginRight": "5px",
                                                },
                                            ),
                                            html.I(
                                                id="dots",
                                                className="fa-solid fa-ellipsis-vertical",
                                                style={
                                                    "cursor": "pointer",
                                                    "marginLeft": "5px",
                                                },
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                            html.Div(
                                html.Img(
                                            src="assets/Capture.png",  # Make sure 'your-image.png' is in the 'assets' folder
                                            style={"width": "100%", "height": "50%"},  # Adjust the size as needed
                                        ),
                            )],
                            className="flex-fill",
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginBottom":"30px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                
                                                html.Div(
                                                    "Topic 1",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    className="circle", children="AS"
                                                ),
                                                html.Div(
                                                    "1. What are the client names?",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.P("A: The client is ABC Company LLC"),
                                                        html.P("Searched Documents: Document_contract_1.pdf, page 2; Document_contract_2.pdf,page 3, 4"),
                                                    ],
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex",
                                        ),
                                    ],
                                ),
                                ##### repeat ###
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    className="circle", children="AS"
                                                ),
                                                html.Div(
                                                    "2. What are the client names?",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                
                                                html.Div(
                                                    children=[
                                                        html.P("A: The client is ABC Company LLC"),
                                                        html.P("Searched Documents: Document_contract_1.pdf, page 2; Document_contract_2.pdf,page 3, 4"),
                                                    ],
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex",
                                        ),
                                    ],
                                ),
                                
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginBottom":"30px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                
                                                html.Div(
                                                    "Topic 2",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    className="circle", children="AS"
                                                ),
                                                html.Div(
                                                    "1. What are the client names?",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.P("A: The client is ABC Company LLC"),
                                                        html.P("Searched Documents: Document_contract_1.pdf, page 2; Document_contract_2.pdf,page 3, 4"),
                                                    ],
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex",
                                        ),
                                    ],
                                ),
                                ##### repeat ###
                                html.Div(
                                    style={
                                        "background-color": "#E5ECFF",
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    className="circle", children="AS"
                                                ),
                                                html.Div(
                                                    "2. What are the client names?",
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex align-items-center",
                                        ),
                                    ],
                                ),
                                html.Div(
                                    style={
                                        "padding": "10px",
                                        "marginLeft":"40px"
                                    },
                                    children=[
                                        html.Div(
                                            children=[
                                                
                                                html.Div(
                                                    children=[
                                                        html.P("A: The client is ABC Company LLC"),
                                                        html.P("Searched Documents: Document_contract_1.pdf, page 2; Document_contract_2.pdf,page 3, 4"),
                                                    ],
                                                    style={"marginLeft": "5px"},
                                                ),
                                            ],
                                            className="d-flex",
                                        ),
                                    ],
                                ),
                                

                                html.Div(
                                    style={
                                        "background-color": "white",
                                        "padding": "10px",
                                    },
                                ),

                                html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(dbc.Input(type="text", placeholder="Ask a question..."), width=9),
                                                dbc.Col(dbc.Button("Send", color="primary", className="mb-2", style = {"width":"150px"}), width=3)
                                            ],
                                            className="g-0"
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(width=9),  # Empty column for alignment
                                                dbc.Col(dbc.Button("Select a file", color="info", className="mb-2", style = {"width":"150px"}), width=3)
                                            ],
                                            className="g-0"
                                        )
                                    ],
                                    style={
                                        "background-color": "#00008B",  # This sets the background color to blue
                                        "padding": "10px",  # Add some padding around the entire div
                                        "border-radius": "5px",  # Optional: if you want rounded corners
                                        "color": "white" ,
                                         "marginTop":"100px" # Change text color to white if needed
                                    }
                                ),
                                
                            ],
                            className="flex-fill",
                        ),
                    ],
                    className="d-flex justify-content-between ",
                    
                ),
            ],
            className="content",
            style={"paddingLeft": "20rem", "overflow": "hidden"},
        ),
    ]
)


