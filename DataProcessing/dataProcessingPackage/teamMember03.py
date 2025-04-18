# File Name: teamMember03.py
# Student Name: Rithu Aynampudi
# email: Aynampru@mail.uc.edu
# Assignment Number: Assignment08
# Due Date: 04/20/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Uses a csv file with data to print something interesting
# Brief Description of what this module does: This module uses data from a csv file to provide correct data using class, def, and print statements
# Citations: W3Schools(https://www.w3schools.com/python/), RealPython(https://realpython.com/)
 
# teamMember03.py

class teamMember03:
    def print_something_interesting(self, data):
        org_email_count = sum(1 for row in data if row['email'].strip().endswith('.org'))
        print(f"Total emails ending in '.org': {org_email_count}")
        print("team member 03")
         