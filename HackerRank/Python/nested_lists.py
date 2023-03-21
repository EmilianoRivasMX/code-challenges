"""
Given the names and grades for each student in a class of  students, store them in a 
nested list and print the name(s) of any student(s) having the second lowest grade.

If there are multiple students with the second lowest grade order their names alphabetically.
"""

# if __name__ == '__main__':
#     records = []
#     students = int(input("\nNumber of students: "))
#     print(30*"-")

#     # Itera el numero de veces que indique el usuario
#     for _ in range(students): 
#         name = input("Name: ")
#         score = float(input("Score: "))
#         records.append([name, score])
#         print(30*"-")

#     print(f"All records: {records}")

#     # Order records
#     records.sort(key=lambda record: int(record[1]))

#     # Looks for the second lowest grade
#     for i in range(students):
#         if records[i][1] != records[0][1]:
#             second_lowest_grade = records[i][1]
#             break

#     # Look for students with second lowest grade
#     second_lowest_grade_studens = [record[0] for record in records if record[1] == second_lowest_grade]
#     second_lowest_grade_studens.sort()

#     # Print results
#     print(f"Ordered records: {records}")
#     print(f"Second lowest grade: {second_lowest_grade}")
#     print(f"Studens: {second_lowest_grade_studens}")

if __name__ == '__main__':
    records = []
    students = int(input())
    for _ in range(students):
        name = input()
        score = float(input())
        records.append([name, score])
        
    # Order records
    records.sort(key=lambda record: record[1])

    # Looks for the second lowest grade
    for i in range(students):
        if records[i][1] != records[0][1]:
            second_lowest_grade = records[i][1]
            break

    # Looks for students with second lowest grade and sort them alphabetically
    second_lowest_grade_students = [record[0] for record in records if record[1] == second_lowest_grade]
    second_lowest_grade_students.sort()

    # Print results
    print(*second_lowest_grade_students, sep='\n')