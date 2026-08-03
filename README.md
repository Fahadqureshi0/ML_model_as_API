# 🚀 ML Model as API

Convert a Machine Learning model into a REST API using **FastAPI**. This project demonstrates how to deploy a trained ML model as an API and consume it using HTTP requests.

---

## 📌 Features

- 🚀 FastAPI-based REST API
- 🤖 Machine Learning Model Integration
- 📥 JSON Input Support
- 📤 JSON Response
- 📖 Interactive Swagger Documentation
- ⚡ High Performance API

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- NumPy
- Pydantic
- Requests

---

## 📂 Project Structure

```text
ML_model_as_API/
│
├── ML_api.py                  # FastAPI application
├── API_Implementation.py       # Client script to test API
├── diabetes_model.sav          # Trained ML model
├── requirements.txt
└── README.md
```

---

## 🚀 Run the API

```bash
uvicorn ML_api:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📥 Sample Request

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

---

## 📤 Sample Response

```json
{
  "prediction": "The person is diabetic."
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ML_model_as_API.git

cd ML_model_as_API

pip install -r requirements.txt
```


---

## 👨‍💻 Author

**Fahad Qureshi**

### 🌐 Connect with me

- 💼 LinkedIn: https://www.linkedin.com/in/fahadqureshi/
- 💻 GitHub: https://github.com/FahadQureshi
