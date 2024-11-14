# TinyTalk: Proof of Concept
This is a proof of concept (demo) for TinyTalk. It is a simple chat application that allows user to record a 5 second audio of them pronouncing certian words, and then transcribe the audio to text, as well as assess the user's pronunciation, using [Azure Cognitive Services])(https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview).

## Installation
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Copy `config.yaml.example` to `config.yaml` and fill in the API keys
4. Run the application using `python main.py`