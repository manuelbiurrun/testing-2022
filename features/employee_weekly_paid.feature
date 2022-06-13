Feature: Employee's weekly paid

Here we specify the definitions which are relative to the business domain.
Business Definitions:
    Employee - a person who works for another in return for financial or other compensations.
    Wage - a fixed regular payment per hour to an employee.
    Hours Worked - the quantity of hours worked by an employee throughout a week.
    Name - the employee's name. This is the employee's identifier.
    Weekly Paid - the weekly earnings of the employee. It will be computed depending on Hours Worked and Wage.

This feature file was created with the purpose to test the employee's weekly paid calculation.
Here we have two possible scenarios:

1) If Hours Worked <= 40 (in other words, there is no extra hours), then he weekly paid must be calculated as:
    Weekly Paid = Wage * Hours Worked
2) If Hours Worked > 40, then the hours up to 40 must be computed the same as in case 1), whereas the extra hours
    must be multiplied by a factor of 1.5. So, the computation must be:
    40 * Wage + (Hours Worked - 40) * Wage * 1.5

# Weekly paid = Hours Worked * Wage
Scenario Outline: The employee's weekly paid must be calculated as the product of hours worked and the wage, if the number of hours is less than or equal to 40.
    Given an employee with these parameters
    | Name    | Hours Worked   | Wage   |
    | <Name>  | <Hours_Worked> | <Wage> |
    When we calculate the employee weekly paid
    Then the employee weekly paid will be <Weekly_Paid>

    Examples:
    | Name     | Hours_Worked | Wage | Weekly_Paid |
    | Anthony  | 40           | 3500 | 140000      |
    | Alice    | 39           | 3500 | 136500      |
    | Sarah    | 38           | 3500 | 133000      |

# Weekly paid = 40 * Wage + extra hours * Wage * 1.5
Scenario Outline: The employee's weekly paid must multiply the extra hours (more than 40) by a factor of 1.5.
    Given an employee with these parameters
    | Name    | Hours Worked   | Wage   |
    | <Name>  | <Hours_Worked> | <Wage> |
    When we calculate the employee weekly paid
    Then the employee weekly paid will be <Weekly_Paid>

    Examples:
    | Name     | Hours_Worked | Wage | Weekly_Paid |
    | Anthony  | 41           | 3500 | 145250      |
    | Alice    | 50           | 3500 | 192500      |
    | Sarah    | 60           | 3500 | 245000      |
