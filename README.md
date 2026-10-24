# 🛡️ PhishGuard
### Phishing URL Detection & Awareness System

## 📌 Project Overview

PhishGuard is a Python-based cybersecurity project developed to identify potentially suspicious URLs using rule-based detection techniques.

The application analyses different characteristics of a URL and generates a risk score to help users recognise common phishing indicators.

It also provides an interactive dashboard, URL scan history, risk visualisation and downloadable security reports.

This project was developed as part of a cybersecurity internship to gain practical experience in phishing detection, URL analysis and security awareness.

## 🎯 Project Objectives

- Understand common phishing techniques and suspicious URL patterns.
- Develop a rule-based URL risk detection system using Python.
- Analyse URLs based on predefined security indicators.
- Generate risk scores and classify URLs into different risk levels.
- Create an interactive dashboard for displaying analysis results.
- Promote cybersecurity awareness through preventive security tips.

## 🚀 Features

### 1. URL Risk Analysis
Analyses URLs using indicators such as:
- HTTP instead of HTTPS
- Unusually long URLs
- IP addresses in place of domain names
- Suspicious keywords
- @ symbols in URLs
- Excessive subdomains

### 2. Risk Classification
Classifies URLs into three categories:

- 🟢 Low Risk
- 🟠 Suspicious
- 🔴 High Risk

### 3. Interactive Dashboard
A Streamlit-based interface displays the risk score, classification and detection details.

### 4. URL Scan History
Maintains a history of analysed URLs during the current application session.

### 5. Risk Distribution Chart
Visualises the distribution of analysed URLs across different risk categories.

### 6. Downloadable Security Report
Allows users to download scan results in CSV format.

### 7. Cybersecurity Awareness
Provides basic guidance on recognising phishing attempts and protecting sensitive information.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Data handling and CSV reports |
| HTML/CSS | Dashboard styling |
| urllib.parse | URL parsing and analysis |
| ipaddress | IP address identification |

## 📂 Project Structure

```text
Phishguard/
│
├── app.py
├── detector.py
├── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Execution

**Step 1:** Download or clone the project repository.

**Step 2:** Open the project folder in VS Code.

**Step 3:** Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

**Step 4:** Run the application:

```bash
python -m streamlit run app.py
```

**Step 5:** Open the local address displayed in the terminal to access the PhishGuard dashboard.

## 🧪 Testing

The application was tested using the following example URLs:

| Test URL | Risk Level | Risk Score |
|---|---|---|
| https://example.com | Low Risk | 0/100 |
| http://example.com | Suspicious | 20/100 |
| http://192.0.2.1/login | High Risk | 60/100 |

The results demonstrate how different URL characteristics influence the rule-based risk score.

## ⚠️ Limitations

- The application uses predefined rules rather than machine learning.
- It does not verify whether a website is genuinely malicious.
- HTTPS alone does not guarantee that a website is safe.
- The risk score is a heuristic indicator, not a probability of phishing.
- Scan history is stored temporarily during the application session.
- Some legitimate URLs may be flagged, while some phishing URLs may go undetected.

## 🔮 Future Enhancements

- Machine learning-based phishing detection.
- Integration with threat intelligence services.
- Domain reputation analysis.
- Improved URL validation.
- Persistent scan history storage.

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming
- Phishing detection concepts
- URL parsing and analysis
- Rule-based security assessment
- Web application development
- Data visualisation
- Cybersecurity awareness

## 👩‍💻 Project Information

**Project Name:** PhishGuard — Phishing URL Detection & Awareness System

**Domain:** Cybersecurity

**Project Type:** Internship Project

**Developed Using:** Python, Streamlit and Pandas

---

*Disclaimer: PhishGuard is an educational cybersecurity project. Its results should not be treated as definitive security assessments.*