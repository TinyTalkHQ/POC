import pyaudio
import wave

def record_audio(filename, duration=5, channels=1, rate=44100, chunk=1024):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    frames = []

    print("🟢 Recording started...")
    for _ in range(int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    print("🔴 Recording finished.")
    print("\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def record_audio_prompt(words_dictionary):
    words_list = "\n".join([f"{item['emoji']} {item['word']}" for item in words_dictionary])
    input(f"\nWords to say:\n\n{words_list}\n\n > Press ENTER to start recording \n")
    filename = 'recorded_sample.wav'
    record_audio(filename, duration=5)
    return filename