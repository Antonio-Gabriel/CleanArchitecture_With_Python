from src.infra.database.database import get_database_connection


def make_migrations():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statement
    on the database
    """

    connection = get_database_connection()

    statement_location = """        
        CREATE TABLE IF NOT EXISTS location(
            id integer primary key  autoincrement not null,
            district text not null,
            city text not null,
            road text not null
        )
    """

    connection.execute(statement_location)

    statement_employee = """
        CREATE TABLE IF NOT EXISTS employee(
            id integer primary key autoincrement not null,
            location integer not null,
            name text NOT NULL,
            email text NOT NULL,
            phone integer,

            foreign key (location) 
                references location(id)
        )
    """

    connection.execute(statement_employee)

    connection.commit()
    connection.close()
