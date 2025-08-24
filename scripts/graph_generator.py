import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json("data/book_list.json")

df = df.sort_values(by=['voto', 'titolo'], ascending=[False, True], na_position='last')

sns.set(style="whitegrid")
altezza = max(3.5, 0.6 * len(df))
plt.figure(figsize=(9, altezza))
ax = sns.barplot(data=df, y="titolo", x="voto", color="skyblue")

ax.set_xlim(0, 5)
ax.set_xticks(np.arange(0, 5.5, 0.5), minor=True)
ax.grid(axis='x', which='minor', color='lightgray', linestyle='-', linewidth=0.4)
ax.grid(axis='x', which='major', color='lightgray', linestyle='-', linewidth=0.4)

plt.xlabel('')
plt.ylabel('')
plt.title('')
ax.set_yticklabels([])

for i, row in enumerate(df.itertuples()):
    ax.text(-0.02, i-0.15, row.titolo, va='center', ha='right',
            fontsize=10, color='black', transform=ax.get_yaxis_transform())
    ax.text(-0.02, i+0.2, f"{row.autore} | {row.anno}", va='center', ha='right',
            fontsize=9, color='gray', transform=ax.get_yaxis_transform())

for i, row in enumerate(df.itertuples()):
    if pd.notna(row.voto):
        val = row.voto
        if val % 1 == 0:
            label = f"{int(val)}"
        elif val * 10 % 1 == 0:
            label = f"{val:.1f}".replace('.', ',')
        else:
            label = f"{val:.2f}".replace('.', ',')
        ax.text(val + 0.1, i + 0.05, label, va='center', fontsize=10, color='black')
    else:
        ax.text(0.1, i, "Voto mancante", va='center', fontsize=10, color='red')

plt.tight_layout()

plt.savefig("docs/graph.png")
