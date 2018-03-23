# Import dependencies
import webbrowser


# Movie class containing properties of movies
class Movie():
    """Class to ceate a constructor for movies to be passed to fresh_tomatoes

    Attributes:
        title (str): title of movie
        storyline (str): brief storyline of movie
        poster_image: link to poster image to be displayed on movies page
        trailer_youtube: link to youtube trailer to be displayed on click

    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
