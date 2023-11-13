from lib.peep import Peep


class PeepRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            item = Peep(row["id"], row["posted_on"],
                        row["peep"], row["user_name"], row["user_id"])
            peeps.append(item)
        return peeps

    def create_new_peep(self, peep):
        rows = self._connection.execute('INSERT INTO peeps (posted_on, peep, user_id) VALUES (%s, %s, %s) RETURNING id', [
            peep.posted_on, peep.peep, peep.peep_id])
        row = rows[0]
        peep.id = row["id"]
        return peep

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
