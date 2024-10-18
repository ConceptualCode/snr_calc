import numpy as np
from scipy.io import wavfile
import os

def generate_silent_audio(filename='silent_audio.wav', sample_rate=8000, duration=2, output_dir='tests'):
    """
    Generates a silent audio file with the specified parameters.

    Args:
        filename (str): The name of the output WAV file (default: 'silent_audio.wav').
        sample_rate (int): The sample rate of the audio (default: 8000 Hz).
        duration (int): Duration of the silent audio in seconds (default: 2 seconds).
        output_dir (str): Directory where the file will be saved (default: 'tests').

    Returns:
        str: The path to the generated silent audio file.
    """
    os.makedirs(output_dir, exist_ok=True)

    num_samples = sample_rate * duration

    # Generate silent audio data
    silent_audio = np.zeros(num_samples, dtype=np.float32)

    file_path = os.path.join(output_dir, filename)

    wavfile.write(file_path, sample_rate, silent_audio)

    print(f"Silent audio file generated: {file_path}")
    return file_path

if __name__ == '__main__':
    
    generate_silent_audio(filename='silent_audio2.wav', sample_rate=8000, duration=2, output_dir='tests')
