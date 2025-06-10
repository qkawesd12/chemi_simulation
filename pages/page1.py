import streamlit as st
st.title("🧪 산-염기 반응 시뮬레이션") #페이지 제목 설정

acids = {"HCl": "강산", "H₂SO₄": "강산", "CH₃COOH": "약산"} #산 종류 설정
bases = {"NaOH": "강염기", "KOH": "강염기", "NH₃": "약염기"} # 염기 종류 설정
acid = st.selectbox("산 선택", list(acids.keys())) #드롭다운 (산)
base = st.selectbox("염기 선택", list(bases.keys())) #드롭다운 (염기)

acid_vol = st.number_input("산 부피 (mL)", min_value=0.0, step=10.0) # 산 부피 입력 받기
acid_conc = st.number_input("산 농도 (M)", min_value=0.0, step=0.1) # 산의 몰농도 입력 받기
base_vol = st.number_input("염기 부피 (mL)", min_value=0.0, step=10.0) # 염기의 부피 입력 받기
base_conc = st.number_input("염기 농도 (M)", min_value=0.0, step=0.1) # 염기의 몰농도 입력 받기

#버튼 클릭시 반응 계산
if st.button("반응 확인"):
  acid_mol = (acid_vol / 1000) * acid_conc #산의 몰 수 계산
  base_mol = (base_vol / 1000) * base_conc #염기의 몰 수 계산

  if acid_mol == 0 or base_mol == 0:
      st.warning("몰 수가 0입니다. 농도와 부피를 확인해주세요.")
  else:
      st.subheader("🧬 반응 결과")
      st.write(f"{acid} + {base} → 염 + H₂O") # 기본 반응식 출력

    #산과 염기의 몰 비율 계산 및 표시
      ratio = round(acid_mol / base_mol, 2)
      st.write(f"산/염기 몰 비율: {ratio}")
    #몰 비율에 따른 반응 상태 분석 
      if abs(ratio - 1) < 0.05:
        st.success("완전 중화")
      elif ratio < 1:
        st.info("염기가 과잉입니다. 중화는 부분적으로 일어납니다.")
      else:
        st.info("산이 과잉입니다. 중화는 부분적으로 일어납니다.")
