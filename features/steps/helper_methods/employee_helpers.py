from typing import Any

from features.steps.parameter_dictionary import parameter_dictionary
from features.implementation.Employee import Employee
from features.steps.interfaces.employee.interface_employee import InterfaceEmployee


def initialize_employee_structure(context) -> None:
    """
        It defines a new empty dictionary (or re-assigns an existing one) to store the employee data.

        Args:
            context: behave context
    """
    context.employee_data = {}  # cleaning the reference to the data


def create_employee_from_table(table) -> dict:
    """
        It creates an employee, and sets their parameters taking the data from the table as the input parameters.
        It returns the employee object

        Args:
            table: context.table

        Returns:
            dict - A dictionary containing the employee object created.
    """
    new_employee = InterfaceEmployee.get_empty_object()
    for parameter_name in table.headings:
        # The table will have only one row, so we can get rows[0], and then select the correct cell by using the
        # parameter name.
        value = table.rows[0][parameter_name]
        translated_name = parameter_dictionary.get(parameter_name)
        InterfaceEmployee.set_parameter_value(translated_name, value, new_employee)
    return {"object": new_employee}


def calculate_weekly_paid(employee_data: dict) -> None:
    """
        It calculates the weekly paid for the employee data received as the input parameter. It updates the
        employee_data dictionary with the result of the calculation.

        Args:
            employee_data: dict
    """
    employee_data.update({"weekly_paid": employee_data["object"].get_weekly_paid()})


def get_fail_message_not_equal(parameter_name: str,
                               actual_value: Any,
                               expected_value: Any) -> str:
    """
        It returns an error message expressing that the parameter does not have the expected value.

        Args:
            parameter_name: str
            actual_value: Any
            expected_value: Any

        Returns:
            str - The error message.
    """
    return f"Parameter '{parameter_name}' does not have the expected value."\
           f"\nExpected Value: '{str(expected_value)}'"\
           f"\nActual Value: '{str(actual_value)}'"


def verify_weekly_paid(employee_data: dict, expected_weekly_paid: int) -> None:
    """
        It verifies that the expected weekly paid for the employee is equal to the actual weekly paid.

        It throws an assertion error in case expected_weekly_paid is not equal to actual_weekly_paid.

        Args:
            employee_data: dict
            expected_weekly_paid: int
    """
    actual_weekly_paid = employee_data["weekly_paid"]
    assert float(employee_data["weekly_paid"]) == float(expected_weekly_paid),\
           get_fail_message_not_equal("weekly_paid", actual_weekly_paid, expected_weekly_paid)
