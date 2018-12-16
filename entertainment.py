import media
import fresh_tomatoes
toy_story = media.Movie("Toy story", 
			"a story of a boy and his toys that come to life",
			"http://172.104.50.103/static/images/f4.jpg",
			"https://www.youtube.com/watch?v=N4mEzFDjqtA")

print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
			"A marine on an alien planet",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzOIgHHbdAL_o84YhGw6PGgdMcK99bbnfde6QdSuIzouXvE6oyzw",
			"https://www.youtube.com/watch?v=N4mEzFDjqtA")


print(avatar.storyline)
#avatar.show_trailer()

school_of_rock =media.Movie("school of rock", "using rock music to learn",
				"http://webneel.com/sites/default/files/images/blog/t-natuwal.jpg",
				"https://www.youtube.com/watch?v=3PsUJFEBC74")
print(school_of_rock)
#school_of_rock.show_trailer()

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
			"https://cdn-images-1.medium.com/max/2000/1*brjYnVlXwM3j_SWXImT0Rg.png",
			"https://www.youtube.com/watch?v=N4mEzFDjqtA")
print(ratatouille)
#ratatouille.show_trailer()

midnight_in_paris = media.Movie("midnight in paris","going back to meet authors ",
			"https://cdn-images-1.medium.com/max/2000/1*brjYnVlXwM3j_SWXImT0Rg.png",
			"https://www.youtube.com/watch?v=N4mEzFDjqtA")
print(midnight_in_paris)
#midnight_in_paris.show_trailer()

hunger_games = media.Movie("Hunger games", "A really real reality show",
			"https://cdn-images-1.medium.com/max/2000/1*brjYnVlXwM3j_SWXImT0Rg.png",
			"https://www.youtube.com/watch?v=N4mEzFDjqtA")

print(hunger_games)
#hunger_games.show_trailer()

movies = [toy_story, avatar, school_of_rock , ratatouille ,midnight_in_paris ,hunger_games ]
fresh_tomatoes.open_movies_page(movies)

