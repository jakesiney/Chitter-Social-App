from lib.peep import Peep


class PeepRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Create a new user
    def create_new_peep(self, peep):
        rows = self._connection.execute('INSERT INTO peeps (posted_on, peep, user_id) VALUES (%s, %s, %s) RETURNING id', [
            peep.posted_on, peep.peep, peep.peep_id])
        row = rows[0]
        peep.id = row["id"]
        return peep

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
