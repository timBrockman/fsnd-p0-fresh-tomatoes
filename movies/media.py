"""
Media.py

Classes
    Movie

Dependencies
    webbrowser
"""
import webbrowser

class Movie(object):
    '''
    This creates a movie objects

    Attributes
        title (str): the title of the movie
        storyline (str): a brief description of the movie
        poster_image_url (str): the url of the movie poster image
        trailer_youtube_url (str): a url of the YouTube trailer
    '''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        A convienient method to preview the trailer in your default browser
        Returns
            (bool) True
        '''
        webbrowser.open(self.trailer_youtube_url)
        return True

  