import streamlit as st

st.title('이것은 타이틀입니다')

st.header('헤더를 입력할 수 있어요! :sparkles:')

st.subheader('이것은 subheader 입니다.')

st.caption('캡션을 한번 넣어 봤습니다')

sample_code = '''
def function():
    print('hello world')
'''

st.code(sample_code, language='python')

st.text('일반적인 텍스트입니다.')

st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정합니다.')