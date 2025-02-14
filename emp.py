print("Employee Wage Calculator (Max: 100 hours OR 20 days)")

wage_type = input("Enter 'daily' or 'hourly' wage: ").strip().lower()
total_wage = 0
days = 0
hours = 0

if wage_type == "daily":
    daily_wage = float(input("Enter your daily wage (Rs.): "))
    
    while days < 20:
        days += 1
        total_wage += daily_wage
        print(f"Day {days}: Total Wage = Rs. {total_wage}")

elif wage_type == "hourly":
    hourly_wage = float(input("Enter your hourly wage (Rs.): "))
    hours_per_day = float(input("Enter hours worked per day: "))

    while days < 20 and hours < 100:
        days += 1
        hours += hours_per_day
        total_wage += hourly_wage * hours_per_day
        print(f"Day {days}: Total Wage = Rs. {total_wage}")

        if hours >= 100:
            break

else:
    print("Invalid input!")

print(f"Final Wage: Rs. {total_wage}")










