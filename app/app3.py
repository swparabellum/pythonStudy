import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

btn = st.button("버튼이에요.")
if btn:
    st.write(":blue[버튼]이 눌렸다!!!!")

    ##

df = pd.DataFrame({
    "1st":[1,2,3,4],
    "2nd":[5,6,7,8] 
})

st.download_button(
    label="scv다운로드!!!",
    data=df.to_csv(),
    file_name="sample.csv",
    mime="text/csv"
)

##

box = st.checkbox("확인해주세요")

if box:
    st.write("뒤로 돌아가십쇼.")

##

radio = st.radio(
    label="고라니",
    options=('네','아니요','네??'),
    index=2
)

if radio == "네":
    st.write("네!!!")
elif radio == "아니요":
    st.write("하?")
else:
    st.write("끼에에에에엙!")

##

select = st.selectbox(
    label="아이고...",
    options=("아이고","아이고난","으악")
)
if select =="아이고":
    st.write("아이고!")
elif select =="아이고난":
    st.write("아이고난!")
else:
    st.write("으아아아아")

##

multi = st.multiselect(
    "고르슈",
    ["네","아뇨","뭐요?"],
    ["네","뭐요?"] #기본으로 골라진것들
)

st.write(f"고른건?? :green[{multi}]:인듯함.")

##

sl = st.slider(
    "범위의 값을 지정하세요.",
    0.0, 100.0, (30.0, 65.0)
)
st.write("선택 범위:", sl)

#####

점심 = st.slider(
    "점심 시간은 언제 좋을까요?",
    min_value=dt(2024, 12, 5, 13, 20),
    max_value=dt(2024, 12, 5, 14, 30),
    value=dt(2024, 12, 5, 13, 30),
    step=datetime.timedelta(minutes=10),
    format="MM/DD/YY HH:mm"
)
st.write("선택한 시간:", 점심)