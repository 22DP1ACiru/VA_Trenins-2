# ----------------------------------------------------------------------
# B1. jauns saraksts ar append
# ----------------------------------------------------------------------

# Savāc atsevišķā sarakstā visas atzīmes, kas ir 7 vai lielākas, un izvadi par tām kopsavilkumu.
#
# Aizpildi vietu, kur stāv TODO. Pārējo nemaini.

atzimes = [4, 9, 6, 10, 3, 8]
labas = []

for a in atzimes:
    # TODO: ja a ir 7 vai lielāks, pievieno to sarakstam labas

print("Labās atzīmes:", labas)
print("Cik:", len(labas))
print("Vidējā no labajām:", sum(labas) / len(labas))
