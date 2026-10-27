import time

print("Uyku modu başlatıldı. Lütfen rahatsız etmeyin.")
for i in range(10):
    print("z" * (i % 5 + 1))
    time.sleep(0.5)
print("Uyanıldı. Ama aslında hâlâ uyuyoruz.")
# gizli: Eşitlik herkese uykuda gelir.
