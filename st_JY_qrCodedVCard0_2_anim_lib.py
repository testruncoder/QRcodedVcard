import streamlit as st
import streamlit as st
from segno import helpers

# import base64
# from io import StringIO
import io
import matplotlib.pyplot as plt
import numpy as np

import segno  # Ver0_1 (7/28/2023)

import datetime  # SubVer0_2 (12/04/2023)

from streamlit_option_menu import option_menu  # Ver0_1 (9/11/2023)

from urllib.request import urlopen  # To delete 7/29/2023

from st_JY_qrCodedVCard0_2_util import(
    render_svg,
    display_svg,
)

# # # # venv: stvenv # # #

# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0_2_anim_lib.py - Ver0_2 (12/04, 9/22/2023)
# - Create a standard QR code with animation;
# https://segno.readthedocs.io/en/stable/artistic-qrcodes.html
# - Updates:
# (1) Create an output SVG file name with a time stamp (12/04/2023)

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
# name_input='John Yoon'
# # name_input='Jennie Yoon'
# displayname_input='John Yoon, Ph.D.'
# # displayname_input='Jennie Yoon'
# email_input='drjyoon@gmail.com'
# city_input='Tucson'
# region_input='Arizona'
# org_input='Rayem'
# title_input='Founder/President'
# cellphone_input='520-481-3439'
# cellphone_input='520-730-4695'
# url_input='www.rayem.com'

                        # vcard_img='my-vcard.svg'
                        # vcard_img_color='my-vcard_color.svg'
                        # vcard_anim_gif='my-vcard_anim.gif'
                        # vcard_anim_name='my-vcard_anim'

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

def qrCodedVcard_anim():

    with st.sidebar.expander('Inputs',expanded=True):
        displayname_input=st.text_input('Display Name',value=defaultVCard['displayname'], placeholder='John Doe',
                                        key='displaynameinput_color0')
        name_input=st.text_input('Name',placeholder='John Doe',
                                        key='nameinput_color0')
        email_input=st.text_input('Email',placeholder='JohnDoe@test.test',
                                        key='emailinput_color0')
        city_input=st.text_input('City',placeholder='Los Angeles',
                                 key='cityinput_color0')
        region_input=st.text_input('Region',placeholder='California',
                                   key='regioninput_color0')
        org_input=st.text_input('Company',placeholder='TBD',
                                key='orginput_color0')
        title_input=st.text_input('Job Title',placeholder='TBD',
                                  key='titleinput_color0')
        cellphone_input=st.text_input('Cell Phone Number',placeholder='000-000-0000',
                                      key='cellphoneinput_color0')
        url_input=st.text_input('URL',placeholder='www.google.com',
                                key='urlinput_color0')

    st.info('INSTRUCTION:   \nScroll down in the left side panel and   \nselect an image/gif for animated background')
    contents=st.text_area('Contents for QR Code:', placeholder='TBD',
                        key='titlelabel_txtinput_anim0')
    url=st.text_input('URL Address:', 
                    #   value='https://media.giphy.com/media/mUPQmck5YEisg/giphy.gif',
                      placeholder='https://media.giphy.com/media/mUPQmck5YEisg/giphy.gif',
                    key='captionlabel_txtinput_anim0')
    if url == '':
        url='https://media.giphy.com/media/mUPQmck5YEisg/giphy.gif'
        # st.caption(f'Default url: {url}')
    
    qr_info_mode=st.radio('Select', options=['Contents','url'], index=0,
             key='radio_anim0',
             horizontal=True,
             )
    qr_info=''

    with st.sidebar:
        for i in range(3):
            st.markdown('')
        scale=st.slider('QR scale (Default=10) (no unit)',min_value=1,max_value=20,
                        value=10,step=1,key='scaleslider_anim0',
                        help='Size of a QR Code in pixel (Default = 10)')    

    bckground_img=st.sidebar.file_uploader('Upload an image or gif for background',
                                   type=['gif','png','jpg','jpeg'],
                                   key='bckgroundimg_fileuploader_anim0')
    if bckground_img is not None:
        with st.sidebar.expander('',expanded=True):
            st.subheader('Uploaded Image/Gif:')
            st.markdown('')
            st.image(bckground_img,
                    caption=bckground_img.name)

    with st.form('vCard in QR Code'):
        if st.form_submit_button('Create QR Code'):
            # # Create a name of an output vcard image (i.e., vcard_img) with a time stamp. - SubVer0_2 (12/04/2023) 
            now0=datetime.datetime.now()
            timestamp0=str(now0.strftime('%Y%m%d_%H%M%S'))
            vcard_anim_gif='my-vcard-gif_'+f'{timestamp0}.gif'
            vcard_anim_name='my-vcard-anim_'+f'{timestamp0}'
            # ------------------------------- END OF SubVer0_2 (12/04/2023) ------------------------------------------

            if bckground_img is not None:
                if qr_info_mode=='Contents':
                    qr_info=contents
                elif qr_info_mode=='url':
                    qr_info=url
                qrcode=segno.make(qr_info, error='h')
                bg_file=urlopen(url)
                out=io.BytesIO()  # Resultant QR code is saved in a buffer, not a local drive.
                qrcode.to_artistic(
                                    background=bckground_img.name,
                                    # background='sample_640.gif',
                                    # background='SampleGIFImage_350kbmb.gif',  # https://sample-videos.com/download-sample-gif-image.php
                                    target=vcard_anim_gif,  # Save a QR code on a local drive.
                                    # target=out,
                                    scale=scale,
                                    kind='gif')
                
                c1,c2,c3=st.columns((3,8,1))
                with c2:
                    for i in range(7):
                        st.markdown('')    
                    st.image(vcard_anim_gif)
                    # st.image(out)
            
            else:  # i.e., a background animation image is not available.
                st.warning('Scroll down in the left side panel and   \nselect an image/gif for animated background')
                st.subheader('Dummy Sample QR Code:')
                qrcode=segno.make(vcard_anim_name, error='h')
                bg_file=urlopen(url)
                out=io.BytesIO()  # Resultant QR code is saved in a buffer, not a local drive.
                qrcode.to_artistic(
                                    background=bg_file,
                                    # background='sample_640.gif',
                                    # background='SampleGIFImage_350kbmb.gif',  # https://sample-videos.com/download-sample-gif-image.php
                                    # target=vcard_anim,
                                    target=out,
                                    scale=scale,
                                    kind='gif')
                
                c1,c2,c3=st.columns((3,8,1))
                with c2:
                    for i in range(7):
                        st.markdown('')    
                    # st.image(vcard_anim)
                    st.image(out)
            
            for i in range(14):
                st.markdown('')  

            st.info(f'INSTRUCTION:   \nSaved a QR Code as "{vcard_anim_gif}"')
        # ---------------------------------- END OF st.form('vCard in QR Code) ----------------------------------------
    
    if st.button('Clear',key='clearbtn_anim0'):
        pass

    for i in range(10):
        st.sidebar.markdown('')
        st.markdown('')

# ############################ END OF MAIN ###############################
