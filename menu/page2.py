import streamlit as st
st.title("🔋 산화-환원 반응 시뮬레이션")

st.write("예시 반응: Zn + Cu²⁺ → Zn²⁺ + Cu")
reaction = st.text_input("반응식 입력 (예: Zn + Cu²⁺)")

if st.button("분석하기"):
  if "Zn" in reaction and "Cu²⁺" in reaction:
    st.subheader("🧬 분석 결과")
    st.write("Zn은 전자를 잃고 Zn²⁺로 산화되었습니다.")
    st.write("Cu²⁺는 전자를 얻고 Cu로 환원되었습니다.")
    st.write("→ 총 전자 이동 수: 2 (공격력 척도 가능)")
  else:
    st.warning("지원되지 않는 반응입니다. 예시 반응만 작동합니다.")
