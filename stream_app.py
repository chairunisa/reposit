
import streamlit as st
import pandas as pd

def navBar():
    menu_data = [
        {'id':"Sentimen Analysis", 'icon': "fab fa-chart-bar", 'label': "Sentiment Anlysisis"},
        {'id':"Visualization", 'icon': "fab fa-chart-bar", 'label': "Visualization"},
    ]
    over_theme = {'txc_inactive': '#FFFFFF'}
    menu_id=hc.nav_bar(menu_definition=menu_data, override_theme=over_theme, home_name='Home', first_selected=0)
    return menu_id
        
        
st.set_page_config(page_title='Analysis', layout = "wide")
menu_id = navbar == 'Home':
    st.write('---------------------------')
    st.write('')
    
    



    

