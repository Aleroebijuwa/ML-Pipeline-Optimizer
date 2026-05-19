from context_managers import SQLDatabase


def test_database():
    with SQLDatabase("test.db") as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
        cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
        cursor.execute("SELECT * FROM users")

        print(cursor.fetchall())


if __name__ == "__main__":
    test_database() 

    from context_managers import FileHandler


def test_file():
    with FileHandler("sample.txt", "w") as f:
        f.write("ML Pipeline Optimizer is working!")


    with FileHandler("sample.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    test_file()