# aGrIk's Python Extensions
# Author - aGrIk
# Процедура, рекурсивно удаляющая все файлы с одинаковым расширением во всех вложенных директориях (ОСТОРОЖНО: МОЖЕТ ПОВЛИЯТЬ НА РАБОТУ СИСТЕМЫ)
# 
# Аргумент directory - путь к сканируемой папке 
# Аргумент extension - расширение файла (либо на что он заканчивается)
# Для путей Windows использовать removeFilesByExtension(r"путь", extension)
# Для вывода действий в консоль раскомментируйте соответствующие строки

def removeFilesByExtension(directory, extension):
    import os
    directory = os.path.abspath(directory)
    #print("[HANDLE]: " + directory)
    if len(os.listdir(directory)) > 0:
        print("[HANDLE]: Folder isn't empty, scanning")
        for element in os.listdir(directory):
            path = os.path.join(directory, element)
            #print("[SCANNER]: " + path)
            if os.path.isdir(path): removeFilesByExtension(path)
            if os.path.isfile(path) and element.endswith(extension) == 0: 
                os.remove(path)
                #print("[DELETE]: " + directory)
            #elif os.path.getsize(path) > 0: print("[HANDLE]: Incorrect file, skipping")
    #else:
        #print("[HANDLE]: Folder is empty")
