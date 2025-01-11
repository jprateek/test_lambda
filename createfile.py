import csv
import os

def create_csv_file(filename):
    # Define the header
    header = ['name', 'age']
    
    # Define some sample data
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    # Construct the file path
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, filename)
    
    # Check if the file already exists
    if not os.path.exists(file_path):
        # Write to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f'File {filename} created successfully.')
    else:
        print(f'File {filename} already exists.')

# Example usage
print('Creating a CSV file...')
create_csv_file('output.csv')