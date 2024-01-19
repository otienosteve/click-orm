from models import session, Director, Movie

directors = [{
  "id": 1,
  "name": "Matthiew"
}, {
  "id": 2,
  "name": "Archibold"
}, {
  "id": 3,
  "name": "Worthington"
}, {
  "id": 4,
  "name": "Mathilde"
}, {
  "id": 5,
  "name": "Alissa"
}]


# director_list =[]
# for director in directors:
#     new_director = Director(**director)
#     director_list.append(new_director)

# session.add_all(director_list)

movie_directors = [{
  "movie_id": 1,
  "director_id": 2
}, {
  "movie_id": 2,
  "director_id": 4
}, {
  "movie_id": 3,
  "director_id": 2
}, {
  "movie_id": 4,
  "director_id": 5
}, {
  "movie_id": 5,
  "director_id": 3
}, {
  "movie_id": 6,
  "director_id": 3
}, {
  "movie_id": 7,
  "director_id": 2
}, {
  "movie_id": 8,
  "director_id": 4
}, {
  "movie_id": 9,
  "director_id": 2
}, {
  "movie_id": 10,
  "director_id": 1
}]
for mv_dr in movie_directors:
    director = session.query(Director).filter_by(id=mv_dr['director_id']).first()
    movie = session.query(Movie).filter_by(id=mv_dr['movie_id']).first()
    director.movies.append(movie)
    session.commit()



# session.add_all([Director(**director) for director in directors])