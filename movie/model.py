import json
from os import path

from mvc.movie import Actor, Movie


class Model:
    def __init__(self):
        self._dump_filename = "./movies.json"
        self._all_movies = []
        self.load()

    @property
    def all_movies(self):
        return self._all_movies

    @all_movies.setter
    def all_movies(self, value):
        self._all_movies = value

    def dump(self, movie_obj):
        with open(self._dump_filename, "a") as file:
            json.dump(movie_obj.__dict__, file, default=lambda x: x.__dict__)
            file.write("\n")

    def load(self):
        json_movies = []
        self.all_movies = []
        existing_file = path.isfile(self._dump_filename)
        if existing_file:
            with open(self._dump_filename) as file:
                for line in file:
                    dict_movie = json.loads(line)
                    json_movies.append(dict_movie)
            for movie in json_movies:
                actors = []
                for actor in movie["_actors"]:
                    actors.append(Actor(name=actor["_name"],
                                        last_name=actor["_last_name"],
                                        role=actor["_role"]))
                self.all_movies.append(Movie(title=movie["_title"],
                                             date_released=movie["_date_released"],
                                             actors=movie["_actors"]))
        return self.all_movies

    def add_movie(self, movie_obj):
        self.all_movies.append(movie_obj)
        self.dump(movie_obj)
