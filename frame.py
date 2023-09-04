import streamlit as st
import pandas as pd

st.title('streamlit dataframe🎨')

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.dataframe(dataframe, use_container_width=False)
st.table(dataframe)

st.metric(label="온도", value="10°C", delta="1.2°C")
st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,323.5 원", delta="-0.23%")
col2.metric(label="일본JPY(100엔)", value="903.04 원", delta="-0.24%")
col3.metric(label="유럽연합EUR", value="1,430.16 원", delta="-0.19%")