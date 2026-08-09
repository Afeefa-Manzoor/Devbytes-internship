# Task 7: NLP Sentiment Classification Model

## Objective
Clean a dataset of movie reviews, perform text tokenization and bag-of-words
encoding, and train a model to predict review sentiment (positive / negative).

## Dataset
[NLTK `movie_reviews` corpus](https://www.nltk.org/nltk_data/) — 2,000 real,
human-labeled movie reviews, evenly split between positive and negative
(1,000 each). Downloaded automatically at run time via `nltk.download`.

If the download is unavailable (e.g. no internet access), the notebook
automatically falls back to a programmatically generated, balanced synthetic
review dataset so it always runs end-to-end without manual setup.

## Approach
1. **Load data** — fetch the NLTK corpus with a synthetic-data fallback
2. **Validate** — check for nulls, empty text, and expected label values
3. **Clean & tokenize** — lowercase, strip punctuation/digits, remove stopwords
4. **Split & encode** — stratified 80/20 train/test split, then bag-of-words
   encoding via `CountVectorizer` (3,000-word vocabulary)
5. **Train** — Multinomial Naive Bayes classifier
6. **Evaluate** — accuracy, precision/recall/F1, confusion matrix
7. **Visualize** — confusion matrix and top predictive words per class

## Results
- **Test accuracy:** 81.75%
- Balanced precision/recall (~0.82) across both classes — no class bias
- Full metrics and outputs are in the executed notebook

## Files
- `Task7_NLP_Sentiment_Classification.ipynb` — full pipeline, fully executed
- `visualizations/confusion_matrix.png` — test-set confusion matrix
- `visualizations/top_predictive_words.png` — words most associated with each class

## Notes
- No hardcoded paths, filenames, or column names — all configuration lives
  in a single constants block at the top of the notebook
- All logic is wrapped in reusable, documented functions
  (`load_movie_reviews`, `clean_text`, `train_model`, `evaluate_model`,
  `plot_top_predictive_words`)
- All cells are executed top-to-bottom with saved outputs
