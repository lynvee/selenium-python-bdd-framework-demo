Feature: Try to use Elements module

    Scenario Outline: Text Box
        Given Go to Demo page
        When Select <name> option
        And Select <module> module
        And Enter <data> to textbox
        And Submit textbox
        Examples:
        | name     |module  |data       |
        | elements |textbox |valid data |
    
    Scenario Outline: Check Box
        Given Go to Demo page
        When Select <name> option
        And Select <module> module
        Examples:
        | name     |module  |
        | elements |checkbox|
    
    Scenario Outline: Radio Button
        Given Go to Demo page
        When Select <name> option
        And Select <module> module
        Examples:
        | name     |module     |
        | elements |radiobutton|