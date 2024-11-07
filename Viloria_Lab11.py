# Empty List
grades = []
passed = []

while True:
    grade = input("Enter your Grade (or type 'done' to finish): ")

    if grade.lower() == "done":
        break
    if not grade.isdigit() or int(grade) <= 39 or int(grade) >= 101:
        print("Please enter a valid grade between 40 and 100, or 'done' to finish.")
    else:
        grade = int(grade)
        grades.append(grade)
        if grade >= 75:
            passed.append(grade)
        print(f"Grade is: {grade}")

if grades:
    average = sum(grades) / len(grades)
    passing_percent = (len(passed) / len(grades)) * 100
    print(f"Average Grade: {average:.2f}")
    print(f"Passing students percentage: {passing_percent:.2f}%")
    print(f"Number of students passed: {len(passed)}")
    print("All grades entered:", grades)
else:
    print("No grades inputted")
