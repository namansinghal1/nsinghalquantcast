import argparse
from collections import defaultdict

class CookieParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_file(self, date):
        # Create a dictionary to store the frequency of each cookie
            
        try:
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
            return cookie_count
        except FileNotFoundError:
            print("Error: File not found")

    def most_active_cookie(self, date):
        cookie_count = self.parse_file(date)
        # Find the maximum count of any cookie
        max_count = max(cookie_count.values())
        return max_count

    def get_most_active(self, date):
        cookie_count = self.parse_file(date)
        max_count = self.most_active_cookie(date)
        most_active = []
        for cookie, count in cookie_count.items():
            if count == max_count:
                most_active.append(cookie)
        return most_active

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path to the log file')
    parser.add_argument('-d', '--date', help='Date to check for the most active cookie')
    args = parser.parse_args()
    cp = CookieParser(args.file_path)
    print('\n'.join(cp.get_most_active(args.date)))
