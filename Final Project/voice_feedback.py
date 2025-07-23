# import pyttsx3
# import threading

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)

# def speak_emotion(emotion):
#     def run():
#         engine.say(f"You look {emotion}")
#         engine.runAndWait()
#     threading.Thread(target=run).start()


# import pyttsx3
# import threading

# # Do NOT keep a global engine instance
# def speak_emotion(emotion):
#     def run():
#         try:
#             engine = pyttsx3.init()
#             engine.setProperty('rate', 150)
#             engine.say(f"You look {emotion}")
#             engine.runAndWait()
#         except Exception as e:
#             print(f"[Voice Error] {e}")

#     threading.Thread(target=run, daemon=True).start()

import subprocess

def speak_emotion(emotion):
    try:
        # You can customize voice with -v Alex or -r 150 for speed
        subprocess.Popen(['say', f'You look {emotion}'])
    except Exception as e:
        print(f"[Voice Error] {e}")