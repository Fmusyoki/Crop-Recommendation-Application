

from deta import Deta
import streamlit_authenticator as stauth



DETA_KEY = "d0dvvc8t_6cv7wGJdYtxkoxCknJr8F3APtdmvzase"

deta = Deta(DETA_KEY)


#THIS IS HOW TO CREATE/CONNECT A DATABASE

dy  = deta.Base("password")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raise an error"""
    
    return dy.insert({"key": username, "name": name, "password": password})

def fetch_all_users():
    """Returns a dict of all users"""
    res = dy.fetch()
    return res.items




dh = deta.Base("agri")


def insert_data(county,Maize,Bean,wheat,rice,bananas,cabbage,njahi):
    """Returns the report on a successful creation, otherwise raises an error"""
    return dh.put({"key": county, "Maize":Maize, "Bean":Bean, "wheat":wheat, "rice":rice, "bananas":bananas, "cabbage":cabbage, "njahi":njahi})


def fetch_all():
    """Returns a dict of all periods"""
    res = dh.fetch()
    return res.items


def fetch_alls():
    """Returns a dict of all periods"""
    res = dh.fetch()
    return res.items






