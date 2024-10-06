#from dotenv import load_dotenv
#load_dotenv()

#from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.predict("내가 좋아하는 동물은")
#print(result)
import streamlit as st
import time
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요",)


if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)





#st.title("_Streamlit_ is : blue[cool] :sunglasses:")
#st.write("시의 주제는", title)


