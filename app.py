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
import base64

def get_room_metrics(db_path='sqlite/temperature_and_humidity.db') -> pd.DataFrame:
	conn = sqlite3.connect(db_path)
	room_metrics = pd.read_sql_query('SELECT rowid, * FROM room_metrics', conn)
	conn.close()

	room_metrics['date'] = pd.to_datetime(room_metrics['date'])
	return room_metrics

room_metrics = get_room_metrics()

fig = px.line(
	room_metrics, 
	x='date', 
	y='temperature',
 	title='Temperature (°C)'
)


# room_metrics['date'] = room_metrics['date'].dt.strftime('%a %b %d %I:%M')

navbar = dbc.Navbar(
	[
		html.A(
			dbc.Row(
				[
					dbc.Col(dbc.NavbarBrand("Dashboard", className="ml-2")),
					dbc.Col(dbc.NavbarBrand("Setup", className="ml-2")),
					dbc.Col(dbc.NavbarBrand("Code Review", className="ml-2")),
					dbc.Col(dbc.NavbarBrand("Future Plans", className="ml-2"))
				],
				align="center",
                no_gutters=True,
			)
		)
	],
)

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(children=[
	html.Div(html.H1('domus', style={'textAlign': 'center'})),
	navbar,
	dcc.Graph(
		id='graph',
		figure=fig,
	),
	dcc.Interval(
		id='interval',
		disabled=False,
		interval=5*60*1000, # in milliseconds
		n_intervals=0
    )
])

@app.callback(Output('graph', 'figure'),
              Input('interval', 'n_intervals'))
def update_metrics(n):
	return px.line(
		get_room_metrics(),
		x='date', 
		y='temperature',
		title='Temperature (°C)'
	)


if __name__ == '__main__':
	app.run_server(debug=True)
	# print(room_metrics)
	# print(room_metrics.dtypes)

