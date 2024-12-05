import streamlit as st
import pandas as pd


# streamlit run app2.py --server.port 8080

st.title("데이터 프레임 화면")

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

df= pd.DataFrame(arr)

st.dataframe(df,use_container_width=True)

##

st.title("테이블 화면")

st.table(df)

##

st.metric(label="온도",value="8",delta="1.2")
st.metric(label="삼성전자",value="50000",delta="-400")

col1,col2,col3 = st.columns(3)
col1.metric(label="온도",value="8",delta="1.2")
col2.metric(label="삼성전자",value="50000",delta="-400")
col3.metric(label="일성전자",value="99900",delta="400")