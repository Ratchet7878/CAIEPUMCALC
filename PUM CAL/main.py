def marks():
    boundaries = []
    check = input("AS/A Level? ")
    if check.lower() == 'as':
        for i in range(5):
            mark = int(input("Enter mark 'a' to 'e' only : "))
            boundaries.append(mark)
    elif check.lower() == 'a':
        for i in range(6):
            mark = int(input("Enter mark 'A*' to 'E' only : "))
            boundaries.append(mark)
    else:
        return "Error"

    return boundaries

def weightMarks(weiFact, rawMark):
    rawMark = rawMark * weiFact
    return rawMark

def totalMark(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum


def gradeCheck(arr, rawMark, arrLen):
    if arrLen == 5:
        if rawMark >= arr[0]:
            return "a (ASL)"
        elif rawMark >= arr[1]:
            return "b (ASL)"
        elif rawMark >= arr[2]:
            return "c (ASL)"
        elif rawMark >= arr[3]:
            return "d (ASL)"
        elif rawMark >= arr[4]:
            return "e (ASL)"
        else:
            return "UNGRADED"
    else:
        if rawMark >= arr[0]:
            return "A* (AL)"
        elif rawMark >= arr[1]:
            return "A (AL)"
        elif rawMark >= arr[2]:
            return "B (AL)"
        elif rawMark >= arr[3]:
            return "C (AL)"
        elif rawMark >= arr[4]:
            return "D (AL)"
        elif rawMark >= arr[5]:
            return "E (AL)"
        else:
            return "UNGRADED"

def pumCalc(totalMark, arr, lenArr, grade):
    if lenArr == 5:
        if grade == 'a (ASL)':
            pum = (((totalMark - arr[1]) // (arr[0] - arr[1])) * 10) + 80
        elif grade == 'b (ASL)':
            pum = (((totalMark - arr[2]) // (arr[1] - arr[2])) * 10) + 70
        elif grade == 'c (ASL)':
            pum = (((totalMark - arr[3]) // (arr[2] - arr[3])) * 10) + 60
        elif grade == 'd (ASL)':
            pum = (((totalMark - arr[4]) // (arr[3] - arr[4])) * 10) + 50
        elif grade == 'e (ASL)':
            pum = ((totalMark // arr[4]) * 10) + 40
        elif grade == 'UNGRADED':
            pum = 0
        return pum
    elif lenArr >= 6:
        if grade == 'A* (AL)':
            pum = (((totalMark - arr[1]) // (arr[0] - arr[1])) * 10) + 90
        elif grade == 'A (AL)':
            pum = (((totalMark - arr[2]) // (arr[1] - arr[2])) * 10) + 80
        elif grade == 'B (AL)':
            pum = (((totalMark - arr[3]) // (arr[2] - arr[3])) * 10) + 70
        elif grade == 'C (AL)':
            pum = (((totalMark - arr[4]) // (arr[3] - arr[4])) * 10) + 60
        elif grade == 'D (AL)':
            pum = (((totalMark - arr[5]) // (arr[4] - arr[5])) * 10) + 50
        elif grade == 'E (AL)':
            pum = ((totalMark // arr[5]) * 10) + 40
        elif grade == 'UNGRADED':
            pum = 0
        return pum

# MAIN PROGRAM

exam = input("Enter the syllabus name : ")
code = input("Enter the syllabus code : ")
print("Enter the grade boundaries from the grade threshold")
#gets the grade boundaries
boundaries = []
boundaries = marks()
n = len(boundaries)
#gets the individual mark of the candidates
individual_marks = []
for i in range(5):
    mark = int(input("Enter marks for P1 to P5 in order. Put '0' if the marks don't exist : "))
    individual_marks.append(mark)
#weights the marks
for i in range(len(individual_marks)):
    weight = int(input("Enter weighting factors for P1 to P5 in order. Put '1' if the marks don't exist : "))
    individual_marks[i] = individual_marks[i] * weight
#calculate total mark for grading
total = totalMark(individual_marks)
#calculates the grade
grade = gradeCheck(boundaries, total, n)
#calculates the PUM

percentage = pumCalc(total, boundaries, n, grade)

#creates file
file = open("Results.txt", "w")

file.writelines("Component Name : ")
file.writelines(exam)
file.writelines("\n")
file.writelines("Component Code : ")
file.writelines(code)
file.writelines("\n")
file.writelines("Component Grade : ")
file.writelines(grade)
file.writelines("\n")
file.writelines("Percentage Uniform Mark : ")
file.writelines(str(percentage))


file.close()


