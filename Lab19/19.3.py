import pickle
def task_input():
    task={}
    task['Назва предмету']= input ('Назва предмету')
    task['Кількість годин']= input('Кількість годин')
    task['Викладач']= input('Викладач').split(' ')
    task['Рейтинг']= input('Рейтинг')
    with open('taskdb.txt','wb') as file:
        pickle.dump(task,file)
    return task

def num_of_task():
    n = int(input('Кількість предметів: '))
    return [task_input() for i in range(n)]

def search_task(task_list, task_title):
    return list(filter(lambda task: task['Назва предмету'] == task_title, task_list))

task_list = num_of_task()

while True:
    decision = input('Почнемо пошук {так/ні}?')
    if decision == 'ні':
        break
    task_title = input('Предмет:')
    result = search_task(task_list, task_title)
    if len(result) > 0:
        print(result)
    else:
        print('No result!')