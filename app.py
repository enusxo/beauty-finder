
import streamlit as st
import pandas as pd

st.title(" Beauty Finder")
st.write("색상명으로 화장품을 찾아보세요!")

df = pd.read_csv("beauty_data.csv", encoding="utf-8-sig")

keyword = st.text_input("찾고 싶은 색상명을 입력하세요")

if keyword.strip():
    result = df[
        df["색상명"].astype(str).str.contains(
            keyword.strip(), case=False, regex=False, na=False
        )
    ]

    if result.empty:
        st.warning("검색 결과가 없습니다.")
    else:
        st.success(f"{len(result)}개의 검색 결과를 찾았어요!")
        st.dataframe(result, hide_index=True, use_container_width=True)
