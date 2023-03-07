import datetime
import gspread  # from code institue love-sandwiches walkthrough
# import Credentials class code from code institute love-sandwiches
from google.oauth2.service_account import Credentials

# SCOPE name and code for contastant from the code institute
# love-sandwiches walkthrough
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# CREDS name and code for constant from the code institute
# love-sandwiches walkthough
CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS name and code for constant from the code institute
# love-sandwiches walkthrough
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT name and code for constant from the code institute
# love-sandwiches walkthrough
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET name and code for constant from the code institute
# love-sandwiches walkthrough
SHEET = GSPREAD_CLIENT.open('Transporter')


class Job:
    """
    Job class to hold all user input job related
    """
    def __init__(self, jname, ord_no, tsize, ddate, dtime, cdate, ctime):
        # properties
        self.jname = jname
        self.ord_no = ord_no
        self.tsize = tsize
        self.ddate = ddate
        self.dtime = dtime
        self.cdate = cdate
        self.ctime = ctime

    def details(self):
        """
        Returns all the job details in a list
        """
        return [self.jname, int(self.ord_no), float(self.tsize), self.ddate,
                self.dtime, self.cdate, self.ctime]


# Idea & code from code insitute - love-sandwiches walkthrough project
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


# Idea & code from code institute - love-sandwiches walkthrough project
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
    except ValueError as e:
        print(f"Invaild entry: {e}, please try again\n")
        return False

    return True


# Idea and code from code institute - love-sandwiches walkthrough project
def get_ord_no():
    """
    A function to get the order number from the user
    It will repeat the request for the user input until the data is valid
    """
    while True:
        print("Please enter an order number.")
        print("The order number should consist of 5 numbers.")
        print("Example: 12345\n")

        ord_str = input('Enter the order number here: \n')

        if validate_ord_input(ord_str):
            print("Order no. is valid\n")
            break

    return ord_str


# Idea and code from code institute - love-sandwiches walkthrough project
def validate_ord_input(int_data):
    """
    Inside the try, checks if there are 5 numbers in the order number
    and checks that the input is an integer
    """
    try:
        values_list = SHEET.worksheet("transport_details")
        values = values_list.col_values(2)
        # Below code idea from GeeksforGeeks website
        if (int_data in values):
            raise ValueError(
                f"ORD{int_data} already exists"
            )
        int(int_data)
        if len(int_data) != 5:
            raise ValueError(
                f"Order no. must have 5 numbers, you entered {len(int_data)}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n")
        return False

    return True


# Idea and code from code institute - love-sandwiches walkthrough project
def get_truck_size():
    """
    A function to get the truck size for the job from the user
    It will repeat the request for input until the input is valid
    """
    while True:
        print("Please enter the truck size required for the job.")
        print("Truck size must be a number.")
        print("For 45ft Artic enter 44 and for 30ft Artic enter 36")
        print("Accepted Truck sizes: 7.5, 10, 12, 15, 18, 26, 36, 44")

        truck_str = input('Enter the truck size required here: \n')

        if validate_truck_input(truck_str):
            break

    return truck_str


# Idea and code from code institute - love-sandwiches walkthrough project
def validate_truck_input(float_data):
    """
    Inside the try, checks the input is a number
    It also checks the value can be converted to a float,
    as well as checking it is a valid truck size from a list
    of trucks
    """
    try:
        truck_sizes = ['7.5', '10', '12', '15', '18', '26', '36', '44']
        # Below code idea from GeeksforGeeks website
        if (float_data in truck_sizes):
            print("Truck size is valid\n")
        else:
            raise ValueError(
                f"Truck size must be a size from the accepted list. "
                f"You entered '{float_data}'"
            )
        float(float_data)
        if len(float_data) <= 0:
            raise ValueError(
                f"Truck size must be one of the sizes from the accepted list"
                f"You entered '{float_data}'"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n")
        return False

    return True


# Idea and code from code institute - love-sandwiches walkthrough project
def get_del_date():
    """
    A function for the user to input the required delivery date
    It will repeat the request for data until it is valid
    """
    while True:
        print("Please enter the delivery date.")
        print("It must be in DD-MM-YYYY format.")
        print("Example: 21-03-2023\n")

        del_date_str = input('Enter the delivery date here: \n')

        if validate_date_input(del_date_str):
            break

    return del_date_str


def get_col_date():
    """
    A function to for the user to input the required collection date
    for the job
    It will repeat the request for data until it is valid
    """
    while True:
        print("Please enter the collection date.")
        print("It must be in DD-MM-YYYY format")
        print("Example: 21-03-2023\n")

        col_date_str = input('Enter the collection date here: \n')

        if validate_date_input(col_date_str):
            break

    return col_date_str


# Idea and code from code institute - love-sandwiches walkthrough project
def validate_date_input(date_data):
    """
    Inside the try, checks for a valid date entry in the format
    of DD-MM-YYYY
    """
    try:
        if datetime.datetime.strptime(date_data, '%d-%m-%Y'):
            print("Date is valid \n")
        else:
            raise ValueError(
                f"The date {date_data} is incorrect"
                f"It must be in a DD-MM-YYYY format"
            )
    except ValueError as e:
        print(f"Invaild entry {e}, please try again. \n")
        return False

    return True


# Idea and code from code institute - love-sandwiches walkthrough project
def get_del_time():
    """
    A function for the user to input the delivery time required
    for the truck to be on site
    """
    while True:
        print("Please enter the required delivery time.")
        print("It must be in a 24 hour format, HH:MM.")
        print("Example: 18:00\n")
        print("Remember 12:00 is accepted as midday, and 00:00 as midnight!\n")

        del_time_str = input('Enter the delivery time here: \n')

        if validate_time(del_time_str):
            break

    return del_time_str


def get_col_time():
    """
    A function for the user to input the collection time required
    for the truck to be on site
    """
    while True:
        print("Please enter the required collection time.")
        print("It must be in a 24 hour format, HH:MM.")
        print("Example: 18:00\n")
        print("Remember 12:00 is accepted as midday, and 00:00 as midnight!\n")

        col_time_str = input('Enter the collection time here: \n')

        if validate_time(col_time_str):
            break

    return col_time_str


def validate_time(time_data):
    """
    Inside the try, checks for a valid time entry in a 24 hour format
    HH:MM
    """
    try:
        if datetime.datetime.strptime(time_data, '%H:%M'):
            print("Time is valid \n")
        else:
            raise ValueError(
                f"The {time_data} is incorrect"
                f"It must be in a 24 hour, HH:MM format."
            )
    except ValueError as e:
        print(f"Invalid entry {e}, please try again. \n")
        return False

    return True


# Idea and code from code institute - love-sandwiches walkthrough project
def update_transport_details(job_data):
    """
    Updates the transport details google sheet
    Adds new row of data using the user inputs provided
    """
    print("Adding new job details to Transporter sheet...\n")
    transport_sheet = SHEET.worksheet('transport_details')
    transport_sheet.append_row(job_data)
    print("Job details added successfully!\n")


# Idea and code from code institute - love-sandwiches walkthrough project
def main():
    job_name = get_job_name()
    ord_num = get_ord_no()
    truck_size = get_truck_size()
    del_date = get_del_date()
    del_time = get_del_time()
    col_date = get_col_date()
    col_time = get_col_time()


# Idea and code from code institute - love-sandwiches walkthrough project
main()
