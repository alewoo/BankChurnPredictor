# Bank Customer Churn Predictor 🏦

## Overview
An end-to-end machine learning application that predicts customer churn probability and generates personalized engagement strategies using ML models and LLMs.

![Streamlit App Demo](path_to_your_demo_gif.gif)

## 🔥 Features
- **Multi-Model Prediction**: Ensemble of 9 different ML models including XGBoost, Random Forest, and SVM
- **Interactive Dashboard**: Built with Streamlit for easy data input and visualization
- **AI-Driven Engagement**: Personalized customer retention strategies using Groq's LLM
- **Advanced ML Techniques**: 
  - SMOTE for handling imbalanced data
  - Feature engineering for improved accuracy
  - Voting classifier for ensemble predictions

## 🚀 Live Demo
Try out the live application here: [Bank Churn Predictor](https://bank-churn-predictor.streamlit.app)

## 💻 Tech Stack
- Python 3.12
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Groq API
- Plotly

## 📊 Model Performance
- XGBoost with SMOTE: 86% accuracy
- Feature-engineered model: 88% accuracy
- Voting Classifier: 87% accuracy

## 🛠️ Installation & Setup

1. Clone the repository
  bash
  git clone https://github.com/yourusername/bank-churn-predictor.git
  cd bank-churn-predictor
2. Install dependencies
  bash
  pip install -r requirements.txt
3. Set up environment variables
  Create a .env file and add your Groq API key
  GROQ_API_KEY=your_api_key_here
4. Run the application
  streamlit run main.py

## 📁 Project Structure
bank-churn-predictor/
├── main.py # Main Streamlit application
├── utils.py # Utility functions
├── requirements.txt # Project dependencies
├── models/ # Trained ML models
│ ├── xgb_model.pkl
│ ├── rf_model.pkl
│ └── ...
├── notebooks/ # Jupyter notebooks
│ └── model_training.ipynb # Model training and analysis
└── README.md

## 🔮 Future Improvements
- [ ] Retrain models with different feature engineering approaches
- [ ] Implement GradientBoostingClassifier and StackingClassifier
- [ ] Explore different LLM options and prompting techniques
- [ ] Deploy ML models as separate API endpoints
- [ ] Test models on different churn datasets

## 📝 Blog Post
Read about the development process and technical details in my blog post: [Building a Customer Churn Predictor: From ML Models to AI-Driven Engagement](your_blog_post_link)

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link_to_issues).

## 📫 Contact
- LinkedIn: [Your Name](your_linkedin_profile)
- Twitter: [@yourusername](your_twitter_profile)
- Blog: [Your Blog](your_blog_url)
