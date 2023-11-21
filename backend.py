from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        create_db_query = "CREATE DATABASE if not exist database"
        create_employee_table_query = """
        CREATE TABLE Employee(
            id INT AUTO_INCREMENT PRIMARY KEY,
            FIO VARCHAR(100),
            speciality vsrchar(30)
            stage int,
            salary decimal(14,2),
            Department_id INT
        )
        """
        create_department_table_query = """
                CREATE TABLE Employee(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(30),
                    manager int
                )
                """
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)