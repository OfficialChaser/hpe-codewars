import os
import datetime

def generate_date_range(start_date, stop_date):
    """Generate a list of date strings (YYYY-MM-DD) from start_date to stop_date."""
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    stop = datetime.datetime.strptime(stop_date, "%Y-%m-%d")
    delta = datetime.timedelta(days=1)

    dates = []
    while start <= stop:
        dates.append(start.strftime("%Y-%m-%d"))
        start += delta
    return dates

def find_funds(signal, start_date, stop_date, directory="student_datasets"):
    """Scan transaction files for matching signal and sum funds."""
    date_range = set(generate_date_range(start_date, stop_date))
    transaction_ids = set()
    total_funds = 0.0

    for date in date_range:
        filename = f"{directory}/files/{date}.txt"
        
        if os.path.exists(filename):
        
            with open(filename, "r") as file:
                for line in file:
                    
                    parts = line.strip().split(",")

                    transaction_id, _, _, _, data_out, operator_code = parts

                    if operator_code.strip() == signal:
                        transaction_ids.add(transaction_id.strip())
                        
                        funds = float(data_out)
                        total_funds += funds

    for transaction_id in sorted(transaction_ids):
        print(transaction_id)
    print(f"Funds Found: {total_funds:.2f}")

signal = input()
start_date = input()
stop_date = input()
find_funds(signal, start_date, stop_date) 
