"""
A module that provides functions to translate text between English and French
using the IBM Watson Language Translator service.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates the given English text to French using the IBM Watson Language Translator service.

    Args:
        english_text (str): The text in English to translate.

    Returns:
        str: The translated text in French.
    """
    if english_text is None:
        return None
    response = language_translator.translate(english_text, source='en', target='fr').get_result()
    french_text = response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates the given French text to English using the IBM Watson Language Translator service.

    Args:
        french_text (str): The text in French to translate.

    Returns:
        str: The translated text in English.
    """
    if french_text is None:
        return None
    response = language_translator.translate(french_text, source='fr', target='en').get_result()
    english_text = response['translations'][0]['translation']
    return english_text
