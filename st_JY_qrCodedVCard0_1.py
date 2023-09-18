import streamlit as st
import streamlit as st
from segno import helpers

import base64
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

import segno  # Ver0_1 (7/28/2023)

from streamlit_option_menu import option_menu  # Ver0_1 (9/11/2023)

# from urlib.request import urlopen  # To delete 7/29/2023


# # # # venv: stvenv # # #

# st_JY_qrCodeGenVCard0_1.py - Ver0_1 (9/11, 7/28/2023)
# TO DO:
# (1) Add multiple pages
# (2) Add color options;
# (3) Upload a dictionary that contains all the contact info for eady upload; 
# (4) Add animation options;
# (5) Deploy to heroku or streamlit server;

# - Features:
# (1) Added st.text_input in a side pandel;
# ()


# -----------------------------------------------------------------------------------------------------------------
# st_JY_qrCodeGenVCard0.py - Ver0 (7/27/2023)
# C:\Users\email\OneDrive\DesktopSP7\JY_pyTools\QRcodeGeneratorVCard\st_JY_qrCodeGenVCard0.py
# (1) Generate a QR code in a vCard format per input of contact information
# Therefore, when the QR code is read by a mobile phone camera, the contact info from the QR code
# can be saved into the contact list on the phone.
# https://segno.readthedocs.io/en/latest/contact-information.html

# - Display a svg file in streamlit app
# https://discuss.streamlit.io/t/display-svg/172/4

CODE_TITLE='st_JY_qrCodedVCard0_1.py'
CODE_VER='v 0.1'

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

jyvc={
    'name': 'John Yoon',
    'displayname': 'John Yoon, Ph.D.',
    'email': 'drjyoon@gmail.com',
    'city': 'Tucson',
    'region': 'Arizona',
    'org': 'Rayem',
    'title': 'Founder/President',
    'cellphone': '520-481-3439',
    'url': 'www.rayem.com',
}

defaultVCard={
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

defaultVCard = jyvc
st.markdown(defaultVCard)

# ------------ END OF INPUT CONSTANTS -------------

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

menuOptions=['Home','Colored VCard','Animated VCard']

if __name__ == "__main__":
    st.title(CODE_TITLE)
    st.caption(CODE_VER)
    # ------------------------------------------------------------------------------------------------------
    # SIDEBAR: DISPLAY CODE TITLE
    my_sidebar_expander00=st.sidebar.expander('Code Title:',expanded=False)
    with my_sidebar_expander00:
        st.write(CODE_TITLE)
    # ------------------------------------------------------------------------------------------------------

    with st.sidebar.expander('Inputs',expanded=True):
        displayname_input=st.text_input('Display Name',value=defaultVCard['displayname'], placeholder='John Doe')
        name_input=st.text_input('Name',placeholder='John Doe')
        email_input=st.text_input('Email',placeholder='JohnDoe@test.test')
        city_input=st.text_input('City',placeholder='Los Angeles')
        region_input=st.text_input('Region',placeholder='California')
        org_input=st.text_input('Company',placeholder='TBD')
        title_input=st.text_input('Job Title',placeholder='TBD')
        cellphone_input=st.text_input('Cell Phone Number',placeholder='000-000-0000')
        url_input=st.text_input('URL',placeholder='www.google.com')


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


    caption_label=st.text_input('Caption Info:', placeholder='Personal or Business')

    if st.button('Clear'):
        pass

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
            # qrcode.designator

            # # Some params accept multiple values, like email, phone, url
            # qrcode = helpers.make_vcard(name='Doe;John', displayname='John Doe',
            #                             email=('me@example.org', 'another@example.org'),
            #                             url=['http://www.example.org', 'https://example.org/~joe'])

            if menu_page == 'Home':
                # Create and save a QR code
                qrcode.save(vcard_img, scale=4)
                # qrcode.save(vcard_img_color, dark='darkred',light='lightblue')
                qrcode.save(vcard_img_color, scale=4, 
                            # dark='navy',
                            dark=(8,90,117),
                            # data_dark='darkorange',
                            # data_light='yellow',
                            )

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

            elif menu_page == 'Colored VCard':
                # color=st.color_picker('Pick color', value=vcard_img_color,
                #                       key='colors_colorpicker0')
                c1,c2,c3=st.columns(3)
                with c2:
                    # # Display of colorful QR Code
                    # st.markdown("""___""")
                    for i in range(7):
                        st.markdown('')
            
                    # https://segno.readthedocs.io/en/latest/serializers.html
                    st.subheader(displayname_input)
                    st.caption(caption_label)
                    line_string_color=display_svg(vcard_img_color)
                    render_svg(line_string_color)

            elif menu_page == 'Animated VCard':
                # # Animation - Ver0_1 (7/29/2023)
                qrcode_anim=helpers.make_vcard_data(name=name_input,
                            displayname=displayname_input,
                            email=email_input,
                            city=city_input,
                            region=region_input,
                            org=org_input,
                            title=title_input,
                            cellphone=cellphone_input
                            )
                qrcode1=segno.make(qrcode_anim, error='H')

                url = 'https://media.giphy.com/media/HNo1tVKdFaoco/giphy.gif'
                # ----------------------- END OF ANIMATION - VER0_1 (7/29/2023) ---------------------

            for i in range(14):
                st.markdown('')       
        # ---------------------------------- END OF st.form('vCard in QR Code) ----------------------------------------

    for i in range(10):
        st.sidebar.markdown('')
        st.markdown('')
    # # COLOR URL

# ############################ END OF MAIN ###############################