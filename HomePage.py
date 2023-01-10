import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="IpynbMobileViewer")
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.reportview-container .main footer {visibility: hidden;} 
</style>
"""
#st.markdown(hide_st_style, unsafe_allow_html=True)

st.header(":blue[Juyter/Ipynb Mobile Viewer]")
st.text("This is an android application used to view Jupyter/Ipynb files in mobile")

st.write("[Google Play Link](https://google.com)")

section = '<p style="font-family:sans-serif; color:Red; font-size: 25px;">Steps</p>'
st.markdown(section,unsafe_allow_html=True)

no1 = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">Homepage with 2 Renders, Please select any render and click \'Get Started\'.</p>'
no2 = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">HTML Page will be opened with the selected Render, please select the ipynb file.</p>'
no3 = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">Ipynb File will be rendered and displayed on screen. To Download as \"PDF\" click on the download icon.</p>'
no4 = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">Pdf files will be downloaded to Documents/IpynbViewer. To Customise download click on the options menu and click Customise.</p>'
no5 = '<p style="font-family:sans-serif; color:Green; font-size: 18px;">Customise and click on \"Save as PDF\" and select location for download.</p>'

st.markdown(no1, unsafe_allow_html=True)
st.image("data/11.jpg",channels="BGR")
st.markdown(no2, unsafe_allow_html=True)
st.image("data/22.jpg",channels="BGR")
st.markdown(no3, unsafe_allow_html=True)
st.image("data/33.jpg",channels="BGR")
st.markdown(no4, unsafe_allow_html=True)
st.image("data/4.jpg",channels="BGR")
st.markdown(no5, unsafe_allow_html=True)
st.image("data/55.jpg",channels="BGR")


HtmlFile = open("data/google3f727a4ee007d4cb.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code)


