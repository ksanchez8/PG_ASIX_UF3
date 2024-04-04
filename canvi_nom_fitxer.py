import os

"""
1. Renombrar fichero
2.1 Obtener nombre fichero
2.2 Renombrar el fichero
3.1.1 Pdir al usuario la ruta
3.2.1 Comprobar si el fichero exite
3.2.2 Separamos ectension de la ruta
3.2.3 Renombrar el fichero
"""

class Renombrar:
    def inicio(self):
        fichero = obtener_nombre()
        renombrar_fichero(fichero)

    def obtener_nombre(self):
        fichero = input("Escribe el nombre de la ruta: ")
        return fichero
    
    def renombrar_fichero(self, fichero):
        existe = fichero_existe(fichero)
        if existe:
            nuevo_nombre = separar_extension(fichero)
            renombrar(fichero, nuevo_nombre)
    
    def fichero_existe(self, fichero):
        existe = os.path.exists(fichero)
        return existe
    
    def separar_extension(self, fichero):
        pos = fichero.rfind('.')
        return fichero