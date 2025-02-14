def calculate_wage():
    print("Employee Wage Calculator (20 Working Days/Month)")

    wage_type = input("Do you earn 'daily' or 'hourly'? ").strip().lower()

    if wage_type == "daily":
        daily_wage = float(input("Enter your daily wage (Rs.): "))
        monthly_wage = daily_wage * 20

    elif wage_type == "hourly":
        hourly_wage = float(input("Enter your hourly wage (Rs.): "))
        hours_per_day = float(input("Enter hours you work per day: "))
        monthly_wage = hourly_wage * hours_per_day * 20

    else:
        print("Invalid input! Please enter 'daily' or 'hourly'.")
        return

    print(f"Your estimated monthly wage: Rs. {monthly_wage:.2f}")

calculate_wage()









