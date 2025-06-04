st.title("🧪 산-염기 반응 시뮬레이터")

acids = {"HCl": "강산", "H₂SO₄": "강산", "CH₃COOH": "약산"}
bases = {"NaOH": "강염기", "KOH": "강염기", "NH₃": "약염기"}
acid = st.selectbox("산 선택", list(acids.keys()))
base = st.selectbox("염기 선택", list(bases.keys()))

acid_vol = st.number_input("산 부피 (mL)", min_value=0.0, step=10.0)
acid_conc = st.number_input("산 농도 (M)", min_value=0.0, step=0.1)
base_vol = st.number_input("염기 부피 (mL)", min_value=0.0, step=10.0)
base_conc = st.number_input("염기 농도 (M)", min_value=0.0, step=0.1)

if st.button("반응 확인"):
  acid_mol = (acid_vol / 1000) * acid_conc
  base_mol = (base_vol / 1000) * base_conc

  if acid_mol == 0 or base_mol == 0:
      st.warning("몰 수가 0입니다. 농도와 부피를 확인해주세요.")
  else:
      st.subheader("🧬 반응 결과")
      st.write(f"{acid} + {base} → 염 + H₂O")

      ratio = round(acid_mol / base_mol, 2)
      st.write(f"산/염기 몰 비율: {ratio}")

      if abs(ratio - 1) < 0.05:
        st.success("완전 중화")
      elif ratio < 1:
        st.info("염기가 과잉입니다. 중화는 부분적으로 일어납니다.")
      else:
        st.info("산이 과잉입니다. 중화는 부분적으로 일어납니다.")
