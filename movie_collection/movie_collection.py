# Simple movie collection (adding, finding a movie and listing all movies)

# --- An empty list is created to store the elements (movies) ---
movies = []


# --- Defining functions for each functionality

def add_movie():
    new_title = input("Write the movie title: ")
    new_director = input("Write the movie director: ")
    new_release = input("Write the movie release year: ")

    new_movie = {
        "title": new_title,
        "director": new_director,
        "release": new_release
    }

    movies.append(new_movie)

    print("New movie added successfully")


def find_movie():
    movie_title = input("Please, give me the title of the movie that you want to find: ")
    for movie in movies:
        if movie['title'] == movie_title:
            print(f"'{movie['title']}', directed by {movie['director']}, {movie['release']}")


def list_movie():
    for movie in movies:
        print(f"'{movie['title']}', directed by {movie['director']}, {movie['release']}")


# --- Managing the user input ---

# Python has first class functions (a function is treated as any other type),
# therefore we create a dictionary to pair the user input indirectly with corresponding function
options = {
    "a": add_movie,
    "l": list_movie,
    "f": find_movie
}

# --- Asking for user input ---
MENU = """ Please choose one of the options below:
a - add a new movie
l - list the movies
f - find a movie 
q - quit 
"""


def menu():
    user_input = input(MENU)

    while user_input != "q":
        if user_input in options:
            select_function = options[user_input]
            select_function()

        else:
            print("Wrong input, try again")

        user_input = input(MENU)


menu()
