import streamlit as st

st.title("화학 반응 시뮬레이션")

import streamlit as st

# CSS 스타일 추가 (사용자 제공 코드 반영)
st.markdown("""
<style>
.meal-item {
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    text-align: center;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    font-size: 1.1rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: background-color 0.3s ease, color 0.3s ease;
}
body {
    background-color: #ffffff;
    color: black;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
@media (prefers-color-scheme: dark) {
    body {
        background-color: #121212;
        color: white;
    }
    .meal-item {
        background-color: #333333;
        color: white;
        box-shadow: 0 2px 10px rgba(255,255,255,0.1);
    }
}
@media (prefers-color-scheme: light) {
    .meal-item {
        background-color: #f0f0f0;
        color: black;
    }
}
</style>
""", unsafe_allow_html=True)

# 메인 화면용 HTML 구조
st.markdown("""
<div class="meal-item">
  <div>⚗️ <strong>화학 반응 시뮬레이터</strong></div>
  <div>📚 자율교육과정 & 정보과학 연계 프로젝트</div>
</div>
<div class="meal-item" style="justify-content: center; font-size: 0.95rem; font-weight: normal;">
  - 산-염기 중화, 산화-환원, 몰 농도 등 화학 반응 개념을 쉽고 빠르게 계산해보세요.<br>
  - 게임 제작 시 필요한 화학 반응 이해에 도움을 줍니다.
</div>
""", unsafe_allow_html=True)
