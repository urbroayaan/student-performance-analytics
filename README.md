# 📊 Student Performance Analytics System

A Python-based data analytics project that analyzes student academic performance using structured CSV data.  
The project demonstrates clean coding practices, data processing, analytics, and industry-standard tools like **Pandas**.

---

## 🚀 Project Overview

This project processes student marks data to:
- Calculate individual student averages
- Identify top-performing students (including tie handling)
- Compute subject-wise performance trends
- Detect the weakest subject overall
- Classify students into performance categories

The project was built incrementally to emphasize **core logic first**, followed by **clean structure**, and finally **pandas-based analytics**.

---

## 🧩 Features

- 📂 CSV-based data ingestion  
- 📈 Student-wise average calculation  
- 🏆 Topper identification with tie handling  
- 📊 Subject-wise average analysis  
- ⚠️ Weakest subject detection  
- 🏷️ Performance classification (Excellent / Good / Average / Needs Improvement)  
- 🧼 Clean, modular, and readable code  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Libraries:** Pandas  
- **Data Format:** CSV  
- **Concepts Used:**  
  - Data structures (lists, dictionaries)  
  - Time & space complexity analysis  
  - Functional decomposition  
  - Vectorized data operations  

---

## 📁 Project Structure

student-performance-analytics/
│
├── students.csv # Input dataset
├── main.py # Pandas-based analytics script
└── README.md # Project documentation

---

## 📄 Sample Input (`students.csv`)

name,sub1,sub2,sub3
Ayaan,99,85,90
Rahul,60,72,68
Neha,88,91,84
Sara,55,65,58

---

## 🖥️ Sample Output

Student Averages:
Ayaan 91.33
Rahul 66.67
Neha 87.67
Sara 59.33

Topper(s): Ayaan with average 91.33

Subject-wise Averages:
sub1 75.5
sub2 78.25
sub3 75.0

Weakest Subject: sub3

Student Performance:
Ayaan Excellent
Rahul Average
Neha Excellent
Sara Average

---

## 🧠 Key Learnings

- Difference between row-wise and column-wise operations
- Why logic-first development makes analytics tools easier to use
- How Pandas simplifies complex aggregation tasks
- Writing scalable and interview-ready Python code
- Translating raw data into meaningful insights

---

## ⏱️ Complexity Analysis

- **Time Complexity:**  
  - Student & subject analytics: `O(n × m)`  
  - Vectorized operations handled efficiently by Pandas
- **Space Complexity:**  
  - `O(n + m)` for stored data and computed metrics  

---

## 📌 Project Status

✅ Core analytics complete  
✅ Pandas-based implementation complete  

**Next planned enhancements:**
- Data visualization using Matplotlib / Seaborn  
- Support for dynamic number of subjects  
- Exporting reports to CSV or PDF  

---

## ✨ Resume Bullet (You can use this)

> Built a Python-based student performance analytics system using Pandas to process CSV data, compute subject-wise trends, identify top performers, and classify student performance with clean, modular code.

---

## 👤 Author

**Ayaan Anildutt**  
B.Tech Student | AI & Data Science  
