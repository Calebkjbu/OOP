import streamlit as st

from PIL import Image

col1, col2 = st.columns((4, 5))

with col1:
    st.title("My Resume")
    st.header("Caleb Kempka")

with col2:
    image = Image.open('deez.png')
    st.image(image, width=200)
st.divider()
st.markdown("About me")
st.text("I am athletic, smart")
st.text("I attend JBU")
st.text("I study cybersecurity and AI")
st.text("I worked in alot of different places, I worked for certain residnets with taking care of thier lawns and also helping them with famrs, i also worked in a bunch of restarunts ")
st.text("I ejoy playing sports outside for my hobby and hanging out with friends ")
st.text("Contact:Erm nah")
st.markdown("contact deez")
st.text_input("your name:")
st.text_input("email id:")
message = st.text_area("your message")
st.button("send message")



