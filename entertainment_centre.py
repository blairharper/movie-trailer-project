import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy, and his toys that come to life.",
 												"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 												"https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
										 "A marine on an alien planet",
										 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
										 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

shape_of_water = media.Movie("The Shape of Water",
														 "At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity.",
														 "https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png",
														 "https://www.youtube.com/watch?v=XFYWazblaUA")

# avatar.show_trailer()
# print(shape_of_water.storyline)
# shape_of_water.show_trailer()

movies = [toy_story, avatar, shape_of_water]
fresh_tomatoes.open_movies_page(movies)