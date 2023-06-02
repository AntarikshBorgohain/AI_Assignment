from langdetect import detect_langs

language_names = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bn': 'Bengali',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'fi': 'Finnish',
    'fr': 'French',
    
}

def identify_language(text):
    try:
        languages_identified = detect_langs(text)
        if len(languages_identified) > 0:
            language_code= languages_identified[0].lang
            language_name = language_names.get(language_code)
            return language_name
    except:
        return "Unable to identify language"


text = input("Please enter a sentence in your language: ")
language = identify_language(text)
print(f"The detected language is: {language}")

