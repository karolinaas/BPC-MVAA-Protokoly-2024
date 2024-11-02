from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

################################################################################
# Převodník U/U
################################################################################

UU_U1 = import_data_column("uloha5_offline.xlsx", "5B", 13, 3, 16)
UU_U2 = import_data_column("uloha5_offline.xlsx", "5B", 13, 5, 16)

plt.figure(1, figsize=(11.69, 8.27)) # A4 landscape size
plt.plot(UU_U1, UU_U2, color="red", marker="x", markersize="10", markeredgecolor="crimson")

UU_xlim = np.array([UU_U1[0], UU_U1[-4]])
UU_k, UU_q = np.polyfit(UU_U1[:-4], UU_U2[:-4], 1)
plt.plot(UU_xlim, UU_k * UU_xlim + UU_q, color="black", linestyle="--", linewidth=1)

plt.grid(True)
plt.xlabel("$U_1\ [V]$")
plt.ylabel("$U_2\ [V]$")
plt.title("Závislost $U_2 = f(U_1)$")

plt.savefig("grafy/graf_prevodnik_UU.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Převodník U/I
################################################################################

UI_U1 = import_data_column("uloha5_offline.xlsx", "5B", 13, 23, 20)
UI_I2 = import_data_column("uloha5_offline.xlsx", "5B", 13, 25, 20)

plt.figure(2, figsize=(11.69, 8.27)) # A4 landscape size
plt.plot(UI_U1, UI_I2, color="red", marker="x", markersize="10", markeredgecolor="crimson")

UI_xlim = np.array([UI_U1[0], UI_U1[-1]])
UI_k, UI_q = np.polyfit(UI_U1[:-1], UI_I2[:-1], 1)
plt.plot(UI_xlim, UI_k * UI_xlim + UI_q, color="black", linestyle="--", linewidth=1)

plt.grid(True)
plt.xlabel("$U_1\ [V]$")
plt.ylabel("$I_2\ [mA]$")
plt.title("Závislost $I_2 = f(U_1)$")

plt.savefig("grafy/graf_prevodnik_UI.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Převodník I/I
################################################################################

II_I1 = import_data_column("uloha5_offline.xlsx", "5B", 13, 47, 17)
II_I2 = import_data_column("uloha5_offline.xlsx", "5B", 13, 49, 17)

plt.figure(3, figsize=(11.69, 8.27)) # A4 landscape size
plt.plot(II_I1, II_I2, color="red", marker="x", markersize="10", markeredgecolor="crimson")

II_xlim = np.array([II_I1[0], II_I1[-4]])
II_k, II_q = np.polyfit(II_I1[:-4], II_I2[:-4], 1)
plt.plot(II_xlim, II_k * II_xlim + II_q, color="black", linestyle="--", linewidth=1)

plt.grid(True)
plt.xlabel("$I_1\ [mA]$")
plt.ylabel("$I_2\ [mA]$")
plt.title("Závislost $I_2 = f(I_1)$")

plt.savefig("grafy/graf_prevodnik_II.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Převodník I/U
################################################################################

IU_I1 = import_data_column("uloha5_offline.xlsx", "5B", 13, 68, 17)
IU_U2 = import_data_column("uloha5_offline.xlsx", "5B", 13, 70, 17)

plt.figure(4, figsize=(11.69, 8.27)) # A4 landscape size
plt.plot(IU_I1, IU_U2, color="red", marker="x", markersize="10", markeredgecolor="crimson")

IU_xlim = np.array([IU_I1[0], IU_I1[-5]])
IU_k, IU_q = np.polyfit(IU_I1[:-5], IU_U2[:-5], 1)
plt.plot(IU_xlim, IU_k * IU_xlim + IU_q, color="black", linestyle="--", linewidth=1)

plt.grid(True)
plt.xlabel("$I_1\ [mA]$")
plt.ylabel("$U_2\ [V]$")
plt.title("Závislost $U_2 = f(I_1)$")

plt.savefig("grafy/graf_prevodnik_IU.pdf", format="pdf", bbox_inches="tight")

################################################################################
# Převodník log U/U
################################################################################

logUU_U1 = import_data_column("uloha5_offline.xlsx", "5B", 13, 89, 7)
logUU_U2 = import_data_column("uloha5_offline.xlsx", "5B", 13, 91, 7)

plt.figure(5, figsize=(11.69, 8.27)) # A4 landscape size
plt.plot(logUU_U1, logUU_U2, color="red", marker="x", markersize="10", markeredgecolor="crimson")

logUU_xlim = np.array([logUU_U1[0], logUU_U1[-1]])
logUU_k, logUU_q = np.polyfit(np.log(logUU_U1[:-1]), logUU_U2[:-1], 1)
plt.plot(logUU_xlim, logUU_k * np.log(logUU_xlim) + logUU_q, color="black", linestyle="--", linewidth=1)

plt.grid(True, which="both")
plt.xlabel("$U_1\ [V]$")
plt.ylabel("$U_2\ [V]$")
plt.title("Závislost $U_2 = f(U_1)$")
plt.xscale("log")

plt.savefig("grafy/graf_prevodnik_logUU.pdf", format="pdf", bbox_inches="tight")

plt.show()