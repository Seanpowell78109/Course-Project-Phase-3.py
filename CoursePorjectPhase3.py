import datetime

def is_valid_date(date_str):
    
    try:
        datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def write_employee_data(filename, data):
    
    with open(filename, "a") as f:
        f.write("|".join(str(item) for item in data) + "\n")

def generate_report(filename):
    """Generates an employee report based on user input."""

    from_date_input = input("Enter the From Date (mm/dd/yyyy) or 'All': ")

    if from_date_input.lower() != "all" and not is_valid_date(from_date_input):
        print("Invalid date format. Please use mm/dd/yyyy.")
        return

    totals = {
        "employees": 0,
        "hours": 0,
        "tax": 0,
        "net_pay": 0,
    }

    with open(filename, "r") as f:
        for line in f:
            record = line.strip().split("|")
            if len(record) != 6:  # Check if the record has the expected number of fields
                print(f"Skipping invalid record: {line.strip()}")
                continue

            from_date, to_date, name, hours, rate, tax_rate = record
            hours = float(hours)
            rate = float(rate)
            tax_rate = float(tax_rate)

            if from_date_input.lower() == "all" or from_date == from_date_input:
                gross_pay = hours * rate
                income_tax = gross_pay * tax_rate
                net_pay = gross_pay - income_tax

                print(f"From Date: {from_date}, To Date: {to_date}, Employee: {name}, Hours: {hours:.2f}, Rate: ${rate:.2f}, Gross Pay: ${gross_pay:.2f}, Tax Rate: {tax_rate:.2%}, Income Tax: ${income_tax:.2f}, Net Pay: ${net_pay:.2f}")

                totals["employees"] += 1
                totals["hours"] += hours
                totals["tax"] += income_tax
                totals["net_pay"] += net_pay

    print("\n--- Report Totals ---")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']:.2f}")
    print(f"Total Income Tax: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net_pay']:.2f}")

# Example usage (replace with your actual data entry loop):
filename = "employee_data.txt"

# Simulate data entry (replace with your actual data entry loop)
employee_data = [
    ("01/01/2023", "01/15/2023", "Alice", 40, 20, 0.20),
    ("01/01/2023", "01/15/2023", "Bob", 35, 25, 0.25),
    ("01/16/2023", "01/31/2023", "Charlie", 42, 22, 0.22),
]

for data in employee_data:
    write_employee_data(filename, data)

generate_report(filename)
