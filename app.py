import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load the processed sales data
df = pd.read_csv('data/processed_sales.csv')

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date to get total sales
df_grouped = df.groupby('date')['sales'].sum().reset_index()

# Create line chart
fig = px.line(df_grouped, x='date', y='sales', title='Total Daily Sales Over Time')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales ($)',
    shapes=[
        dict(
            type="line",
            x0="2021-01-15", x1="2021-01-15",
            y0=0, y1=df_grouped['sales'].max(),
            line=dict(color="Red", dash="dash"),
        )
    ],
    annotations=[
        dict(
            x='2021-01-15',
            y=df_grouped['sales'].max(),
            xref='x', yref='y',
            text="Price Increase",
            showarrow=True,
            arrowhead=1
        )
    ]
)

# Create Dash app
app = dash.Dash(__name__)
app.title = "Sales Visualiser"

app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Visualiser'),
    html.P(children='Sales over time. Pink Morsel price increased on Jan 15, 2021.'),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
