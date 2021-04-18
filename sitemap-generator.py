import pandas as pd
import os
import streamlit as st
import base64

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p class="big-font">Simple Sitemap Generator</p>
<b>Directions: </b></ br><ol>
<li>Upload CSV of ScreamingFrog crawl or URL list</li>
<li>CSV must have URLs under a column named 'Address' (Standard in ScreamingFrog)</li>
</ol>
""", unsafe_allow_html=True)

filename = st.text_input('Create Sitemap File Name','ex domain-sitemap')
filename = filename.replace(' ','-')
filename = filename + ".xml"

get_csv = st.file_uploader("Upload CSV File",type=['csv'])

if get_csv is not None:
    df = pd.read_csv(get_csv)

    urls = df['Address'].tolist()

    urllist = "<urlset xsi:schemaLocation='http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'>"

    for i in urls:
      urllist += f"<url><loc>{i}</loc></url>" + "\n"

    urllist += "</urlset>"
    
    def get_xml_download_link(filename):
        with open(filename, 'r') as f:
            xml = f.read()
        b64 = base64.b64encode(xml.encode()).decode()
        return f'<a href="data:file/xml;base64,{b64}" download="{filename}">Download Sitemap XML file</a>'

    open(filename, "w").write(urllist)
    st.write(":sunglasses: Sitemap Generation Successful :sunglasses:")
    st.markdown(get_xml_download_link(filename), unsafe_allow_html=True)
    
    
st.write('Author: [Greg Bernhardt](https://twitter.com/GregBernhardt4) | Friends: [Rocket Clicks](https://www.rocketclicks.com) and [Physics Forums](https://www.physicsforums.com)')
