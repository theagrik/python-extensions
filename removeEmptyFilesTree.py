# aGrIk's Python Extensions
# 
# Процедура, рекурсивно удаляющая все пустые файлы во всех вложенных директориях (ОСТОРОЖНО: МОЖЕТ ПОВЛИЯТЬ НА РАБОТУ СИСТЕМЫ)
# 
# Аргумент directory - путь к сканируемой папке 
# Для путей Windows использовать removeEmptyFilesTree(r"путь")
# Для вывода действий в консоль раскомментируйте соответствующие строки

def removeEmptyFilesTree(directory):
    import os
    directory = os.path.abspath(directory)
    #print("[HANDLE]: " + directory)
    if len(os.listdir(directory)) > 0:
        print("[HANDLE]: Folder isn't empty, scanning")
        for element in os.listdir(directory):
            path = os.path.join(directory, element)
            #print("[SCANNER]: " + path)
            if os.path.isdir(path): removeEmptyFilesTree(path)
            if os.path.isfile(path) and os.path.getsize(path) == 0: 
                os.remove(path)
                #print("[DELETE]: " + directory)
            #elif os.path.getsize(path) > 0: print("[HANDLE]: File isn't empty, skipping")
    else:
        #print("[HANDLE]: Folder is empty")
