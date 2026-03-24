# StayPricerAPI 🏠💰

A professional FastAPI-based microservice that leverages a trained Keras/TensorFlow model to suggest accommodation prices based on capacity, rooms, and bathrooms.

## 🚀 Features

- **Machine Learning Integration**: Real-time price prediction using a pre-trained Keras model.
- **Modular Architecture**: Clean separation of concerns (API, Services, Models, Core).
- **International Standards**: Codebase and documentation translated to English.
- **Versioning**: API documentation versioned under `/api/v1/`.
- **Docker Ready**: Easy containerization for consistent deployment.

## 📂 Project Structure

```text
stay-pricer-api/
├── app/
│   ├── main.py            # Entry point: initializes FastAPI and includes routers
│   ├── api/               # API Controllers/Routers
│   │   └── v1/
│   │       └── prediction_router.py
│   ├── core/              # Configuration and constants
│   ├── models/            # Pydantic schemas (data shapes)
│   ├── services/          # Business logic: handles ML loading and prediction
│   └── ml_models/         # Storage for .keras and .npz files
├── .dockerignore
├── .env                  # Environment variables
├── Dockerfile            # Container configuration
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

## 🛠️ Local Installation

### Prerequisites
- Python 3.13 (or compatible version)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alexis-Lozada/StayPricerAPI.git
   cd stay-pricer-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate.ps1
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🐳 Docker Usage

1. **Build the image:**
   ```bash
   docker build -t stay-pricer-api .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name stay-pricer-api stay-pricer-api
   ```

---

## 📡 API Usage

Once running, access the automatic interactive documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Example Request

**POST** `/api/v1/predict`

```json
{
  "capacity": 4,
  "rooms": 2,
  "bathrooms": 1.5
}
```

### Example Response

```json
{
  "suggested_price": 1250.50,
  "currency": "MXN"
}
```

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information (if applicable).
