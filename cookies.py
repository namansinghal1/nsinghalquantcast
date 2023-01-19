import argparse
from collections import defaultdict

class CookieParser:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def most_active_cookie(self, date):
        # Create a dictionary to store the frequency of each cookie
        cookie_count = defaultdict(int)

        # Open the log file and iterate through each line
        with open(self.file_path, 'r') as f:
            for line in f:
                # Split the line into the cookie and timestamp
                cookie, timestamp = line.strip().split(',')
                # Extract the date from the timestamp
                log_date = timestamp.split('T')[0]
                # Check if the log date matches the specified date
                if log_date == date:
                    # Increment the count for the current cookie
                    cookie_count[cookie] += 1

        # Find the maximum count of any cookie
        max_count = max(cookie_count.values())

        # Create a list to store the most active cookies
        most_active = []
        # Iterate through the cookie count dictionary
        for cookie, count in cookie_count.items():
            # Check if the current cookie has the maximum count
            if count == max_count:
                # Add the current cookie to the most active list
                most_active.append(cookie)

        return most_active

if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser()
    # Add the file path and date arguments
    parser.add_argument('file_path', help='Path to the log file')
    parser.add_argument('-d', '--date', help='Date to check for the most active cookie')
    # Parse the command line arguments
    args = parser.parse_args()
    # Create an instance of the CookieParser class
    cp = CookieParser(args.file_path)
    # Call the most_active_cookie method and print the result
    print('\n'.join(cp.most_active_cookie(args.date)))
