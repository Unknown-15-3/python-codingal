import matplotlib.pyplot as plt

student = ["Daniel", "Emma", "Sophia", "Xiandra", "Adam", "Lois", "Danny"]

student_marks = [43, 75, 63, 55, 64, 31, 78]

mark_percentage = []

for x in student_marks:
    res = (x/80)*100
    mark_percentage.append(res)
print("The mark percentage of students are:- ", mark_percentage)

def marks_line_chart():
    plt.plot(student, student_marks)
    plt.title("studends mark line graph")
    plt.xlabel("students")
    plt.ylabel("marks obtained")
    plt.show()
marks_line_chart()
def percentage_bar_chart():
    plt.bar(student, mark_percentage)
    plt.title("students percentage in bar graph")
    plt.xlabel("students")
    plt.ylabel("percentage obtained")

percentage_bar_chart()