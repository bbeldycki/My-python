import subprocess
import os
# sciezka + plik do odczytu
fdirname = "/home/bbeldycki/skrypty_cluster/temp_list_1.00.dat"

# sciezka do katalogow do czyszczenia
dirname = "/home/bbeldycki/python/"
    
# czytam plik linia po linii, nastepnie usuwam znak nowej linii (.strip()), a potem wykonuje operacje na tym stringu 
# w tym przypadku usuwam wszystkie zbedne pliki w danym katalogu
with open(fdirname) as file:
  for line in file:
    line = line.strip()
    os.remove(dirname+line+"/*")

