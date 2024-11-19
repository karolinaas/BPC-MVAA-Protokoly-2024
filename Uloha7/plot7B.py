from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

f = import_data_column("Uloha7_offline.xlsx", "7B", 7, 15, 12)

A1 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 16, 12)
NEXT1 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 17, 12)
ACRN1 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 18, 12)

A2 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 19, 12)
NEXT2 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 20, 12)
ACRN2 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 21, 12)

A3 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 22, 12)
NEXT3 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 23, 12)
ACRN3 = import_data_column("Uloha7_offline.xlsx", "7B", 7, 24, 12)

################################################################################
# A=f(f)
################################################################################

plt.figure(1, figsize=(11.69, 8.27))

plt.plot(f, A1, color="tab:red", marker = "x", markersize = 10, markeredgewidth=2, label="Reproduktorová dvojlinka")
plt.plot(f, A2, color="tab:green", marker = "x", markersize = 10, markeredgewidth=2, label="UTP kat. 6")
plt.plot(f, A3, color="tab:blue", marker = "x", markersize = 10, markeredgewidth=2, label="S-STP kat.7")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.xticks([0.01, 0.1, 1, 10], labels=["0,01", "0,1", "1", "10"])
plt.xlabel("Kmitočet $f$ [MHz]")
plt.ylabel("Útlum $A$ [dB]")
plt.title("Závislost $A=f(f)$")

plt.savefig("grafy/graf1.pdf", format="pdf", bbox_inches="tight")

################################################################################
# A=f(f)
################################################################################

plt.figure(2, figsize=(11.69, 8.27))

plt.plot(f, NEXT1, color="tab:red", marker = "x", markersize = 10, markeredgewidth=2, label="Reproduktorová dvojlinka")
plt.plot(f, NEXT2, color="tab:green", marker = "x", markersize = 10, markeredgewidth=2, label="UTP kat. 6")
plt.plot(f, NEXT3, color="tab:blue", marker = "x", markersize = 10, markeredgewidth=2, label="S-STP kat.7")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.xticks([0.01, 0.1, 1, 10], labels=["0,01", "0,1", "1", "10"])
plt.xlabel("Kmitočet $f$ [MHz]")
plt.ylabel("Přeslech signálu $NEXT$ [dB]")
plt.title("Závislost $NEXT=f(f)$")

plt.savefig("grafy/graf2.pdf", format="pdf", bbox_inches="tight")

################################################################################
# A=f(f)
################################################################################

plt.figure(3, figsize=(11.69, 8.27))

plt.plot(f, ACRN1, color="tab:red", marker = "x", markersize = 10, markeredgewidth=2, label="Reproduktorová dvojlinka")
plt.plot(f, ACRN2, color="tab:green", marker = "x", markersize = 10, markeredgewidth=2, label="UTP kat. 6")
plt.plot(f, ACRN3, color="tab:blue", marker = "x", markersize = 10, markeredgewidth=2, label="S-STP kat.7")

plt.legend()
plt.xscale("log")
plt.grid(True, which="both")
plt.xticks([0.01, 0.1, 1, 10], labels=["0,01", "0,1", "1", "10"])
plt.xlabel("Kmitočet $f$ [MHz]")
plt.ylabel("Odstup přeslechu $ACR_N$ [dB]")
plt.title("Závislost $ACR_N=f(f)$")

plt.savefig("grafy/graf3.pdf", format="pdf", bbox_inches="tight")

plt.show()
