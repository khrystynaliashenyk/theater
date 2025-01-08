from repositories.director_repository import DirectorRepository
from repositories.theater_repository import TheaterRepository
from repositories.hall_repository import HallRepository
from repositories.actor_repository import ActorRepository
from repositories.play_repository import PlayRepository
from repositories.role_repository import RoleRepository
from repositories.buyer_repository import BuyerRepository
from repositories.seat_repository import SeatRepository
from repositories.schedule_repository import ScheduleRepository
from repositories.ticket_repository import TicketRepository

class Context:
    def __init__(self):
        self.directors = DirectorRepository()
        self.theaters = TheaterRepository()
        self.halls = HallRepository()
        self.actors = ActorRepository()
        self.plays = PlayRepository()
        self.roles = RoleRepository()
        self.buyers = BuyerRepository()
        self.seats = SeatRepository()
        self.schedules = ScheduleRepository()
        self.tickets = TicketRepository()