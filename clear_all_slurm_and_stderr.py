import subprocess
import os

# sciezka do katalogow do czyszczenia
dirname = "/home/bbeldycki/python/"
    
# usuwam wszystkie pliki slumr i stderr (produkt olbiczen na clustrze)
os.remove(dirname+"/slurm*")
os.remove(dirname+"/stderr*")

