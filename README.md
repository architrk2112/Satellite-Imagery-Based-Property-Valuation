# 🚀 Project Setup & Execution Guide

Follow these steps in order to set up and run the complete pipeline.

---

## 📁 1. Project Structure Setup

**Ensure all project files are in the same root directory:**
- Python scripts (`.py`)
- Jupyter notebooks (`.ipynb`)
- Excel datasets (`.xlsx`)

---

## 🛰️ 2. Download Satellite Images

Execute the data fetcher script:
```bash
python data_fetcher.py
```

**What this does:**
- Fetches satellite images using latitude/longitude coordinates
- Automatically creates required directories:
```
  images_train/
  images_test/
```
- Saves images as `<id>.png` (matching dataset IDs)

---

## 🔧 3. Data Preprocessing

Open and execute the preprocessing notebook:
```bash
jupyter notebook preprocessing.ipynb
```

**This notebook will:**
- Load `train.xlsx` and `test.xlsx`
- Perform feature engineering and data transformations
- Generate processed datasets:
  - `train_processed.pkl`
  - `test_processed.pkl`

---

## 🤖 4. Model Training & Prediction

Open and run the model training notebook:
```bash
jupyter notebook model_training.ipynb
```

**This notebook will:**
- Train the **XGBoost tabular model**
- Train the **CNN image model**
- Train the **fusion model** (combining tabular + image features)

**Generated outputs:**
- `XGB_model.pkl`
- `fusion_model.pkl`
- `submission_23323022`

> ⚠️ **Note:** If `submission_23323022` already exists, it will be **overwritten** during execution.

---

## 📝 Execution Summary
```mermaid
graph LR
    A[Setup Files] --> B[Run data_fetcher.py]
    B --> C[Run preprocessing.ipynb]
    C --> D[Run model_training.ipynb]
    D --> E[submission_23323022]
```

---

## ✅ Final Checklist

- [ ] All files in same directory
- [ ] Satellite images downloaded
- [ ] Data preprocessing completed
- [ ] Models trained successfully
- [ ] Submission file generated
---
