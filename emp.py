class EmployeeWage:
    @classmethod
    def calculate_wage(cls, company, wage_type, wage, max_days, max_hours, hours_per_day=0):
        total_wage = 0
        total_days = 0
        total_hours = 0

        while total_days < max_days and (wage_type == "daily" or total_hours < max_hours):
            total_days += 1
            if wage_type == "daily":
                total_wage += wage
            else:
                total_hours += hours_per_day
                total_wage += wage * hours_per_day
                if total_hours >= max_hours:
                    break

        print(f"{company} - Final Wage: Rs. {total_wage}")

EmployeeWage.calculate_wage("Company A", "daily", 500, 20, 100)
EmployeeWage.calculate_wage("Company B", "hourly", 50, 22, 120, 5)













