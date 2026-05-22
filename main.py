import pyttsx3
import time
import msvcrt  # Windows terminal se ek-ek key capture karne ke liye
import sys

# Voice setup (Ekdum simple)
bot = pyttsx3.init()
bot.setProperty('rate', 160)  # Bolne ki speed

def Bot_speak(text):
    print(f"🤖 bot: {text}")
    bot.say(text)
    bot.runAndWait()

# --- CHOTA TAB TOGGLE LOGIC ---
def get_password_with_tab(prompt_msg):
    print(prompt_msg, end="", flush=True)
    password = ""
    visible = False  # Shuruat me hidden (*) rahega

    while True:
        ch = msvcrt.getch()  # Key press pakdo screen par dikhane se pehle
        
        # A. ENTER KEY (Windows me b'\r')
        if ch == b'\r' or ch == b'\n':
            print()
            break
            
        # B. TAB KEY (Show/Hide Toggle)
        elif ch == b'\t': 
            visible = not visible  # Status ulti kar do
            # Line saaf karke naye status ke hisab se text ya * dikhao
            sys.stdout.write('\r' + ' ' * (len(prompt_msg) + len(password) + 5) + '\r' + prompt_msg)
            sys.stdout.write(password if visible else '*' * len(password))
            sys.stdout.flush()

        # C. BACKSPACE KEY (Mitane... ke liye)
        elif ch == b'\x08': 
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
                
        # D. NORMAL TYPING
        else:
            try:
                decoded = ch.decode('utf-8')
                if len(decoded) == 1 and ord(decoded) >= 32:
                    password += decoded
                    sys.stdout.write(decoded if visible else '*')
                    sys.stdout.flush()
            except:
                pass
    return password
# ------------------------------

# Main Game Loop
wrong_attempts = 0

Bot_speak("LOL... System is locked HEHE... Enter the master password, boss.")

while True:
    # Tumhari purani input line ki jagah ab humara custom TAB function chalega
    password = get_password_with_tab("\n... Password [Press TAB to Show/Hide]: ")

    # Case 1: Sahi Password
    if password == "shubham11":
        Bot_speak("Access Granted! Welcome back, Commander Shubham. All systems are online.")
        break

    # Case 2: Agar user ne apna naam 'Tony Stark' dala
    elif password.lower() == "tony stark":
        Bot_speak("Sir? You are not Mr. Stark. You don't even have an Iron Man suit. Try again!")

    # Case 3: Agar user ne kuch nahi dala, bas enter daal diya...
    elif password == "":
        Bot_speak("Are you sleeping? Please type something!")

    # Case 4: Galat Password (With Funny Warning Counts)
    else:
        wrong_attempts += 1
        
        if wrong_attempts == 1:
            Bot_speak("Wrong password! Bro, who are you? Tell me your real identity.")
        elif wrong_attempts == 2:
            Bot_speak("Access Denied again! Keep trying, but I am watching you.")
        elif wrong_attempts == 3:
            Bot_speak("System hacked! Security breach! Self destructing in 5... 4... 3...")
            time.sleep(1)
            Bot_speak("Just kidding. But you are blocked. Bye!")
            break