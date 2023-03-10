from scipy.io import wavfile
import numpy as np
import argparse

RATE = 44100

def note(freq, len, volume=1.0, rate=RATE):
    t = np.linspace(0,len,len*rate)
    amplitude = np.iinfo(np.int16).max * volume
    data = np.sin(2*np.pi*freq*t) * amplitude
    return data.astype(np.int16) # two byte integers

def combine_notes(notes):
    combined = np.stack(notes, axis=0)
    combined = np.sum(notes, axis=0) * (1 / len(notes))
    return combined.astype(np.int16)

def encode_as_sound(binary, freq, duration):
    sounds = []
    for digit in binary:
        if digit == '0':
            sounds.append(note(freq, duration, 0.0))
        elif digit == '1':
            sounds.append(note(freq, duration, 1.0))
        else:
            raise ValueError('Script can only encode binary digits')
    data = np.concatenate(sounds)
    wavfile.write('data.wav',RATE,data) # writing the sound to a file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encodes binary string as sound file. Writes out to data.wav')
    parser.add_argument('binary', type=str, help='Binary string. Ex: 1101')
    parser.add_argument('--freq', type=int, default=100, help='Tone frequency. Defaults to 100 Hz.')
    parser.add_argument('--duration', type=int, default=1, help='Duration for each digit in seconds. Defaults to 1.')
    args = parser.parse_args()

    encode_as_sound(args.binary, args.freq, args.duration)