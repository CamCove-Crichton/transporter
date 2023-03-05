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
        print("Please enter an order number")
        print("The order number should consist of 5 numbers")
        print("Example: 12345\n")

        ord_str = input('Enter the order number here\n')

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
    # values_list = SHEET.worksheet("transport_details")
    # values = values_list.col_values(2)
    try:
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
    print("Please enter the truck size required for the job")
    print("Truck size must be a number")
    print("For 45ft Artic please enter 44 and for 30ft Artic enter 36")
    print("Accepted Truck sizes: 7.5, 10, 12, 15, 18, 26, 36, 44")

    truck_str = input('Enter the truck size required here \n')
    validate_truck_input(truck_str)


def validate_truck_input(float_data):
    """
    Inside the try, checks the input is a number
    """

    try:
        truck_sizes = ['7.5', '10', '12', '15', '18', '26', '36', '44']
        if (float_data in truck_sizes):
            print("Valid truck size")
        else:
            raise ValueError(
                f"Truck size must be a size from the accepted list"
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


def main():
    job_name = get_job_name()
    ord_num = get_ord_no()


get_truck_size()
