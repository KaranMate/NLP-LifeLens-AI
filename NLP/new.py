import streamlit as st
import joblib

# -------------------------------
# Load Existing Model
# -------------------------------
model = joblib.load("MultinomialNB.pkl")
model = joblib.load("LogisticRegression.pkl")   
model = joblib.load("scaler.pkl")
# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="LifeLens AI",
    page_icon="🔮",
    layout="centered"
)

# -------------------------------
# Ultra-Premium Styling
# -------------------------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #000000);
}
.main {
    background: #ffffff;
    padding: 2.5rem;
    border-radius: 22px;
}
.hero {
    text-align: center;
}
.hero h1 {
    font-size: 44px;
    font-weight: 900;
}
.hero p {
    color: #555;
    font-size: 17px;
}
.glass {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    text-align: center;
}
.badge {
    padding: 16px 34px;
    border-radius: 40px;
    font-size: 20px;
    font-weight: bold;
    display: inline-block;
}
.stable { background: linear-gradient(45deg,#11998e,#38ef7d); color:white; }
.risk { background: linear-gradient(45deg,#f7971e,#ffd200); }
.unstable { background: linear-gradient(45deg,#cb2d3e,#ef473a); color:white; }

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Hero Section
# -------------------------------
st.markdown("""
<div class="hero">
    <h1>🔮 LifeLens AI</h1>
    <p>Predictive Intelligence for Life Stability & Decision Risk</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------
# Input Section
# -------------------------------
st.subheader("🧩 Describe Your Current Situation")

text = st.text_area(
    "",
    height=200,
    placeholder="Example: I am planning to quit my job, start a business, and move to a new city without much savings."
)

# -------------------------------
# Smart Metrics
# -------------------------------
if text:
    col1, col2, col3 = st.columns(3)
    col1.metric("Words", len(text.split()))
    col2.metric("Clarity Score", f"{min(100, len(text.split())*4)}%")
    col3.metric("Decision Density", text.count("and") + text.count(","))

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Analyze Life Stability", use_container_width=True) and text:

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    st.divider()
    st.subheader("📊 Stability Assessment")

    if prediction == "Stable":
        css = "stable"
        msg = "Your situation appears well-balanced with manageable risks."
    elif prediction == "At Risk":
        css = "risk"
        msg = "Multiple uncertainty signals detected. Strategic planning recommended."
    else:
        css = "unstable"
        msg = "High instability detected. Decisions may carry significant risk."

    st.markdown(
        f"""
        <div class="glass">
            <div class="badge {css}">{prediction}</div>
            <p style="margin-top:15px;font-size:16px;">{msg}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("""
<div class="footer">
This system provides decision-risk insights, not personal or financial advice.<br>
Developed by <b>Karan Mate</b> | Applied NLP Intelligence
</div>
""", unsafe_allow_html=True)


#model = joblib.load("MultinomialNB.pkl")
#model = joblib.load("LogisticRegression.pkl")   
#model = joblib.load("scaler.pkl")      # ✅ use your actual file name

