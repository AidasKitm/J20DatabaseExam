from database_operations import CUD_query, select_query

def create_user_table():
    #     username,password,firstname,lastname,
    query = """CREATE TABLE IF NOT EXISTS User(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username TEXT,
                password TEXT,
                first_name TEXT,
                last_name TEXT)"""
    CUD_query(query)

def create_user(username ,password ,first_name ,last_name):
    query = "INSERT INTO User(username,password,first_name,last_name) VALUES (%s,%s,%s,%s)"
    params = [username ,password ,first_name ,last_name]
    CUD_query(query ,params)

def select_user(id):
    query = "SELECT * FROM User WHERE id = %s"
    params = [id]
    select_query(query, params)

def update_user_last_name(id ,new_last_name):
    query = "UPDATE User SET last_name = %s WHERE id = %s"
    params = [new_last_name ,id]
    CUD_query(query, params)

def delete_user_by_id(id):
    query = "DELETE FROM User WHERE id = %s"
    params = [id]
    CUD_query(query, params)

