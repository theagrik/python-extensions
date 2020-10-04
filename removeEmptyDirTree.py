# aGrIk's Python Extensions
# 
# Процедура, рекурсивно удаляющая все вложенные пустые папки в директории (ОСТОРОЖНО: МОЖЕТ ПОВЛИЯТЬ НА РАБОТУ СИСТЕМЫ)
# 
# Аргумент directory - путь к сканируемой папке
# Для путей Windows использовать removeEmptyDirTree(r"путь")
# Для вывода действий в консоль раскомментируйте соответствующие строки

def removeEmptyDirTree(directory):
    import os
    directory = os.path.abspath(directory)
    print("[HANDLE]: " + directory)
    if len(os.listdir(directory)) > 0:
        #print("[HANDLE]: Folder isn't empty, scanning")
        for element in os.listdir(directory):
            path = os.path.join(directory, element)
            #print("[SCANNER]: " + path)
            if os.path.isdir(path): removeEmptyDirTree(path)
    if len(os.listdir(directory)) == 0:
        os.rmdir(directory)
        #print("[DELETE]: " + directory)