from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello from Dash!"),
    html.P("If you see this, your setup is perfect.")
])

if __name__ == '__main__':
    app.run(debug=True)
