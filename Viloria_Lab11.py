# Empty List
grades = []
passed = []

while True:
    grade = input("Enter your Grade (or type 'done' to finish): ")
    if grade.lower() == "done":
        break
    else:
        try:
            grade = int(grade)
            grades.append(grade)
            if grade >= 75:
                passed.append(grade)
            print(f"Grade is: {grade}")
        except ValueError:
            print("Please enter a valid grade or 'done' to finish.")

if grades:
    average = sum(grades) / len(grades)
    passing_percent = (len(passed) / len(grades)) * 100
    
    print(f"Average Grade: {average:.2f}")
    print(f"Passing students percentage: {passing_percent:.2f}%")
else:
    print("No Grades Inputted")

