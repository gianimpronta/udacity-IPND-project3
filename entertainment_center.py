"""
IPND Stage 3 - Make Your Own Movie Website
Module - 'entertainment_center' - driver module
Author - Gianpaolo Impronta
Date - 17/05/17

READTHIS - Run this module, 'entertainment_center', to bring up the movie website
         - 'entertainment_center, 'media' and 'fresh_tomatoes' modules must all be in the same directory
         - modify this module, 'entertainment_center' to add or subtract movies on the movie website
"""

import media
import fresh_tomatoes


fight_club = media.Movie("Fight Club",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "8,8",
                         "1999",
                         "David Fincher",
                         "139",
                         "Drama")

the_godfather = media.Movie("The Godfather",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA",
                            "9,2",
                            "1972",
                            "Francis Ford Coppola",
                            "175",
                            "Crime, Drama")

dark_knight = media.Movie("The Dark Knight",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "9,0",
                          "2008",
                          "Christopher Nolan",
                          "142",
                          "Action, Crime, Drama")

return_king = media.Movie("The Lord of the Rings: The Return of the King",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SY1000_SX668_AL_.jpg",
                          "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
                          "8,9",
                          "2003",
                          "Peter Jackson",
                          "201",
                          "Adventure, Drama, Fantasy")

inception = media.Movie("Inception",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "8,8",
                        "2010",
                        "Christopher Nolan",
                        "148",
                        "Action, Adventure, Sci-Fi")

silence = media.Movie("Silence of the Lambs",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=RuX2MQeb8UM",
                      "8,6",
                      "1991",
                      "Jonathan Demme",
                      "118",
                      "Crime, Drama, Thriller")

movies = [fight_club, the_godfather, dark_knight, return_king, inception, silence]
fresh_tomatoes.open_movies_page(movies)
