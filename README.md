# 🧁 Muffin vs Cupcake Classifier (Enhanced with FastAPI UI)

An enhancement to a machine learning model that predicts whether a recipe is for a **muffin** or a **cupcake**, now dressed with a user-friendly web interface. Built using **NumPy**, **Pandas**, **Scikit-Learn**, **FastAPI**, **HTML**, **CSS**, and **JavaScript**.

---

## 🚀 Project Overview

This project features:

- A trained **Random Forest Classifier** that distinguishes between muffin and cupcake recipes.
- A simple web interface powered by **FastAPI** and **Jinja2 templates**.
- An interactive API endpoint to classify new recipes based on ingredients.
- A `/model-info` route to inspect the internal model configuration.

---

## 🧠 Technologies Used

| Category         | Tools / Libraries                          |
|------------------|--------------------------------------------|
| Programming Lang | Python 3, HTML, CSS, JavaScript            |
| Data             | NumPy, Pandas                              |
| Machine Learning | Scikit-learn (RandomForestClassifier)      |
| Web Framework    | FastAPI                                    |
| Templating       | Jinja2                                     |
| Packaging        | joblib                                     |

---

## 📂 Project Structure

├── ml_components/
│ ├── muffins_vs_cupcakes.csv # Training dataset
│ └── model.joblib # Saved ML model
├── templates/
│ └── base.html # UI Template
├── main.py # FastAPI app
├── README.md # Project documentation


---

## 📊 Dataset

The dataset (`muffins_vs_cupcakes.csv`) contains ingredient quantities and a label identifying whether the recipe is a muffin or a cupcake.

**Features**:
- Flour, Milk, Sugar, Butter, Egg, Baking Powder, Vanilla, Salt

**Target**:
- `Type`: `Muffin` or `Cupcake` (encoded as 1 and 0)

---

## ⚙️ How It Works

1. **Training the Model**  
   A `RandomForestClassifier` is trained on the labeled recipe dataset and saved using `joblib`.

2. **Serving Predictions**  
   The FastAPI app loads the trained model and serves predictions via:
   - `POST /predict`: Accepts ingredient values and returns a prediction.
   - `GET /model-info`: Returns model parameters.

3. **User Interface**  
   A lightweight HTML page allows manual input and displays the predicted recipe type.

---

## 🧪 Example API Usage

**POST /predict**
```json
{
  "Flour": 2,
  "Milk": 1,
  "Sugar": 1,
  "Butter": 1,
  "Egg": 1,
  "Baking_Powder": 1,
  "Vanilla": 1,
  "Salt": 1
}

{
  "prediction": "Cupcake"
}

```


## 💻 Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
