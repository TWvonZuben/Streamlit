import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle
import sklearn
#from sklearn.ensemble import RandomForestRegressor
from io import BytesIO


st.set_page_config(layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<style>



[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stSidebar"] {
    background-color: #8EA140;
    textColor = "#000000"
}


</style>
""", unsafe_allow_html=True)


language = st.sidebar.radio('', ['English :flag-us:', 'Português :flag-br:'])
if language == 'English :flag-us:':
    
    st.sidebar.title('**Options**')
    
    pageselected = st.sidebar.selectbox('', ['Home','Potentials prediction'])
    
    
    # Initialize session state variables
    if 'selected_elements' not in st.session_state:
        st.session_state.selected_elements = []
    if 'selected_material' not in st.session_state:
        st.session_state.selected_material = []
    
    if 'sel_material' not in st.session_state:
        st.session_state.sel_material = []
    if 'sel_material' not in st.session_state:
        st.session_state.sel_material = []
    
    
    if 'sel_El_conc' not in st.session_state:
        st.session_state.sel_El_conc = []
    if 'sel_pH' not in st.session_state:
        st.session_state.sel_pH = []
    if 'sel_concentration' not in st.session_state:
        st.session_state.sel_concentration = []
    if 'sel_selec_electrolyte' not in st.session_state:
        st.session_state.sel_selec_electrolyte = []
    if 'sel_option_reference' not in st.session_state:
        st.session_state.sel_option_reference = []
    if 'sel_option_analyte' not in st.session_state:
        st.session_state.sel_option_analyte = []
    
    if pageselected == 'Home' :
        st.image("https://github.com/TWvonZuben/Streamlit/blob/main/caper_cover.png?raw=true")
    
        st.header('Welcome to CAPER!', divider='rainbow')
    
        st.subheader("This tool was created to assist electrochemical scientists in predicting the results of the onset and oxidation potential of the electrooxidation of methanol and ethanol reactions. The work is better explained in the article 'Machine Learning Predictions of Onset and Oxidation Potentials for Methanol and Ethanol Electrooxidation: Comprehensive Analysis and Experimental Validation' and is based on Machine Learning models that utilize information from electrochemical reactions and electrode materials obtained from the literature to predict potentials.")
        st.subheader("The periodic table below illustrates the distribution of chemical elements used in working electrodes, as presented in the database that feeds the model. Consequently, we expect better predictions for materials with more information available in the literature and, consequently, in the database. Additionally, it is more probable that the prediction will be more accurate for methanol oxidation, as 70% of the database information is related to this analyte. The RMSE of the models is 0.169 V for oxidation potentials and 0.185 V for onset potentials.")
    
        st.image("https://github.com/TWvonZuben/Streamlit/blob/main/table.png?raw=true", width=1200)
    
        st.subheader("The initiative aims to aid and accelerate the study and discovery of new electrode materials! If you encounter any problems or have any suggestions, please feel free to contact us at thevonzuben@gmail.com :flag-br:")
        st.subheader("The tools are simple and intuitive to use, but for optimal use and to avoid mistakes, please read the instructions provided below.")
    
        st.header('Instructions', divider='rainbow')
    
        st.subheader(":test_tube: To use the tool, first, select the option 'Potential predictions' on the left sidebar. After that, the options 'Reaction Conditions' and 'Working Electrode descrition' will appear.")
        st.subheader(":test_tube: Under 'Reaction Conditions', you must choose the electrolyte used in the reaction and its concentration. Additionally, select the pH of the solution. Choose the analyte you want to oxidize (methanol or ethanol) and its concentration. Finally, select the reference electrode you are using.")
        st.subheader(":test_tube: The Machine Learning model considers separately the material of the working electrode and the material deposited on it. Thus, under 'Working Electrode description', you must choose the chemical elements used in the 'Working Electrode material' and the chemical elements used in the 'Deposited material', selecting the elements from the periodic table.")
        st.subheader(":eyes: If you want to clear all selected elements from the Periodic Table, simply click on 'Reset' in the bottom right corner.")
        st.subheader(":eyes: In the case of Nitrogen (N) and Carbon (C), options to be chosen will appear on the right side after selecting these elements.")
    
        st.subheader(":red[Attention!] If there is any material deposited on the Working Electrode, please complete the 'Deposited material' field with the same information that you provided for the 'Working Electrode material'.")
