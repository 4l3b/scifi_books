import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json("libri_scifi.json")

df = df.sort_values(by=['voto', 'titolo'], ascending=[False, True], na_position='last')

altezza = max(3.5, 0.52 * len(df))
plt.figure(figsize=(9, altezza), facecolor='#121212')
sns.set_style("whitegrid")

ax = sns.barplot(
    data=df,
    y="titolo",
    x="voto",
    color='#91d7b9',
    edgecolor='#50a080',
    width=0.75
)

ax.set_facecolor('#121212')
ax.set_xlim(0, 5.10)
ax.set_xticks(np.arange(0, 5.5, 0.5), minor=True)

ax.grid(axis='x', which='minor', color='#50a080', linestyle='-', linewidth=0.3)
ax.grid(axis='x', which='major', color='#80a090', linestyle='-', linewidth=0.6)
ax.grid(axis='y', visible=False)

ax.tick_params(axis='x', colors='#80a090', labelsize=10)

ax.axvline(x=5, color='#80a090', linestyle='-', linewidth=0.6)

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('#121212')
    spine.set_linewidth(0.8)

ax.set_yticklabels([])
plt.xlabel('')
plt.ylabel('')
plt.title('')

for i, row in enumerate(df.itertuples()):
    ax.text(-0.015, i-0.14, row.titolo, va='center', ha='right', fontfamily='DejaVu Sans Mono', fontsize=9, color='#a0f0d0', transform=ax.get_yaxis_transform())
    ax.text(-0.015, i+0.17, f"{row.autore} | {row.anno}", va='center', ha='right', fontfamily='DejaVu Sans Mono', fontsize=8, color='#c0e0b0', transform=ax.get_yaxis_transform())

for i, row in enumerate(df.itertuples()):
    if pd.notna(row.voto):
        val = row.voto
        if val % 1 == 0:
            label = f"{int(val)}"
        elif val * 10 % 1 == 0:
            label = f"{val:.1f}".replace('.', ',')
        else:
            label = f"{val:.2f}".replace('.', ',')
        ax.text(val + 0.1, i + 0.05, label, va='center', fontfamily='DejaVu Sans Mono', fontsize=9, color='#a0f0d0')
    else:
        ax.text(0.1, i, "Voto mancante", va='center', fontfamily='DejaVu Sans Mono', fontsize=9, color='red')

plt.tight_layout()
plt.savefig("graph.png", dpi=300)
