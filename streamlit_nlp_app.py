import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="NLP Application", page_icon="🙉")
st.markdown(
    """
    <style>
    .img-container img {
        max-height: 300px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title('NLP Application')
st.header('Natural Language Processing')
st.subheader('Instructions')
st.write('This application provides two functionalities: Sentiment Analysis and Text Translation (English to German). Choose an option from the dropdown, input your text, and see the results.')

option = st.selectbox(
    "Options",
    [
        "Sentiment analysis of text (eng)",
        "Translate text (eng to ger)"
    ],
)

if option == "Sentiment analysis of text (eng)":
    st.markdown('<div class="img-container"><img src="https://editor.analyticsvidhya.com/uploads/98719sentimss.png" alt="Sentiment Analysis" style="width:100%;"></div>', unsafe_allow_html=True)
    text = st.text_area(label="Input text for sentiment analysis")
    if text:
        st.write('Analyzing sentiment...')
        with st.spinner('Please wait...'):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.success('Analysis complete!')
                st.write(answer)
            except Exception as e:
                st.error(f'Error: {e}')

elif option == "Translate text (eng to ger)":
    st.markdown('<div class="img-container"><img src="https://media.istockphoto.com/id/1302292830/vector/uk-and-german-flag-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=GD500or1_rcS9M64FJyCArSxtgE7TXxr4EVIkMdVbWc=" alt="Translation" style="width:100%;"></div>', unsafe_allow_html=True)
    text = st.text_area(label="Input text for translation")
    if text:
        st.write('Translating text...')
        with st.spinner('Please wait...'):
            try:
                translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text)
                st.success('Translation complete!')
                st.write(translation[0]['translation_text'])
            except Exception as e:
                st.error(f'Error: {e}')

st.write('Łukasz Rybak - s15339')
