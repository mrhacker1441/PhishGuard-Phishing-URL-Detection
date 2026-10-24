import streamlit as st
from detector import detect_phishing
import pandas as pd
from datetime import datetime

from pathlib import Path

css_file = Path(__file__).parent / "style.css"

with open(css_file, encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Page configuration
st.set_page_config(
    page_title="PhishGuard | Cybersecurity",
    page_icon="🛡️",
    layout="wide"
)

# Initialize scan history
if "scan_history" not in st.session_state:
    st.session_state.scan_history = []

# Main heading
st.title("🛡️ PhishGuard")
st.subheader("Phishing URL Detection & Awareness System")

st.write(
    "Protect yourself from suspicious links! "
    "Enter a URL below to analyse potential phishing indicators."
)

st.divider()

# URL input
url = st.text_input(
    "🔗 Enter Website URL",
    placeholder="https://example.com"
)

# Analyse button
if st.button("🔍 Analyse URL", type="primary"):

    result, score, reasons = detect_phishing(url)
    
    # Save valid scan results to history
    if result != "Invalid URL":
        st.session_state.scan_history.append({
            "Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "URL": url,
            "Risk Level": result,
            "Risk Score": score,
            "Detection Reasons": "; ".join(reasons)
        })

    if result == "Invalid URL":
        st.error("Please enter a valid URL.")

    else:
        st.subheader("📊 Security Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Risk Score", f"{score}/100")

        with col2:
            st.metric("Risk Level", result)

        st.progress(score / 100)

        if result == "High Risk":
            st.error("🔴 High Risk: Multiple suspicious indicators detected.")

        elif result == "Suspicious":
            st.warning("🟠 Suspicious: Some risk indicators detected.")

        else:
            st.success("🟢 Low Risk: No major indicators detected by these rules.")

        st.subheader("🔎 Detection Details")

        for reason in reasons:
            st.write("•", reason)

        st.info(
            "Note: This is a rule-based educational tool. "
            "Its results do not guarantee whether a website is safe."
        )

st.divider()

# Awareness section
st.subheader("🔐 Cybersecurity Awareness Tips")

with st.expander("How to identify phishing websites"):
    st.write("""
    - Check the website domain carefully.
    - Avoid suspicious links received through emails or messages.
    - Never share passwords or OTPs on untrusted websites.
    - Remember that HTTPS alone does not guarantee safety.
    - Enable two-factor authentication whenever possible.
    """)

with st.expander("What should you do if you encounter a phishing link?"):
    st.write("""
    - Do not enter personal information.
    - Avoid downloading unknown files.
    - Report suspicious messages to the relevant platform.
    - Change your password if you entered credentials.
    - Enable multi-factor authentication.
    """)

st.divider()

st.caption(
    "PhishGuard | Cybersecurity Internship Project | "
    "Built using Python & Streamlit"
)

# Scan History Section
st.divider()
st.subheader("📜 URL Scan History")

if st.session_state.scan_history:

    df = pd.DataFrame(st.session_state.scan_history)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📊 Risk Distribution")

    risk_counts = df["Risk Level"].value_counts()

    st.bar_chart(risk_counts)

    st.subheader("📥 Download Security Report")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="PhishGuard_Security_Report.csv",
        mime="text/csv"
    )

else:
    st.info("No URLs analysed yet. Start scanning to view history.")
