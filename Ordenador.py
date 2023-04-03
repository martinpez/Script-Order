import os ,shutil,sys
from tqdm import tqdm
from time import sleep
def route ():
         while True:
                print("_" * 35)
                print("\t Organizador ")
                print("_" * 35)
                ruta = input("Type the route you want to organize: ")
                if os.path.exists(ruta):
                        os.chdir(ruta)
                        cwd = os.getcwd()
                        print("_" * 35)
                        print("the modified route is: ",cwd)
                        print("")
                        comfirm = input(" ◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉ y / n : ")
                        if comfirm == 'y' or comfirm == 'yes' or comfirm == 'si':            
                                print(" ")
                                print(" ")
                                barra()
                                funcion_principal()
                                funcion_principal()       
                        elif (comfirm == 'no' or comfirm == 'not' or comfirm == 'n'):
                                route()
                else:
                        print("NO existe esa ruta")
def funcion_principal ():

 while (True):

            if os.path.exists("DocumentosMicrosof") == True:
                    pass
            else:
                    os.mkdir("DocumentosMicrosof")
                    continue
            if os.path.exists ("Imagenes") == True:
                    pass
            else: 
                    os.mkdir("Imagenes")
                    continue
            if os.path.exists ("Videos") == True :
                    pass
            else:
                    os.mkdir("Videos")
                    continue
            if os.path.exists ("PDF") == True:
                    pass
            else:
                    os.mkdir("PDF")
                    continue
            if os.path.exists("Ejecutables") == True:
                    pass
            else:
                    os.mkdir ("Ejecutables")
                    continue
            if os.path.exists("WinRar") == True:
                    pass
            else: 
                    os.mkdir("WinRar")
                    continue
            if os.path.exists("Otros") == True:
                    pass
            else:
                    os.mkdir("Otros")
                    continue
            if os.path.exists("archivos programacion") == True:
                    pass
            else:
                    os.mkdir("archivos programacion")
                         
                    break
            
                        #Extenciones de imagenes
            extencionesimagenes = r".png", r".jpg" , r".webp" , r".jpeg" ,r"PNG"
            imagenes = [_ for _ in os.listdir() if _.endswith(extencionesimagenes)]
                    
            for i in (imagenes):
                    shutil.move(i, "Imagenes")
                    
                        #Extenciones de Documentos Microsoft
            extencionesMicrosft = r".xls", r".pptx" , r".docx" , r".doc" , r".ppt" , r".xlsx" 
            Dmicrosoft = [_ for _ in os.listdir() if _.endswith(extencionesMicrosft)]
                    
            for i in (Dmicrosoft):
                    shutil.move(i, "DocumentosMicrosof")
                    
                        
                        #Extenciones de videos
            extencionesVideos = r".mp4"
            videos = [_ for _ in os.listdir() if _.endswith(extencionesVideos)]
                    
            for i in (videos):
                    shutil.move(i, "Videos")



                        #Extenciones de pdf
            extencionesPdf = r".pdf"
            pdf = [_ for _ in os.listdir() if _.endswith(extencionesPdf)]
                    
            for i in (pdf):
                    shutil.move(i, "PDF")


                        #extenciones de exe
            extencionesExe = r".exe" r".msi"
            exe = [_ for _ in os.listdir() if _.endswith(extencionesExe)]
                    
            for i in (exe):
                    shutil.move(i, "Ejecutables")
                    

                        #extenciones de rar
            extencionesRar = r".rar", r".zip"
            Rar = [_ for _ in os.listdir() if _.endswith(extencionesRar)]
                    
            for i in (Rar):
                    shutil.move(i, "WinRar")
                

                        # Otros
            extencionesVarias = r".txt" ,r".bat" 
            Otros = [_ for _ in os.listdir() if _.endswith(extencionesVarias)]
                    
            for i in (Otros):
                    shutil.move(i, "Otros")
                    break            
            
                        #
            archivosprogramacion = r".java"  , r".cpp" , r".py" , r".html" , r".js"
            pdf = [_ for _ in os.listdir() if _.endswith(archivosprogramacion)]
                    
            for i in (pdf):
                    shutil.move(i, "archivos programacion")



def barra ():
    tareas = ["revicion","extencionesVarias", "extencionesRar", "extencionesExe", "extencionesPdf", "extencionesVideos","extencionesMicrosft","extencionesimagenes"]
    for i in tqdm(tareas):
        sleep(0.5)
    
# programa principal

while True:
                print("_" * 35)
                print("\t Organizador ")
                print("_" * 35)
                ruta = input("Type the route you want to organize: ")
                if os.path.exists(ruta):
                        os.chdir(ruta)
                        cwd = os.getcwd()
                        print("_" * 35)
                        print("the modified route is: ",cwd)
                        print("")
                
                        comfirm = input(" ◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉ y / n : ")
                        if comfirm == 'y' or comfirm == 'yes' or comfirm == 'si':
                                
                                print(" ")
                                print(" ")
                                barra()
                                print("")
                                funcion_principal()
                                funcion_principal()
                                
                                SystemExit
                        elif (comfirm == 'no' or comfirm == 'not' or comfirm == 'n'):
                                route()            
                else:
                        print("NO existe esa ruta")
                 





