import streamlit as st

st.title("화학 반응 시뮬레이션")
#CSS 스타일 정의
st.markdown("""
<style>
/*상단 타이틀 블록 스타일 정의*/
.meal-item {
    padding: 15px 20px; /*안쪽 여백*/
    margin-bottom: 15px; /*아래쪽 여백*/
    border-radius: 12px; /*모서리 둥글게*/
    text-align: center; /*텍스트 가운데 정렬*/
    display: flex; /*수평 정렬을 위한 flex 설정*/
    justify-content: space-between; /*좌우 요소 간격*/
    align-items: center; /*수직 정렬*/
    font-weight: 700; /*굵은 글씨*/
    font-size: 1.3rem; /*글자 크기*/
    box-shadow: 0 4px 12px rgba(64, 60, 255, 0.25); /*그림자 효과*/
    transition: background-color 0.3s ease, color 0.3s ease; /*부드러운 색상 변화*/
    background: linear-gradient(90deg, #5a72ff, #7c5aff); /*그라데이션*/
    color: #e0e0ff; /*글자 색*/
}
/*기본 배경 및 폰트 설정*/
.body {
    background-color: #f0f2ff;
    color: #2a2a72;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
/*다크 모드 적용시 스타일 설정*/
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
/*라이트 모드 전용 스타일*/
@media (prefers-color-scheme: light) {
    .meal-item {
        background: linear-gradient(90deg, #5a72ff, #7c5aff);
        color: #e0e0ff;
    }
}
/*설명 블럭 스타일일*/
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
/*설명 블럭의 다크 모드 스타일*/
@media (prefers-color-scheme: dark) {
    .description {
        background: linear-gradient(90deg, #1f1c3a, #2a2470);
        color: #c6c6ff;
        box-shadow: 0 2px 8px rgba(90, 82, 255, 0.25);
    }
}
</style> 
""", unsafe_allow_html=True)
# 시뮬레이터 상단 타이틀 영역 표시,간단한 설명 문구 표시, 페이지 목록 소개용 설명 박스
st.markdown("""
<div class="meal-item">
  <div>🔬 <strong>화학 반응 시뮬레이터</strong></div>
  <div>⚗️ 💥 🌡️</div>
</div> 
<div class="description">
  🔎 산·염기 중화 · 산화·환원 · 몰 농도 계산을 간편하게<br>
  ✨ 쉽고 빠르게 화학 반응을 이해하는 학습 도우미
</div>
<div class="description">
  page1 - 산-염기 반응 시뮬레이션<br>
  page2 - 산화-환원 반응 시뮬레이션<br>
  page3 - 몰 수 / 농도 계산기<br>
  page4 - 기체 발생 반응<br>
  page5 - 침전 반응
</div>
""", unsafe_allow_html=True)
