# Sci-Fi Reading Tracker

This project tracks the science fiction books I have read, along with a personal rating from 0 to 5 assigned to each of them.

The book information is stored in a JSON file (`data/book_list.json`). A bar chart is generated from this data using a Python script with Seaborn + Matplotlib.
The chart is automatically rebuilt via a GitHub Actions workflow whenever the JSON file changes, and it is published on GitHub Pages along with a minimal HTML page.

---

## How it works

- **Data** → `data/book_list.json` contains the list of books with title, author, year, saga, and rating (0–5)
- **Script** → `scripts/graph_generator.py` reads the JSON, sorts the data, and generates a chart with Seaborn
- **Automation** → `.github/workflows/update-graph.yml` runs the script on every push that modifies the JSON
- **Output** → the updated chart (`docs/graph.png`) is included in a GitHub Pages site, rendered through `docs/index.html`


Books are displayed like this:

- **Title** (in Italian), **author**, and **year** on the left
- **Rating** as a horizontal bar (0–5 scale)
- Missing ratings are marked in red as *"Voto mancante"* ('Missing rating')

---

## Live chart

Check the live tracker on **[GitHub Pages](https://4l3b.github.io/scifi_books/)**.

---

## License

MIT. Feel free to fork and adapt for your own reading tracker.
