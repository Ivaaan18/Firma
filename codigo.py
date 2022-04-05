import os
import pathlib
import shutil
from distutils.dir_util import copy_tree



c = r'\c$\Users'
ruta_aplicativo = pathlib.Path().absolute()
ruta_aplicativo = str(ruta_aplicativo)
ruta_archivos_inicio = (ruta_aplicativo + '\\' + 'prueba_aplicativo')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def printear_usuarios(pc, c=r'\c$\Users'):
    
    os.chdir(r'\\' + pc + c)
    
    users=os.listdir() #Lista de los usuarios logados en pc

    start_letter1 = ('a1')
    start_letter2 = ('a2')
    start_letter3 = ('A1')
    start_letter4 = ('A2')

    with_s1 = [x for x in users if x.startswith(start_letter1)] 
    with_s2 = [x for x in users if x.startswith(start_letter2)] 
    with_s3 = [x for x in users if x.startswith(start_letter3)] 
    with_s4 = [x for x in users if x.startswith(start_letter4)] 

    usuarios_pc = with_s1 + with_s2 + with_s3 + with_s4
    
    
    return(usuarios_pc)

def ejecucion_de_copia():
    
    for pc in pcs: #Este bucle itera la lista de pcs 

        try: #Control de errores pc
            #1.- Si tenemos los usuarios nos podemos saltar esta parte.

            usuarios_pc = printear_usuarios(pc, c)
            print('\n')
            print(color.BOLD + pc + color.END)


            for usuario in usuarios_pc: #Dentro de cada pc iteramos en los usuarios.
                usuario = usuario.capitalize()
                if usuario in os.listdir(ruta_archivos_inicio): 
                    print(usuario)
                    try: #Control de errores de usuarios
                        ruta = '\AppData\Roaming\Microsoft'
                        directorio_microsoft = r'\\' + pc + c + "\\" + usuario + ruta

                        DIRECTORIO_ORIGEN = ruta_archivos_inicio + '\\' + usuario
                        #DIRECTORIO_ORIGEN = r'C:\\Users\\adm-a202781\\firma\\biblioteca'
                        DIRECTORIO_DESTINO = directorio_microsoft


                        if 'Signatures' in os.listdir(directorio_microsoft):
                            print("Copiando... del directorio: " + DIRECTORIO_ORIGEN + ' al directorio: ' + DIRECTORIO_DESTINO + "\\" + "Signatures")
                            #copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO + "\\" + "Signatures")
                            print("Copiado", "\n")


                        else:
                            print("Copiando... del directorio: " + DIRECTORIO_ORIGEN + ' al directorio: ' + DIRECTORIO_DESTINO + "\\" + "Firmas")
                            #copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO + "\\" + "Firmas")
                            print("Copiado", "\n")                  

                    except:
                        ruta = '\AppData\Roaming\Microsoft'
                        directorio_microsoft = r'\\' + pc + c + "\\" + usuario + ruta

                        DIRECTORIO_ORIGEN = ruta_archivos_inicio + '\\' + usuario
                        #DIRECTORIO_ORIGEN = r'C:\\Users\\adm-a202781\\firma\\biblioteca'
                        DIRECTORIO_DESTINO = directorio_microsoft

                        #os.mkdir(directorio_microsoft + "\\" + "Signatures")
                        print("Copiando... del directorio: " + DIRECTORIO_ORIGEN + ' al directorio: ' + DIRECTORIO_DESTINO + "\\" + "Signatures")
                        #copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO + "\\" + "Signatures")
                        print("Copiado", "\n")

                else:
                    pass
        except: #Con el primer for itereamos en los pcs, realizamos este control de errores para evitar perder tiempo a la hora de saber que no tenemos conexion al pc
            print('\n' + "No se puede acceder al pc "+ color.BOLD + pc + color.END + " está desconectado")

pcs = ['pcs0345','pcs0346', 'pcs0347', 'pcs0348']

ejecucion_de_copia()

print("finalizado")