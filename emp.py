class EmployeeWage:
    total_wage = 0
    total_days = 0
    total_hours = 0

    @classmethod
    def calculate_wage(cls):
        wage_type = input("Daily or Hourly? ").strip().lower()

        if wage_type == "daily":
            daily_wage = float(input("Daily wage (Rs.): "))
            while cls.total_days < 20:
                cls.total_days += 1
                cls.total_wage += daily_wage
                print(f"Day {cls.total_days}: Rs. {cls.total_wage}")

        elif wage_type == "hourly":
            hourly_wage = float(input("Hourly wage (Rs.): "))
            hours_per_day = float(input("Hours per day: "))
            while cls.total_days < 20 and cls.total_hours < 100:
                cls.total_days += 1
                cls.total_hours += hours_per_day
                cls.total_wage += hourly_wage * hours_per_day
                print(f"Day {cls.total_days}: Rs. {cls.total_wage}")

        print(f"Final Wage: Rs. {cls.total_wage}")

EmployeeWage.calculate_wage()











