import streamlit as st
from gtts import gTTS

# Language options supported by gTTS
LANGUAGE_CODES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
}

def text_to_speech(text, language='en', filename='output.mp3'):
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        # Save the audio file
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit UI
st.title("Text-to-Speech Converter")
st.markdown("### Enter text below, and convert it to speech!")

# Text input
user_text = st.text_area("Enter your text:", "")

# Language selection
language = st.selectbox("Choose language:", list(LANGUAGE_CODES.keys()))

# Convert button
if st.button("Convert to Speech"):
    if user_text.strip():
        selected_language_code = LANGUAGE_CODES[language]
        output_file = text_to_speech(user_text, language=selected_language_code)
        if output_file:
            st.success(f"Speech generated successfully in {language}!")
            
            # Read the audio file as binary and display in Streamlit
            with open(output_file, "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")  # Play audio directly
    else:
        st.warning("Please enter some text.")
