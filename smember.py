import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title='검측도우미', page_icon='🏗️', layout='wide')

st.write('### 검측도우미')
mem_list = ['기둥', '벽체', '보', '슬래브']
# member = st.selectbox('부재선택', mem_list)
member = st.pills('조회할 부재를 선택하세요', mem_list)

if member == '기둥':
    col_list = os.listdir('./IMG/COL')
    col_list = [ext.strip('.png') for ext in col_list]
    col_list.sort()
    col = st.pills('기둥선택', col_list)
    try:
        st.image(f'./IMG/COL/{col}.png')
    except:
        st.text('')
    else:
        pass
    
elif member == '벽체':
    st.text('벽체입니다')
    
elif member == '보':
    floor_list = os.listdir('./IMG/BEAM')
    floor_list.sort()
    floor = st.pills('층 선택', floor_list)
    
    try:
        beam_list = os.listdir(f'./IMG/BEAM/{floor}')
        beam_list = [ext.strip('.png') for ext in beam_list]
        beam_list.sort()   
        beam = st.pills('보 선택', beam_list)
        st.image(f'./IMG/BEAM/{floor}/{beam}.png')
    except:
        st.text('')
    else:
        pass
    
elif member == '슬래브':
    df_slab = pd.read_csv('./IMG/SLAB/SLABINDEX.csv')
    df_slab = df_slab.set_index('NAME')
    slab_list = df_slab.columns
    
    try:
        slab = st.pills('슬래브 선택', slab_list)
        slab_type = df_slab.loc['TYPE', slab]
        st.image(f'./IMG/SLAB/SL{slab_type}.png')
        st.table(df_slab[slab])
    except:
        st.text('')
    else:
        pass
    
    
else:
    st.text('')

