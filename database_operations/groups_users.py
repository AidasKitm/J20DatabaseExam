from database_operations import CUD_query, select_query


def create_group_users_table():
    query = """CREATE TABLE IF NOT EXISTS Groupusers(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER,
                group_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (group_id) REFERENCES GroupU(id))
                """
    CUD_query(query)


def create_group_user(user_id, group_id):
    query = "INSERT INTO Groupusers(user_id, group_id) VALUES (%s,%s)"
    params = [user_id, group_id]
    CUD_query(query, params)


def select_group_user(id):
    query = "SELECT * FROM Groupusers WHERE id = %s"
    params = [id]
    select_query(query, params)


def update_group_user(id, new_group_id):
    query = "UPDATE Groupusers SET new_group_id = %s WHERE id = %s"
    params = [new_group_id, id]
    CUD_query(query, params)


def delete_group_user_by_id(id):
    query = "DELETE FROM Groupusers WHERE id = %s"
    params = [id]
    CUD_query(query, params)
