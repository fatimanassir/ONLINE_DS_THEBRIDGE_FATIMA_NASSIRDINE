
import os
import shutil
from variables import doc_types, img_types, software_types, mi_ruta


#funcion que me crea carpetas.
def Crear_carpetas(mi_ruta):
    carpetas = ["Imagenes", "Documentos", " Software", "Otros" ]
    for carpeta in carpetas:
        os.mkdir(os.path.join(mi_ruta, carpeta))
        
#funcion que me clasifica archivos:
def Clasificar_archivos(archivo):
    archivo = archivo.lower() #esto lo hago para pasar todo a nimusculas.
    # for archivo in os.listdir(mi_ruta):
    if archivo.endswith(doc_types):
        return "Documentos"
    elif archivo.endswith(img_types):
        return "Imagenes"
    elif archivo.endswith(software_types):    
        return "Software"
    else:
        return "Otros"   

#funcion para momver archivos:
def mover_archivo(mi_ruta, archivo, destino):    
    origen = os.path.join(mi_ruta, archivo) # esto crea la ruta completa del archivo actual.
    destino_f = os.path.join(mi_ruta, destino, archivo) #la ruta donde quiero mover el archivo.
    shutil.move(origen, destino_f) #me mueve el archivo.