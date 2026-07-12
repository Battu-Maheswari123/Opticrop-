# 🌱 OptiCrop - Smart Crop Recommendation System

OptiCrop is a Machine Learning-based web application that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions. The system helps farmers make informed decisions by analyzing agricultural data and predicting the best crop.

---

## 📌 Features

- 🌾 Crop recommendation using Machine Learning
- 📊 Predicts the best crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - Soil pH
  - Rainfall
- 🖥️ Simple and user-friendly web interface
- ⚡ Fast prediction using a trained ML model

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Bootstrap
- Joblib

---

## 📂 Project Structure

```
OptiCrop/
│── app.py
│── model.py
│── train_model.py
│── requirements.txt
│── README.md
│
├── models/
│   └── crop_model.pkl
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   └── images/
│
└── utils/
    └── preprocessing.py
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/OptiCrop.git
```

### Navigate to the project

```bash
cd OptiCrop
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset

This project uses the Crop Recommendation Dataset containing:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall
- Crop Label

---

## 🤖 Machine Learning Model

The project uses the **Random Forest Classifier** from Scikit-learn for crop prediction.

Model workflow:

1. Load dataset
2. Data preprocessing
3. Train Random Forest model
4. Save trained model using Joblib
5. Predict crop from user input

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Prediction Form
- Prediction Result

Example:

```
screenshots/home.png
screenshots/result.png
```

---

## 🔮 Future Enhancements

- Weather API integration
- Fertilizer recommendation
- Disease detection
- Yield prediction
- Multi-language support
- Mobile application

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/your-username

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
