## 📌 Objective

This assignment demonstrates:

* Loading and exploring a dataset using **pandas**
* Performing **basic data analysis**
* Creating **visualizations** with **matplotlib** (and seaborn for styling)
* Summarizing **findings and observations**

---

## 📂 Files Included

* `Iris_data.ipynb` → Main Jupyter Notebook with code, analysis, and plots ✅
* `README.md` → This file, describing the project

---

## 🛠️ Requirements

Install the following Python libraries before running the notebook/script:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

---

## ▶️ How to Run

1. Open the Jupyter Notebook:

   ```bash
   jupyter notebook Iris_data.ipynb
   ```

   OR run the script:

   ```bash
   python Iris_data.py
   ```

2. Run all cells to reproduce results and visualizations.

---

## 📊 Tasks Completed

### Task 1: Load & Explore Dataset

* Loaded the **Iris dataset** (from `sklearn.datasets`)
* Displayed first rows, dataset structure, and checked for missing values

### Task 2: Basic Data Analysis

* Calculated descriptive statistics (`.describe()`)
* Grouped by species and computed average petal length

### Task 3: Data Visualization

Created four different plots:

1. 📈 Line chart → Petal length trend
2. 📊 Bar chart → Average petal length per species
3. 📉 Histogram → Sepal length distribution
4. 🔵 Scatter plot → Sepal length vs. petal length

---

## 🔎 Findings

* **Iris-setosa** has the shortest petals, while **Iris-virginica** has the longest.
* Sepal length and petal length show a **positive correlation**.
* Petal length distribution is distinct between species → useful for classification.
* The dataset is **clean (no missing values)** and ready for machine learning tasks.

---

✅ This submission meets all assignment requirements:

* Data loading & exploration
* Basic analysis
* Visualizations
* Findings/observations
