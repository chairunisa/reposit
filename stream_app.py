import csv
import streamlit as st
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import string
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def main():
    st.title("Analisis Sentimen Aplikasi Peduli Lindungi")

    menu = ["ANALISIS", "ABOUT"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "ANALISIS":
        st.subheader("Dataset")
        df = pd.read_csv("dataset_baruNEW.csv")
        st.write(df)
        st.subheader('Preprocessing Data')
        with st.spinner('Wait text Process in progress.....'):
            with st.expander('Expand for details'):
                st.subheader('Lower Case all review:')
                df['clean_data'] = df['content'].str.lower()
                st.table(df[['content','clean_data']].head(3))

                st.subheader('Tokenizing all review:')
                df['clean_data'] = df['clean_data'].apply(lambda x: nltk.word_tokenize(x))
                st.table(df[['content','clean_data']].head(2))

                st.subheader('Stopwords')
                list_stopwords = stopwords.words('indonesian')
                list_stopwords.extend(["yg","gpp","dg","gua","gw","dgn","ny","nya","klo","kalo",
                                       "tdk","g","ga","gk","gak","krn","gue","sdh","loh","n","utk",
                                        "trs","ya","dl","y","aja","sih","nih","loh","ko","yah","wkwkwk","jgn"])
                list_stopwords = set(list_stopwords)
                def stopwords_removal(text):
                    return [word for word in text if word not in list_stopwords]
                df['clean_data'] = df['clean_data'].apply(stopwords_removal) 
                st.table(df[['content','clean_data']].head(2))

                st.subheader('Stemming')
                def stemming(content):
                    factory = StemmerFactory()
                    stemmer = factory.create_stemmer()
                    content = [stemmer.stem(word) for word in content]
                    return content
                df['clean_data']=df['clean_data'].apply(stemming)
                st.table(df[['content','clean_data']].head(2))

                st.subheader('Remove Angka & Karakter spesial')
                def clean_text(text):
                    text = re.sub('[0-9]+', " ", text)
                    text = text.translate(str.maketrans("","",string.punctuation))
                    text = text.strip()
                    return text
                df['clean_data'] = df['clean_data'].astype("string").apply(clean_text)
                st.table(df[['content','clean_data']].head(3))



        st.subheader('Data after preprocessing text')
        st.dataframe(df[['userName','score','at','clean_data']])

        def convert_df(df):
            return df.to_csv().encode('utf-8')
            
            
        csv = convert_df(df)
        
        st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')


        st.subheader('Pelabelan')

        lexicon_positive= dict()
        with open('lexicon_positive.csv','r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                lexicon_positive[row[0]] = (row[1])
                
        lexicon_negative= dict()
        with open('lexicon_negative.csv','r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                lexicon_negative[row[0]] = (row[1])

        def sentimen(clean_data):
            score = 0
            for word in clean_data:
                if (word in lexicon_positive):
                    score = score+lexicon_positive[word]
            for word in clean_data:
                if ( word in lexicon_negative):
                    score = score+lexicon_negative[word]
            polarity = ''
            if (score>0):
                polarity = 'positif'
            else:
                polarity = 'negatif'
            return score, polarity

        results = df['clean_data'].apply(sentimen)
        results = list(zip(*results))
        df['polarity_score'] = results[0]
        df['polarity'] = results[1]


        st.dataframe(df[['userName','score','at','clean_data','polarity_score','polarity']])









    else:
        st.subheader("ABOUT")   

if __name__ == '__main__':
    main()





    

