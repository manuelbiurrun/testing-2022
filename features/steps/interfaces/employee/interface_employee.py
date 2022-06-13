""" Class InterfaceEmployee """
from typing import Any

from features.implementation.Employee import Employee


class InterfaceEmployee:
    @staticmethod
    def get_empty_object() -> Employee:
        """
            It creates and returns an Employee object.

            Returns:
                an Employee object.
        """
        return Employee()

    @staticmethod
    def get_parameter_value(translated_name: str,
                            employee_object: Employee) -> Any:
        """
            It returns the value associated to the Employee attribute
            given by the translated_name.

            Args:
                translated_name: str
                employee_object: Employee

            Returns:
                Any - the value associated to the attribute called translated_name.
        """
        return getattr(employee_object, translated_name)

    @staticmethod
    def set_parameter_value(translated_name: str,
                            value: Any,
                            employee_object: Employee) -> None:
        """
            It sets the value associated to the Employee attribute
            given by the translated_name.

            Args:
                translated_name: str
                value: Any
                employee_object: Employee
        """
        if translated_name in ["hours_worked", "wage"]:
            value = float(value)
        setattr(employee_object, translated_name, value)
