from audio_recorder import record_audio_prompt
from azure_speech_analysis import transcribe_and_assess
from config_loader import load_config

def main():
    # Load config data
    config = load_config()
    words_dictionary = config["words_dictionary"]
    api_keys = config["api_keys"]

    # Record audio
    audio_file = record_audio_prompt(words_dictionary)

    # Transcribe and assess
    expected_text = " ".join([item["word"] for item in words_dictionary])
    transcribe_and_assess(audio_file, expected_text, api_keys)

if __name__ == "__main__":
    main()
