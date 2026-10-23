# ----------------------------------------------------------------------
# B2. funkcija ciklā
# ----------------------------------------------------------------------

# Uzraksti funkciju, kas aprēķina cenu pēc atlaides, un izmanto to ciklā visām cenām.
#
# Aizpildi vietu, kur stāv TODO. Pārējo nemaini.

def ar_atlaidi(cena, atlaide=10):
    # TODO: atdod cenu pēc atlaides

cenas = [100, 250, 40]
kopa = 0

for c in cenas:
    kopa = kopa + ar_atlaidi(c)

print("Kopā:", round(kopa, 2))
