class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    # TODO 3) Instantiate a NetflixQueue object.
    # TODO 4) Add your movies to the Netflix queue.
    # TODO 5) Print all the movies in your queue.
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."
    harry_potter = Movie('Harry Potter',4.5)
    print(harry_potter.get_ticket_price())
    parent_trap = Movie('Parent Trap', 5)
    mickey_mouse = Movie ('Mickey Mouse', 1.5)
    iron_man = Movie('Iron Man', 4.5)
    abomindable = Movie('abomindable', 4.75)
    movies = NetflixQueue()
    movies.add_movie(harry_potter)
    movies.add_movie(parent_trap)
    movies.add_movie(mickey_mouse)
    movies.add_movie(iron_man)
    movies.add_movie(abomindable)
    best = movies.get_best_movie()
    print('The best movie is ' + best.title)
    movies.sort_movies_by_rating()
    print('the second best movie is ' + movies.movies[1].title)

