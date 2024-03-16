import csv

'''Считывание файла'''
with open('vacancy.txt', encoding='utf8') as file:
    r = csv.reader(file, delimiter=';')
    r = list(r)[1:]
    r = sorted(r, key=lambda x: x[3])

'''Программа работает до ввода "устал"'''
search = input()
length = len(r)
prev_ind = 0
while search != 'устал':
    ind = length // 2
    cur_length = length // 2
    answer = []

    '''Алгоритм бинарного поиска'''
    while not answer:
        if r[ind][3] > search:
            ind -= cur_length // 2
            cur_length //= 2
        elif r[ind][3] < search:
            ind += max(cur_length // 2, 1)
            cur_length //= 2
        elif r[ind][3] == search:
            start = ind
            if start - 1 > 0:
                while r[start - 1][3] == search:
                    start -= 1
            end = start
            if end + 1 < length:
                while r[end + 1][3] == search:
                    end += 1
            answer = r[start: end + 1]

            '''Вывод ответа, если удалось найти'''
            for line in sorted(answer, key=lambda x: int(x[0])):
                salary, work_type, size, role, company = line
                salary = int(salary)
                print(f'В {company} найдена искомая вакансия: {role}. З/п составит: {salary}')

        '''Вывод ответа, если не удалось найти'''
        if (ind == 0 or ind == len(r) - 1 or prev_ind == ind) and r[ind][3] != search:
            print('К сожалению, ничего не удалось найти')
            break
        prev_ind = ind

    '''Новый ввод'''
    search = input()
