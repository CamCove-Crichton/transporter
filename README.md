# Transporter

Transporter is a Python terminal program designed to take job input with regards to transport delivery & collection details, and calculate what date and time the truck should be scheduled to load and unload at the depot. Once data is entered, it will be printed to the Transporter google sheet. A user also has the ability to look up specific jobs using the order number and the data will be printed to the Python terminal and will have the choice to edit a previously entered detail of the job that has been called back.

## Deployment
- [Click here](https://the-transporter.herokuapp.com/) to run the Transporter program

1. Updated the requirements.txt file for Heroku deployment
2. Went to [Heroku](https://dashboard.heroku.com/) and signed into my account
3. Selected "Create App", gave it a name, selected the region and press "Create App"
4. Went into the "Settings" tab
5. In the "Settings" tab, I setup my Config Vars and added my buildpacks
6. Went to the "Deploy" tab
7. In the "Deploy" tab, I selected 'GitHub' as the deployment method
8. Searched for my repo and clicked "Connect"
9. I enabled 'Automatic Deploys' and then clicked "Deploy Branch" having the "main" branch selected

![deployed transporter program](/assets/README%20images/AmIResponsive%20Transporter.png)

### Lucid chart on Transporter logic

![lucid chart flow diagram](/assets/README%20images/Lucidchart%20Transporter.png)

## How to input data:



## Features:
*text with screen grabs*

## Development:

- I created a google worksheet and named it Transporter
- Utilised the walkthrough videos from the Code Institute's "love-sandwiches" project to assist with setting up my credentials using Google Cloud and enabling the Google Drive API and the Google Sheets API
- Created a github repository using the Code Institute Python student template provided, and opened a Gitpod workspace
- Using the help of the walkthrough videos from the Code Institute, I was able to import my json credentials file and added it to the .gitignore directory
- Once setup, I went to my google sheet, and shared it with my project using the client email within my credentials file
- Again using the assistance of the Code Institute walkthrough videos I was able to import the gspread library and then the Credentials class from the google.oauth2.service_account library
- Setup the constants in the run.py file
- Created two variables using the gspread methods to access the google sheet and tested it is accessing the sheet using a print function and removed them once I confirmed it was working
- Created a class 'Job' to use as the data model to hold the data for the job that the user inputs and tested that it works
- Created a function to take the user input for the job name and then used another function to validate the input for the job name
- I then used a while loop to loop through my function for the job name to repeat the request for data until it has passed the validation tests to break the loop
- Added in a function to update the google worksheet so when the user data has been collected, it will be updated in the google sheet
- Added in a function for the user to input the order number data, and will then validate it
- Added validation for the order number input to check that order number consists of 5 numbers and that the input is an integer. It will repeat the request for input until the input is valid, as well as check the Transporter google sheet for existing order numbers, so each order number is unique
- Created a main function to call all the functions that are required when the program is run
- Added in a function for the user to input the size of truck that is required for the job
- Created a function to validate the truck size user input on three validations, a value must be entered, it must be able to be converted to a float, and it must exist in a predefined list of truck sizes
- Added in a function for the user to input a delivery date required for the job, and it will repeat the request for the data until the date entered is a valid date to the format it requires
- Created a fuction to validate date input from the user in a format of DD-MM-YYYY
- Added in a function for the user to input a collection date for the job, and it will repeat the request until the input is valid. It utilises the same date validation function as the delivery date validation
- Added in a function for the user to input a required delivery time for the job, it will repeat the request for the data until the input from the user is valid
- I then added in a validation function to validate the time inputs from the user
- Added in a function for the user to input a collection time and utilise the same time validation function to validate the input. It will also repeat the request for the user to input the time until the data is valid
- Once receiving all the data, I assigned all the user inputs to their own variables and then called them in the Jobs class, and tested it is pushing the data through to the google sheet
- I then moved onto adding in a function to calculate the loading date using the inputs from the user, using if elif statements and nested if statements to check for the truck size to determine the date the truck should load on
- Using a similar approach as the calculating load date function, I added a function to calculate the unloading date
- I then began working on the logic for calculating the loading time, and worked it into the same function as the calculating load date, to return a tuple, and then in the main function created two variable to unpack the returned values to utilise later
- Afterwards, I then added in a similar calculation to the function for calculating the unloading date, so it works out the date and the time and returns to a tuple, and again in the main function, added in two variables to unpack the values to utilise later
- Added in a subclass to use the super classes existing properties and add in the calculated loading and unloading details to then use all of these results and user input to update the Transporter google sheet
- Added in a function to lookup existing jobs on the Transporter google sheet to return all the job information
- I then added in a function to loop through the program, for the user to choose either to enter a new job, or to lookup an existing job or to quit the program altogether
- The user then has the option to update the previously input details for the specific job they have called back
- I also then added in a welcome message when the program starts and a leaving message for when the user decides to exit the program
- I refactored the functions for the user input for the delivery date and the collection date to have the "try" & "except" statements in these functions, as they are the main function, and within the "try" statements, it should call any other functions to run to try for validation. I would have liked to do this with all the functions, but due to time constraints, I did not have enough time to do so

```
{
while True:
        print("Please enter the delivery date.")
        print("It must be in DD-MM-YYYY format.")
        print("Example: 21-03-2023\n")

        date_format = '%d-%m-%Y'
        today = datetime.datetime.now()
        del_date_str = input('Enter the delivery date here: \n')

        try:
            validate_date_input(del_date_str)
            delivery_date = datetime.datetime.strptime(
                del_date_str, date_format)
            if delivery_date >= today:
                print('Date is valid\n')
            else:
                raise ValueError(
                    f'The date {delivery_date.strftime(date_format)}\
 is invalid\n'
                    f'Date cannot be before {today.strftime(date_format)}'
                )
        except ValueError as error:
            print(f"Invaild entry {error}, please try again. \n")
        else:
            break

    return del_date_str
}
```



## Future Development:
1. I would like to be able to develop time slots for the trucks, depending on the truck size, so instead of just stipulating a time to begin the load or unload, it also has a time the loading or unloading has to be finished by
2. A further development on the truck time slots would be to then have the transporter check the google sheet for conflicting time slots, return a message to say the time slot is not available and to offer an alternative time slot
3. I would also like to develop it further to allow the user to input the cost being charged to the client, and the cost quoted by the transport company and to have the program calculate the amount of profit or loss being made in a percentage format

## Data Model:
- I decided to use a class as my data model. The class stores all the input the user enters, and has a method to display all the inputs in a readable format to the user
- I also used a sub-class of the main class to hold all the calculated data, so this can be appended using the method in the main class as well as extending onto it with its own method to add to the details of the job in a readable format to the user

## Testing:

### Bugs

- Solved bug: Adding in a validation for testing the date for delivery is not before the current date. I had to refactor the function to have the "try" & "except" statments in the main delivery date function and then to break the loop use an "else" statement with the "try" & "except" statements
- Solved bug: Adding in a validation for the collection date, to test the collection date is not before the delivery date. I have to refactor the function again to have the "try" & "except" statements in the main collection function and to take a parameter, to use the delivery date as the argument. I then also had to use the "else" statement with the "try" & "except" statements to break the while loop when no errors are raised

### Unfixed Bugs

- When you run through the full job entry and then when you select to lookup a job, enter a job number, it calls up the job and asks if you want to edit the previously entered details, if you select "n", it then takes you back to the loop if you want to enter a new job, lookup an existing job or quit, and if at that stage you select to quit, the program seems to crash - Due to time constraints I have not managed to rectify this bug yet

### Validator Testing:

![CI Python Linter results](/assets/README%20images/Linter%20Transporter.png)


## Credits:

[Code Institute](https://codeinstitute.net/)
- Love Sandwiches walkthrough project
- Python module content
- Tutor support

[GeeksforGeeks](https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/)
- Reminder on how to search for a value in a list of values

[C#Corner](https://www.c-sharpcorner.com/UploadFile/75a48f/working-with-date-and-time-python/)
- Read up on how to format the date input in a particular way

[Stack Overflow](https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python)
- Assistance with how to validate a date input
- Assistance with how to validate a time input

[tutorialspoint](https://www.tutorialspoint.com/How-to-perform-arithmetic-operations-on-a-date-in-Python)
- Information on how to use arithmitic on dates and times

[W3Schools](https://www.w3schools.com/python/python_tuples_unpack.asp)
- Refresher on unpacking tuples

[gspread documentation](https://docs.gspread.org/en/v5.7.0/user-guide.html#cell-object)
- Information on how to get values from a row or column
- Information on how to update a cell value

### Code Credits:

[Code Institute](https://codeinstitute.net/)
- Code for the majority of the user input functions taken from Code Institutes - Love Sandwiches walkthrough project
```
{
    def get_job_name():
    """
    A function to get the job name from the user
    It will repeat the request for the user input until the data is valid
    """
    while True:
        print("Please enter a job name")
        print("The job name must consist of three or more characters")
        print("Example: Job Name 1\n")

        job_str = input('Enter the job name here: \n')

        if validate_jname_input(job_str):
            print("Job name is valid\n")
            break

    return job_str
}
```

- Code for the majority of the validation functions taken from Code Institutes - Love Sandwiches walkthrough project
```
{
    def validate_jname_input(string):
    """
    Inside the try, checks if there are three characters or more
    """
    try:
        if len(string) <= 3:
            raise ValueError(
                f"Job name must consist of 3 or more characters\n"
                f"You entered {len(string)} character(s)"
            )
    except ValueError as error:
        print(f"Invaild entry: {error}, please try again\n")
        return False

    return True
}
```