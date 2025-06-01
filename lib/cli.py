import click
from models import Base, engine
from helpers import list_books, add_book, delete_book, review_book

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    Base.metadata.create_all(engine)
    click.echo("Database initialized.")

@cli.command()
def books():
    list_books()

@cli.command()
@click.option('--title', prompt='Title')
@click.option('--author', prompt='Author')
@click.option('--year', prompt='Year', type=int)
@click.option('--genre', prompt='Genre')
@click.option('--user', prompt='Username')
def add(title, author, year, genre, user):
    add_book(title, author, year, genre, user)

@cli.command()
@click.argument('book_id', type=int)
def delete(book_id):
    delete_book(book_id)

@cli.command()
@click.argument('book_id', type=int)
@click.option('--rating', prompt='Rating (1–5)', type=int)
@click.option('--review', prompt='Your review')
def review(book_id, rating, review):
    review_book(book_id, rating, review)

if __name__ == '__main__':
    cli()
