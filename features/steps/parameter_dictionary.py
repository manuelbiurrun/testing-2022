"""
    'parameter_dictionary' stores a key-value mapping between the human-readable terms coming from the Gherkin code,
    and the attribute names to get or set inside the system implementation that we need to test.

    For example: when there is a Gherkin sentence which mentions the 'Hours Worked', we will know that the
    parameter we will have to set or get is the 'hours_worked' attribute (thanks to the dictionary entry:
    {"Hours Worked": "hours_worked"}).
"""
parameter_dictionary = {
    "Name": "name",
    "Hours Worked": "hours_worked",
    "Wage": "wage",
    "employee weekly paid": {"type": "method", "name": "get_weekly_paid"},
}
