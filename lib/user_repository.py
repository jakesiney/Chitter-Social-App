from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        rows = self._connection.execute('INSERT INTO users (user_name, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
            user.user_name, user.first_name, user.last_name, user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return user

    def get_by_username(self, user_name):
        rows = self._connection.execute(
            'SELECT * from users WHERE user_name = %s', [user_name])
        if rows:
            row = rows[0]
            return User(row["id"], row["user_name"], row["first_name"], row["last_name"], row["email"], row["password"])
        else:
            return None

    def validate_login(self, user_name, password):
        rows = self._connection.execute(
            'SELECT * from users WHERE user_name = %s AND password = %s', [user_name, password])
        if len(rows) == 1:
            return True
        else:
            return False

    def get_by_id(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        if rows:
            row = rows[0]
            return User(row["id"], row["user_name"], row["first_name"], row["last_name"], row["email"], row["password"])
        else:
            return None

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
