# aGrIk's Python Extensions
# Author - aGrIk
# Функция, рекурсивно пересчитывающая количество вложенных файлов и папок в директории. Возвращает массив в формате [папки, файлы]
# 
# Аргумент directory - путь к сканируемой папке 
# Для путей Windows использовать countFilesAndFolders(r"путь")
# Для вывода действий в консоль раскомментируйте соответствующие строки

def countFilesAndFolders(directory):
    import os
    directory = os.path.abspath(directory)
    folder = 0
    file = 0
    if len(os.listdir(directory)) > 0:
        for element in os.listdir(directory):
            path = os.path.join(directory, element)
            if os.path.isdir(path): 
                #print("[FOLDER]: " + path)
                foldret = countFilesAndFolders(path)
                folder += int(foldret[0]) + 1
                file += int(foldret[1])
            if os.path.isfile(path):
                #print("[FILE]: " + path)            
                file += 1
    ret = str(folder) + ";" + str(file)
    return ret.split(";")
