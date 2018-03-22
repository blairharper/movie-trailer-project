# Import dependencies
import media
import fresh_tomatoes

# List of good movies as instances of the media.Movie class
journey = media.Movie("The Hundred-Foot Journey", 
					"The Kadam family leaves India for France where they open"
					"a restaurant directly across the road from Madame Mallory's Michelin-starred eatery.",
					"https://upload.wikimedia.org/wikipedia/en/1/11/The_Hundred_Foot_Journey_%28film%29_poster.jpg",
 					"https://www.youtube.com/watch?v=MWo67uhzoQg")


avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

shape_of_water = media.Movie("The Shape of Water",
					"At a top secret research facility in the 1960s," 
					"a lonely janitor forms a unique relationship with an amphibious creature" 
					"that is being held in captivity.",
					"https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png",
					"https://www.youtube.com/watch?v=XFYWazblaUA")

death_becomes_her = media.Movie("Death Becomes Her",
					"When a woman learns of an immortality treatment, she sees it as a way to outdo her long-time rival.",
					"https://upload.wikimedia.org/wikipedia/en/8/8a/Death_Becomes_Her.jpg",
					"https://www.youtube.com/watch?v=0jPuZLUY4II")

devil_wears_prada = media.Movie("The Devil Wears Prada",
					"A smart but sensible new graduate lands a job as an assistant to Miranda Priestly," 
					"the demanding editor-in-chief of a high fashion magazine.",
					"https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
					"https://www.youtube.com/watch?v=XTDSwAxlNhc")

girl_gifts = media.Movie("The Girl with All the Gifts",
					"A scientist and a teacher living in a dystopian future embark" 
					"on a journey of survival with a special young girl named Melanie.",
					"https://upload.wikimedia.org/wikipedia/en/c/c7/The_Girl_with_All_the_Gifts_poster.jpg",
					"https://www.youtube.com/watch?v=HjGkB_oWTe0")

cure = media.Movie("A Cure for Wellness",
					"An ambitious young executive is sent to retrieve his company's CEO"
					"from an idyllic but mysterious 'wellness center' at a remote location"
					"in the Swiss Alps, but soon suspects that the spa's treatments are not what they seem.",
					"https://upload.wikimedia.org/wikipedia/en/d/df/CureforWellnessOfficialPoster.jpeg",
					"https://www.youtube.com/watch?v=4mcVodJmBlU")

last_holiday = media.Movie("Last Holiday",
					"Upon learning of a terminal illness, a shy woman (Queen Latifah)"
					" decides to sell off all her possessions and live it up at a posh European hotel.",
					"https://upload.wikimedia.org/wikipedia/en/0/0e/Last_holiday.jpg",
					"https://www.youtube.com/watch?v=fBUcxMNInL8")

# Assign the movies to a list data structure
movies = [journey, girl_gifts, avatar, shape_of_water, death_becomes_her,
		 devil_wears_prada, cure, last_holiday]

# Pass the list of movies to fresh_tomatoes to serve the web page
fresh_tomatoes.open_movies_page(movies)