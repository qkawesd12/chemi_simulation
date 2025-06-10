import streamlit as st
st.title("☣️ 기체 발생 반응")

#기체가 발생하는 대표적 화학 반응 정의
reactions = {
"HCl + Zn": "ZnCl₂ + H₂↑ (수소 발생)",
"Na₂CO₃ + HCl": "CO₂↑ + NaCl + H₂O (이산화탄소 발생)"
}

selected = st.selectbox("반응 선택", list(reactions.keys())) #드롭다운 제공

if st.button("기체 확인"):
  st.subheader("🧬 생성 반응") #생성 반응 결과 제목 출력
  st.write(reactions[selected]) #선택된 반응에 대응하는 생성물 출력
