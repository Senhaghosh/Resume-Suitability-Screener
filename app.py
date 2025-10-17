import streamlit as st
import pickle
from PyPDF2 import PdfReader
from clean_helper import cleanResume
import matplotlib.pyplot as plt

# -------------------------
# Load Model and Vectorizer
# -------------------------
clf = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# -------------------------
# Category Mapping
# -------------------------
categoryMapping = {
    15: 'Java Developer',
    23: 'Testing',
    8: 'DevOps Engineer',
    20: 'Python Developer',
    24: 'Web Designing',
    12: 'HR',
    13: 'Hadoop',
    3: 'Blockchain',
    10: 'ETL Developer',
    18: 'Operations Manager',
    6: 'Data Science',
    22: 'Sales',
    16: 'Mechanical Engineer',
    1: 'Arts',
    7: 'Database',
    11: 'Electric Engineering',
    14: 'Health and fitness',
    19: 'PMO',
    4: 'Business Analyst',
    9: 'Dotnet Developer',
    2: 'Automation Testing',
    17: 'Network Security Engineer',
    21: 'SAP Developer',
    5: 'Civil Engineer',
    0: 'Advocate'
}

role_to_index = {v: k for k, v in categoryMapping.items()}

# -------------------------
# Streamlit UI
# -------------------------
st.title("📄 Resume Suitability Screener")

target_role = st.selectbox("Select the Job Role", list(categoryMapping.values()))

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF only, max 5)", 
    type=["pdf"], 
    accept_multiple_files=True
)

if uploaded_files:
    # Warn if more than 5 files
    if len(uploaded_files) > 5:
        st.warning("⚠ You can upload a maximum of 5 resumes. The 6th file and beyond will not be processed.")

    if target_role:
        target_index = role_to_index[target_role]

        resume_names = []
        suitability_scores = []

        # Process only the first 5 resumes
        for uploaded_file in uploaded_files[:5]:
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text() + " "

            cleaned = cleanResume(text)
            input_features = tfidf.transform([cleaned])

            if hasattr(clf, "predict_proba"):
                probs = clf.predict_proba(input_features)[0]
                role_prob = probs[target_index] * 100
                resume_names.append(uploaded_file.name)
                suitability_scores.append(role_prob)

        # -------------------------
        # Donut chart: normalize to sum 100
        # -------------------------
        if suitability_scores:
            total = sum(suitability_scores)
            if total == 0:
                st.info("All suitability scores are 0. Cannot generate chart.")
            else:
                normalized_scores = [score / total * 100 for score in suitability_scores]
                labels = [f"{name} ({score:.1f}%)" for name, score in zip(resume_names, normalized_scores)]

                fig, ax = plt.subplots()
                wedges, texts = ax.pie(
                    normalized_scores,
                    labels=labels,
                    startangle=90,
                    wedgeprops=dict(width=0.4),
                    labeldistance=1.15
                )
                ax.set_title(f"Suitability of Different Candidates for the role of {target_role}\n\n")
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
                st.pyplot(fig)