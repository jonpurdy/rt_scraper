
reader = [["name sample", "notes sample"]]


final_list = []

for row in reader:

	movie_name = row[0]
	notes = row[1]
	rating = rt_scraper(movie_name)

	new_row = []

	new_row.append(movie_name)
	new_row.append(notes)
	new_row.append(rating)

	final_list.append(new_row)


# key = movie_name, value = note
notes_dict = {}

# key = movie_name, value = rating
rating_dict = {}

for row in reader:

	movie_name = row[0]
	notes = row[1]
	rating = rt_scraper(movie_name)

	notes_dict[movie_name] = notes
	rating_dict[movie_name] = rating

# notes dict
# key						value
# Lost in Translation		Great movie
# Casino					Great movie as well

# ratings dict
# key						value
# Lost in Translation		95
# Casino					80


for key in notes_dict:

	# key
	# notes_dict[key]