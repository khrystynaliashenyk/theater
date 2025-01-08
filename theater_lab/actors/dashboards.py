from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_avg_ticket_price_by_play(df):
    fig = go.Figure(
        data=[go.Pie(labels=df['schedule__play__title'], values=df['avg_price'], title='Average Ticket Price by Play')])

    slider_steps = [
        {
            'label': f'{i + 1} Plays',
            'method': 'update',
            'args': [
                {
                    'values': [df['avg_price'][:i + 1]],  # Show the first 'i+1' plays
                    'labels': [df['schedule__play__title'][:i + 1]],  # Show labels for the selected number of plays
                },
                {'title': f'Top {i + 1} Plays by Ticket Price'}
            ]
        }
        for i in range(1, len(df))
    ]

    fig.update_layout(
        sliders=[{
            'active': 0,
            'currentvalue': {
                'prefix': 'Number of Plays: ',
                'visible': True
            },
            'steps': slider_steps
        }]
    )

    return fig


def plot_total_revenue_by_play(df):
    fig = px.bar(df, x='schedule__play__title', y='total_revenue', title='Total Revenue by Play')

    fig.update_layout(
        updatemenus=[{
            'buttons': [
                {
                    'label': play,
                    'method': 'update',
                    'args': [
                        {'x': [df[df['schedule__play__title'] == play]['schedule__play__title']],
                         'y': [df[df['schedule__play__title'] == play]['total_revenue']]},
                        {'title': f'Total Revenue for {play}'}
                    ]
                } for play in df['schedule__play__title'].unique()
            ],
            'direction': 'down',
            'showactive': True,
        }]
    )
    return fig


def plot_seat_occupancy_per_hall(df):
    fig = px.pie(df, names='hall__name', values='seat_count', title='Seat Occupancy by Hall')
    return fig

def plot_performance_graph(times):
    num_threads = [item[0] for item in times]
    execution_times = [item[1] for item in times]

    fig = go.Figure(
        data=[go.Scatter(x=num_threads, y=execution_times, mode='lines+markers')],
        layout=go.Layout(
            title="Час виконання залежно від кількості потоків",
            xaxis={'title': 'Кількість потоків'},
            yaxis={'title': 'Час виконання (секунди)'}
        )
    )
    return fig


from math import pi
from bokeh.plotting import figure
from bokeh.embed import components

from bokeh.io import show
from bokeh.models import Slider, ColumnDataSource
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.transform import cumsum
from math import pi

def bokeh_line_chart(df):
    x = df['schedule__play__title']
    y = df['avg_price']

    p = figure(title="Average Ticket Price Trend by Play", x_range=x, height=400, tools="pan,box_zoom,reset,save")
    p.line(x=x, y=y, line_width=2, color="blue", legend_label="Avg Price")
    p.circle(x=x, y=y, size=8, color="red", legend_label="Data Points")

    p.xaxis.major_label_orientation = pi / 4
    p.xaxis.axis_label = "Play Title"
    p.yaxis.axis_label = "Average Price"
    p.legend.location = "top_left"

    script, div = components(p)
    return script, div



from bokeh.models import ColumnDataSource
from bokeh.transform import cumsum
from bokeh.palettes import Category20, Category20c


def bokeh_pie_chart(df):
    df['angle'] = df['total_revenue'] / df['total_revenue'].sum() * 2 * pi
    df['color'] = Category20[len(df)]

    source = ColumnDataSource(df)

    p = figure(height=400, title="Revenue Distribution by Play", toolbar_location=None, tools="hover",
               tooltips="@schedule__play__title: @total_revenue", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white", fill_color='color',
            legend_field='schedule__play__title',
            source=source)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div

def bokeh_bar_chart(df):
    x = df['hall__name']
    y = df['seat_count']

    p = figure(x_range=x, title="Seat Occupancy by Hall", height=400, toolbar_location=None, tools="pan,box_zoom,reset,save")
    p.vbar(x=x, top=y, width=0.8, color="green", legend_field='hall__name')

    p.xaxis.major_label_orientation = pi / 4
    p.xaxis.axis_label = "Hall Name"
    p.yaxis.axis_label = "Number of Seats"
    p.legend.location = "top_left"

    script, div = components(p)
    return script, div
import plotly.graph_objects as go
import plotly.express as px

def plot_avg_ticket_price_by_play1(data):
    fig = px.bar(data, x='schedule__play__title', y='avg_price', title='Average Ticket Price by Play')
    return fig

def plot_ticket_price_range(data):
    fig = px.bar(data,
                 x='schedule__play__title',
                 y=['min_price', 'max_price'],
                 title='Ticket Price Range by Play')
    return fig
import plotly.express as px

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from django.shortcuts import render
import pandas as pd


from bokeh.layouts import column

def bokeh_ticket_price_range(data):
    print(data)

    play_titles = data['schedule__play__title'].tolist()
    min_prices = data['min_price']
    max_prices = data['max_price']

    min_price_source = ColumnDataSource(data={'play_title': play_titles, 'price': min_prices})
    max_price_source = ColumnDataSource(data={'play_title': play_titles, 'price': max_prices})

    min_price_plot = figure(
        x_range=play_titles, height=300, title="Minimum Ticket Price by Play",
        toolbar_location=None, tools=""
    )
    min_price_plot.vbar(x='play_title', top='price', width=0.4, source=min_price_source, color="blue")
    min_price_plot.xaxis.major_label_orientation = 1
    min_price_plot.yaxis.axis_label = 'Price'
    min_price_plot.xaxis.axis_label = 'Play'

    max_price_plot = figure(
        x_range=play_titles, height=300, title="Maximum Ticket Price by Play",
        toolbar_location=None, tools=""
    )
    max_price_plot.vbar(x='play_title', top='price', width=0.4, source=max_price_source, color="green")
    max_price_plot.xaxis.major_label_orientation = 1
    max_price_plot.yaxis.axis_label = 'Price'
    max_price_plot.xaxis.axis_label = 'Play'

    return column(min_price_plot, max_price_plot)

