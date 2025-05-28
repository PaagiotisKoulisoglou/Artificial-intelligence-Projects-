import sounddevice as sd 
from scipy.io.wavfile import write 
import keyboard
import time 

from dorenv import load_dotenv
load_dotenv()
import os 



from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def record_audio():

    print("Press Enter to start recording...")
    keyboard.wait('enter')
    print("Recording... Press Enter again to Stop.")

    start_time = time.time()
    
    fs = 44100 
    channels = 2 

    recording = sd.rec(int(fs * 300), samplerate,channels=channels)

    keyboard.wait('enter')
    print('Stopping...')
    print()

    sd.stop()

    duration = time() - start_time

    write("output.wav", fs, recording[:int(duration * fs)])

def speech_to_text():

    audio_file=  open("output.wav", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
    )

    return:transcription.text

def transcribe():

    while True:
        record_audio()

        output = speech_to_text()

        print()
        print('Transcription')
        print(output)
        print()



if __name__ ==  "__main__":
    transcribe()
