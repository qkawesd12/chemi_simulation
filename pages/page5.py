import streamlit as st

st.title("🧬 침전 반응")

#침전 반응 예시
reactions = {
"AgNO₃ + NaCl": ("AgCl↓ + NaNO₃", "흰색 침전"),
"BaCl₂ + Na₂SO₄": ("BaSO₄↓ + NaCl", "흰색 침전"),
"Pb(NO₃)₂ + KI": ("PbI₂↓ + KNO₃", "노란색 침전")
}

selected = st.selectbox("반응 선택", list(reactions.keys()))

if st.button("침전 확인"):
  result, color = reactions[selected]
  st.subheader("🧬 생성 반응")
  st.write(result) #생성된 반응식 출력
  st.write(f"→ 침전 색: **{color}**") #침전 색상 출력
