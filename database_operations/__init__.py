import pymysql

class DatabaseContextManager:
    def __init__(self,select_query=False):
        self.select_query = select_query

    def __enter__(self):
        self.connection = pymysql.connect(user="root", password="root", host="localhost", database="finance")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.select_query == False:
            self.connection.commit()
        self.connection.close()

def CUD_query(query, params=None):
    with DatabaseContextManager() as cursor:
        cursor.execute(query,params)

def select_query(query, params=None):
    with DatabaseContextManager(select_query=True) as cursor:
        cursor.execute(query,params)
        for record in cursor.fetchall():
            print(record)


    # Database test:
#
# Sukurti duombaze asmeninių finansų valdymo puslapiui.
#
# Vartotojas turi turėti paskyra.
#
# Vartotojas turi galėti susikurti išlaidų įrašus ir pasirinkti kategorija išlaidai.
#
# Vartotojas turi turėti opcija pasirinkti mėnesio ir metų išlaidų atvaizdavimą.
#
# Vartotojas gali turėti susikūres grupe prie kurios galės pridėti kitus vartotojus
# ir galės pažiūrėti visų vartotojų išlaidas kurie yra šioje grupėje.
