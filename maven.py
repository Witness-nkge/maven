import streamlit as st
from PIL import Image

image = Image.open('maven_logo_2.png')

st.image(image)
st.title('Maven')
st.write('''Maven is a tech company mostly focusing in solving socio-economic challenges with the use
of technology and innovating in technology''')
st.write('''Currently at Maven we are only developing software apps under Software Mavens but as time
goes on we are aiming on doing more and more in technology''')
st.subheader('Softwares')
st.write('Our latest app is Pantonmath')
st.write('pantonmath is an android question and answers application.\nOur aim in this application is to assist learners in answering comprehension questions.')
st.subheader('Contact us')
st.write('email address: mavenm113@gmail.com')
st.write('mobile no: +27 79 395 5045')
st.write('facebook: @WMaven')
st.write('location : Koffiekraal, 2848')
