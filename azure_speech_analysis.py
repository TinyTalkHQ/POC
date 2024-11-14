import azure.cognitiveservices.speech as speechsdk

def transcribe_and_assess(audio_file, expected_text, api_keys):
    # Set up speech config
    speech_key = api_keys["azure_speech_key"]
    service_region = api_keys["azure_service_region"]
    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region
    )

    # Set up pronunciation assessment config
    pronunciation_config = speechsdk.PronunciationAssessmentConfig(
        reference_text=expected_text,
        grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
        granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
        enable_miscue=True,
    )

    # Set up audio config
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

    # Create a speech recognizer
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    # Apply the pronunciation assessment config
    pronunciation_config.apply_to(recognizer)

    # Perform recognition and assessment
    result = recognizer.recognize_once()

    # Check the results
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
        # Extract pronunciation assessment results
        pronunciation_result = speechsdk.PronunciationAssessmentResult(result)
        print(f"Pronunciation Score: {pronunciation_result.pronunciation_score}")
        for idx, word in enumerate(pronunciation_result.words):
            print(
                f" > Word: {word.word} - Score: {word.accuracy_score} - Comment: {word.error_type}"
            )
        return pronunciation_result
    else:
        print(f"Speech could not be recognized: {result.reason}")
        return None
