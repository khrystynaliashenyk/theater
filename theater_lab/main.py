# main.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theater_lab.settings')

django.setup()

from context import Context

def call_repository_methods():
    facade = Context()

    print("Directors:")
    directors = facade.directors.get_all()
    for director in directors:
        print(director)
    print("--------------------------------")
    print(facade.directors.get_by_id(1))
    print("--------------------------------")
    print(facade.directors.create("John", "Doe", "1980-01-01"))

    print("\nTheaters:")
    theaters = facade.theaters.get_all()
    for theater in theaters:
        print(theater)
    print("--------------------------------")
    print(facade.theaters.get_by_id(1))
    print("--------------------------------")
    print(facade.theaters.create("Royal Theater", "123 Main St", 5))

    print("\nActors:")
    actors = facade.actors.get_all()
    for actor in actors:
        print(actor)
    print("--------------------------------")
    print(facade.actors.get_by_id(1))
    print("--------------------------------")
    print(facade.actors.create("Jane", "Smith", "1985-05-15"))

if __name__ == "__main__":
    call_repository_methods()
