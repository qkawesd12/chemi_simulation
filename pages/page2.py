import streamlit as st

# 페이지 설정
st.set_page_config(page_title="산화-환원 반응 시뮬레이터", layout="wide")

st.title("🔋 산화-환원 반응 시뮬레이터")

# 금속과 이온 데이터
metals = {
    "Zn (아연)": {"symbol": "Zn", "oxidation": 2},
    "Mg (마그네슘)": {"symbol": "Mg", "oxidation": 2},
    "Fe (철)": {"symbol": "Fe", "oxidation": 2},
    "Cu (구리)": {"symbol": "Cu", "oxidation": 2},
    "Ag (은)": {"symbol": "Ag", "oxidation": 1},
}

ions = {
    "Cu²⁺ (구리 이온)": {"symbol": "Cu²⁺", "reduction": 2},
    "Ag⁺ (은 이온)": {"symbol": "Ag⁺", "reduction": 1},
    "Fe³⁺ (철 이온)": {"symbol": "Fe³⁺", "reduction": 3},
    "Zn²⁺ (아연 이온)": {"symbol": "Zn²⁺", "reduction": 2},
    "Mg²⁺ (마그네슘 이온)": {"symbol": "Mg²⁺", "reduction": 2},
}

# 사용자 입력
metal_choice = st.selectbox("🔹 금속 선택", list(metals.keys()))
ion_choice = st.selectbox("🔸 이온 선택", list(ions.keys()))

# 결과 출력
if st.button("⚗️ 반응 확인"):
    metal = metals[metal_choice]
    ion = ions[ion_choice]

    st.subheader("🔬 반응 분석")
    st.write(f"{metal['symbol']} + {ion['symbol']} → ?")

    if metal['symbol'] in ion['symbol']:
        st.warning("🚫 동일한 금속과 이온입니다. 반응이 일어나지 않습니다.")
    else:
        st.write(f"▶️ {metal['symbol']}은 산화되어 {metal['symbol']}⁺ 상태가 되며 전자 {metal['oxidation']}개를 방출합니다.")
        st.write(f"▶️ {ion['symbol']}은 환원되어 금속이 되며 전자 {ion['reduction']}개를 받습니다.")
        st.success(f"총 전자 이동 수: {ion['reduction']}개")
