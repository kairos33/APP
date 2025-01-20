import streamlit as st
view = [100, 150, 60]
st.write('# Youtube view')
st.write('## raw')
view
st.write('## chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview