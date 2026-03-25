
import os
import shutil
from variables import doc_types, img_types, software_types, mi_ruta
from funciones import Crear_carpetas, Clasificar_archivos, mover_archivo


def main():
    Crear_carpetas(mi_ruta)    
    
    for archivo in os.listdir(mi_ruta):        
        if os.path.isfile(os.path.join(mi_ruta, archivo)): # os.path es la ruta a donde esta apuntando el kernel.
            destino = Clasificar_archivos(archivo)        
            mover_archivo(mi_ruta, archivo, destino)
            
        
if __name__ == "__main__":
    main()     
