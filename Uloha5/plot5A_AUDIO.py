from excel_data_import import import_data_column
from matplotlib import pyplot as plt
import numpy as np

f = import_data_column("charakteristika.xlsx", "List1", 5, 1, 32)
Z = import_data_column("charakteristika.xlsx", "List1", 5, 4, 32)
phi = import_data_column("charakteristika.xlsx", "List1", 5, 5, 30)

fig, ax1 = plt.subplots()

fig.set_figwidth(11.69)
fig.set_figheight(8.27)

notes_color = "tab:cyan"
plt.grid(True, which="both")
plt.xscale("log")
plt.title("Kmitočtové charakteristiky přenosu zesilovače")
plt.axhline(np.max(Z), color = notes_color, linestyle = "--")
plt.axhline(np.max(Z) - 3, color = notes_color, linestyle = "--")
plt.axvline(78250, ymax = 0.85, color = notes_color, linestyle = "--")
plt.text(2e3, np.max(Z) - 2.5, "Přenosové pásmo", color = notes_color, horizontalalignment = "center", verticalalignment = "bottom", bbox=dict(facecolor = "white", edgecolor = notes_color))
plt.text(78250, -12, "78,25 kHz", color = notes_color, horizontalalignment = "center", bbox=dict(facecolor = "white", edgecolor = notes_color))
plt.text(4, np.max(Z), "8,729 dB", color = notes_color, horizontalalignment = "left", verticalalignment = "top", bbox=dict(facecolor = "white", edgecolor = notes_color))
plt.text(4, np.max(Z) - 3, "5,729 dB", color = notes_color, horizontalalignment = "left", verticalalignment = "top", bbox=dict(facecolor = "white", edgecolor = notes_color))

ax1_color = "tab:blue"
ax1.plot(f, Z, color = ax1_color, marker = "x", markersize = 10)
ax1.set_xlabel("Kmitočet [Hz]")
ax1.set_ylabel("Modul přenosu [dB]", color = ax1_color)
ax1.tick_params(axis = "y", labelcolor = ax1_color)

ax2_color = "tab:red"
ax2 = ax1.twinx()
ax2.plot(f[:30], phi, color = ax2_color, marker = "+", markersize = 10)
ax2.set_ylabel("Fáze přenosu [°]", color = ax2_color)
ax2.tick_params(axis = "y", labelcolor = ax2_color)

fig.tight_layout()

plt.savefig("grafy/graf_kmitoctova_charakteristika.pdf", format="pdf", bbox_inches="tight")
plt.show()