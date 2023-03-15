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


class JobInputs:
    """
    Job class to hold all user input job related
    """
    def __init__(
                 self, jname, ord_no, tsize, ddate, dtime, cdate, ctime):
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

    def description(self):
        """
        Returns all the detials in a descriptive easy to read
        bit of information for the user
        """
        job_description = f"1) Job Name: {self.jname}\n\
2) ORD#: {self.ord_no}\n3) Truck Size: {self.tsize}\n\
4) Delivery Date: {self.ddate}\n5) Delivery Time: {self.dtime}\n\
6) Collection Date: {self.cdate}\n7) Collection Time: {self.ctime}"
        return job_description


class FullJobDetails(JobInputs):
    """
    A subclass to hold all the job details including the loading
    and unloading details
    """
    def __init__(self, jname, ord_no, tsize, ddate, dtime, cdate, ctime,
                 ldate, ltime, unl_date, unl_time):
        #  properties
        super().__init__(jname, ord_no, tsize, ddate, dtime, cdate, ctime)
        self.ldate = ldate
        self.ltime = ltime
        self.unl_date = unl_date
        self.unl_time = unl_time

    def details(self):
        """
        Returns all the job details in a list
        """
        return [self.jname, int(self.ord_no), float(self.tsize), self.ddate,
                self.dtime, self.cdate, self.ctime, self.ldate, self.ltime,
                self.unl_date, self.unl_time]

    def full_description(self):
        """
        Returns the string from the superclass description method,
        and then adds on additional information about the loading
        and unloading dates and times
        """
        return f"{super().description()}\n8) Loading Date: {self.ldate}\n\
9) Loading Time: {self.ltime}\n10) Unloading Date: {self.unl_date}\n\
11) Unloading Time: {self.unl_time}\n"


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
        if int_data in values:
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
        if float_data in truck_sizes:
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


# Assistance from stackoverflow & C-Sharp Corner for validation
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
    It will repeat the request for data until the data is valid
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


