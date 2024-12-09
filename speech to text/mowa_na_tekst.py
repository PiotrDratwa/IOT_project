from transformers import pipeline
import sounddevice as sd
import paho.mqtt.client as mqtt
import numpy as np
import torch

# device = torch.device("cpu")

print("Starting application...")

# MQTT Configuration
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 1883
MQTT_TOPIC = 'emqx/esp8266_lab_jk_pd'


# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
    else:
        print(f"Failed to connect, return code {rc}")
    client.subscribe(MQTT_TOPIC)  # Subscribe to the topic (optional if only publishing)


# Whisper ASR model initialization
print("Loading Whisper model...")
whisper_asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")


def record_audio(duration=5, samplerate=16000):
    print(f"Recording audio for {duration} seconds...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.float32)
    sd.wait()  # Wait until recording finishes
    print("Recording complete.")
    return audio.flatten()  # Keep as float32

def transcribe_audio(audio):
    """
    Convert audio to text using the Whisper ASR model.
    """
    print("Transcribing audio...")
    try:
        result = whisper_asr(audio)  # Usuń parametr 'language'
        return result["text"]
    except Exception as e:
        print(f"Error in transcription: {e}")
        return ""


if __name__ == "__main__":
    try:
        # Create MQTT client and assign callbacks
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()  # Run MQTT client in the background

        while True:
            duration = 5  # Duration for each recording
            samplerate = 16000  # Audio sampling rate
            audio_data = record_audio(duration=duration, samplerate=samplerate)
            transcription = transcribe_audio(audio_data)
            client.publish(MQTT_TOPIC, transcription)
            print(f"Transcribed text: {transcription}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Press Ctrl+C to exit...")