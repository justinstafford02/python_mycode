#!/usr/bin/env python3

def get_user_info():
    # Get user's name input
    name = input("What is your name? ")

    valid_age = False
    while not valid_age:
        # Get user's age input
        age = input("What is your age? ")
        try:
            # Try to convert the entered age into an integer
            age = int(age)
            valid_age = True
        except ValueError:
            # Handle age is not a valid integer
            print("Invalid input. Please enter a valid age (integer).")

    # Get user favorite movie 
    movie = input("What is your favorite movie? ")
    capitalized_movie = movie.capitalize()

    # Get movie's genre 
    genre = input("What is the genre of this movie?")

    # Get actor name from movie
    actor = input("Name an actor from this movie?")

    # Create the finalized info string (f-string)
    info = f"Name: {name}, Favorite Movie: {capitalized_movie} Genre: {genre}, Actor: {actor}"

    # Print the user's information
    print(info)

# Call the function to run the program
get_user_info()

