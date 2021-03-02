from database_operations import CUD_query, select_query
import datetime


def create_expense_table():
    query = """CREATE TABLE IF NOT EXISTS Expense(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                title TEXT,
                amount DECIMAL(10,2),
                date DATETIME,
                user_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (category_id) REFERENCES Categories(id))"""
    CUD_query(query)


def create_expense(title, amount, user_id, category_id):
    date = datetime.date.today()
    query = "INSERT INTO Expense(title,amount,date,user_id,category_id) VALUES (%s,%s,%s,%s,%s)"
    params = [title, amount, date, user_id, category_id]
    CUD_query(query, params)


def select_expense(id):
    query = "SELECT * FROM Expense WHERE id = %s"
    params = [id]
    select_query(query, params)


def update_expense_title(id, new_expense_title):
    query = "UPDATE Expense SET title = %s WHERE id = %s"
    params = [new_expense_title, id]
    CUD_query(query, params)


def delete_expense_by_id(id):
    query = "DELETE FROM Expense WHERE id = %s"
    params = [id]
    CUD_query(query, params)
