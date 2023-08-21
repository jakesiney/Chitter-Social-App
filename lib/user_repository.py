from lib.user import User


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Create a new user
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (user_name, full_name, email) VALUES (%s, %s, %s) RETURNING id', [
            user.user_name, user.full_name, user.email])
        row = rows[0]
        user.id = row["id"]
        return user

    # # Retrieve all books
    # def all(self):
    #     rows = self._connection.execute('SELECT * from books')
    #     books = []
    #     for row in rows:
    #         item = Book(row["id"], row["title"], row["author_name"])
    #         books.append(item)
    #     return books

    # # Find a single book by its id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author_name"])

    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None
