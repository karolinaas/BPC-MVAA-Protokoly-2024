from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np
import locale

################################################################################
# Převodní charakteristika Č/A převodníku
################################################################################

Umer = import_data_column("Uloha6_offline.xlsx", "6A", 22, 5, 17)
N = import_data_column("Uloha6_offline.xlsx", "6A", 22, 3, 17)

plt.figure(1, figsize=(11.69, 8.27))

plt.plot(N, Umer, color="red", marker="+", markersize="15", markeredgecolor="crimson", markeredgewidth=2)
#plt.ylim(-6, 6)
plt.yticks(np.arange(-5, 6, 1))
plt.xticks(np.arange(0, 257, 32))

plt.grid(True)
plt.xlabel("$N$ [-]")
plt.ylabel("$U_{měř}$ [V]")
plt.title("Závislost $U_{měř} = f(N)$")

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Průběh chyby v závislosti na vstupním slově
################################################################################

DeltaU = import_data_column("Uloha6_offline.xlsx", "6A", 22, 8, 17)
#DeltaU *= 1e3

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(N, DeltaU, "o", marker="x", markersize="10", markeredgecolor="crimson", markeredgewidth=2)
plt.yticks(np.arange(-0.002, 0.008, 0.001))
plt.xticks(np.arange(0, 257, 32))

plt.grid(True)
plt.xlabel("$N$ [-]")
plt.ylabel("$\Delta_U$ [V]")
plt.title("Závislost $\Delta_U = f(N)$")

print(DeltaU)

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

#plt.show()