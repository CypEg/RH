# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:28:09 2024

@author: cypri
"""

#%% Importation des librairies
import streamlit as st
import pandas as pd

#%% Importation des données
df = pd.read_csv("courses-info.csv")

#%% Nettoyage des données
col_name = {'title':'Cours', 
            'charge-e-de-gestion-des-ressources-humaines': 'Charge.e de gestion des ressources humaines',
            'manager-rh':'Manager RH',
            'gestionnaire-de-paie':'Gestionnaire de paie',
            'data-architect':'Data architect',
            "developpeur-se-dapplication-python":"Developpeur.se d'application python",
            'developpeur-web-junior':'Developpeur web junior',
            'community-manager':'Community manager',
            'responsable-marketing-operationnel':'Responsable marketing operationnel',
            'developpeur-se-d-application-php-symfony':"Developpeur.se d'application php symfony",
            'data-scientist':'Data scientist',
            'expert-e-en-strategie-marketing-et-communication':'Expert.e en stratégie marketing',
            'data-analyst':'Data analyst',
            'theme':'Theme'}
df = df.rename(col_name, axis = 1)

gestion = df.loc[df["Charge.e de gestion des ressources humaines"] == True,["Cours", 'Theme']]
manager = df.loc[df["Manager RH"] == True,["Cours", 'Theme']]
paie = df.loc[df["Gestionnaire de paie"] == True,["Cours", 'Theme']]
architect = df.loc[df["Data architect"] == True,["Cours", 'Theme']]
dev_python = df.loc[df["Developpeur.se d'application python"] == True,["Cours", 'Theme']]
dev_web = df.loc[df["Developpeur web junior"] == True,["Cours", 'Theme']]
community = df.loc[df["Community manager"] == True,["Cours", 'Theme']]
market = df.loc[df["Responsable marketing operationnel"] == True,["Cours", 'Theme']]
dev_php = df.loc[df["Developpeur.se d'application php symfony"] == True,["Cours", 'Theme']]
scientist = df.loc[df["Data scientist"] == True,["Cours", 'Theme']]
expert = df.loc[df["Expert.e en stratégie marketing"] == True,["Cours", 'Theme']]
analyst = df.loc[df["Data analyst"] == True,["Cours", 'Theme']]


#%% Ajout du titre
st.title("RH & Paie entretien")

#%% Ajout du contenu
st.markdown("<div style='text-align: justify;'>Nombre de cours selon leur thème.</div>", unsafe_allow_html=True)
theme = df['Theme'].value_counts()
st.write(theme)
st.write("Nombre total de cours :", len(df))

st.markdown("<div style='text-align: justify;'>Cours disponible selon l'emploi:</div>", unsafe_allow_html=True)

choix1 = ["Charge.e de gestion des ressources humaines", "Manager RH", "Gestionnaire de paie", "Data architect", "Developpeur.se d'application python",
          "Developpeur web junior",'Community manager', 'Responsable marketing operationnel',"Developpeur.se d'application php symfony",
          'Data scientist', 'Expert.e en stratégie marketing','Data analyst']

option1 = st.selectbox('Emploi', choix1)

if option1 == "Charge.e de gestion des ressources humaines":
    st.write(gestion)
elif option1 == "Manager RH":
    st.write(manager)
elif option1 == "Gestionnaire de paie":
    st.write(paie)    
elif option1 == "Data architect":
    st.write(architect) 
elif option1 == "Developpeur.se d'application python":
    st.write(dev_python)    
elif option1 == "Developpeur web junior":
    st.write(dev_web)        
elif option1 == "Community manager":
    st.write(community)      
elif option1 == "Responsable marketing operationnel":
    st.write(market)   
elif option1 == "Developpeur.se d'application php symfony":
    st.write(dev_php)
elif option1 == "Data scientist":
    st.write(scientist)
elif option1 == "Expert.e en stratégie marketing":
    st.write(expert)
elif option1 == "Data analyst":
    st.write(analyst)    