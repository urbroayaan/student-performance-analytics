# 📊 Student Performance Analytics System

A Python-based data analytics project that processes student academic records from a CSV file, performs performance analysis using Pandas, and visualizes insights using Matplotlib.

This project demonstrates clean data handling, analytical thinking, and basic data visualization — all built with industry-standard tools.

---

## 🚀 Project Overview

The system analyzes student marks to:
- Calculate individual student averages
- Identify top-performing students (with tie handling)
- Compute subject-wise average performance
- Detect the weakest subject
- Classify students into performance categories
- Visualize insights using bar charts

The project was built step-by-step, starting from core Python logic and evolving into a Pandas-based analytics pipeline.

---

## ✨ Features

- 📂 CSV-based data ingestion  
- 📈 Student-wise average calculation  
- 🏆 Topper identification with tie handling  
- 📊 Subject-wise average analysis  
- ⚠️ Weakest subject detection  
- 🏷️ Performance classification  
- 📉 Basic data visualization using Matplotlib  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Libraries:** Pandas, Matplotlib  
- **Data Format:** CSV  

---

## 📁 Project Structure

student-performance-analytics/
│
├── students.csv # Input dataset
├── main.py # Analytics + visualization script
└── README.md # Documentation

yaml
Copy code

---

## 📄 Sample Input (`students.csv`)

name,sub1,sub2,sub3
Ayaan,99,85,90
Rahul,60,72,68
Neha,88,91,84
Sara,55,65,58

yaml
Copy code

---

## 🖥️ Sample Output (Console)

Student Averages:
Ayaan 91.33
Rahul 66.67
Neha 87.67
Sara 59.33

Topper(s): Ayaan with average 91.33

Subject-wise Averages:
sub1 75.50
sub2 78.25
sub3 75.00

Weakest Subject: sub3

Student Performance:
Ayaan Excellent
Rahul Average
Neha Excellent
Sara Average

yaml
Copy code

---

## 📊 Visualizations

- Bar chart showing **student-wise average performance**
- Bar chart showing **subject-wise average performance**

These visualizations make trends and weak areas easy to identify at a glance.

---

## 🧠 Key Learnings

- Row-wise vs column-wise analytics using Pandas
- Translating raw data into meaningful insights
- Importance of clean code structure
- Using visualization to communicate results
- Applying time and space complexity awareness

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n × m)` (students × subjects)  
- **Space Complexity:** `O(n + m)`  

---

## 📌 Project Status

✅ Analytics complete  
✅ Visualization complete  

Future enhancements may include:
- Support for dynamic number of subjects
- Advanced visualizations
- Exporting reports

---

## 👤 Author

**Ayaan Anildutt**  
B.Tech (AI & Data Science)
