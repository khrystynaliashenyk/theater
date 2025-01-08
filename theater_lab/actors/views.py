from django.shortcuts import render, get_object_or_404, redirect
from plotly import plot

from .forms import ActorForm, TheaterForm, DirectorForm
from NetworkHelper import NetworkHelper

def home(request):
    return render(request, 'home.html')

def actor_list(request):
    actors = NetworkHelper.get_list('actors')
    return render(request, 'actors/actor_list.html', {'actors': actors})

def actor_create(request):
    if request.method == "POST":
        form = ActorForm(request.POST)
        if form.is_valid():
            actor_data = form.save(commit=False)
            success = NetworkHelper.create_item('actors', {
                'first_name': actor_data.first_name,
                'last_name': actor_data.last_name,
                'date_of_birth': actor_data.date_of_birth,
            })
            if success:
                return redirect('actor_list')
    else:
        form = ActorForm()

    return render(request, 'actors/actor_create_or_edit.html', {'form': form})

def actor_edit(request, pk):
    actor = NetworkHelper.get_item('actors', pk)
    if not actor:
        return redirect('actor_list')

    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            actor_data = form.save(commit=False)
            success = NetworkHelper.update_item('actors', pk, {
                'first_name': actor_data.first_name,
                'last_name': actor_data.last_name,
                'date_of_birth': actor_data.date_of_birth,
            })
            if success:
                return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)

    return render(request, 'actors/actor_create_or_edit.html', {'form': form})


def actor_detail(request, pk):
    actor = NetworkHelper.get_item('actors', pk)  # Замініть 'actors' на правильний endpoint API
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def actor_delete(request, pk):
    success = NetworkHelper.delete_item('actors', pk)  # Replace 'actors' with the correct endpoint
    if success:
        return redirect('actor_list')
    return render(request, 'actors/', {'message': 'Failed to delete actor'})


from context import Context
context = Context()
def director_list(request):
    directors = context.directors.get_all()
    return render(request, 'directors/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = context.directors.get_by_id(pk)
    return render(request, 'directors/director_detail.html', {'director': director})

def director_create_or_edit(request, pk=None):
    director = context.directors.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director_data = form.save(commit=False)
            if pk:
                context.directors.update(director.id, director_data.first_name, director_data.last_name, director_data.date_of_birth)
            else:
                context.directors.create(director_data.first_name, director_data.last_name, director_data.date_of_birth)
            return redirect('director_list')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'directors/director_create_or_edit.html', {'form': form})

def director_delete(request, pk):
    director = context.directors.get_by_id(pk)
    if request.method == "POST":
        director.delete()
        return redirect('director_list')
    return render(request, 'directors/confirm_delete.html', {'director': director})

def theater_list(request):
    theaters = context.theaters.get_all()
    return render(request, 'theaters/theater_list.html', {'theaters': theaters})

def theater_detail(request, pk):
    theater = context.theaters.get_by_id(pk)
    return render(request, 'theaters/theater_detail.html', {'theater': theater})
