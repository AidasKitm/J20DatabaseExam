from database_operations import CUD_query, select_query

def create_categories_table():
    query = """CREATE TABLE IF NOT EXISTS Categories(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name TEXT)"""
    CUD_query(query)


def create_category(name):
    query = "INSERT INTO Categories(name) VALUES (%s)"
    params = [name]
    CUD_query(query, params)


def select_category(id):
    query = "SELECT * FROM Categories WHERE id = %s"
    params = [id]
    select_query(query, params)


def update_category_name(id, new_category_name):
    query = "UPDATE Categories SET name = %s WHERE id = %s"
    params = [new_category_name, id]
    CUD_query(query, params)


def delete_category_by_id(id):
    query = "DELETE FROM Categories WHERE id = %s"
    params = [id]
    CUD_query(query, params)

