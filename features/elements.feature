Feature: Try to use Elements module

    Scenario Outline: Text Box
        Given Go to Demo page
        When Select <name> option
        And Select <module> module
        And Enter <data> to textbox
        Examples:
        | name     |module  |data       |
        | elements |textbox |valid data |