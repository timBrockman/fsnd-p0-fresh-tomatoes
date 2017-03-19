import media
import fresh_tomatoes

faster_pussycat = media.Movie("Faster, Pussycat! Kill! Kill!",
                              "Go Go Girls run amok",
                              "http://t0.gstatic.com/images?q=tbn:ANd9GcSe9_tk9j-Pzg6Qa0"
                              "__ihIc1G0jxpubmiIksLa0NF_Nl4GIRV9y",
                              "https://www.youtube.com/watch?v=tiE4QWPDxus")

kellys_heros = media.Movie("Kelly's Heros",
                           "World War 2 from a 70's perspective",
                           "http://imgc.allpostersimages.com/images/P-473-488-90"
                           "/56/5665/DR1UG00Z/posters/kelly-s-heroes.jpg",
                           "https://www.youtube.com/watch?v=Iby1Ni0VJxg")

extreme_prejudice = media.Movie("Extreme Prejudice",
                                "A Texas Ranger and a ruthless narcotics kingpin",
                                "https://images-na.ssl-images-amazon.com/images/"
                                "M/MV5BNDcwNTM2MTU3OF5BMl5BanBnXkFtZTYwNDgzMzc4._V1_.jpg",
                                "https://www.youtube.com/watch?v=vCqRCutZsGo")

movies = [faster_pussycat, extreme_prejudice, kellys_heros]

fresh_tomatoes.open_movies_page(movies)

