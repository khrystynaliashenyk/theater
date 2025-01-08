from django.urls import path
from .views import actor_list, actor_detail, actor_create_or_edit, actor_delete
from .views import director_list, director_detail, director_create_or_edit, director_delete
from .views import theater_list, theater_detail, theater_create_or_edit, theater_delete
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('actors/', actor_list, name='actor_list'),
    path('actors/<int:pk>/', actor_detail, name='actor_detail'),
    path('actors/create/', actor_create_or_edit, name='actor_create'),
    path('actors/edit/<int:pk>/', actor_create_or_edit, name='actor_edit'),
    path('actors/delete/<int:pk>/', actor_delete, name='actor_delete'),

    path('directors/', director_list, name='director_list'),
    path('directors/<int:pk>/', director_detail, name='director_detail'),
    path('directors/create/', director_create_or_edit, name='director_create'),
    path('directors/edit/<int:pk>/', director_create_or_edit, name='director_edit'),
    path('directors/delete/<int:pk>/', director_delete, name='director_delete'),

    path('theaters/', theater_list, name='theater_list'),
    path('theaters/<int:pk>/', theater_detail, name='theater_detail'),
    path('theaters/create/', theater_create_or_edit, name='theater_create'),
    path('theaters/edit/<int:pk>/', theater_create_or_edit, name='theater_edit'),
    path('theaters/delete/<int:pk>/', theater_delete, name='theater_delete'),
    path('api/buyers/total-count/', views.total_buyer_count, name='total_buyer_count'),
    path('api/plays/genre-count/', views.play_count_by_genre, name='play_count_by_genre'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/plays/avg-duration-by-genre/', views.avg_duration_by_genre, name='avg_duration_by_genre'),

    path('plotly-dashboard/', views.dashboard_view_plotly, name='plotly_dashboard'),

    path('api/plays/avg-ticket-price/', views.avg_ticket_price_by_play, name='avg_ticket_price_by_play'),
    path('api/plays/total-revenue/', views.total_revenue_by_play, name='total_revenue_by_play'),
    path('api/plays/by-director/', views.plays_by_director, name='plays_by_director'),
    path('api/seats/occupancy/', views.seat_occupancy_per_hall, name='seat_occupancy_per_hall'),
    path('api/plays/count-by-year/', views.play_count_by_year, name='play_count_by_year'),
   # path('dashboard1/', views.dashboard_view1, name='dashboard1'),
    path('dashboard/plotly/', views.plotly_dashboard_view, name='dashboard_plotly'),
    path('dashboard/bokeh/', views.bokeh_dashboard_view, name='dashboard_bokeh'),
    path('api/ticket-price-statistics/', views.ticket_price_statistics, name='ticket_price_statistics'),
    path('dashboard/plotly1/', views.ticket_price_dashboard_view, name='ticket_price_dashboard_plotly'),
    path('dashboard/bokeh1/', views.ticket_price_dashboard_view_bokeh, name='bokeh_dashboard'),

]

