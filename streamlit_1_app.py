import streamlit as st
import spacy
from spacy import displacy

import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article


st.title("Named Entity Recognizer")

st.info("I am Sourudra Nag and this is my NLP Assignment.")

st.success("This website analyzes Paragraph or News Article.")

if(st.button("More Info")):
    st.text("The website enables users to input a paragraph or news article and promptly displays the named entities identified by the spaCy model.")


status = st.radio("Select One Option: ", ('Write A Paragraph', 'Enter a URL'))

if (status == 'Write A Paragraph'):
    
    text = st.text_area("Type Your Paragraph Below")

    if(st.button("Process")):
      doc = nlp(text)
      ent_html = displacy.render(doc, style="ent", jupyter=False)
      # Display the entity visualization in the browser:
      st.markdown(ent_html, unsafe_allow_html=True)

    

else:

    url_input = st.text_input("Enter The URL Below:")
    if st.button("Process"):
        article = Article (url_input)
        article.download()
        article.parse()
        doc = nlp(article.text)
        displacy.render(doc, style='ent', jupyter=False)
        st.markdown(displacy.render(doc, style='ent', jupyter=False), unsafe_allow_html=True)


level = st.slider("Rate the website out of 10", 1, 10)
st.text('You have rated this website: {} out of 10'.format(level))
