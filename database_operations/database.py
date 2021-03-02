from database_operations.user import *
from database_operations.categories import *
from database_operations.expense import *
from database_operations.groups import *
from database_operations.groups_users import *


# create_user("user","user","user","user")
# create_user("user1","user1","user1","user1")
#
# create_category("savings")
# create_category("food")
#
# create_expense("index500",10,1,1)
#
#
# create_group("nuomininkai")
#
# create_group("seimos_islaidos")
#

def join_expenses_by_user(user_id):
    query = """SELECT User.first_name,Expense.title,amount  FROM Expense
                JOIN User ON User.id = Expense.user_id
                JOIN Categories ON Categories.id = Expense.category_id
                WHERE user_id = %s"""
    params = [user_id]
    select_query(query, params)


def join_grouped_users(group_id):
    query = """SELECT User.first_name, Expense.title,Expense.amount, GroupU.name FROM Groupusers
                JOIN User ON User.id = Groupusers.user_id
                JOIN GroupU ON GroupU.id = Groupusers.group_id
                JOIN Expense ON Expense.user_id = Groupusers.user_id
                WHERE group_id = %s"""
    params = [group_id]
    select_query(query, params)


def select_user_expense_by_date(user_id, date_from="2020-01-01", date_to="2021-01-01"):
    query = """SELECT User.first_name, Expense.amount, Categories.name, Expense.date FROM Expense
                JOIN User ON User.id = Expense.user_id
                JOIN Categories ON Categories.id = Expense.category_id
                WHERE user_id = %s AND Date BETWEEN %s AND %s"""
    params = [user_id, date_from, date_to]
    select_query(query, params)

# create_expense("maistas",10.10,2,2)
# join_expenses_by_user(2)
# join_grouped_users(2)

select_user_expense_by_date(2,"2021-01-01","2022-01-01")


