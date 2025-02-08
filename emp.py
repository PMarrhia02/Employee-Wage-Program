import random

def check_attendance():
    print("Welcome to Employee Wage Computation Program on Master Branch")

    attendance = random.choice([1, 0])

    match attendance:
        case 0:
            print("The Employee is Absent")
            return 0
        case 1:
            print("The Employee is Present")
            job_type = input("Enter a type of job (part/full): ")

            match job_type:
                case 'part':
                    return 20 * 6
                case 'full':
                    return 20 * 8
                case _:
                    return "Invalid job type"

if __name__ == "__main__":
    wage = check_attendance()
    print("Wage:", wage)
    print("Welcome to Employee Wage Computation")






