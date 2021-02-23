from movie import Movie, Actor
from movie.view import View


def main():
    view = View()
    print("Here are empty list of movies")
    view.show_all()
    print("Please add the first movie")
    movie_to_add = Movie(
        title="The Imitation Game",
        date_released=2014,
        actors=[
            Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing"),
            Actor(name="Kira", last_name="Knightley", role="Joan Clarke")
        ]
    )
    view.add_movie(movie_obj=movie_to_add)
    view.show_all()

    movie_to_add_two = Movie(
        title="Solaris",
        date_released=1972,
        actors=[
            Actor(name="Donatas", last_name="Banionis",
                  role="Kris Kelvin"),
            Actor(name="Natalya", last_name="Bondarchuk",
                  role="Hari")
        ]
    )
    view.add_movie(movie_obj=movie_to_add_two)
    view.show_all()

    
if __name__ == '__main__':
    main()
    
