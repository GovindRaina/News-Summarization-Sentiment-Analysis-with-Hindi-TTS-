from gtts import gTTS
import os

def generate_hindi_audio(text, filename="output.mp3"):
    """
    Converts the given text into Hindi speech and saves it as an audio file.
    """
    if not text.strip():
        return None  # Return None if the text is empty
    
    # Convert text to Hindi speech
    tts = gTTS(text=text, lang='hi')
    
    # Save the audio file
    tts.save(filename)
    
    return filename  # Return the filename for reference

# Example Usage
if __name__ == "__main__":
    sample_text = "टेस्ला की नई इलेक्ट्रिक कार बाजार में बहुत लोकप्रिय हो रही है।"
    audio_file = generate_hindi_audio(sample_text)
    print(f"Audio saved as: {audio_file}")
