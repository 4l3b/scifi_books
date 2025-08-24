# Sci-Fi Reading Tracker

This is a project to track the science fiction books I read.  
All books are stored in a JSON file (`data/libri.json`), and an automated workflow generates a bar chart with my ratings.  

The chart is rebuilt by GitHub Actions whenever the JSON file changes, and it is published on GitHub Pages.

---

## How it works

- **Data** → `data/libri.json` contains the list of books with title, author, year, saga, and rating (0–5).
- **Script** → `scripts/genera_grafico.py` reads the JSON, sorts the data, and generates a chart with Seaborn + Matplotlib.
- **Automation** → `.github/workflows/update-graph.yml` runs the script on every push that modifies the JSON.
- **Output** → the updated chart (`docs/grafico.png`) is published on GitHub Pages along with a minimal HTML page.


Books are displayed like this:

- **Title** + author and year on the left
- **Rating** as a horizontal bar (0–5 scale)
- Missing ratings are marked in red as *“Voto mancante”*

---

## Live chart

Check the live tracker here:  
**[My Sci-Fi Tracker on GitHub Pages](https://YOUR_USERNAME.github.io/YOUR_REPO/)**

---

## License

MIT. Feel free to fork and adapt for your own reading tracker.
