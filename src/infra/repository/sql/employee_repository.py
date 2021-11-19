from typing import List, Type

from src.core.entities import Employee

from src.core.repositories import IEmployeeRepository
from src.infra.database import get_database_connection

class EmployeeRepository(IEmployeeRepository):

    def __init__(self):
        self.__connection = get_database_connection()


    def save_employee(self, employee: Type[Employee]) -> None:
        """ save the employee on database"""
        
        add_data_statement = """ 
            insert into location(district, city, road)
            values (?, ?, ?)
        """
        
        cursor = self.__connection.cursor()
        cursor.execute(add_data_statement, (                
                employee.location.district, 
                employee.location.city, 
                employee.location.road
                )   
            )

        add_data_statement_employee = """
            insert into employee(location, name, email, phone)
            values (?, ?, ?, ?)
        """

        cursor.execute(add_data_statement_employee, (                
                cursor.lastrowid,
                employee.name,
                employee.email,
                employee.phone
                )
            )

        self.__connection.commit()
        cursor.close()        


    def get_employees(self) -> List[Employee]:
        """ Get all employee"""
        
        sql_query = """
            select  
            e.name, e.email, e.phone, 
            l.district, l.city, l.road 
            from employee e 
            inner join location l 
            ON
            e.location = l.id ;
        """

        cursor = self.__connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()                

        cursor.close()
        self.__connection.close()
        
        return result

    
    def delete_employee(self, id: int) -> Employee:
        """ Delete the given employee"""

        pass


    def __get_afected_row_trigger(self, id: int):

        sql_query = """
            select id from location where id = ?
        """

        cursor = self.__connection.cursor()
        cursor.executemany(sql_query, (id,))
        result = cursor.fetchone()
        
        return result
