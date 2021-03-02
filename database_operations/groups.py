from database_operations import CUD_query, select_query

#   Naujo table kodo kopijavimo todo is seno table:
#   Persikopijuojam
#   Pakeiciam funkciju/metodu pavadinimus i naujo table pavadinima
#   Persivadinam table uzklausose
#   Persivadinam table lauku pavadinimus pagal nauja table
#   persivadinam parametrus funkcijoje ir uzklausos parametruose
#
def create_group_table():
    query = """CREATE TABLE IF NOT EXISTS GroupU(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name TEXT)
                """
    CUD_query(query)


def create_group(name):
    query = "INSERT INTO GroupU(name) VALUES (%s)"
    params = [name]
    CUD_query(query, params)


def select_group(id):
    query = "SELECT * FROM GroupU WHERE id = %s"
    params = [id]
    select_query(query, params)


def update_group_name(id, new_group_name):
    query = "UPDATE GroupU SET name = %s WHERE id = %s"
    params = [new_group_name, id]
    CUD_query(query, params)


def delete_group_by_id(id):
    query = "DELETE FROM GroupU WHERE id = %s"
    params = [id]
    CUD_query(query, params)
