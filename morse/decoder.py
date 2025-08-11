import wave, numpy as np
from .const import UNIT
from .table import morse_code_dict

def sound_to_text(file):
    # Read the wav file
    with wave.open(file, 'rb') as wf:
        fr = wf.getframerate()
        nframes = wf.getnframes()
        nchannels = wf.getnchannels()
        sw = wf.getsampwidth()
        raw = wf.readframes(nframes)

    if sw != 2:
        raise ValueError("Expected 16-bit WAV.")

    # Convert to mono
    audio = np.frombuffer(raw, dtype=np.int16)
    if nchannels == 2:
        audio = audio.reshape(-1, 2).mean(axis=1).astype(np.int16)

    # Normalize and get amplitude
    audio = np.abs(audio.astype(np.float32) / 32768.0)

    # Smooth envelope (5 ms)
    win = max(1, int(0.005 * fr))
    env = np.convolve(audio, np.ones(win)/win, mode='same')

    # Threshold to decide tone vs silence
    threshold = 0.2 * np.max(env)
    tone_mask = env > threshold

    # Group consecutive samples into runs
    runs = []
    current = tone_mask[0]
    count = 0
    for val in tone_mask:
        if val == current:
            count += 1
        else:
            runs.append((current, count))
            current = val
            count = 1
    runs.append((current, count))

    # Convert runs to morse symbols based on UNIT timing
    morse = ''
    for is_tone, count in runs:
        seconds = count / fr
        units = round(seconds / UNIT)

        if is_tone:
            if units <= 1:
                morse += '.'
            else:
                morse += '-'
        else:
            if units >= 6:
                morse += ' / '     # word gap
            elif units >= 2:
                morse += ' '       # letter gap
            else:
                pass               # symbol gap

    # Decode Morse to text
    rev_dict = {v: k for k, v in morse_code_dict.items() if k != ' '}
    decoded_words = []
    for word in morse.split(' / '):
        letters = word.strip().split(' ')
        decoded_words.append(''.join(rev_dict.get(l, '') for l in letters))

    decoded_text = ' '.join(decoded_words)
    print("Decoded Morse:", morse)
    print("Decoded Text :", decoded_text)
    return decoded_text