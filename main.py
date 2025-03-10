# Liczba chłopaków ogółem
chlopaki_ogolem = 5

# Chłopaki, którzy nie szukają przypraw:
# - Butcher szuka Homelandera
# - Frenchy szuka zioła
# - Pimpek się zgubił

chlopaki_nie_szukaja = 3

# Pozostali chłopaki szukają przypraw
chlopaki_szukajacy_przypraw = chlopaki_ogolem - chlopaki_nie_szukaja

print(f"Liczba chłopaków szukających przypraw: {chlopaki_szukajacy_przypraw}")