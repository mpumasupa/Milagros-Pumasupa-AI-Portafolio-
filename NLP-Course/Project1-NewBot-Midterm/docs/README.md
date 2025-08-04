# NewsBot Intelligence System

## Project Overview
The NewsBot Intelligence System is an end-to-end Natural Language Processing (NLP) pipeline that automatically analyzes, classifies, and extracts insights from news articles. Built for real-world applications, this project demonstrates all major NLP techniques covered in our course, including preprocessing, feature extraction, sentiment analysis, classification, and entity recognition.

## How to Use
1. Clone or download this repository.
2. Upload `BBC News Train.csv` into the notebook environment or use your own compatible dataset (minimum 500 articles, 4+ categories, English).
3. Open `notebooks/newsbot_pipeline.ipynb` in Google Colab or Jupyter Notebook.
4. Run each cell in order from top to bottom.
5. Review the visualizations and model results for insights.

## Repository Structure
ITAI2373-NewsBot-Midterm/

├── data/

│ └── BBC News Train.csv # Original dataset

├── notebooks/

│ └── newsbot_pipeline.ipynb # Main notebook

├── docs/

│ ├── README.md # This file

│ └── NewsBot_Reflection.pdf 

└── optional/

└── demonstration_video_link.txt #



## Key Features & Insights
- **Preprocessing:** Cleans and standardizes all news text for reliable analysis.
- **TF-IDF Analysis:** Highlights the most important terms driving each news category.
- **POS & Syntax:** Reveals grammatical patterns and writing style differences.
- **Sentiment Analysis:** Quantifies article tone and tracks mood by category.
- **Classification:** Automatically assigns news articles to categories with high accuracy.
- **Entity Recognition:** Extracts and summarizes key people, organizations, and places.

## Team Contributions
| Name              | Modules/Responsibilities                          |
|-------------------|---------------------------------------------------|
| John Castor       | Preprocessing, Sentiment, Documentation           |
| Dylan Castillo    | Classification, NER, Data Setup                   |
| Milagros Pumasupa | Feature Extraction, POS, Syntax Analysis          |
| Ola Bakare        | Named Entity Recognition, notebook organization   |

## Demo & Presentation
- Video Walkthrough: https://youtu.be/1xrNLgBblAo

## Next Steps / Future Improvements
- Integrate more advanced models (e.g., SVM, BERT)
- Build a web dashboard for real-time news analysis
- Add trend and topic modeling capabilities

## License & Acknowledgments
- Dataset: [BBC News Classification Dataset - Kaggle](https://www.kaggle.com/competitions/learn-ai-bbc/data)
- Built using scikit-learn, spaCy, NLTK, pandas, matplotlib, and textblob
- For educational use in ITAI2373

