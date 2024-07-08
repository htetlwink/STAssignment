import streamlit as st
print("hello this is run complete...")
with st.container():
    st.header("This is Streamlit Assignment",divider=True)
    st.write("I'm Htet Lwin Kyaw and this is my streamlit assignment. I use this sentence using .text Function.")
    st.image("dog.jpeg",caption="Dog Running on Grass",width=450)
    st.audio("LineCarSee.mp3", autoplay=True)
    name = st.text_input("Your Name")
    selected = st.selectbox("Which Animal do you like ?", options=["Dog","Cat","Fish","Bird"])
    petno = st.slider(f"How many {selected} do you like to pet ?",min_value=0,max_value=10)
    checked1 = st.checkbox("I'm okay to share the data.")

submitted = st.button("Submit")
if submitted:
    st.write(f"{name} likes {selected} and happy to own {petno} {selected}s.")
