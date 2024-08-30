import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to process user voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        chat_box.insert(tk.END, f"You: {text}\n")
        process_response(text)
    except sr.UnknownValueError:
        speak_text("Sorry, I did not understand that.")
        status_label.config(text="Listening failed. Try again.")

# Function to generate bot response
def process_response(text):
    # Example response logic
    if "hello" in text.lower():
        response = "Hello! How can I help you today?"
    else:
        response = "Sorry, I can't answer that yet."
    
    speak_text(response)
    chat_box.insert(tk.END, f"Bot: {response}\n")
    status_label.config(text="")

# GUI Setup
app = tk.Tk()
app.title("Voice Chatbot")

chat_frame = tk.Frame(app)
chat_box = tk.Text(chat_frame, wrap=tk.WORD, bg="light yellow")
chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)
chat_frame.pack(pady=10, padx=10)

status_label = tk.Label(app, text="Click 'Start' to speak", fg="blue")
status_label.pack()

start_button = tk.Button(app, text="Start", command=recognize_speech)
start_button.pack()

app.geometry("400x400")
app.mainloop()
