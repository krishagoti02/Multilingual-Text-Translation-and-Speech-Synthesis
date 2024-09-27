# Multilingual-Text-Translation-and-Speech-Synthesis

The Multilingual Text Translation and Speech Synthesis system is a Python-based solution that combines Google Cloud Translation and Text-to-Speech services to translate text into multiple languages and convert the translated text into speech. It allows users to choose from various languages and voice types to create personalized audio output.

## Features
- **Language Translation:** Translates text into multiple languages using the Google Cloud Translation API.
- **Text-to-Speech Conversion:** Converts translated text into audio using the Google Cloud Text-to-Speech API.
- **Custom Voice Selection:** Offers various voice types for different languages.
- **Speech Customization:** Adjust speech rate and volume to create the desired audio experience.
- **MP3 Audio Output:** Saves the synthesized speech as an MP3 file.

## Project Workflow
1. **User Input:** Users provide text to be translated and select the target language.
2. **Language Translation:** The input text is translated into the selected target language.
3. **Voice Selection:** Users choose a voice type for speech synthesis based on the language.
4. **Speech Synthesis:** The translated text is converted into audio and saved as an MP3 file.

## Prerequisites
Before running the project, ensure you have the following:

- Python 3.x
- Google Cloud API credentials (service account with access to Translation and Text-to-Speech APIs)
- Required Python packages:
   1. google-cloud-translate
   2. google-cloud-texttospeech

## Steps
1. Input the text to be translated.
2. Choose the target language for translation.
3. Select a voice type for the speech output.
4. The translated text will be converted to speech and saved as an MP3 file.
 ## Results
The system accurately translates text into multiple languages and generates high-quality audio files. Users can adjust the speed and volume of the speech to fit their needs.
