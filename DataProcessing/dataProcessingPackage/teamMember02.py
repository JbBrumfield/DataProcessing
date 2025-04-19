# File Name: teamMember02.py
# Student Name: Sharvari Patil
# email: patilsg@mail.uc.edu
# Assignment Number: Assignment08
# Due Date: 04/20/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Uses a csv file with data to print something interesting
# Brief Description of what this module does: This module uses data from a csv file to provide correct data using class, def, and print statements
# Citations: W3Schools(https://www.w3schools.com/python/), RealPython(https://realpython.com/)
 

class teamMember02:
    def print_something_interesting(self, data):
        """
        Prints something interesting from the csv
        @Returns the number of addresses that contain BLVD in them
        """
        blvd_count = sum(1 for row in data if 'Blvd' in row['address'])
        print(f"Number of addresses containing 'Blvd': {blvd_count}")
        print("team member 02")

