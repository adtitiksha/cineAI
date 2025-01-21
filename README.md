# 🎥 Sentiment Analysis and Academy Awards Prediction Using BERT

## 📖 Overview
This project, **CineAI**, combines sentiment analysis and machine learning to predict the likelihood of movies winning Academy Awards. By analyzing user reviews, sentiment scores, movie metadata, and BERT embeddings of movie plots, we aim to build a robust predictive framework for award outcomes.

---

## 🎯 Objectives
1. **Sentiment Analysis**: Analyze user reviews to compute sentiment scores using NLTK, TextBlob, or VADER.
2. **Data Integration**: Combine user review data with movie metadata.
3. **Dataset Alignment**: Identify movies common to both datasets.
4. **BERT Embeddings**: Use BERT for movie plot embeddings and predictions.
5. **Model Optimization**: Incorporate additional features to enhance prediction accuracy.

---

## 🚀 Methodology
1. **Sentiment Analysis**:
   - Compute sentiment scores using NLTK, TextBlob, and VADER.
   - Analyze the correlation between sentiment scores and ratings.
2. **Data Integration**:
   - Create a unified dataset with sentiment scores and movie metadata.
3. **Plot Embeddings**:
   - Generate BERT embeddings for movie plots using Hugging Face Transformers.
4. **Prediction Models**:
   - Train Logistic Regression, Random Forest, and Neural Network models.
   - Evaluate models with and without additional features.
5. **Performance Metrics**:
   - Measure accuracy, precision, and recall to validate model performance.

---

## 📊 Results
1. **Sentiment Analysis**:
   - High correlation observed between sentiment scores and overall ratings.
   - Sentiment means effectively differentiate award winners from non-winners.
2. **Prediction Models**:
   - **Initial Model Accuracy**: 78%.
   - **Enhanced Accuracy**: 85% (with additional features).

---

## 🔮 Future Scope
- Explore advanced embedding models like GPT for improved plot representation.
- Conduct time-based sentiment analysis to identify trends.
- Include external data such as social media and critic reviews.
- Develop hybrid models combining NLP with advanced machine learning techniques.

---

## 💻 Technologies Used
- **Programming Languages**: Python
- **Libraries**:
  - Pandas, NumPy for data manipulation
  - NLTK, TextBlob, VADER for sentiment analysis
  - Hugging Face Transformers for BERT embeddings
  - Matplotlib, Seaborn for visualizations
- **Machine Learning Models**:
  - Logistic Regression, Random Forest, Neural Networks

---

## 📈 Visualizations
1. **Sentiment Distribution**: Bar charts showing sentiment score distributions.
2. **Correlation Matrix**: Heatmaps visualizing feature relationships.
3. **Model Accuracy**: Comparisons of accuracy scores across models.

---

## 📜 Conclusion
By combining sentiment analysis and BERT embeddings, this project demonstrates the potential of machine learning in predicting Academy Award outcomes. The integration of diverse data sources highlights the promise of this approach for predictive modeling.

---

## 📂 Project Structure
