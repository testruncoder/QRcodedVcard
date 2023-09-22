import streamlit as st
import base64


# st_JY_qrCodedVCard0_2_util.py - Ver0_2 (9/22/2023)
# - Utility functions for 'QR Coded VCard" app
# --> st_JY_qrCodedVCard0_2.py;

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>'%b64
    st.write(html, unsafe_allow_html=True)
# ########################## END OF render_svg() #############################

def display_svg(vcard_img_svg):
    f=open(vcard_img_svg,'r')
    lines=f.readlines()
    line_string="".join(lines)
    return line_string
# ########################## END OF display_svg() #############################
