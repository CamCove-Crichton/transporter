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


example = Job('Test', '012344', '7.5', '10/03/23',
              '08:00', '11/03/23', '02:00')

print(example.details())
