import streamlit as st
st.title("📊 몰 수 / 농도 계산기")

moles = st.number_input("물질의 몰 수 (mol)", min_value=0.0, step=0.01) #사용자로부터 물질의 몰 수 입력 받기
volume = st.number_input("용액 부피 (L)", min_value=0.0, step=0.01) #사용자로부터 용액의 부피 입력 받기

if st.button("농도 계산"):
  if volume == 0:
    st.warning("부피는 0이 될 수 없습니다.")
  else:
    molarity = moles / volume
    st.success(f"몰농도: {molarity:.2f} M")
