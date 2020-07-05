import subprocess
import os
# sciezka + plik do odczytu
fdirname = "/home/bbeldycki/python/temp_list.dat"

# sciezka do katalogow do czyszczenia
dirname = "/home/bbeldycki/python/"
    
# czytam plik linia po linii, nastepnie usuwam znak nowej linii (.strip()), a potem wykonuje operacje na tym stringu 
# w tym przypadku w linii zawarta jest nazwa kolejnej listy zawirajace nazwy katalogow
# czyszcze wszystkie te katalogi z plikow
with open(fdirname) as file:
  for line in file:
    line = line.strip()
    with open(line) as file:
      for line1 in file:
        line1 = line1.strip()
        os.remove(dirname+line+"/*")

