# ----------------------------------------------------------------------
# A2. saraksts tiek nonullēts ciklā
# ----------------------------------------------------------------------

# Jāsavāc visi skaitļi, kas lielāki par 4. Sarakstā paliek tikai pēdējais.
#
# Salabo kodu, lai programma strādātu pareizi. Tad palaid ar F5.

skaitli = [3, 8, 2, 9]

for s in skaitli:
    lielie = []
    if s > 4:
        lielie.append(s)

print(lielie)
