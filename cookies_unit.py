import unittest
import collections
from cookies import CookieParser

class TestMostActiveCookie(unittest.TestCase):
    def test_most_active_cookie(self):
        # Test data
        file_path = 'cookie_log.csv'
        date = '2018-12-09'
        expected_result = ['AtY0laUfhglK3lC7']

        cp = CookieParser(file_path)

        print(cp.most_active_cookie(date))
        # Call the function and check if the result matches the expected result
        
        self.assertEqual(collections.Counter(expected_result), collections.Counter(cp.most_active_cookie(date)))
        
    def test_multiple_cookies(self):
        # Test data
        file_path = 'cookie_log.csv'
        date = '2018-12-08'
        expected_result = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        cp = CookieParser(file_path)
        print("got tf here", cp.most_active_cookie(date))
        
        # Call the function and check if the result matches the expected result
        self.assertEqual(collections.Counter(expected_result), collections.Counter(cp.most_active_cookie(date)))
        
    def test_no_cookies(self):
        # Test data
        file_path = 'cookie_log.csv'
        date = '2018-12-07'
        expected_result = ['4sMM2LxV07bPJzwf']
        cp = CookieParser(file_path)
        print(cp.most_active_cookie(date))
        
        # Call the function and check if the result matches the expected result
        self.assertEqual(collections.Counter(expected_result), collections.Counter(cp.most_active_cookie(date)))

if __name__ == '__main__':
    unittest.main()
