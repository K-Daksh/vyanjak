from aiortc.contrib.media import MediaPlayer
import platform

def test_audio():
    if platform.system() == "Windows":
        # Replace with your actual microphone name
        audio = MediaPlayer("audio=Microphone Array (AMD Audio Device)", format="dshow")
    else:
        # Modify for your OS if necessary
        audio = MediaPlayer("/dev/audio", format="alsa")

    # Just for testing, loop indefinitely
    while True:
        pass

test_audio()
