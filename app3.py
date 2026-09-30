import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="포춘쿠키",
    page_icon="🥠"
)

st.title("🥠 포춘쿠키 하나 먹어보세요!")
st.success("시험 기간 지친 여러분을 위해 포춘쿠키를 준비했어요.")

msg = pd.read_csv("message.csv", encoding="utf-8-sig")

if st.button("포춘쿠키 확인하기"):
    ra = st.empty()
    with ra.container():
        st.image("image.gif", width=250)
        st.write("포춘쿠키를 여는 중입니다.")

    time.sleep(3)
    f = random.choice(msg["message"].tolist())
    with ra.container():
        st.subheader("포춘쿠키가 열렸어요!")
        st.warning(f)