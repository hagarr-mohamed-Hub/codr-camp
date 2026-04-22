import streamlit as st
st.write("Every Piece tells a story, Find yours")
st.set_page_config(
    page_title='Soهايلة For Handmade Crafts'
)
home_page= st.Page(
    page='home.py',
    title='Soهايلة Gallery',
    default=True
)
shop_page= st.Page(
    page='shop.py',
    title='Shop Now',
)
custom_page= st.Page(
    page='custom.py',
    title='Custom Orders',
   )

signin_page= st.Page(
    page='signin.py',
    title='Sign In',
)
signup_page= st.Page(
    page='signup.py',
    title='Sign Up',
)
menu_page= st.Page(
    page='menu.py',
    title='Discover Your Pieces',
)
chatbot_page= st.Page(
    page='chatbot.py',
    title='Talk With AI',
)
contact_page= st.Page(
    page='contact.py',
    title='Contact Us',
)
all_pages=st.navigation(
    pages=[home_page, shop_page, custom_page, signin_page, signup_page, 
    menu_page, chatbot_page, contact_page],
    position='top'
)
all_pages.run()