def theater_create_or_edit(request, pk=None):
    theater = context.theaters.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = TheaterForm(request.POST, instance=theater)
        if form.is_valid():
            theater_data = form.save(commit=False)
            if pk:
                context.theaters.update(theater.id, theater_data.name, theater_data.address, theater_data.number_of_halls)
            else:
                context.theaters.create(theater_data.name, theater_data.address, theater_data.number_of_halls)
            return redirect('theater_list')
    else:
        form = TheaterForm(instance=theater)
    return render(request, 'theaters/theater_create_or_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ActorForm, TheaterForm, DirectorForm
from NetworkHelper import NetworkHelper

def home(request):
    return render(request, 'home.html')

def actor_list(request):
    actors = NetworkHelper.get_list('actors')
    return render(request, 'actors/actor_list.html', {'actors': actors})


def actor_create_or_edit(request, pk=None):
    actor = NetworkHelper.get_item('actors', pk) if pk else None
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            actor_data = form.save(commit=False)
            if pk:
                success = NetworkHelper.update_item('actors', pk, {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
            else:
                success = NetworkHelper.create_item('actors', {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)

    return render(request, 'actors/actor_create_or_edit.html', {'form': form})


def actor_detail(request, pk):
    actor = NetworkHelper.get_item('actors', pk)  # Замініть 'actors' на правильний endpoint API
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def actor_delete(request, pk):
    # Attempt to delete the actor using the API
    success = NetworkHelper.delete_item('actors', pk)  # Replace 'actors' with the correct endpoint
    if success:
        return redirect('actor_list')
    return render(request, 'actors/', {'message': 'Failed to delete actor'})


from context import Context
context = Context()
def director_list(request):
    directors = context.directors.get_all()
    return render(request, 'directors/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = context.directors.get_by_id(pk)
    return render(request, 'directors/director_detail.html', {'director': director})

def director_create_or_edit(request, pk=None):
    director = context.directors.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director_data = form.save(commit=False)
            if pk:
                context.directors.update(director.id, director_data.first_name, director_data.last_name, director_data.date_of_birth)
            else:
                context.directors.create(director_data.first_name, director_data.last_name, director_data.date_of_birth)
            return redirect('director_list')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'directors/director_create_or_edit.html', {'form': form})

def director_delete(request, pk):
    director = context.directors.get_by_id(pk)
    if request.method == "POST":
        director.delete()
        return redirect('director_list')
    return render(request, 'directors/confirm_delete.html', {'director': director})

def theater_list(request):
    theaters = context.theaters.get_all()
    return render(request, 'theaters/theater_list.html', {'theaters': theaters})

def theater_detail(request, pk):
    theater = context.theaters.get_by_id(pk)
    return render(request, 'theaters/theater_detail.html', {'theater': theater})
def theater_create_or_edit(request, pk=None):
    theater = context.theaters.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = TheaterForm(request.POST, instance=theater)
        if form.is_valid():
            theater_data = form.save(commit=False)
            if pk:
                context.theaters.update(theater.id, theater_data.name, theater_data.address, theater_data.number_of_halls)
            else:
                context.theaters.create(theater_data.name, theater_data.address, theater_data.number_of_halls)
            return redirect('theater_list')
    else:
        form = TheaterForm(instance=theater)
    return render(request, 'theaters/theater_create_or_edit.html', {'form': form})

def theater_delete(request, pk):
    theater = context.theaters.get_by_id(pk)
    if request.method == "POST":
        theater.delete()
        return redirect('theater_list')
    return render(request, 'theaters/confirm_delete.html', {'theater': theater})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from repositories.play_repository import *
from repositories.seat_repository import *
from repositories.buyer_repository import *

@api_view(['GET'])
def total_buyer_count(request):
    total_buyers = get_total_buyer_count()
    return Response(total_buyers)

@api_view(['GET'])
def play_count_by_genre(request):
    queryset = get_play_count_by_genre()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))


from django.shortcuts import render
from .dashboards import *
import pandas as pd
import requests


def dashboard_view(request, plot_play_count_by_genre=None):
    response = requests.get('http://127.0.0.1:8000/theater/api/plays/genre-count/')

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        plot = plot_play_count_by_genre(df)
        return render(request, 'dashboard.html', {'plotly_chart': plot.to_html()})
    else:
        return render(request, 'dashboard.html', {'error': 'Failed to fetch data from API'})


@api_view(['GET'])
def avg_duration_by_genre(request):
    queryset = get_avg_duration_by_genre()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

def dashboard_view_plotly(request, plot_genre_chart=None):
    response = requests.get('http://127.0.0.1:8000/theater/api/plays/avg-duration-by-genre/')

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        plot = plot_genre_chart(df)

        return render(request, 'plotly_dashboard.html', {'plotly_chart': plot.to_html()})
    else:
        return render(request, 'plotly_dashboard.html', {'error': 'Failed to fetch data from API'})


@api_view(['GET'])
def avg_ticket_price_by_play(request):
    queryset = get_avg_ticket_price_by_play()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def total_revenue_by_play(request):
    queryset = get_total_revenue_by_play()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def plays_by_director(request):
    queryset = get_plays_by_director()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def seat_occupancy_per_hall(request):
    queryset = get_seat_occupancy_per_hall()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))
@api_view(['GET'])
def play_count_by_year(request):
    queryset = get_play_count_by_year()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))


