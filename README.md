# 💼 Resume Suitability Screener

A **Machine Learning-powered web app** that automatically evaluates resumes and calculates candidate suitability scores for specific job roles.

---

## 🧾 Project Overview
This project helps HRs and recruiters automatically screen resumes using Machine Learning.  
It analyses resume content, compares it with target job roles, and computes a **suitability percentage** for each candidate.  
The frontend is built using **Streamlit**, offering an interactive and easy-to-use interface.

---

## ⚙️ Tech Stack
- 🐍 **Python** – Core programming language  
- 🧠 **Scikit-learn** – Machine Learning model training (Random Forest & KNN)  
- 📊 **Pandas, NumPy** – Data preprocessing and manipulation  
- 🔠 **LabelEncoder, Train-Test Split** – Data transformation and model validation  
- 🌐 **Streamlit** – Web app frontend for user interaction  
- 🧩 **Pickle** – Model serialization (loading trained model and vectorizer)  
- 📄 **PyPDF2** – Resume text extraction from PDFs  
- 🎨 **Matplotlib** – Donut chart visualization  

---

## ✨ Features
- Upload upto 5 resumes at a time in PDF format  
- Select a target job role (e.g., Data Scientist, Java Developer, etc.)  
- Predict candidate suitability percentage  
- Display results with an interactive **donut chart**  
- Highlights the most suitable candidate visually  
- Simple, fast, and fully automated interface
    
---

**Roles & Work Done:**  
- Collected and cleaned the dataset (Kaggle Updated Resume Dataset)  
- Applied `LabelEncoder` for category encoding  
- Used `train_test_split` for model evaluation  
- Trained **Random Forest** and **KNN** classifiers  
- Saved trained models using `pickle`  
- Built an interactive **Streamlit app** for final deployment  

---

## 🎯 Mission Statement
> “To automate the resume screening process and help recruiters identify top candidates efficiently using Machine Learning.”
