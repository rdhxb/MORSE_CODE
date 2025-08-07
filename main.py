from pygame import mixer
import time
# program will change the text into morse code 
# and then decode it back to the original text

# Space between symbols: The space between dots and dashes within a single letter is equal to one dot. 
# Space between letters: The space between letters within a word is equal to three dots (or one dash). 
# Space between words: The space between words is equal to seven dots (or a little more than two dashes). 

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}




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
            time.sleep(0.2) # dot 1 time unit
            sound.stop()
        if char == '-':
            sound.play()
            time.sleep(0.6) #  dash 3 times units
            sound.stop()
        if char == '/':
            time.sleep(1.4) # space beetwen words 7 time units
        if char == ' ':
            time.sleep(0.6) # space beetwen letters 3 units 
        else:
            time.sleep(0.2) #space between dots and dashes 1 time unit



text = str(input('Enter some text > '))
morse_to_sound(text_to_morse(text))