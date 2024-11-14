import speech_recognition as sr
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

def transcribe_audio(audio_file):
    """Transcribe speech from an audio file."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        transcription = recognizer.recognize_google(audio_data)
        print(f"Transcription: {transcription}")
        return transcription
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
        return ""


def analyze_speech(transcription):
    """Analyze the transcription for speech rate and mispronunciations."""
    # Calculate speech rate (words per minute)
    words = nltk.word_tokenize(transcription)
    num_words = len(words)
    wpm = (num_words / 5) * 60
    print(f"Speech Rate: {wpm:.2f} words per minute")

    # Placeholder for mispronounced words analysis
    expected_words = ["car", "ball", "apple", "star"]
    mispronounced_words = [
        word for word in expected_words if word.lower() not in transcription.lower()
    ]
    print(f"Mispronounced Words: {', '.join(mispronounced_words)}")

    analysis_results = {"speech_rate": wpm, "mispronounced_words": mispronounced_words}

    return analysis_results
