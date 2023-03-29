import streamlit as st

st.title('한국건설기술연구원, Google GIS')

agree = st.checkbox('위성지도')

if agree:
    st.write('삐빅 위성지도입니다.')

agree = st.checkbox('하천지도')

if agree:
    st.write('삐빅 하천지도입니다.')

agree = st.checkbox('지표')

if agree:
    st.write('삐빅 지표입니다.')

col1, col2 = st.columns(2)

with col2:
    text_input = st.text_input("검색 👇")
    if text_input:
        st.write("검색 지역: ", text_input)

workplace = st.selectbox(
    '당신이 근무하는 곳은 어디입니까?',
    ('본원(일산)', '화재안전연구소(화성)', '하천실험센터(안동)', 'SOC실증연구센터(연천)'),
    index=0
)


if workplace == '본원(일산)':
    st.write('위치 : 일산')
elif workplace == '화재안전연구소(화성)':
    st.write('위치 : 화성')
elif workplace == '하천실험센터(안동)':
    st.write('위치 : 안동')
else:
    st.write('위치 : 연천')

