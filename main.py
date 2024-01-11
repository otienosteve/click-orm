#!/usr/bin/python3
import click 

from models import User, Director, Movie, session
# create a movie
# add a director
# create a user
# create a director
# associate them 
# display directors, movies and users 


@click.command()
def show_users():
    users = session.query(User).all() 
    click.echo('id  name  email')
    for user in users:
        click.echo(f'|{user.id}|{user.name}|{user.email}|')

@click.command()
def create_user():
    id = click.prompt("Enter user id", type=int)    
    name = click.prompt("Enter name", type=str) 
    email = click.prompt("Enter email", type=str) 
    user = User(id=id, name=name, email=email)
    session.add(user)
    session.commit()
    click.echo('user added successfully')

@click.command()
def show_movies():
    movies = session.query(Movie).all() 
    # click.echo('id    email')
    for movie in movies:
        click.echo(f'|{movie.id}|{movie.name}|{movie.photo_url}|{movie.user.name}')

@click.command()
def create_movie():
    id = click.prompt("Enter movie id", type=int)    
    name = click.prompt("Enter movie name", type=str) 
    photo_url = click.prompt("Enter photo Url", type=str) 
    user_id = click.prompt("Enter User Id", type=int)

    new_movie = Movie(id=id, name=name, photo_url=photo_url, user_id=user_id)
    session.add(new_movie)
    session.commit()
    print("Movie Added Successfully")

# show_users()
# create_user()
# show_movies()
# create_movie()

# if  __name__ == '__main__':
for i in range(1000):
    click.echo('Welcome to Movies Corner')
    click.echo('Select Option To Continue')
    click.echo('1: Create User')
    click.echo('2: Show Users')
    click.echo('3: show movies')
    click.echo('4: create movies')
    click.echo('5: Exit App')
    option = click.prompt("Enter Option", type=int)
    if option == 1:
        create_user()
    elif option == 2:
        show_users()
    elif option == 3:
        show_movies()
    elif option == 4:
        create_movie()
    elif option == 5:
        break
        