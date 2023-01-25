import streamlit as st

st.title("Contacts :envelope:")

#use local CSS---------
def local_css(file_name):
    with open(file_name)as f:
      st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("C:/Users/admin/Desktop/didas/style/style.css.txt")


with st.container():
    st.write("---")
    st.header("You can contact Dreamfar Group by filling bellow")
    st.write("##")
    icon="envelope"
 #----documentation-------
    contact_form="""
    <form action="https://formsubmit.co/didasifrimin@gmail.com" method="POST">
      <input type="hidden" name = "_captcha" value="false">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="  Your Email" required>
      <textarea name="message" placeholder="Comment" required></textarea>
      <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
      st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()

