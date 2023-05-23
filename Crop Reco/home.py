import streamlit as st
import streamlit_authenticator as stauth 
import database as db
import uploadcsv
import analysis
import filter
import crop_reco
from PIL import Image
from deta import Deta

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;  
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)




with st.sidebar.container():
    image = Image.open("C:/Users/charl/Downloads/ANALYSIS-removebg-preview.png")
    if image is not None:
        image = Image.open("C:/Users/charl/Downloads/ANALYSIS-removebg-preview.png")
    new_image = image.resize((350, 250))
    st.image(new_image)
    
    # st.image(image, use_column_width=True)

choice = st.sidebar.selectbox('Login/Signup',['Login','Signup'])

if choice == 'Login':
    users = db.fetch_all_users()
    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]
    credentials = {"usernames":{}}

    for un, name, pw in zip(usernames, names, hashed_passwords):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({un:user_dict})


    authenticator = stauth.Authenticate(credentials, "streamlit-navbar-flaskless", "auth", cookie_expiry_days=30)


    name, authentication_status, username = authenticator.login("Login", "main")


        # st.markdown(hide_bar, unsafe_allow_html=True)
    if authentication_status == None:
        st.warning('Please enter your username and password')
    
    if authentication_status == False:
        st.warning('Please enter your correct username or password')
        

        
        # st.markdown(hide_bar, unsafe_allow_html=True)  
        
    if authentication_status:
        st.sidebar.title("Main Menu 💒" )
        st.sidebar.success(f"Welcome {name}👋")
        
        PAGES = {
            "Upload CSV": uploadcsv,
            "Analysis": analysis,
            "Filter Data":filter,
            "Crop Recommender":crop_reco
        }

        st.sidebar.title('Navigation ')
        selection = st.sidebar.radio("Go To Pages", list(PAGES.keys())
                            
                                    
                                    
                                    )
        page = PAGES[selection]
        page.app()
        
        

        st.sidebar.success("Select a page above.")
        
        
            
        authenticator.logout("Logout", "sidebar")
        



if choice == 'Signup':
    st.subheader("Create An Account")
    new_username= st.text_input('Username', placeholder="Enter Email")
    new_name = st.text_input('Full Name', placeholder="Enter Full Name")
    new_password = st.text_input('Password',type='password', placeholder="Enter Password")
    password = [new_password]
    hashed_passwords = stauth.Hasher(password).generate()
    submit = st.button('Sign Up',"main")
    
    if submit:
        for x in hashed_passwords:
            db.insert_user(new_username,new_name, x)
        st.success('Your account is created successfully')
        st.info("Go To Login Menu To login")
   
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

   
