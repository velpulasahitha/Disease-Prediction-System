# 🩺 Disease Prediction and Doctor Recommendation System

## 📌 Project Overview

The Disease Prediction and Doctor Recommendation System is a Machine Learning-based application that predicts possible diseases based on symptoms provided by users and recommends relevant medical specialists.

The project aims to demonstrate how machine learning can be integrated with web technologies to provide an accessible health-information application.

## 🚀 Features

- Disease prediction based on user-selected symptoms.
- Machine Learning-based classification using a Decision Tree Classifier.
- Doctor recommendations based on predicted diseases.
- User registration and login.
- Interactive web interface.
- Dashboard for users.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model | Decision Tree Classifier |

## 📂 Project Structure

```text
Disease-Prediction-System/
│
├── app.py
├── model.py
├── model.pkl
├── doctor_mapping.py
├── Training.csv
├── Testing.csv
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── test.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/velpulasahitha/Disease-Prediction-System.git
```

### 2. Navigate to the project folder

```bash
cd Disease-Prediction-System
```

### 3. Install required libraries

```bash
pip install flask pandas numpy scikit-learn
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Visit the local URL displayed in your terminal, usually:

```text
http://127.0.0.1:5000/
```

## 🧠 Machine Learning Model

The project uses a Decision Tree Classifier to predict diseases based on input symptoms.

The trained model is stored in `model.pkl` and used by the application for predictions.

## 🔮 Future Enhancements

- Improve prediction performance through model evaluation.
- Add more disease and symptom information.
- Improve user interface and accessibility.
- Enhance doctor recommendation functionality.

## 👩‍💻 Developer

**Velpula Sahitha**

Computer Science and Engineering Student

GitHub: [@velpulasahitha](https://github.com/velpulasahitha)

---

**Note:** This project is developed for educational purposes. Predictions are not a substitute for professional medical diagnosis or advice.
