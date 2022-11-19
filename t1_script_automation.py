import csv, os
import shutil

def csv_read():
    file_name = 'C:/Users/USUARIO/Desktop/task3/students.csv'

    with open(file_name, newline='\n') as f:
        jump = next(f)
        read = csv.reader(f)
        data = dict(read)

    return data
        


def create_directories(dictionary):
    for creation in dictionary:
        if not os.path.exists('C:/Users/USUARIO/Desktop/task3/'+ dictionary[creation] + '.' + creation):
            os.mkdir('C:/Users/USUARIO/Desktop/task3/' + dictionary[creation] + '.' + creation)


create_directories(csv_read())


########################################################################################

game_move, python_move = [], []
tutorial_and_games_path = 'C:/Users/USUARIO/Desktop/task3/data'
lista = os.listdir(tutorial_and_games_path)
#print(lista)

for item in lista:
     if 'game' in item.lower() and "." not in item:
        #print(item) 
        game_move.append(item)
        
     if 'python' in item.lower():
        python_move.append(item)

#print(game_move)
#print(python_move)

path_move = 'C:/Users/USUARIO/Desktop/task3'

for item in game_move:
    if os.path.exists(tutorial_and_games_path + '/' + item):
        shutil.move(tutorial_and_games_path + '/' + item,'C:/Users/USUARIO/Desktop/task3/15.Games')


for item in python_move:
    if os.path.exists(tutorial_and_games_path + '/' + item):
        shutil.move(tutorial_and_games_path + '/' + item,'C:/Users/USUARIO/Desktop/task3/16.Tutorials')