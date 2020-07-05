import subprocess
# sciezka + plik
fdirname = "/home/bbeldycki/skrypty_cluster/temp_list_1.00.dat"

# czytam plik linia po linii, nastepnie usuwam znak nowej linii (.strip()), a potem wykonuje operacje na tym stringu 
# w tym przypadku tworze odpowienia ilosc ponazywanych katalogow oraz kopiuje pliki do kazdego z katalogu
with open(fdirname) as file:
  for line in file:
    line = line.strip()
    subprocess.call(["mkdir "+line],shell=True)
    subprocess.call(["cp ./1.dat ./"+line+"/"],shell=True) # przypadek gdy plik znajduje sie w tym samym katalogu
    # co skrypt, ale mozna z dowolnego miejsca
    

