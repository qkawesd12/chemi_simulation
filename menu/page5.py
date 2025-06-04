import streamlit as st
elif page == "침전 반응":
st.title("🧬 침전 반응")

reactions = {
"AgNO₃ + NaCl": ("AgCl↓ + NaNO₃", "흰색 침전"),
"BaCl₂ + Na₂SO₄": ("BaSO₄↓ + NaCl", "흰색 침전"),
"Pb(NO₃)₂ + KI": ("PbI₂↓ + KNO₃", "노란색 침전")
}

selected = st.selectbox("반응 선택", list(reactions.keys()))

if st.button("침전 확인"):
  result, color = reactions[selected]
  st.subheader("🧬 생성 반응")
  st.write(result)
  st.write(f"→ 침전 색: **{color}**")
