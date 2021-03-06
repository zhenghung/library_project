# Author-based functions


def find_author_id(db, author_name):
    names = author_name.split(" ", 1)
    first_name = names[0].capitalize()
    if len(names) > 1:
        last_name = names[1].capitalize()
    else:
        last_name = ""

    author_id = db.execute("""SELECT id FROM author WHERE first_name = ?
                    AND last_name = ?""", (first_name, last_name)).fetchone()

    if author_id:
        return author_id[0]
    else:
        db.execute("""INSERT INTO author(first_name, last_name)
                   VALUES (?,?)""", (first_name, last_name))
        author_id = db.execute("""SELECT id FROM author WHERE first_name = ?
                               AND last_name = ?""",
                               (first_name, last_name)).fetchone()[0]
        return author_id


def get_author_name_from_id(db, id):
    author_result = db.execute("""SELECT first_name, last_name
                               FROM author
                               WHERE id = ?;""", (id,)).fetchone()
    first_name = author_result['first_name']
    last_name = author_result['last_name']

    author_name = first_name + ' ' + last_name

    return author_name


def get_author_list(db):
    author_results = db.execute("""SELECT DISTINCT author.id FROM author
                                INNER JOIN book on book.author_id = author.id
                                ORDER BY last_name;""").fetchall()

    authors = [{'id': a['id'], 'name': get_author_name_from_id(db, a['id'])}
               for a in author_results]

    return authors
