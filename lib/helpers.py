from models import session, Book, Genre, User
from tabulate import tabulate

def list_books():
    books = session.query(Book).all()
    if books:
        print(tabulate([(b.id, b.title, b.author, b.rating) for b in books], headers=["ID", "Title", "Author", "Rating"]))
    else:
        print("No books found.")

def add_book(title, author, year, genre_name, username):
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)

    user = session.query(User).filter_by(name=username).first()
    if not user:
        user = User(name=username)
        session.add(user)

    book = Book(title=title, author=author, year=year, genre=genre, user=user)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added.")

def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        print(f"Deleted book {book.title}")
    else:
        print("Book not found.")

def review_book(book_id, rating, review):
    book = session.query(Book).get(book_id)
    if book:
        book.rating = rating
        book.review = review
        session.commit()
        print("Review updated.")
    else:
        print("Book not found.")
