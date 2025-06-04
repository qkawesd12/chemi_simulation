import streamlit as st
st.title("☣️ 기체 발생 반응")

reactions = {
"HCl + Zn": "ZnCl₂ + H₂↑ (수소 발생)",
"Na₂CO₃ + HCl": "CO₂↑ + NaCl + H₂O (이산화탄소 발생)"
}

selected = st.selectbox("반응 선택", list(reactions.keys()))

if st.button("기체 확인"):
  st.subheader("🧬 생성 반응")
  st.write(reactions[selected])
