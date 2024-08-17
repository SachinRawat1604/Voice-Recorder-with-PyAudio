import pyaudio
import wave
import os

CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def record_audio():
    # Records audio from the default input device for a specified duration.

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames

def play_audio(frames):
    # Plays the recorded audio.

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    print("* Playing")

    for frame in frames:
        stream.write(frame)

    stream.stop_stream()
    stream.close()
    p.terminate()

def save_audio(frames, filename):
    # Saves the recorded audio to a WAV file.

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))  # type: ignore
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    # The main function that provides a menu-driven interface for recording, playing, and saving audio.
    print("Welcome to the Audio Recorder!")
    while True:
        print("1. Record audio")
        print("2. Play audio")
        print("3. Save audio")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            frames = record_audio()
        elif choice == "2":
            play_audio(frames)
        elif choice == "3":
            filename = input("Enter the filename (without extension): ")
            save_audio(frames, f"{filename}.wav")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()