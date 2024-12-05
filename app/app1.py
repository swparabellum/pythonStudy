import streamlit as st
st.title("타이틀 입니다.")
st.title("스마일 :sunglasses:")
st.header("헤더 입니다.")
st.subheader("작은 헤더")
st.caption("캡션 입니다.")
st.code("arr = []", language="python")
sample_code = """
def 함수():
    return 1 + 1
"""
st.code(sample_code, language="python")
st.text("일반적으로 글 작성")
st.markdown("웹개발은 **너무 너무** 쉽다")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]")
st.latex(r"\sqrt{x^2+y^2}=1")