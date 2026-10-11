import json
from pathlib import Path

# Store the JSON file in the same folder as this Python file
DATA_FILE = Path(__file__).with_name("employees.json")


def load_employees():
    """Load employee records from JSON."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            print("Invalid data format. Starting with an empty list.")
            return []

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON file is empty or invalid. Starting with an empty list.")
        return []


def save_employees(employees):
    """Save employee records to JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)
        return True
    except OSError as error:
        print("Could not save data:", error)
        return False


def get_employee_id():
    while True:
        employee_id = input("Enter employee ID: ").strip()

        if employee_id:
            return employee_id

        print("ID cannot be empty.")


def get_salary():
    while True:
        try:
            salary = float(input("Enter salary: "))

            if salary >= 0:
                return salary

            print("Salary cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")


def add_employee(employees):
    employee_id = get_employee_id()

    if any(e["id"] == employee_id for e in employees):
        print("This employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    salary = get_salary()

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    if save_employees(employees):
        print("Employee added successfully.")


def list_employees(employees):
    if not employees:
        print("No employee records found.")
        return

    print("\n--- Employee Records ---")

    for employee in employees:
        print(
            "ID:", employee["id"],
            "| Name:", employee["name"],
            "| Department:", employee["department"],
            "| Salary:", employee["salary"]
        )


def search_employee(employees):
    employee_id = get_employee_id()

    for employee in employees:
        if employee["id"] == employee_id:
            print("Employee found:")
            print(employee)
            return

    print("Employee not found.")


def update_employee(employees):
    employee_id = get_employee_id()

    for employee in employees:
        if employee["id"] == employee_id:
            print("Leave a field blank to keep its current value.")

            name = input(
                f"Name [{employee['name']}]: "
            ).strip()

            department = input(
                f"Department [{employee['department']}]: "
            ).strip()

            if name:
                employee["name"] = name

            if department:
                employee["department"] = department

            change_salary = input(
                "Change salary? (y/n): "
            ).strip().lower()

            if change_salary == "y":
                employee["salary"] = get_salary()

            if save_employees(employees):
                print("Employee updated successfully.")
            return

    print("Employee not found.")


def delete_employee(employees):
    employee_id = get_employee_id()

    for employee in employees:
        if employee["id"] == employee_id:
            confirm = input(
                "Delete this employee? (y/n): "
            ).strip().lower()

            if confirm == "y":
                employees.remove(employee)

                if save_employees(employees):
                    print("Employee deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Employee not found.")


def filter_by_department(employees):
    department = input("Enter department to filter: ").strip().lower()

    matches = [
        employee for employee in employees
        if employee["department"].lower() == department
    ]

    list_employees(matches)


def sort_employees(employees):
    if not employees:
        print("No records to sort.")
        return

    print("1. Sort by name")
    print("2. Sort by salary")

    choice = input("Choose sorting option: ").strip()

    if choice == "1":
        sorted_list = sorted(
            employees,
            key=lambda employee: employee["name"].lower()
        )
    elif choice == "2":
        sorted_list = sorted(
            employees,
            key=lambda employee: employee["salary"]
        )
    else:
        print("Invalid sorting option.")
        return

    list_employees(sorted_list)


def show_statistics(employees):
    if not employees:
        print("No data available for statistics.")
        return

    salaries = [employee["salary"] for employee in employees]
    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)

    highest = max(employees, key=lambda e: e["salary"])
    lowest = min(employees, key=lambda e: e["salary"])

    print("\n--- Employee Statistics ---")
    print("Total employees:", len(employees))
    print("Total salary:", round(total_salary, 2))
    print("Average salary:", round(average_salary, 2))
    print(
        "Highest salary:",
        highest["name"], "-", highest["salary"]
    )
    print(
        "Lowest salary:",
        lowest["name"], "-", lowest["salary"]
    )

    print("\nEmployees by department:")

    department_counts = {}

    for employee in employees:
        department = employee["department"]
        department_counts[department] = (
            department_counts.get(department, 0) + 1
        )

    for department, count in department_counts.items():
        print(department, ":", count)


def main():
    employees = load_employees()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add employee")
        print("2. List all employees")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Filter by department")
        print("7. Sort employees")
        print("8. Show statistics")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            list_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            update_employee(employees)
        elif choice == "5":
            delete_employee(employees)
        elif choice == "6":
            filter_by_department(employees)
        elif choice == "7":
            sort_employees(employees)
        elif choice == "8":
            show_statistics(employees)
        elif choice == "9":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()