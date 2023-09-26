import sys
import time
import random

#módulo os do Python fornece funções para interagir com o sistema operacional. E
import os
# O módulo shutil oferece várias operações de alto nível em arquivos e coleções
import shutil
 
 

#Método watchdog para automatizar a movimentação dos arquivos entre as
# pastas assim que eles forem baixados, usaremos o

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/André/Downloads"              # Adicione o caminho da sua pasta "Downloads".
to_dir = "C:/Users/André/Desktop/opro103" # Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):
    #código para genrenciar o evento de criação de um novo arquivo no diretório

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Baixado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                # condicional para over os arquivos
                if os.path.exists(path2):

                    print("diretorio existe....")
                    print("moonwalkando" + file_name +"....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("criando diretorio")
                    os.makedirs(path2)
                    print("moonwalkando" + file_name +"....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)
#: defina o valor do parâmetro recursive (recursivo) como True para observar as alterações em todos ossubdiretórios do caminho fornecido.


# Inicie o Observer
observer.start()
## loop
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()
