# python-sbe-example
SBE example based on Gherkin

Requirements to run:
Python 3.10 installed
pip install -r requirements.txt
Execute the following command inside this folder:
behave

It should execute the feature file called "employee_weekly_paid.feature", running all the requirements written on it. For every scenario, it will print on the standard output the Gherkin lines on green color if everything is OK, or in case of an error, it will print the line which fails in red color, printing the corresponding error message as well.