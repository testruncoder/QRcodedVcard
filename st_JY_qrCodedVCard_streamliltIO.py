import streamlit as st
from segno import helpers

import base64
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

import segno  # Ver0_1 (7/28/2023)

from streamlit_option_menu import option_menu  # Ver0_1 (9/11/2023)

# from urlib.request import urlopen  # To delete 7/29/2023

# # Ver0_2 (9/22/2023)
from st_JY_qrCodedVCard0_2_mono_lib import qrCodedVcard_mono
from st_JY_qrCodedVCard0_2_color_lib import qrCodedVcard_color
from st_JY_qrCodedVCard0_2_anim_lib import qrCodedVcard_anim


# st_JY_qrCodedVCard_0_2_streamliltIO.py  - Ver0_2 (12/04, 9/22/2023)
# - Main app code for deployment to streamlit cloud;
# - A version of code that is deployed to streamlit cloud server by commenting out some code lines.
# - Just converted the file name from st_JY_qrCodeGenVCard0_2.py to st_JY_qrCodedVCard_streamliltIO.py
# - Update:
# (1) Create an output SVG file name with a time stamp (12/04/2023)
# => Refer to C:\Users\email\OneDrive\DesktopSP7\JY_pyTools\QRcodedVCard\st_JY_qrCodedVCard0_3.py

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0_1_streamlitIO.py - Ver0_1 (9/22/2023)
# - Note that 'github.com/testruncoder' has been set up with the python file name "st_JY_qrCodeGenVCard0_1.py", though.

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0_2.py - Ver0_2 (9/22/2023)
# - Updates:
# (1) Broke down to multiple libraray files:

# - New:
# (1) st_JY_qrCodedVCard0_2_util.py
# (2) st_JY_qrCodedVCard0_2_mono_lib.py
# (3) st_JY_qrCodedVCard0_2_color_lib.py
# (4) st_JY_qrCodedVCard0_2_anim_lib.py

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0_1.py - Ver0_1 (9/11, 7/28/2023)
# TO DO:
# (1) Add multiple pages
# (2) Add color options;
# (3) Upload a dictionary that contains all the contact info for eady upload; 
# (4) Add animation options;
# (5) Deploy to heroku or streamlit server;

# - Features:
# (1) Added st.text_input in a side pandel;

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0.py - Ver0 (7/27/2023)
# (1) Generate a QR code in a vCard format per input of contact information
# Therefore, when the QR code is read by a mobile phone camera, the contact info from the QR code
# can be saved into the contact list on the phone.
# https://segno.readthedocs.io/en/latest/contact-information.html

# - Display a svg file in streamlit app
# https://discuss.streamlit.io/t/display-svg/172/4


# CODE_TITLE='st_JY_qrCodedVCard0_2.py'
CODE_TITLE='QR Coded VCard'
CODE_VER='v 0.2'

# # INPUT CONSTANTS

vcard_img='my-vcard.svg'
vcard_img_color='my-vcard_color.svg'

defaultVCard0={
    'name': '',
    'displayname': '',
    'email': '',
    'city': '',
    'region': '',
    'org': '',
    'title': '',
    'cellphone': '',
    'url': '',
}

defaultVCard = defaultVCard0
# st.markdown(defaultVCard)

# ------------ END OF INPUT CONSTANTS -------------

# def render_svg(svg):
#     """Renders the given svg string."""
#     b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
#     html = r'<img src="data:image/svg+xml;base64,%s"/>'%b64
#     st.write(html, unsafe_allow_html=True)
# # ########################## END OF render_svg() #############################

# def display_svg(vcard_img_svg):
#     f=open(vcard_img_svg,'r')
#     lines=f.readlines()
#     line_string="".join(lines)
#     return line_string
# # ########################## END OF display_svg() #############################

menuOptions=['Standard','Colored VCard','Animated VCard']

if __name__ == "__main__":
    # Ver0_1 (9/22/2023)
    st.set_page_config(
    page_title='QRCodedVCard',
    # page_icon=icon,
    layout='centered',  # layout='wide',
    initial_sidebar_state='auto',  # 'auto', 'expanded', 'collapsed'
        )
    
    st.title(CODE_TITLE)
    st.caption(CODE_VER)
    # ------------------------------------------------------------------------------------------------------
    # SIDEBAR: DISPLAY CODE TITLE
    my_sidebar_expander00=st.sidebar.expander('Code Title:',expanded=False)
    with my_sidebar_expander00:
        st.write(CODE_TITLE)
    # ------------------------------------------------------------------------------------------------------

    menu_page=option_menu(None, menuOptions,
                          icons=[],
                          orientation='horizontal',
                          styles={
                              'nav-link': {
                                  # 'font-size': '20px',
                                  '--hover-color': '#eee',
                              },
                              'nav-link-selected': {'background-color': 'sky blue'},
                          },
                        )

    if menu_page == 'Standard':
        st.subheader(menu_page)
        qrCodedVcard_mono()
    elif menu_page == 'Colored VCard':
        st.subheader(menu_page)
        qrCodedVcard_color()

    elif menu_page == 'Animated VCard':
        st.subheader(menu_page)
        qrCodedVcard_anim()

    for i in range(10):
        st.sidebar.markdown('')
        st.markdown('')

# ############################ END OF MAIN ###############################
