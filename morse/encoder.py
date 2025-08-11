from pygame import mixer
import time, wave, numpy as np
from .const import UNIT, FREQUENCY, SAMPLE_RATE
from .table import morse_code_dict

def text_to_morse(text):
    morse_code = ''
    for letter in text.upper():
        if letter in morse_code_dict:
            morse_code += morse_code_dict[letter] + ' '
    
    print(morse_code)
    return morse_code



def morse_to_sound(text_to_morse):
    mixer.init()
    sound = mixer.Sound('hz_700.mp3')
        
    for char in text_to_morse:
        if char == '.':
            sound.play()
            time.sleep(UNIT) # dot 1 time unit
            sound.stop()
            time.sleep(UNIT)
        if char == '-':
            sound.play()
            time.sleep(3*UNIT) #  dash 3 times units
            sound.stop()
            time.sleep(UNIT)
        if char == '/':
            time.sleep(6*UNIT) # space beetwen words 7 time units 1 is alrready added in char .-
        if char == ' ':
            time.sleep(2*UNIT) # space beetwen letters 3 units 1 is alrready added in char .-
        else:
            pass


def save_morse_to_wav(morse_code, filename='morse'):
    def tone(duration):
        n = int(duration * SAMPLE_RATE)
        t = np.arange(n) / SAMPLE_RATE
        wave_data = 0.5 * np.sin(2 * np.pi * FREQUENCY * t)
        return np.int16(wave_data * 32767)

    def silence(duration):
        n = int(duration * SAMPLE_RATE)
        return np.zeros(n, dtype = np.int16)
    

    samples = []
    

    for char in morse_code:
        if char == '.':
            samples.append(tone(UNIT))
            samples.append(silence(UNIT))
        elif char == '-':
            samples.append(tone(3*UNIT))
            samples.append(silence(UNIT))
        elif char == ' ':
            samples.append(silence(2*UNIT))
        elif char == '/':
            samples.append(silence(6*UNIT))

    if samples:
        audio = np.concatenate(samples)
    else:
        audio = silence(UNIT)

    with wave.open((f'morse_code_wav/{filename}{len(samples)}.wav'), 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())


    print(f"Saved Morse to morse_code_wav/{filename}{len(samples)}.wav")
