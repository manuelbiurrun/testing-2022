""" Class Employee """


class Employee:
    def __init__(self, name: str = "",
                 hours_worked: int = 0,
                 wage: int = 0):
        """
            Constructor from the Employee class.

            Args:
                name: str
                hours_worked: int
                wage: int
        """
        self.name = name
        self.hours_worked = hours_worked
        self.wage = wage

    def get_weekly_paid(self) -> float:
        """
            It returns the weekly amount paid to the employee, based on its wage, and the quantity of hours
            worked.

            Returns:
                float - The weekly paid.
        """
        if self.hours_worked > 40:
            return 40 * self.wage + (self.hours_worked - 40) * self.wage * 1.5
        else:
            return self.hours_worked * self.wage
