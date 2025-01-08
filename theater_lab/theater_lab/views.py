from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from context import Context
from serializers import (DirectorSerializer, TheaterSerializer, HallSerializer,
                          ActorSerializer, PlaySerializer, RoleSerializer, BuyerSerializer,
                          SeatSerializer, ScheduleSerializer, TicketSerializer)
context = Context()

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = context.directors.get_all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = context.theaters.get_all()
    serializer_class = TheaterSerializer
    permission_classes = [IsAuthenticated]

class HallViewSet(viewsets.ModelViewSet):
    queryset = context.halls.get_all()
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticated]

class ActorViewSet(viewsets.ModelViewSet):
    queryset = context.actors.get_all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]

class PlayViewSet(viewsets.ModelViewSet):
    queryset = context.plays.get_all()
    serializer_class = PlaySerializer
    permission_classes = [IsAuthenticated]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = context.roles.get_all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = context.buyers.get_all()
    serializer_class = BuyerSerializer
    permission_classes = [IsAuthenticated]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = context.seats.get_all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = context.schedules.get_all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = context.tickets.get_all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


