#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv

PATH_TO_FILE = './Corp Summary.csv'

def uniq_departament(dataframe: list):
    return list(set(elem['Департамент'] for elem in dataframe))


def ierarchy(dataframe: list):
    unique_departament = uniq_departament(dataframe)
    ierarchy = dict.fromkeys(unique_departament)
    for dept in unique_departament:
        otdel = set()
        for line in dataframe:
            if dept == line['Департамент']:
                otdel.add(line['Отдел'])
        ierarchy[dept]=otdel
    print("Иерархия")
    for departament, otdel in ierarchy.items():
        print(departament + ': ' + ', '.join(otdel))
        
        
def departament_report(dataframe: list):
    unique_departaments = uniq_departament(dataframe)
    header = ['Название', 'Численность', 'Минимальная зарплата', 'Максимальная зарплата', 'Cредняя зарплата']
    report = {key: [] for key in header}
    report['Название']=unique_departaments
    
    number_of_people=[]
    for elem in unique_departaments:
        count = 0
        for line in dataframe:
            if elem == line['Департамент']:
                count += 1
        number_of_people.append(count)
    report['Численность']=number_of_people
    
    min_salary=[]
    max_salary=[]
    avg_salary=[]
    for elem in unique_departaments:
        salary = []
        for line in dataframe:
            if elem == line['Департамент']:
                salary.append(int(line['Оклад']))
        avg_salary.append(sum(salary)/len(salary))  
        min_salary.append(min(salary))
        max_salary.append(max(salary))
    report['Cредняя зарплата']=avg_salary
    report['Минимальная зарплата']=min_salary
    report['Максимальная зарплата']=max_salary
 
    return report

def ready_report(dataframe: list):  
    result = departament_report(dataframe)
    with open("report.csv", 'w', encoding='utf-8') as file:
        file.write(";".join(result.keys()) + '\n')
        for tuple_element in zip(result['Название'],result['Численность'],result['Минимальная зарплата'],
                                 result['Максимальная зарплата'],result['Cредняя зарплата'],):
            file.write(";".join(list(map(str, tuple_element))) + '\n')
            
            
def main():
    with open('./Corp Summary.csv', 'r') as file_obj:
        reader = csv.DictReader(file_obj, delimiter=';')
        dataframe = [empl for empl in reader]
    command = 0
    while command != 4:
        print('Выберете одну из четырёх команд: \n         1 - Вывести иерархию департаментов \n         2 - Вывести сводный отчёт по департаментам\n         3 - Сохранить сводный отчёт по департаментам в виде csv-файла\n         4 - Выход из меню'
              )
        command = int(input())
        print()
        if command == 1:
            ierarchy(dataframe)
        if command == 2:
            result = departament_report(dataframe)
            print("{:^15} | {:^11} | {:^20} | {:^20} | {:^20}".format(*result.keys()))
            for tuple_element in zip(result['Название'],
                                     result['Численность'],
                                     result['Минимальная зарплата'],
                                     result['Максимальная зарплата'],
                                     result['Cредняя зарплата'],
                                     ):
                print("{:^15} | {:^11} | {:^20} | {:^21} | {:^20}".format(*tuple_element))
        if command == 3:
            ready_report(dataframe)
            print('Готово')
        if command == 4:
            return 1
if __name__ == '__main__':
    main()


# In[ ]:




