import streamlit as st
import pandas as pd

st.set_page_config(page_title='철근이음정착길이', page_icon='🏗️', layout='wide')

df1 = pd.read_excel('bar_data.xlsx', sheet_name='CON')    #이음길이 데이터 불러오기
df2 = pd.read_excel('bar_data.xlsx', sheet_name='SET')    #정착길이 데이터 불러오기
df3 = pd.read_excel('bar_data.xlsx', sheet_name='ETC')    #기타 데이터 불러오기

st.write('### 철근 이음,정착길이')
st.text('Test용 - 정림건축구조일반사항 자료 기준')

# 선택 박스
con_list = ['21', '24', '27', '30', '35', '40']
con = st.pills('콘크리트 강도 (MPa)', con_list)

bar_list = ['400', '500', '600']
bar = st.pills('철근 강도 (MPa)', bar_list)

mem_list=list(set(df1['부재'].tolist()))
mem_list.sort()
mem = st.pills('부재', mem_list)

loc_list=df1[df1['부재']==mem]['구분'].tolist()
loc = st.pills('위치', loc_list)

dia_list=['D10', 'D13', 'D16', 'D19', 'D22', 'D25']
dia = st.pills('철근직경', dia_list)

st.divider()

try:
    dia1 = con + bar + dia
    is_member = df1['부재'] == mem
    is_locate = df1['구분'] == loc
    ans1 = df1.loc[is_member & is_locate, dia1].tolist()[0]
    ans2 = df2.loc[is_member & is_locate, dia1].tolist()[0]
    ans3 = df3[dia1].tolist()[0]
    ans4 = df3[dia1].tolist()[1]
    ans5 = df3[dia1].tolist()[2]
    
except:
    st.markdown('** 조건을 선택하세요**')
    
else:
    st.markdown(f'인장이음길이(B급): **{ans1}** mm ')
    st.markdown(f'인장정착길이: **{ans2}** mm ')
    st.markdown(f'표준갈고리(Ldh): **{ans3}** mm ')
    st.markdown(f'압축이음길이(Lsc): **{ans4}** mm ')
    st.markdown(f'압축정착길이(Ldc): **{ans5}** mm ')