import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_tilte, poster_image, trailer_youtube, imdb_rating, year, director, duration, ):
        """ initialize instance of class Movie """
        self.title = movie_tilte
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating
        self.year = year
        self.director = director
        self.duration = duration

    def show_trailer(self):
        """ Open a browser with movie's trailer """
        webbrowser.open(self.trailer_youtube_url)
