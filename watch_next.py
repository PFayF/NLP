'''
This program eads in the movies.txt file. Each separate line is a description of a different
movie.
This program creates a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
The function takes in the description as a parameter and returns the
title of the most similar movie.
The solution is hosted on GitHub.
The link for my remote Git repo is in the semantic_similarity.txt file.
'''
import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.


def recommend_movie(descrip):
    similarity_index = 0.9
    best_movies = []
    token_ = nlp(descrip)
    for index, token in enumerate(movie_desc_list):
        token = nlp(token)
        #print(token.similarity(token_))
        if token.similarity(token_) >= similarity_index:
            print(f"{token.similarity(token_)} is higher than similarity index of 0.9!\n")
            best_movies.append(index)
    print(f"Indexes of the best movies to watch are {best_movies}.\n")
    return best_movies


file_info = open('movies.txt', 'r')
lines = file_info.readlines()
file_info.close()

movie_name_list = []
movie_desc_list = []

for line in lines:
    print(line)
    movie_name, movie_desc = line.split(":")
    movie_name_list.append(movie_name)
    movie_desc_list.append(movie_desc)


movie_description = """Will he save
    their world or destroy it? When the Hulk becomes too dangerous for the
    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
    planet where the Hulk can live in peace. Unfortunately, Hulk land on the
    planet Sakaar where he is sold into slavery and trained as a gladiator."""

movies_to_watch = recommend_movie(movie_description)

print(f"\nYou have watched Planet Hulk, so your recommended movies are:\n")
for item in movies_to_watch:
    print(f"{movie_name_list[item]}\n")