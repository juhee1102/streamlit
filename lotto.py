import streamlit as st
import random #랜덤 변수 생성을 위한 라이브러리 
import datetime #날짜 생성 위한 라이브러리

st.title('💰로또 생성기💰')
button = st.button('1등은 나의 것!!')

if button:
    for i in range(1, 6):
        lotto = set()
        while len(lotto) < 6:
            number = random.randint(1, 46) #1에서부터 45까지 번호 랜덤
            lotto.add(number)
        lotto = list(lotto)
        lotto.sort() #데이터 정렬
        st.subheader(f'{i}. 행운의 번호: :green[{lotto}]')
    st.write("로또 번호 생성된 시각: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))