import concurrent.futures
import requests
import pandas as pd
import time
import plotly.graph_objs as go
import plotly.express as px


def fetch_api_data(endpoint):
    response = requests.get(f'http://127.0.0.1:8000/theater/api/{endpoint}')
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None


def fetch_all_data_parallel():
    endpoints = ['plays/avg-ticket-price/', 'plays/total-revenue/', 'seats/occupancy/']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_api_data, endpoints))

    return results


def benchmark_parallel_queries(num_threads, queries):
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(fetch_api_data, queries))

    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


def benchmark_performance():
    queries = ['plays/avg-ticket-price/', 'plays/total-revenue/', 'seats/occupancy/']
    times = []

    for num_threads in [1, 2, 4, 8, 16]:
        execution_time = benchmark_parallel_queries(num_threads, queries)
        times.append((num_threads, execution_time))

    return times

def plotly_dashboard_view(request):
    data_avg_ticket_price, data_total_revenue, data_seat_occupancy = fetch_all_data_parallel()

    times = benchmark_performance()
    performance_graph = plot_performance_graph(times)

    plot_avg_ticket_price = plot_avg_ticket_price_by_play(data_avg_ticket_price)
    plot_total_revenue = plot_total_revenue_by_play(data_total_revenue)
    plot_seat_occupancy = plot_seat_occupancy_per_hall(data_seat_occupancy)

    return render(request, 'dashboard_plotly.html', {
        'plot_avg_ticket_price': plot_avg_ticket_price.to_html(),
        'plot_total_revenue': plot_total_revenue.to_html(),
        'plot_seat_occupancy': plot_seat_occupancy.to_html(),
        'performance_graph': performance_graph.to_html()
    })
from bokeh.plotting import figure
def bokeh_dashboard_view(request):
    data_avg_ticket_price = fetch_api_data('plays/avg-ticket-price/')
    data_total_revenue = fetch_api_data('plays/total-revenue/')
    data_seat_occupancy = fetch_api_data('seats/occupancy/')

    if data_avg_ticket_price is not None and data_total_revenue is not None and data_seat_occupancy is not None:
        line_script, line_div = bokeh_line_chart(data_avg_ticket_price)

        pie_script, pie_div = bokeh_pie_chart(data_total_revenue)

        bar_script, bar_div = bokeh_bar_chart(data_seat_occupancy)

        return render(request, 'dashboard_bokeh.html', {
            'line_script': line_script,
            'line_div': line_div,
            'pie_script': pie_script,
            'pie_div': pie_div,
            'bar_script': bar_script,
            'bar_div': bar_div,
        })
    else:
        return render(request, 'dashboard_bokeh.html', {'error': 'Failed to fetch data from API'})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Max, Min
from theater_lab.models import Ticket
import pandas as pd
@api_view(['GET'])
def ticket_price_statistics(request):
    queryset = Ticket.objects.values('schedule__play__title') \
        .annotate(
            avg_price=Avg('price'),
            min_price=Min('price'),
            max_price=Max('price')
        )
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))
def ticket_price_dashboard_view(request):
    ticket_data = fetch_api_data('ticket-price-statistics/')

    if ticket_data is not None:
        avg_ticket_price_plot = plot_avg_ticket_price_by_play(ticket_data)
        ticket_price_range_plot = plot_ticket_price_range(ticket_data)

        return render(request, 'dashboard1.html', {
            'avg_ticket_price_plot': avg_ticket_price_plot.to_html(),
            'ticket_price_range_plot': ticket_price_range_plot.to_html(),
        })
    else:
        return render(request, 'dashboard1.html', {'error': 'Failed to fetch data from API'})

from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import dodge
from bokeh.plotting import figure

def ticket_price_dashboard_view_bokeh(request):
    ticket_data = fetch_api_data('ticket-price-statistics/')

    if ticket_data is not None:
        ticket_price_range_plot = bokeh_ticket_price_range(ticket_data)

        script, div = components(ticket_price_range_plot)

        return render(request, 'dashboard2.html', {
            'ticket_price_range_script': script,
            'ticket_price_range_div': div,
        })
    else:
        return render(request, 'dashboard2.html', {'error': 'Failed to fetch data from API'})  @api_view(['GET'])