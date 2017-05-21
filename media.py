"""
IPND Stage 3 - Make Your Own Movie Website
Module - 'media' - defines class Movie() - used to store movie related information
Author - Gianpaolo Impronta
Date - 17/05/17
"""


class Movie:
    """ This class provides a way to store movie related information """

    def __init__(self, movie_tilte, poster_image, trailer_youtube, imdb_rating, year, director, duration, genre):
        """ initialize instance of class Movie """
        self.title = movie_tilte
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating
        self.year = year
        self.director = director
        self.duration = duration
        self.genre = genre
