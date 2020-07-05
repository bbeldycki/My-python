import subprocess
import os
# sciezka + plik do odczytu
fdirname = "/home/bbeldycki/skrypty_cluster/listjob.dat"
    
# czytam plik linia po linii, nastepnie usuwam znak nowej linii (.strip()), a potem wykonuje operacje na tym stringu 
# w tym przypadku inicjalizuje obliczenia na clustrze
# ten skrypt musi by w odpowiednim katalogu na /worku/ w camk, zeby proces mogl ruszyc
with open(fdirname) as file:
  for line in file:
    line = line.strip()
    subprocess.call(["sbatch "+line],shell=True)

