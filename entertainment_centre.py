# Import dependencies
import media
import fresh_tomatoes

# List of good movies as instances of the media.Movie class
# Tinyurl.com links are to movie poster images hosted on wikipedia
movie01 = media.Movie("The Hundred-Foot Journey",
                      "The Kadam family leaves India for France.",
                      "https://tinyurl.com/y9bmf4ga",
                      "https://www.youtube.com/watch?v=MWo67uhzoQg")


movie02 = media.Movie("Avatar",
                      "A marine on an alien planet",
                      "https://tinyurl.com/gpoxjtz",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movie03 = media.Movie("The Shape of Water",
                      "At a top secret research facility in the 1960s,"
                      "a lonely janitor forms a unique relationship with an"
                      " amphibious creature that is being held in captivity.",
                      "https://tinyurl.com/y8q3cnpm",
                      "https://www.youtube.com/watch?v=XFYWazblaUA")

movie04 = media.Movie("Death Becomes Her",
                      "When a woman learns of an immortality treatment, she"
                      "sees it as a way to outdo her long-time rival.",
                      "https://tinyurl.com/y9ph3opg",
                      "https://www.youtube.com/watch?v=0jPuZLUY4II")

movie05 = media.Movie("The Devil Wears Prada",
                      "A smart but sensible new graduate lands a job as an"
                      "assistant to Miranda Priestly, the demanding "
                      "editor-in-chief of a high fashion magazine.",
                      "https://tinyurl.com/ycermgv5",
                      "https://www.youtube.com/watch?v=XTDSwAxlNhc")

movie06 = media.Movie("The Girl with All the Gifts",
                      "A scientist and a teacher living in a dystopian future "
                      "embark on a journey of survival with "
                      "a special young girl named Melanie.",
                      "https://tinyurl.com/yawdpnxg",
                      "https://www.youtube.com/watch?v=HjGkB_oWTe0")

movie07 = media.Movie("A Cure for Wellness",
                      "An ambitious young executive is sent to retrieve his "
                      "company's CEO from a mysterious 'wellnes scenter' at a "
                      "remote location in the Swiss Alps, but soon suspects "
                      "that the spa's treatments are not what they seem.",
                      "https://tinyurl.com/y84a2cyz",
                      "https://www.youtube.com/watch?v=4mcVodJmBlU")

movie08 = media.Movie("Last Holiday",
                      "Upon learning of terminal illness, a shy woman decides "
                      "to sell off all her possessions and live it up at a "
                      "posh European hotel.",
                      "https://tinyurl.com/ydz8v4sh",
                      "https://www.youtube.com/watch?v=fBUcxMNInL8")

# Assign the movies to a list data structure
movies = [movie01, movie02, movie03, movie04,
          movie05, movie06, movie07, movie08]

# Pass the list of movies to fresh_tomatoes to serve the web page
fresh_tomatoes.open_movies_page(movies)
