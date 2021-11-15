from src.core.entities import Employee, Location

class EmployeeAdapter:

    @staticmethod
    def create(name: str, email: str, phone: int, district: str, road: str, city: str):
        """ Adapter of dependencies 
            Args:
                name: str
                email: str
                phone: int
                district: str
                road: str
                city: str

        """

        return Employee(
            name=name,
            email=email,
            phone=phone,
            location= Location(
                district=district,
                road=road,
                city=city
                )
            )