# Idea and code from code institute - love-sandwiches walkthrough project
def get_col_time():
    """
    A function for the user to input the collection time required
    for the truck to be on site
    It will repeat the request for data until the data is valid
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


# Assistance from stackoverflow & C-Sharp Corner for validation
# Idea and code from code institute - love-sandwiches walkthrough project
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


# Assistance from tutorialspoint for calculating dates and times
def calc_load_date(job_data):
    """
    A function to calculate the loading date,
    using the data from the user and predetermined times for
    warehouse employee woking hours so trucks are not loading
    late at night or in the small hours of the morning
    """

    print("\nCalculating loading details...\n")

    dateformat = '%d-%m-%Y'
    timeformat = '%H:%M'
    delivery_time = datetime.datetime.strptime(job_data.dtime, timeformat)
    small_load_time = datetime.datetime.strptime('16:00', timeformat)
    medium_load_time = datetime.datetime.strptime('15:00', timeformat)
    large_load_time = datetime.datetime.strptime('14:00', timeformat)

    if float(job_data.tsize) <= 15:
        if job_data.dtime <= '10:00':
            load_date = datetime.datetime.strptime(
                job_data.ddate, dateformat)-datetime.timedelta(days=1)
            load_date = load_date.strftime(dateformat)
            time_diff = small_load_time - delivery_time
            load_time = delivery_time + time_diff
            load_time = load_time.strftime(timeformat)
        elif job_data.dtime > '19:00':
            load_date = job_data.ddate
            time_diff = delivery_time - small_load_time
            load_time = delivery_time - time_diff
            load_time = load_time.strftime(timeformat)
        else:
            load_date = job_data.ddate
            load_time = datetime.datetime.strptime(
                job_data.dtime, timeformat)-datetime.timedelta(hours=3)
            load_time = load_time.strftime(timeformat)
        return (load_date, load_time)

    elif float(job_data.tsize) <= 26:
        if job_data.dtime <= '11:00':
            load_date = datetime.datetime.strptime(
                job_data.ddate, dateformat)-datetime.timedelta(days=1)
            load_date = load_date.strftime(dateformat)
            time_diff = medium_load_time - delivery_time
            load_time = delivery_time + time_diff
            load_time = load_time.strftime(timeformat)
        elif job_data.dtime > '19:00':
            load_date = job_data.ddate
            time_diff = delivery_time - medium_load_time
            load_time = delivery_time - time_diff
            load_time = load_time.strftime(timeformat)
        else:
            load_date = job_data.ddate
            load_time = datetime.datetime.strptime(
                job_data.dtime, timeformat)-datetime.timedelta(hours=4,
                                                               minutes=30)
            load_time = load_time.strftime(timeformat)
        return (load_date, load_time)

    elif float(job_data.tsize) >= 36:
        if job_data.dtime <= '12:00':
            load_date = datetime.datetime.strptime(
                job_data.ddate, dateformat)-datetime.timedelta(days=1)
            load_date = load_date.strftime(dateformat)
            time_diff = large_load_time - delivery_time
            load_time = delivery_time + time_diff
            load_time = load_time.strftime(timeformat)
        elif job_data.dtime > '19:00':
            load_date = job_data.ddate
            time_diff = delivery_time - large_load_time
            load_time = delivery_time - time_diff
            load_time = load_time.strftime(timeformat)
        else:
            load_date = job_data.ddate
            load_time = datetime.datetime.strptime(
                job_data.dtime, timeformat)-datetime.timedelta(hours=5)
            load_time = load_time.strftime(timeformat)
        return (load_date, load_time)


# Assistance from tutorialspoint for calculating dates and times
def calc_unload_date(job_data):
    """
    A function to calculate the unloading date for the job,
    using the data from the user inputs
    """

    print("Calculating unloading details...\n")

    dateformat = '%d-%m-%Y'
    timeformat = '%H:%M'
    collection_time = datetime.datetime.strptime(job_data.ctime, timeformat)
    start_time = datetime.datetime.strptime('08:00', timeformat)
    time_diff = start_time - collection_time

    if float(job_data.tsize) <= 15:
        if job_data.ctime >= '15:00':
            unload_date = datetime.datetime.strptime(
                job_data.cdate, dateformat)+datetime.timedelta(days=1)
            unload_date = unload_date.strftime(dateformat)
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        elif job_data.ctime < '05:00':
            unload_date = job_data.cdate
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        else:
            unload_date = job_data.cdate
            unload_time = datetime.datetime.strptime(
                job_data.ctime, timeformat) + datetime.timedelta(hours=3)
            unload_time = unload_time.strftime(timeformat)
        return (unload_date, unload_time)

    elif float(job_data.tsize) <= 26:
        if job_data.ctime >= '14:00':
            unload_date = datetime.datetime.strptime(
                job_data.cdate, dateformat)+datetime.timedelta(days=1)
            unload_date = unload_date.strftime(dateformat)
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        elif job_data.ctime < '04:00':
            unload_date = job_data.cdate
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        else:
            unload_date = job_data.cdate
            unload_time = datetime.datetime.strptime(
                job_data.ctime, timeformat) + datetime.timedelta(hours=4)
            unload_time = unload_time.strftime(timeformat)
        return (unload_date, unload_time)

    elif float(job_data.tsize) >= 36:
        if job_data.ctime >= '11:30':
            unload_date = datetime.datetime.strptime(
                job_data.cdate, dateformat)+datetime.timedelta(days=1)
            unload_date = unload_date.strftime(dateformat)
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        elif job_data.ctime < '03:30':
            unload_date = job_data.cdate
            unload_time = collection_time + time_diff
            unload_time = unload_time.strftime(timeformat)
        else:
            unload_date = job_data.cdate
            unload_time = datetime.datetime.strptime(
                job_data.ctime, timeformat) + datetime.timedelta(hours=4,
                                                                 minutes=30)
            unload_time = unload_time.strftime(timeformat)
        return (unload_date, unload_time)


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


def edit_selection(num_data):
    """
    A function to handle the users selection to edit specific entries
    for a job
    """
    if num_data == '1':
        job_name = get_job_name()
        return job_name
    elif num_data == '2':
        ord_num = get_ord_no()
        return ord_num
    elif num_data == '3':
        truck_size = get_truck_size()
        return truck_size
    elif num_data == '4':
        del_date = get_del_date()
        return del_date
    elif num_data == '5':
        del_time = get_del_time()
        return del_time
    elif num_data == '6':
        col_date = get_col_date()
        return col_date
    elif num_data == '7':
        col_time = get_col_time()
        return col_time


# Assistance from the gspread docs on finding a cell and getting row values
def search_jobs():
    """
    A fucntion to allow the user to search for the job details
    by the order number
    """
    print('To lookup a jobs transport details, enter the order number')
    print('Example: 12345\n')
    values_list = SHEET.worksheet("transport_details")
    values = values_list.col_values(2)
    search_num = input('Enter the order number here: \n')

    if search_num in values:
        cell = SHEET.worksheet("transport_details").find(search_num)
        job_list = SHEET.worksheet("transport_details").row_values(cell.row)
        j, o, t, d1, t1, d2, t2, d3, t3, d4, t4 = job_list
        call_back = FullJobDetails(j, o, t, d1, t1, d2, t2, d3, t3, d4, t4)
        print(call_back.full_description())
        entry_update = edit_entries(call_back.full_description())
        print(entry_update)


def edit_entries(job_data):
    """
    A function to allow the user to edit an entry if anything
    is incorrect or has changed from the original data
    """
    print('Would you like to update any of the previously entered details?')
    print('Press "y" for Yes')
    print('Press "n" for No')

    edit_choice = input('Enter your choice here: \n')

    if edit_choice == 'y':
        print('Please select a number from the list below')
        print('Please select and edit one option at a time')
        print('Example: 1')
        print(job_data)
        num_selection = input('Select a number to edit the detail here: \n')
        update = edit_selection(num_selection)
        return update
    elif edit_choice == 'n':
        program_loop()


def program_loop():
    """
    A function to loop through either the main job entry functions
    to add a new job to the transporter google sheet,
    or to lookup an existing job on the transporter google sheet
    """
    while True:
        print('Would you like to enter a new job, lookup\
              an existing job or exit?')
        print('Press 1 to enter a new job')
        print('Press 2 to lookup an exisiting job')
        print('Press "q" to exit\n')

        user_choice = input('Enter your choice here: \n')

        if user_choice == '1':
            main()
        elif user_choice == '2':
            search_jobs()
        elif user_choice == 'q':
            break


# Idea and code from code institute - love-sandwiches walkthrough project
def main():
    """
    A function to hold and call all the functions required
    for the program to run
    """
    job_name = get_job_name()
    ord_num = get_ord_no()
    truck_size = get_truck_size()
    del_date = get_del_date()
    del_time = get_del_time()
    col_date = get_col_date()
    col_time = get_col_time()
    job_inputs = JobInputs(job_name, ord_num, truck_size, del_date, del_time,
                           col_date, col_time)
    print(job_inputs.description())
    loading_date, loading_time = calc_load_date(job_inputs)
    print(f"Loading date calculated: {loading_date}")
    print(f"Loading time calculated: {loading_time}\n")
    unloading_date, unloading_time = calc_unload_date(job_inputs)
    print(f"Unloading date calculated: {unloading_date}")
    print(f"Unloading time calculated: {unloading_time}\n")
    full_job_details = FullJobDetails(job_name, ord_num, truck_size, del_date,
                                      del_time, col_date, col_time,
                                      loading_date, loading_time,
                                      unloading_date, unloading_time)
    update_transport_details(full_job_details.details())


# Idea and code from code institute - love-sandwiches walkthrough project
main()
program_loop()
