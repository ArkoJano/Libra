import os
def cls():
    """ Funkcja czyszczaca caly terminal """
    os.system('cls' if os.name=='nt' else 'clear')