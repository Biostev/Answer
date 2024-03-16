import csv

'''Считываем файл'''
with open('vacancy.txt', encoding='utf8') as file:
    r = csv.reader(file, delimiter=';')
    r = sorted(list(r)[1:], key=lambda x: (x[4], int(x[0])))

'''Создаем словарь с данными о компаниях'''
companies = {}
for line in r:
    salary = int(line[0])
    if salary <= 45000:
        salary *= 0.92
    elif salary <= 50000:
        salary *= 0.9
    else:
        salary *= 0.87
    company = line[4]
    if company not in companies.keys():
        companies[company] = []
    companies[company].append(salary)

'''Строим строки для ответа'''
answer = []
for company in companies.keys():
    salaries = companies[company]
    av_salary = sum(salaries) / len(salaries)
    answer.append(f'{company}: {av_salary}')

'''Записываем ответ в файл'''
with open('vacancy_average.txt', 'w', encoding='utf8') as file:
    file.writelines('\n'.join(answer))
