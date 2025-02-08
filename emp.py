import random

def check_attend():
    print("Welcome To Employee Wage Computation Prigram on Master Branch")
    attendance = random.choice([1, 0])
    if attendance == 1:
        print("The Employee is present")
    else:
        print("The Employee is Absent")
if __name__ == "__main__":
  check_attend()
  print("Welcome to Employee Wage Computation")
