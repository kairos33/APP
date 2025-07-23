import streamlit as st
import pandas as pd

st.set_page_config(page_title='철근이음정착길이', page_icon='🏗️', layout='wide')

df1 = pd.read_excel('bar_data.xlsx', sheet_name='A', index_col=[0, 1, 2], header=[0, 1])    #A급 이음길이 데이터 불러오기
df2 = pd.read_excel('bar_data.xlsx', sheet_name='B', index_col=[0, 1, 2], header=[0, 1])    #B급 이음길이 데이터 불러오기
df3 = pd.read_excel('bar_data.xlsx', sheet_name='C', index_col=[0, 1, 2], header=[0, 1])    #기타 데이터 불러오기

st.write('### 철근 이음,정착길이')
st.text('Test용 - 인천청소년특화시설 기준')

# 선택 박스
con_list = [21, 24, 27, 30, 35, 40, 45, 50]
con = st.pills('콘크리트 강도 (MPa)', con_list)

bar_list = [400, 500,550, 600]
bar = st.pills('철근 강도 (MPa)', bar_list)

dia_list = ['D10','D13','D16','D19','D22','D25','D29','D32','D35']
dia = st.pills('철근직경', dia_list)

mem_dic = {'기둥':['주근'],'보':['일반','상부'],'슬래브, 벽체, 내수압슬래브, 지하외벽':['피복=20mm','피복=30mm','피복=40mm이상'],'기초':['@150미만-일반','@150미만-상부','@150이상-일반','@150이상-상부'],}
mem_list = list(mem_dic.keys())
mem = st.pills('부재', mem_list)

try:
    loca_list = mem_dic[mem]
except:
    print("")
else:
    loca = st.pills('구분', loca_list, default=loca_list[0])

try:
    ans1 = df1.loc[(bar, con, dia), (mem, loca)]
    ans2 = df2.loc[(bar, con, dia), (mem, loca)]
    # ans1 = df1.loc[(bar, con, dia), (mem, loca)].tolist()[0]
    # ans2 = df2.loc[(bar, con, dia), (mem, loca)].tolist()[0)]
    ans3 = df3.loc[(bar, con, dia)].tolist()[0]
    ans4 = df3.loc[(bar, con, dia)].tolist()[1]
    ans5 = df3.loc[(bar, con, dia)].tolist()[2]
    ans6 = df3.loc[(bar, con, dia)].tolist()[3]
    
except:
    st.markdown('** 조건을 선택하세요**')

else:
    st.markdown(f'인장정착길이: **{ans1:,.0f}** mm ')
    st.markdown(f'인장이음길이(B급): **{ans2:,.0f}** mm ')
    st.markdown(f'표준갈고리-피복부족(Ldh): **{ans3:,.0f}** mm ')
    st.markdown(f'표준갈고리-피복확보(Ldh): **{ans4:,.0f}** mm ')
    st.markdown(f'압축정착길이(Lsc): **{ans5:,.0f}** mm ')
    st.markdown(f'압축이음길이(Ldc): **{ans6:,.0f}** mm ')
