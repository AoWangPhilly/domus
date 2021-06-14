import sqlite3
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import datetime as dt

conn = sqlite3.connect('sqlite/temperature_and_humidity.db')
room_metrics = pd.read_sql_query('SELECT * FROM room_metrics', conn)
openweather = pd.read_sql_query('SELECT * FROM openweather', conn)

openweather['date'] = pd.to_datetime(openweather['date']).dt.strftime('%m/%d/%y %H:%M')
room_metrics['date'] = pd.to_datetime(room_metrics['date'])

conn.close()

fig = px.line(room_metrics, x='date', y='temperature', title='Temperature (°C)')


navbar = dbc.NavbarSimple(brand='Dashboard', brand_href='#', color='primary', dark=True)

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(children=[
	html.H1(children='domus'),
	navbar,
	dbc.Card(
		dbc.CardBody(
			dcc.Graph(
        			id='example-graph',
        			figure=fig,
				config={"displayModeBar": False}
    			)
		),
		className='mb-3'
	),
	dbc.Card(
		dbc.CardBody(
			dash_table.DataTable(
    				id='table',
    				columns=[{"name": i, "id": i} for i in openweather.columns],
    				data=openweather.to_dict('records')
			)
		),
		className='mb-3'
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)
	# print(room_metrics)
	# print(room_metrics.dtypes)



















