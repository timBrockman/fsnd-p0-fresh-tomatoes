"""
entertainment_center.py
creates movie instances and passes to fresh_tomatoes

Dependencies
  media (local)
  fresh_tomatoes (local)
"""
import media
import fresh_tomatoes


def main():
    # the code that gets run
    faster_pussycat = media.Movie("Faster, Pussycat! Kill! Kill!",
                                  "Go Go Girls run amok",
                                  "https://t0.gstatic.com/images?q=tbn"
                                  ":ANd9GcSe9_tk9j-Pzg6Qa0"
                                  "__ihIc1G0jxpubmiIksLa0NF_Nl4GIRV9y",
                                  "https://www.youtube.com/watch?"
                                  "v=tiE4QWPDxus")

    kellys_heros = media.Movie("Kelly's Heros",
                               "World War 2 from a 70's perspective",
                               "https://s-media-cache-ak0.pinimg.com/originals"
                               "/d7/86/e8/d786e83667e6d2bafb62a5e88dcb7df7"
                               ".jpg",
                               "https://www.youtube.com/watch?v=Iby1Ni0VJxg")

    extreme_prejudice = media.Movie("Extreme Prejudice",
                                    "A Texas Ranger and a ruthless narcotics"
                                    " kingpin",
                                    "https://images-na.ssl-images-amazon.com/"
                                    "images/M/MV5BNDcwNTM2MTU3OF5BMl5BanBnXkFt"
                                    "ZTYwNDgzMzc4._V1_.jpg",
                                    "https://www.youtube.com/watch?"
                                    "v=vCqRCutZsGo")

    # store movie instances in an array
    movies = [faster_pussycat, extreme_prejudice, kellys_heros]

    # create fresh tomatoes page from instances
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
