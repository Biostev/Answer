import csv

'''Считывание файл'''
with open('vacancy.txt', encoding='utf8') as file:
    r = csv.reader(file, delimiter=';')
    r = list(r)[1:]

'''Сортировка компании по убыванию'''
for i in range(len(r)):
    for j in range(1, i):
        line1 = r[j - 1]
        line2 = r[j]
        if line1[4] > line2[4]:
            r[j - 1], r[j] = r[j], r[j - 1]

'''Сортировка зарплаты по убыванию'''
for i in range(len(r)):
    for j in range(i, 1, -1):
        line1 = r[j - 1]
        line2 = r[j]
        if int(line1[0]) > int(line2[0]):
            r[j - 1], r[j] = r[j], r[j - 1]

'''Вывод ответа'''
answer = r[-1]
salary, work_type, size, role, company = answer
salary = int(salary)
print(f'В компании {company} есть профессия: {role}, з/п в такой компании составит: {salary}')
