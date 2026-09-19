"""
Programming Language: Python
IDE Used: Visual Studio Code
Programmers: Hassan Bhatti, Curtis Been
Date: 02/18/2025
Class: CS 4500 - Spring 2025

Description:
This program processes a CSV file containing dates and numerical values.
It extracts column headers (names), dates, and converts numerical values into a presence/absence format.

Central Data Structures:
- List: Used to store names, dates, and presence/absence data.
- CSV File Handling: Reads from an input CSV file and writes outputs to text files.

External Files Used:
- Input: User-provided CSV file.
- Output: 
  - `Names.txt`: Stores organism names, one per line.
  - `DatedData.txt`: Stores dates, one per line.
  - `PresentAbsent.txt`: Stores binary presence/absence values in CSV format.

Execution Instructions:
1. Ensure Python 3.x is installed on your system.
2. Place the CSV file in the same directory as this script.
3. Run the script using: `python SG1.py`
4. Enter the name of the CSV file when prompted.
5. The program will generate three output files.
6. Press ENTER when prompted to exit.

External Sources Used:
- Python CSV module documentation: https://docs.python.org/3/library/csv.html
- File handling documentation: https://docs.python.org/3/tutorial/inputoutput.html
- Python reading a file: https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
- Extracting data from CSV: https://stackoverflow.com/questions/69524576/how-to-extract-specific-data-from-csv-file-and-store-it-in-variable-using-pytho
- Put Extracted data into new file: https://python-forum.io/thread-879.html
- Working with CSV files: https://www.geeksforgeeks.org/working-csv-files-python/
"""

import os
import csv


# Function Definitions
def get_valid_filename():
    """Prompts the user for a valid CSV filename and ensures it exists."""
    while True:
        # Get the filename from the user
        filename = input("Enter the CSV filename: ").strip()
        # Check if the filename is valid
        if filename.lower().endswith('.csv'):
            #check if the file exists
            if os.path.exists(filename):
                return filename  # Return the valid filename
            else:
                print("Error: File does not exist. Try again.")
        else:
            print("Error: Filename must end with .CSV. Try again.")

def process_csv_file(filename):
    """Reads the CSV file and processes data into required output files."""
    # Read the CSV file and extract data
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # Ensure the file has at least two lines (header + data)
        if not data or len(data) < 2:
            print("Error: CSV file must contain at least two lines (header + data). Exiting.")
            return

        # Extract headers (Names), excluding the first empty cell
        names = data[0][1:]
        
        # Lists to store extracted dates and presence/absence data
        dates = []
        presence_absence = []
        
        for row in data[1:]:  # Process data rows
            dates.append(row[0])  # First column is the date
            
            # Convert numerical values to presence/absence (1 for positive, 0 for zero)
            presence_absence.append(["1" if float(val) > 0 else "0" for val in row[1:]])
    
    # Write names to Names.txt, one per line
    with open("Names.txt", 'w') as names_file:
        names_file.write("\n".join(names) + "\n")
    
    # Write extracted dates to DatedData.txt, one per line
    with open("DatedData.txt", 'w') as dates_file:
        dates_file.write("\n".join(dates) + "\n")
    
    # Write presence/absence matrix to PresentAbsent.txt in CSV format
    with open("PresentAbsent.txt", 'w') as presence_file:
        presence_file.writelines(",".join(row) + "\n" for row in presence_absence)

def main():
    """Main function to execute the SG1 program."""
    print("""SG1: This program processes a CSV file containing dates and numerical values.
It extracts names, dates, and presence/absence data and writes them to separate files.""")
    
    filename = get_valid_filename()  # Prompt user for a valid CSV filename
    process_csv_file(filename)  # Process the CSV file
    
    input("Processing complete. Press ENTER to exit.")  # Pause before exiting

if __name__ == "__main__":
    main()
