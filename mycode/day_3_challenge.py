#!/usr/bin/env python3

def get_user_info():
    # After watching Andy's example, I added a list ("Thank you, Andy")
    user_info = []
    # Get user's name input
    name = input("What is your name? ")
    user_info.append(name) # append name into user_info list
    
    valid_age = False
    while not valid_age:
        # Get user's age input
        age = input("What is your age? ")
        user_info.append(age)
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
    user_info.append(capitalized_movie)

    # Get movie's genre 
    genre = input("What is the genre of this movie?")
    user_info.append(genre)

    # Get actor name from movie
    actor = input("Name an actor from this movie?")
    user_info.append(actor)

    # Create the finalized info string (f-string)
    info = f"Name: {name}, Favorite Movie: {capitalized_movie} Genre: {genre}, Actor: {actor}"

    # Print the user's information
    print("User Info List: ", user_info)

# Call the function to run the program
get_user_info()

