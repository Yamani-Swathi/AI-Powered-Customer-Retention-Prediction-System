<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🤖 AI-Powered Customer Retention Prediction System</h1>

<p>
An end-to-end <strong>Machine Learning pipeline</strong> that predicts
<strong>telecom customer churn</strong> and helps businesses take
<strong>proactive customer retention actions</strong> using data-driven insights.
</p>

<p>
This project demonstrates a complete ML lifecycle — from data preprocessing and
feature engineering to model deployment using <strong>Flask</strong>.
</p>

<hr>

<h2>📌 Project Objective</h2>
<p>To build a robust and scalable customer churn prediction system that:</p>

<ul>
  <li>Automatically preprocesses raw customer data</li>
  <li>Selects the most effective features</li>
  <li>Trains and evaluates multiple ML models</li>
  <li>Deploys the best-performing model for real-time predictions</li>
</ul>

<hr>

<h2>🧠 End-to-End Machine Learning Pipeline</h2>
<ol>
  <li>Data Loading</li>
  <li>Missing Value Treatment</li>
  <li>Feature Transformation</li>
  <li>Outlier Detection & Handling</li>
  <li>Categorical Encoding</li>
  <li>Feature Selection</li>
  <li>Class Imbalance Handling</li>
  <li>Feature Scaling</li>
  <li>Model Training & Evaluation</li>
  <li>Hyperparameter Tuning</li>
  <li>Model Saving</li>
  <li>Web Deployment</li>
</ol>

<hr>

<h2>📊 Dataset Description</h2>
<p>The dataset contains telecom customer information such as:</p>

<ul>
  <li>Customer demographics</li>
  <li>Subscription services</li>
  <li>Billing & payment details</li>
  <li>Contract information</li>
</ul>

<p>
<strong>Target Variable:</strong><br>
Churn → Yes / No
</p>

<hr>

<h2>🔍 Data Preprocessing & Feature Engineering</h2>

<h3>1️⃣ Missing Value Handling</h3>
<ul>
  <li><strong>Column handled:</strong> TotalCharges</li>
  <li><strong>Technique used:</strong> Random Sample Imputation</li>
  <li>Preserves original data distribution and variability</li>
</ul>

<hr>

<h3>2️⃣ Feature Transformation</h3>
<p>Applied on numerical features:</p>
<ul>
  <li>tenure</li>
  <li>MonthlyCharges</li>
  <li>TotalCharges</li>
</ul>

<p>
✔ <strong>Min-Max Scaling</strong> was used to normalize values between 0 and 1,
ensuring fair contribution of all numeric features.
</p>

<hr>

<h3>3️⃣ Outlier Detection & Treatment</h3>
<ul>
  <li><strong>Technique used:</strong> Interquartile Range (IQR) Method</li>
  <li>Extreme values outside acceptable bounds were removed to improve model stability</li>
</ul>

<hr>

<h3>4️⃣ Categorical Encoding</h3>
<p>Different encoding strategies were applied based on feature type:</p>
<ul>
  <li><strong>Label Encoding</strong> → Binary features</li>
  <li><strong>One-Hot Encoding</strong> → Multi-category services</li>
  <li><strong>Ordinal Encoding</strong> → Contract duration</li>
</ul>

<p>
✔ Encoding logic was saved and reused during prediction.
</p>

<hr>

<h3>5️⃣ Feature Selection</h3>
<ul>
  <li>Constant feature removal</li>
  <li>Quasi-constant feature removal using variance threshold</li>
</ul>

<p>
✔ Only informative and variance-rich features were retained.
</p>

<hr>

<h3>6️⃣ Handling Class Imbalance</h3>
<ul>
  <li><strong>Technique used:</strong> SMOTE (Synthetic Minority Oversampling Technique)</li>
  <li>Balances churn and non-churn classes to improve recall and AUC</li>
</ul>

<hr>

<h2>🤖 Model Training & Selection</h2>
<p>The following models were trained and evaluated:</p>

<ul>
  <li>Logistic Regression</li>
  <li>K-Nearest Neighbors (KNN)</li>
  <li>Naive Bayes</li>
  <li>Decision Tree</li>
  <li>Random Forest</li>
  <li>AdaBoost</li>
  <li>Gradient Boosting</li>
  <li>Support Vector Machine (SVM)</li>
</ul>

<p>
<strong>✅ Final Model Selected:</strong><br>
Logistic Regression — chosen based on highest ROC-AUC score, stability, and interpretability.
</p>

<hr>

<h2>⚙️ Hyperparameter Tuning</h2>
<ul>
  <li><strong>Technique used:</strong> GridSearchCV</li>
  <li>5-fold cross-validation</li>
  <li>Best parameters selected for optimal performance</li>
</ul>

<p>
✔ Final model saved as <code>best_model.pkl</code>
</p>

<hr>

<h2>📈 Model Evaluation Metrics</h2>
<ul>
  <li>Accuracy</li>
  <li>Precision</li>
  <li>Recall</li>
  <li>F1-Score</li>
  <li>ROC-AUC Curve</li>
</ul>

<p>
The model achieved reliable and consistent performance across all evaluation metrics.
</p>

<hr>

<h2>🌐 Deployment</h2>
<p>
The trained model is deployed using <strong>Flask</strong> to enable real-time predictions.
</p>

<p><strong>Deployment Features:</strong></p>
<ul>
  <li>User-friendly web interface</li>
  <li>Real-time churn prediction</li>
  <li>Probability score output</li>
  <li>Reusable preprocessing pipeline</li>
</ul>

<p><strong>Tech Stack:</strong></p>
<ul>
  <li>Flask</li>
  <li>HTML</li>
  <li>Pickle</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p>
<strong>Yamani Swathi</strong><br>
AI/Machine Learning Enthusiast
</p>

</body>
</html>
