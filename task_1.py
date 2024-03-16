import csv

with open('vacancy.txt', encoding='utf8') as file:
    r = csv.reader(file, delimiter=';')
    r = list(r)[1:]

salaries = {}
for line in sorted(r, key=lambda x: (10 ** 6 - int(x[0]), int(x[2]), x[3])):
    salary, work_type, size, role, company = line
    salary = int(salary)
    if work_type not in salaries.keys():
        salaries[work_type] = (role, salary)

answer = []
for key in salaries.keys():
    answer.append([key, salaries[key][0], salaries[key][1]])
with open('vacancy_new.csv', 'w', encoding='utf8') as file:
    w = csv.writer(file, delimiter=';', quotechar='"', lineterminator='\n')
    w.writerow(['Work_Type', 'Role', 'Salary'])
    w.writerows(answer)

a = salaries['стажер']
print(f"{a[0]} - {a[1]}")
