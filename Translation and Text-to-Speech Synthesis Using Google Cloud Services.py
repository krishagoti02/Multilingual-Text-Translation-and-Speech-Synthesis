
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech_v1 as texttospeech
from google.oauth2 import service_account

# Function to retrieve language codes
def get_language_codes():
    """
    Retrieve a list of language codes supported by the translation service.

    :return: A list of language codes.
    :rtype: list[str]
    """
    # Load the credentials from the service account file
    credentials = service_account.Credentials.from_service_account_file('*****.json') #write your own
    # Create a Translate client with the loaded credentials
    translate_client = translate.Client(credentials=credentials)
    # Retrieve the list of supported languages from the translation service
    languages = translate_client.get_languages()
    # Extract the language codes from the language list
    language_codes = [lang['language'] for lang in languages]
    # Return the list of language codes
    return language_codes

# Function to translate text
def translate_text(text, target_language):
    """Translate the given text to the target language.

    :param text: The text to be translated.
    :type text: str
    :param target_language: The language code of the target language.
    :type target_language: str
    :return: The translated text.
    :rtype: str
    """
    # 
    credentials = service_account.Credentials.from_service_account_file('*****.json') #write your own
    translate_client = translate.Client(credentials=credentials)
    translation = translate_client.translate(text, target_language=target_language)
    translated_text = translation['translatedText']
    return translated_text

# Function to retrieve available voice types for a language
def get_voice_for_language(language_code):
    """Retrieve available voice types for the specified language.

    :param language_code: The language code of the target language.
    :type language_code: str
    :return: A list of available voice types.
    :rtype: list[str]
    """
    # Load the credentials from the service account file
    credentials = service_account.Credentials.from_service_account_file('*****.json') #write your own
    # Create a TextToSpeech client with the loaded credentials
    text_to_speech_client = texttospeech.TextToSpeechClient(credentials=credentials)
    # Convert the language code to lowercase
    language_code = language_code.lower()
    # Retrieve the available voices for the specified language
    voices = text_to_speech_client.list_voices(language_code=language_code).voices
    # Extract the voice names from the voice list
    voice_types = [voice.name for voice in voices]
    # Return the list of available voice types
    return voice_types

# Function to synthesize speech from translated text
def synthesize_speech(text, language_code, voice_type, tts_key_file, output_file, speech_rate=0.75, volume_gain_db=-96.0):
    """
    Synthesize speech from the provided text using the specified language, voice type, and output file.

    :param text: The text to synthesize into speech.
    :type text: str
    :param language_code: The language code of the text.
    :type language_code: str
    :param voice_type: The voice type to use for the synthesized speech.
    :type voice_type: str
    :param tts_key_file: The file path to the text-to-speech service account key file.
    :type tts_key_file: str
    :param output_file: The file path to save the synthesized speech audio.
    :type output_file: str
    :param speech_rate: The speech rate to adjust the speed of the speech (default is 0.75).
    :type speech_rate: float
    :param volume_gain_db: The volume gain in decibels to adjust the volume level (default is 0.0).
    :type volume_gain_db: float
    """
    # Load the credentials from the service account file
    credentials = service_account.Credentials.from_service_account_file(tts_key_file)
    # Create a TextToSpeech client with the loaded credentials
    text_to_speech_client = texttospeech.TextToSpeechClient(credentials=credentials)
    # Create a synthesis input from the provided text
    synthesis_input = texttospeech.SynthesisInput(text=text)
    # Create a voice selection specifying the language code and voice type
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_type
    )
    # Configure the audio settings for the synthesized speech
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speech_rate,  # Adjust the speech rate
        volume_gain_db=volume_gain_db  # Adjust the volume level
    )

    # Synthesize speech with the provided input, voice, and audio settings
    response = text_to_speech_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the synthesized speech audio to the output file
    with open(output_file, 'wb') as f:
        f.write(response.audio_content)

    # Print the confirmation message
    print(f"Audio file saved as {output_file}")

def main():
    """
    Perform translation and text-to-speech synthesis based on user input.

    User will be prompted to choose input language, output language,
    text to be translated, and the voice type for text-to-speech synthesis.
    """
    # Retrieving available language codes
    language_codes = get_language_codes()
    
    print("Available language codes:")
    print(language_codes)

    # Prompt user to choose input language
    input_language = input("Enter the language code for the input text: ").strip()
    if input_language not in language_codes:
        print("Invalid input language code. Please choose from the available language codes.")
        return

    # Prompt user to choose output language
    output_language = input("Enter the language code for the output translation: ").strip()
    if output_language not in language_codes:
        print("Invalid output language code. Please choose from the available language codes.")
        return
    
      # Retrieving available voice types for the output language
    voice_types = get_voice_for_language(output_language)

    print("Available voice types for the output language:")
    print(voice_types)

    # Prompt user to choose the voice type
    voice_type = input("Enter the voice type for text-to-speech synthesis: ").strip()
    if voice_type not in voice_types:
        print("Invalid voice type. Please choose from the available voice types.")
        return

    # Prompt user to enter the text to be translated
    text = input("Enter the text to be translated: ").strip()
    if not text:
        print("Text cannot be empty.")
        return

    # Translating the text to the output language
    translated_text = translate_text(text, output_language)
    # Print the translated text
    print("Translated text:", translated_text)


    # Translation API key and TTS key file
    translation_api_key = '****' #write your own
    tts_key_file = '*****.json' #write your own
    # Define the output file name based on the voice type
    output_file = f"{voice_type}-translate.mp3"

    # Synthesizing speech from the translated text
    synthesize_speech(translated_text, output_language, voice_type, tts_key_file, output_file)

if __name__ == '__main__':
    main()
