import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Genre, Book, Review

# Database setup
engine = create_engine('sqlite:///bookhub.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    click.echo(f"User {name} added.")

@cli.command()
@click.argument('name')
def add_genre(name):
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    click.echo(f"Genre '{name}' added.")

@cli.command()
@click.argument('title')
@click.argument('author')
@click.argument('year', type=int)
@click.argument('genre_id', type=int)
@click.argument('user_id', type=int)
def add_book(title, author, year, genre_id, user_id):
    book = Book(title=title, author=author, year=year, genre_id=genre_id, user_id=user_id)
    session.add(book)
    session.commit()
    click.echo(f"Book '{title}' added.")

@cli.command()
@click.argument('book_id', type=int)
@click.argument('user_id', type=int)
@click.argument('rating', type=int)
@click.argument('comment')
def review_book(book_id, user_id, rating, comment):
    review = Review(book_id=book_id, user_id=user_id, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    click.echo("Review added.")

@cli.command()
@click.option('--genre')
def list_books(genre):
    if genre:
        genre_obj = session.query(Genre).filter_by(name=genre).first()
        if not genre_obj:
            click.echo("Genre not found.")
            return
        books = session.query(Book).filter_by(genre_id=genre_obj.id).all()
    else:
        books = session.query(Book).all()
    for book in books:
        click.echo(f"{book.title} by {book.author} ({book.year})")

@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        click.echo(f"Deleted book {book.title}.")
    else:
        click.echo("Book not found.")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()
