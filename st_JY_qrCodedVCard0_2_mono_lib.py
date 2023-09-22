import streamlit as st
import streamlit as st
from segno import helpers

# import base64
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

import segno  # Ver0_1 (7/28/2023)

from streamlit_option_menu import option_menu  # Ver0_1 (9/11/2023)

# from urlib.request import urlopen  # To delete 7/29/2023

from st_JY_qrCodedVCard0_2_util import(
    render_svg,
    display_svg,
)

# # # # venv: stvenv # # #

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0_2_mono_lib.py - Ver0_2 (9/22/2023)
# - Create a standard QR code in black and white;


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
# (2)


# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0.py - Ver0 (7/27/2023)
# C:\Users\email\OneDrive\DesktopSP7\JY_pyTools\QRcodeGeneratorVCard\st_JY_qrCodeGenVCard0.py
# (1) Generate a QR code in a vCard format per input of contact information
# Therefore, when the QR code is read by a mobile phone camera, the contact info from the QR code
# can be saved into the contact list on the phone.
# https://segno.readthedocs.io/en/latest/contact-information.html

# - Display a svg file in streamlit app
# https://discuss.streamlit.io/t/display-svg/172/4


                        # CODE_TITLE='st_JY_qrCodedVCard0_1.py'
                        # CODE_VER='v 0.1'

# # INPUT CONSTANTS
name_input='John Yoon'
# name_input='Jennie Yoon'
displayname_input='John Yoon, Ph.D.'
# displayname_input='Jennie Yoon'
email_input='drjyoon@gmail.com'
city_input='Tucson'
region_input='Arizona'
org_input='Rayem'
title_input='Founder/President'
cellphone_input='520-481-3439'
cellphone_input='520-730-4695'
url_input='www.rayem.com'

vcard_img='my-vcard.svg'
vcard_img_color='my-vcard_color.svg'

# jyvc={
#     'name': 'John Yoon',
#     'displayname': 'John Yoon, Ph.D.',
#     'email': 'drjyoon@gmail.com',
#     'city': 'Tucson',
#     'region': 'Arizona',
#     'org': 'Rayem',
#     'title': 'Founder/President',
#     'cellphone': '520-481-3439',
#     'url': 'www.rayem.com',
# }

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

# menuOptions=['Home','Colored VCard','Animated VCard']

def qrCodedVcard_mono():

    with st.sidebar.expander('Inputs',expanded=True):
        displayname_input=st.text_input('Display Name',value=defaultVCard['displayname'], placeholder='John Doe',
                                        key='displaynameinput_mono0')
        name_input=st.text_input('Name',placeholder='John Doe',
                                        key='nameinput_mono0')
        email_input=st.text_input('Email',placeholder='JohnDoe@test.test',
                                        key='emailinput_mono0')
        city_input=st.text_input('City',placeholder='Los Angeles',
                                 key='cityinput_mono0')
        region_input=st.text_input('Region',placeholder='California',
                                   key='regioninput_mono0')
        org_input=st.text_input('Company',placeholder='TBD',
                                key='orginput_mono0')
        title_input=st.text_input('Job Title',placeholder='TBD',
                                  key='titleinput_mono0')
        cellphone_input=st.text_input('Cell Phone Number',placeholder='000-000-0000',
                                      key='cellphoneinput_mono0')
        url_input=st.text_input('URL',placeholder='www.google.com',
                                key='urlinput_mono0')

    caption_label=st.text_input('Caption Info:', placeholder='Personal or Business',
                                key='captionlabel_txtinput_mono0')

    with st.sidebar:
        for i in range(3):
            st.markdown('')
        scale=st.slider('QR scale in pixel (Default=4)',min_value=1,max_value=20,
                        value=4,step=1,key='scaleslider_mono0',
                        help='Size of a QR Code in pixel (Default = 4)')

    with st.form('vCard in QR Code'):
        if st.form_submit_button('Create QR Code'):
            qrcode=helpers.make_vcard(name=name_input,
                                    displayname=displayname_input,
                                    email=email_input,
                                    city=city_input,
                                    region=region_input,
                                    org=org_input,
                                    title=title_input,
                                    cellphone=cellphone_input
                                    )

            # # Some params accept multiple values, like email, phone, url
            # qrcode = helpers.make_vcard(name='Doe;John', displayname='John Doe',
            #                             email=('me@example.org', 'another@example.org'),
            #                             url=['http://www.example.org', 'https://example.org/~joe'])

            qrcode.save(vcard_img, scale=scale)  # scale in pixel; You can add: unit='mm' or 'cm'; 
            
            c1,c2,c3=st.columns(3)
            # st.markdown("""___""")
            # st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True) 
            # # https://discuss.streamlit.io/t/horizontal-separator-line/11788/5
            with c2:  
                for i in range(7):
                    st.markdown('')       
                st.subheader(' '+ displayname_input)
                st.caption(caption_label)
                # # Display the generated URL code
                # Code by Rkubinski (12/10/2019)
                # https://gist.github.com/treuille/8b9cbfec270f7cda44c5fc398361b3b1
                line_string=display_svg(vcard_img)
                render_svg(line_string)

            for i in range(14):
                st.markdown('')       
        # ---------------------------------- END OF st.form('vCard in QR Code) ----------------------------------------
    
    if st.button('Clear',key='clearbtn_mono0'):
        pass

    for i in range(10):
        st.sidebar.markdown('')
        st.markdown('')

# ############################ END OF MAIN ###############################