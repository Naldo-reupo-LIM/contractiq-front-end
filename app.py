from dash import Dash, dcc, html, Input, Output, callback
from pages import workspaces, chat_history,docu_chat,feedback,workspace_detail,login,user_account,manage_uploads,b9,c9
import dash_bootstrap_components as dbc

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
        'https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css',
        "styles.css",  # Link to the CSS file
    ])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/docu_chat':
        return docu_chat.layout
    elif pathname == '/chat_history':
        return chat_history.layout
    elif pathname == '/feedback':
        return feedback.layout
    elif pathname == '/workspace_detail':
        return workspace_detail.layout
    elif pathname == '/user_account':
        return user_account.layout
    elif pathname == '/workspaces':
        return workspaces.layout
    elif pathname == '/manage_uploads':
        return manage_uploads.layout
    elif pathname == '/b9':
        return b9.layout
    elif pathname == '/c9':
        return c9.layout
    else:
        return login.layout


if __name__ == '__main__':
    app.run(debug=True)