# File Name : teamMember01.py
# Student Name: Jacob Brumfield
# email:  brumfijb@mail.uc.edu
# Assignment Number: Assignment 08 (remake)
# Due Date:   4/20/2025 (easter!)
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Edit individual team member.py files to print some interesting information based on the dataset.

# Brief Description of what this module does. This module prints the top 5 most common states in the csv file (very interesting)
# Citations: https://stackoverflow.com/questions/36247277/using-python-to-find-the-most-common-values-in-the-column-of-csv-file

# Anything else that's relevant:
from collections import Counter

class teamMember01:
    def print_something_interesting(self, data):
        print("team member 01")
        state_counter = Counter([row['state'] for row in data])
        print("Top 5 most common states in the data:")
        for state, count in state_counter.most_common(5):
            print(f"{state}: {count} entries")
            
        

