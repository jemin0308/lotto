if st.button('번호뽑기'):
    st.session_state.games = make_games(n)
if 'games' in st.session_state:
    for i in range(len(st.session_state.games)):
        st.write(...)