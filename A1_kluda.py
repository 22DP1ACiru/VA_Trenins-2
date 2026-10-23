# ----------------------------------------------------------------------
# A1. funkcija raksta, nevis atdod
# ----------------------------------------------------------------------

# Jāizvada vidējā atzīme. Izvadās skaitlis un tad vārds None.
#
# Salabo kodu, lai programma strādātu pareizi. Tad palaid ar F5.

def videja(saraksts):
    print(sum(saraksts) / len(saraksts))

rezultats = videja([4, 8, 6])
print("Vidējā atzīme ir", rezultats)
