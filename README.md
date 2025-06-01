# BookHub CLI 📚

**BookHub** is a command-line interface (CLI) application to help users track books, categorize them by genre, leave ratings and reviews, and more—all from the terminal.

## Key Features

- ✅ Add and categorize books
- ✅ Multi-user reading lists
- ✅ Leave ratings and reviews
- ✅ Filter and list by genre or year
- ✅ View reading statistics

## Tech Stack

- Python 3.11
- SQLAlchemy ORM
- Alembic (for migrations)
- Pipenv
- Click
- Tabulate

## Usage

```bash
pipenv install
pipenv shell
python lib/cli.py init-db
python lib/cli.py add
python lib/cli.py books
