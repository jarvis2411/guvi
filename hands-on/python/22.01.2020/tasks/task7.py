# print the IMDB star rating ( 6.7)
# print the length of the movie

movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [ {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                   {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"} ]
    }
}

print(movie_box["Robin Hood: Men in Tights"]['imdb_stars'])

print(movie_box["Robin Hood: Men in Tights"]['length'])
