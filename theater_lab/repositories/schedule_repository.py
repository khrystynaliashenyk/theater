from theater_lab.models import Schedule

class ScheduleRepository:
    def get_all(self):
        return Schedule.objects.all()

    def get_by_id(self, schedule_id):
        return Schedule.objects.get(id=schedule_id)

    def create(self, date, time, play, hall):
        schedule = Schedule(date=date, time=time, play=play, hall=hall)
        schedule.save()
        return schedule