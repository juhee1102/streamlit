import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import seaborn as sns
import numpy as np

#한글 출력을 위한 설정
font_path = "C:/Windows/Fonts/GULIM.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})
#데이터 표로 나타내기
st.dataframe(data, use_container_width=True)

# fig : 그래프 그림(?) 그 자체
# ax : 객체는 그래프를 그릴 영역 선택
fig1, ax = plt.subplots()
plt.title("개인별 나이")
ax.bar(data['이름'], data['나이'])

#ax.patches는 그래프의 모든 막대 정보를 나타내는 리스트
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                # 텍스트를 표시할 위치를 지정, 중간위치, 높이값 지정
                (p.get_x() + p.get_width() / 2., p.get_height()),
                # 텍스트의 가로 위치 (ha)와 세로 위치 (va)를 'center'로
                # 설정하여 텍스트가 가운데 정렬되도록 지정
                ha = 'center', va = 'center',
                #텍스트를 막대 위, 9 픽셀 위에 표시
                xytext = (0, 9),
                textcoords = 'offset points')
ax.set_ylim(0, 40)
st.pyplot(fig1)

path = '인구.csv'
# CSV 파일을 데이터프레임으로 읽기
data1 = pd.read_csv(path, encoding='cp949')
print(data1)
st.dataframe(data1, use_container_width=True)

fig3, ax = plt.subplots()
plt.title("연도별 출생아수")
ax.bar(data1['시점'], data1['출생아수(명)'])
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                # 텍스트를 표시할 위치를 지정, 중간위치, 높이값 지정
                (p.get_x() + p.get_width() / 2., p.get_height()),
                # 텍스트의 가로 위치 (ha)와 세로 위치 (va)를 'center'로
                # 설정하여 텍스트가 가운데 정렬되도록 지정
                ha = 'center', va = 'center',
                #텍스트를 막대 위, 9 픽셀 위에 표시
                xytext = (0, 9),
                textcoords = 'offset points')
ax.set_ylim(200000, 500000)
st.pyplot(fig3)

fig4, ax = plt.subplots()
plt.title("연도별 출생아수(선형)")
ax.plot(data1['시점'], data1['출생아수(명)'], color="#F7D358", marker=",", linestyle="-")
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
# 데이터 레이블 표시
for i, txt in enumerate(data1['출생아수(명)']):
    ax.text(data1['시점'][i], txt, str(txt), ha='center', va='bottom')
ax.set_ylim(200000, 500000)
st.pyplot(fig4)


# 이미지 파일 경로 설정
image_path = 'jang.JPG'
# 이미지를 화면에 출력
st.image(image_path)

# 라디오 선택 버튼
ex1 = st.radio(
    '문제 1. 위 사람의 이름은?',
    ('장원영', '이서', '안유진'))

if ex1 == '장원영':
    st.write('정답입니다!🎁')
else:
    st.write("다시 생각해 보세요")


# fig4, ax = plt.subplots()
# plt.title("연도별 출생아수(선형)")
# ax.plot(data1['시점'], data1['출생아수(명)'], color="pink", marker=",", linestyle="-")
# plt.xlabel("연도")
# plt.ylabel("출생아수(단위: 명)")
# # 데이터 레이블 표시
# for i, txt in enumerate(data1['출생아수(명)']):
#     ax.text(data1['시점'][i], txt, str(txt), ha='center', va='bottom')
# ax.set_ylim(200000, 500000)
# st.pyplot(fig4)





# fig2, ax = plt.subplots()
# barplot = sns.barplot(x='이름', y='몸무게', data=data, ax=ax, palette='Set2')
# plt.title("개인별 몸무게")
# # seaborn의 그래프 객체를 Matplotlib의 Figure 객체로 변환
# ax.set_ylim(0, 100)
# for p in ax.patches:
#     ax.annotate(format(p.get_height(), '.1f'),
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'center',
#                 xytext = (0, 9),
#                 textcoords = 'offset points')
#
# fig2 = barplot.get_figure()
# st.pyplot(fig2)
# #############
#
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence
#
# fig, ax = plt.subplots()
#
# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')
#
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()
#
# st.pyplot(fig)
#
# ##### Barcode
#
# code = np.array([
#     1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
#     0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
#     1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
#     1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
#
# pixel_per_bar = 4
# dpi = 100
#
# fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
# ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
# ax.set_axis_off()
# ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
#           interpolation='nearest')
#
# st.pyplot(fig)