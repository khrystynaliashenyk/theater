from theater_lab.models import Play
from django.db.models import Count, Avg, Sum, F
from theater_lab.models import Theater, Director, Play, Actor, Role, Buyer, Ticket, Seat



class PlayRepository:
    def get_all(self):
        return Play.objects.all()

    def get_by_id(self, play_id):
        return Play.objects.get(id=play_id)

    def create(self, title, genre, duration, premiere_date, director=None):
        play = Play(title=title, genre=genre, duration=duration, premiere_date=premiere_date, director=director)
        play.save()
        return play


def get_play_count_by_genre():
    return Play.objects.values('genre').annotate(play_count=Count('id')).order_by('-play_count')

def get_avg_duration_by_genre():
    return Play.objects.values('genre').annotate(avg_duration=Avg('duration')).order_by('-avg_duration')

def get_avg_ticket_price_by_play():
    return Ticket.objects.values('schedule__play__title').annotate(avg_price=Avg('price')).order_by('avg_price')

def get_total_revenue_by_play():
    return Ticket.objects.values('schedule__play__title').annotate(total_revenue=Sum('price')).order_by('-total_revenue')

def get_plays_by_director():
    return Play.objects.values('director__first_name', 'director__last_name').annotate(play_count=Count('id')).order_by('-play_count')

def get_play_count_by_year():
    return Play.objects.extra(select={'year': 'EXTRACT(year FROM premiere_date)'}).values('year').annotate(play_count=Count('id')).order_by('year')
