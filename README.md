# AI-powered Resume Screening and Ranking System

## 📌 Project Overview
The **AI-powered Resume Screening and Ranking System** automates the process of shortlisting resumes based on job descriptions using **NLP and Deep Learning techniques**. This system helps recruiters save time and make data-driven hiring decisions by ranking candidates based on their **relevance to job requirements**.

## 🚀 Features
✅ **Automated Resume Parsing** - Supports PDF and DOCX formats  
✅ **BERT-based Semantic Matching** - Advanced NLP for accurate ranking  
✅ **Named Entity Recognition (NER)** - Extracts skills, education, and experience  
✅ **Interactive Web Interface** - Built with Streamlit for easy use  
✅ **Data Visualization** - Charts for skill and experience insights  
✅ **Secure Resume Processing** - Uses encryption for data protection  
✅ **Multi-language Support** (Future Scope)  

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **NLP Models:** SpaCy, Transformers (BERT)  
- **Libraries:** Pandas, Matplotlib, Plotly, Scikit-learn  
- **Security:** Cryptography (Fernet Encryption)  

## 📂 Project Structure
```bash
├── app.py  # Main Streamlit App
├── requirements.txt  # Dependencies
├── models/  # Pretrained NLP Models
├── data/  # Sample resumes
├── utils.py  # Helper functions
└── README.md  # Project Documentation
```

## 🎯 How It Works
1. **Upload resumes** (PDF/DOCX format).  
2. **Enter job description** to compare against resumes.  
3. **System extracts key information** (skills, education, experience).  
4. **BERT model calculates similarity scores**.  
5. **Candidates are ranked and visualized** for easy selection.  

## 🔧 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/Yashbha25/Resume-Screening-AI.git
cd resume-screening

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 🖼️ Screenshots
### 🎯 Resume Upload & Job Description Input
![image](https://github.com/user-attachments/assets/24345bd2-2d6c-47cd-b756-b475cb50432a)


### 📊 Candidate Ranking & Visualization
![image](https://github.com/user-attachments/assets/6e17d43e-6179-4fcb-9cb1-3bdcd3f8f045)


## 📌 Future Enhancements
- ✅ **Integrate GPT-based Resume Analysis**  
- ✅ **Support Scanned Resumes using OCR**  
- ✅ **Cloud-based API for ATS Integration**  

---
🌟 **Star this repo if you found it useful!** 🚀
