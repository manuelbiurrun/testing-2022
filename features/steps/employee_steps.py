""" Step definitions for Gherkin file: employee_weekly_paid.feature """


from behave import given, when, then, use_step_matcher

from features.steps.helper_methods.employee_helpers import create_employee_from_table
from features.steps.helper_methods.employee_helpers import calculate_weekly_paid
from features.steps.helper_methods.employee_helpers import verify_weekly_paid
from features.steps.helper_methods.employee_helpers import initialize_employee_structure

use_step_matcher("re")


@given(f"an employee with these parameters")
def an_employee_with_these_parameters(context):
    initialize_employee_structure(context)
    context.employee_data = create_employee_from_table(context.table)


@when("we calculate the employee weekly paid")
def we_calculate_the_weekly_paid(context):
    calculate_weekly_paid(context.employee_data)


@then(f"the employee weekly paid will be (?P<weekly_paid>\d+)")
def then_the_employee_weekly_paid_will_be(context, weekly_paid):
    verify_weekly_paid(context.employee_data, weekly_paid)
