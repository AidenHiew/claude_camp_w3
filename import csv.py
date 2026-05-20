import csv
from tkinter import Tk, filedialog

def read_csv(file_path):
    with open(file_path, 'r') as f:
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]
    return data

# Open file picker
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

if file_path:
    data = read_csv(file_path)
    print(f"Loaded {len(data)} rows from {file_path}")
else:
    print("No file selected")

