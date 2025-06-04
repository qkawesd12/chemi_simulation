import streamlit as st

st.title("화학 반응 시뮬레이션")

st.markdown("""
<style>
.meal-item {
    padding: 15px 20px;
    margin-bottom: 15px;
    border-radius: 12px;
    text-align: center;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 1.3rem;
    box-shadow: 0 4px 12px rgba(64, 60, 255, 0.25);
    transition: background-color 0.3s ease, color 0.3s ease;
    background: linear-gradient(90deg, #5a72ff, #7c5aff);
    color: #e0e0ff;
}
.body {
    background-color: #f0f2ff;
    color: #2a2a72;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
@media (prefers-color-scheme: dark) {
    .meal-item {
        background: linear-gradient(90deg, #372a72, #5a3a99);
        color: #d1caff;
        box-shadow: 0 4px 16px rgba(90, 82, 255, 0.8);
    }
    .body {
        background-color: #1a1a2e;
        color: #c6c6ff;
    }
}
@media (prefers-color-scheme: light) {
    .meal-item {
        background: linear-gradient(90deg, #5a72ff, #7c5aff);
        color: #e0e0ff;
    }
}
.description {
    padding: 12px 18px;
    margin-bottom: 10px;
    border-radius: 10px;
    background: linear-gradient(90deg, #d0d4ff, #c2baff);
    color: #2a2a72;
    font-weight: 600;
    font-size: 1rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(64, 60, 255, 0.12);
}
@media (prefers-color-scheme: dark) {
    .description {
        background: linear-gradient(90deg, #1f1c3a, #2a2470);
        color: #c6c6ff;
        box-shadow: 0 2px 8px rgba(90, 82, 255, 0.25);
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="meal-item">
  <div>🔬 <strong>화학 반응 시뮬레이터</strong></div>
  <div>⚗️ 💥 🌡️</div>
</div>
<div class="description">
  🔎 산·염기 중화 · 산화·환원 · 몰 농도 계산을 간편하게<br>
  ✨ 쉽고 빠르게 화학 반응을 이해하는 학습 도우미
</div>
""", unsafe_allow_html=True)
