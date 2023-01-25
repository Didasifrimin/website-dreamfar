import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
#menu_icon="cast"

#with st.sidebar:
#    selected = option_menu(
#        menu_title="Main Page",
#        options=["Homepage","Projects","Contact"],
#    )

#if selected =="Homepage":
#    st.title(f"You have selected{selected}")

#if selected =="Projects":
#    st.title(f"You have selected{selected}")
#if selected =="Contact":
#    st.title(f"You have selected{selected}")
    
#st.set_page_config(page_title="Our webpage WELCOME",page_icon=":tada:",layout="centered")
#st.title("Main Page")
#st.sidebar.success("Select a page above")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#use local CSS---------
def local_css(file_name):
    with open(file_name)as f:
      st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("C:/Users/admin\Desktop/didas/style/style.css.txt")
#-----load assets----
lottie_coding=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_1LhsaB.json")
img_contact_form=Image.open("C:/Users/admin/Desktop/didas/images/didaimg2.png")
img_lottie_animation=Image.open("C:/Users/admin/Desktop/didas/images/prisca2.png")
img_contact_ibra=Image.open("C:/Users/admin/Desktop/didas/images/ibrah2.png")
img_lottie_amon=Image.open("C:/Users/admin/Desktop/didas/images/amon1.png")
img_lottie_christina=Image.open("C:/Users/admin/Desktop/didas/images/christina.png")


st.subheader("Hi WELCOME TO DREAMFAR Group :wave:")
st.title("DREAMFAR GROUP FOR BEST FUTURE DREAMS")
icon=["display","home"]
st.write("This is the group of five people that has been established on 2022 as the result of seeking the right ways to archieves dreams particularly in transforming a society to become digital society,we are conducting diffrent projects in Tanzania and abroad")
st.write("[learn more>](https://twitter.com/dreamfargroup)")

#------purpose-----

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
          st.header("WHAT DREAMFAR GROUP OFFER YOU")
          st.write("##")
          st.write(
              """
              In our group we offer you the following:
              (1)Low cost web development.
              (2)Low cost software application development.
              (3)Project designing and implimentation(Artificial Intelligence).
              (4)Research and project development (Artificial Intelligence).
              (5)Data analysis and problems simulations.
              If you will be interested to work with us, we assures you great perfomance in archieving your goals
              """
    
          )
          st.write("[Our official whatsapp link :calling:>](https://chat.whatsapp.com/ITE4Fh3XhctIG3To6m6Xzb)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")



#---------project------
with st.container():
    st.write("---")
    st.header("Upcoming Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
             st.image(img_contact_form)
    with text_column:
             st.subheader("Website and software application development")
             st.write(
                 """
                 Currently we are going to impliment web and app development in several sectors both government and private sectors,
                 if you will be interested to work with us please check our official whatapp link above.

                 {Didasi Frimin, a Founder and CEO Dreamfar Group}
                 """
             )
             st.markdown("[click here..](https://twitter.com/Didasfrimin)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Researches and Projects(Renewable Energy)")
        st.write(
            """We are also doing researches and projects on Renewable energies with high diversity of Artificial Intelligence,
            if you will be interested to work with us please check our official whatapp link above.

            {Prisca Paul, a Renewable Expert Dreamfar Group}
            """
        )
        st.markdown("[click here..](https://twitter.com/maziku_prisca)")


with st.container():
    #st.write("---")
    #st.header("Upcoming Projects")
    #st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_ibra)      
    with text_column:
        st.subheader("Data Analysis and Problem Simulations :bookmark:")
        st.write(
             """
             We are also dealing with the data analysis and problem simulations in several sectors both government and private sectors,
             if you will be interested to work with us please check our official whatapp link above.

             {Ibrahimu Poul, Physicist and manager Dreamfar Group}
             """
        )
        st.markdown("[click here..](https://twitter.com/ibra_ibrahims)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_amon)
    with text_column:
        st.subheader("Researches and Projects(NRM Pysics)")
        st.write(
            """
            Researches and Projects development in Nuclear radiation and medical physics from low levels to high levels,
            if you will be interested to work with us please check our official whatapp link above.

            {Amon Sylidion, Medical Physicists Dreamfar Group}
            """
        )
        st.markdown("[click here..](https://instagram.com/amon_sylidion?igshid=ZDdkNTZiNTM=)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_christina)
    with text_column:
        st.subheader("Management and Consultancy")
        st.write(
            """
            Researches/Projects management and consultancy in all levels,
            if you will be interested to work with us please check our official whatapp link above.

            {Christina Zephania, Lawyer and marketing manager Dreamfar Group}
            """
        )
        st.markdown("[click here..](https://chat.whatsapp.com/ITE4Fh3XhctIG3To6m6Xzb)")

#--------to be modified above=---------------

with st.container():
    st.write("---")
    st.header("Share your view with Dreamfar group")
    st.write("##")

    #----documentation-------
    contact_form="""
    <form action="https://formsubmit.co/dreamfargroup@gmail.com" method="POST">
      <input type="hidden" name = "_captcha" value="false">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Comment here" required></textarea>
      <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
      st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()




    
    


         



          
