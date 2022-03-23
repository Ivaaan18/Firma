import os
import pathlib

ruta_aplicativo = pathlib.Path().absolute()
ruta_aplicativo = str(ruta_aplicativo)

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


#Listas

#pcs = ['pcs0346']

pcs = ['pcs0345','pcs0346', 'pcs0347', 'pcs0348']
#usuarios = []
c = r'\c$\Users'

pc_fallados = []
usuarios_fallados = []  

#contador = 0


ruta_archivos_inicio = (ruta_aplicativo + '\\' + 'prueba_aplicativo')




for pc in pcs: #Este bucle itera la lista de pcs 
    
    try: #Control de errores pc
        #1.- Si tenemos los usuarios nos podemos saltar esta parte.
        
        usuarios_pc = printear_usuarios(pc, c)
        print('\n')
        print(color.BOLD + pc + color.END)
        #print(usuarios_pc)
        #print(len(usuarios_pc))


        for usuario in usuarios_pc: #Dentro de cada pc iteramos en los usuarios.
            usuario = usuario.strip().lower().replace(" ", "")
            
            try: #Control de errores de usuarios
                ruta = '\AppData\Roaming\Microsoft'
                os.chdir(r'\\' + pc + c + "\\" + usuario + ruta)
                directorio_microsoft = os.listdir()

                try:#control de errores para los prints este hay que quitarlo cuando funcione el código. Sobra!!!!!
                    if 'Firmas' in directorio_microsoft:
                        firma = '\AppData\Roaming\Microsoft\Firmas'
                        os.chdir(r'\\' + pc + c + "\\" + usuario + firma)
                        print(color.BOLD + "usuario: " + usuario + color.END)
                        #print(os.getcwd())  
                        
                        ruta_archivos_destino = (r'\\' + pc + c + "\\" + usuario + firma)
                        print("Ruta de red: " + ruta_archivos_destino)
                        print("Ruta local: " + ruta_archivos_inicio) 
                        
                        
                        #shutil.copy(ruta_carpeta_inicio, ruta_carpeta_destino + "LCE.htm")
                        #shutil.copy(ruta_carpeta_inicio, ruta_carpeta_destino + "LCE_archivos")
                        
                        
                        try:
                            os.chdir(ruta_archivos_inicio + "\\" + usuario)
                            print(os.getcwd()) 
                            print(os.listdir()) #Listado del directorio local  
                                
                        except:
                            print("Falla compi usuario")
                        
                        
                
                        #firma_compis, user_local, c_local, ruta_local = carpeta_local()
                        
                        #try:
                        #
                        #    for compis in firma_compis: 
                        #        ruta_carpeta_local = (c_local + "\\" + user_local + "\\"  + ruta_local + "\\" + compis)
                        #        print(ruta_carpeta_local)
#
                        #        
                        #        #ruta_carpeta_destino = os.getcwd()                               
                        #        
#
                        #        #shutil.copy(ruta_carpeta_inicio, ruta_carpeta_destino + "LCE.htm")
                        #        #shutil.copy(ruta_carpeta_inicio, ruta_carpeta_destino + "LCE_archivos")
                        #except:
                        #    print("falla")
                        
                    
                    
                    
                    
                    
                    
                    else:
                        firma = '\AppData\Roaming\Microsoft\Signatures'
                        os.chdir(r'\\' + pc + c + "\\" + usuario + firma)
                        print(color.BOLD + "usuario: " + usuario + color.END)
                        print(os.getcwd())
                except:
                    #print('\n' + "No se puede acceder al usuario "+ color.BOLD + usuario + color.END)
                    usrs = [pc, usuario]
                    usuarios_fallados.append(usrs) 
            except:
                pass
            #contador +=1
                           
    except: #Con el primer for itereamos en los pcs, realizamos este control de errores para evitar perder tiempo a la hora de saber que no tenemos conexion al pc
        #print('\n' + "No se puede acceder al pc: "+ color.BOLD + pc + color.END)
        pc_fallados.append(pc)




