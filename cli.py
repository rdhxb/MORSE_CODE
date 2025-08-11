from morse.encoder import text_to_morse, morse_to_sound, save_morse_to_wav
from morse.decoder import sound_to_text

while True:
    print('What do you want to do:')
    print('1. Encode ')
    print('2. Decode ')
    print('3. Quit')
    q = input('~ >  ').strip()
    print('')

    match q:
        case '1':
            text = input('Enter text to encode: ')
            morse_str = text_to_morse(text)

            play = input('Play sound? (y/n) ').strip().lower()
            if play == 'y':
                morse_to_sound(morse_str)

            save = input('Save to wav? (y/n) ').strip().lower()
            if save == 'y':
                filename = input('Enter filename (without extension): ').strip()
                save_morse_to_wav(morse_str, filename if filename else 'morse')

        case '2':
            path = input('Enter path to wav file: morse_code_wav/').strip()

            try:
                sound_to_text(f'morse_code_wav/{path}')
            except:
                print('File does not exist try again!\n')

        case '3':
            print('Goodbye!')
            break

        case _:
            print('Invalid choice, try again.\n')
