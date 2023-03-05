# Transporter

Transporter is a Python terminal program designed to take job input with regards to transport delivery & collection details, and calculate what date and time the truck should be scheduled to load and unload at the depot. Once data is entered, it will be printed to the Transporter google sheet. A user also has the ability to look up specific jobs using the order number and the data will be printed to the Python terminal.

*deployment*

*iamresponsive image*

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
- Added validation for the order number input to check that order number consists of 5 numbers and that the input is an integer. It will repeat the request for input until the input is valid
- Created a main function to call all the functions that are required when the program is run
- Added in a function for the user to input the size of truck that is required for the job
- Created a function to validate the truck size user input on three validations, a value must be entered, it must be able to be converted to a float, and it must exist in a predefined list of truck sizes




## Future Development:
*text ideas on how to develop further*

## Data Model:
*text on the data model used*

## Testing:

### Bugs

### Unfixed Bugs


## Validator Testing:


## Credits:

[Code Institute](https://codeinstitute.net/)
- Love Sandwiches walkthrough project
- Python module content
- Tutor support

