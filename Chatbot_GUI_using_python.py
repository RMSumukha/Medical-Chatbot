import random
import pyttsx3
from tkinter import *

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[1].id)
import tkinter as tk


def speak(msg):
    engine.say(msg)
    engine.runAndWait()


root = Tk()

root.title("Chat bot")

root.geometry("550x350+250+130")

botsaid = StringVar()

hello = ["hi", "is anyone there?", "hello", "good day"]
bye = ["see you later", "goodbye", "I am Leaving", "have a good day"]
howare = ["how are you", "whats up", "how you doing"]
name = ["who are you", "what is your name", "do you have any name", "what should i call you"]
hours = ["when are you guys open", "what are your hours", "hours of operation", "time", "work"]
doctors = ["any information about doctors?"]
appointments = ["book an appointment", "book", "appointment", "book appointment", "when can i come",
                "when can i meet the doctor?", "doctor meet"]
services = ["lab test", "general checkup", "doctor appointment"]
times = ["10am", "1pm", "3pm", "5pm", "8pm"]
print("****\n")


def chat():
    if userinput.get().lower() in hello:
        botan = ["Hello!", "Hi there, how can I help ?", "Greetings sir!"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().lower() in howare:
        botan = ["I am fine, thanks", "Happy", "I am good"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().lower() in name:
        botan = ["My name is Devi. I am your personal healthcare companion", "You can call me Devi",
                 "Devi the Healthcare bot in your service", "Call me Devi"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in bye:
        botan = ["Sad to see you go :(", "Talk to you later", "Goodbye", "Have a nice day"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in hours:
        botan = ["We are open 7 am to 4 pm monday to saturday"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in doctors:
        botan = ["Dr.Ishan:general-surgeon, Dr.Kishan:gynecologist,  Dr.Karthik-dentist,  Dr.Kunal-cardiologist"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in appointments:
        botan = ["select the service for booking an appointment"]
        botan2 = services
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
        botsaid.set(botan2)
        speak(botan2)
    elif userinput.get().lower() in services:
        botan1=["You have selected " + userinput.get().lower() ]
        botan = ["enter the date of appointment in ddmmyyyy"]
        botsaid.set(botan1)
        speak(botan1)
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().isdigit():
        speak("entered date is ")
        speak(userinput.get())
        botan4 = userinput.get()
        speak("Select the time from")
        botsaid.set(times)
        speak(times)

    elif userinput.get().lower() in times:
        botan3 = ["Appointment booked at " + userinput.get().lower()]
        botsaid.set(random.choice(botan3))
        speak(random.choice(botan3))

    else:
        botan = ["did not get that"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))


head = Label(root, text="Devi:Healthcare Bot", font=("times new roman", 20))
head.place(x=200, y=10)

holder = Frame(root)
holder.place(x=80, y=100)

usertext = Label(holder, text="Input-", font=("times new roman", 15), height=3)
usertext.grid(row=0, column=0)

userinput = Entry(holder, font=("times new roman", 15))
userinput.grid(row=0, column=1)

submitbtn = Button(holder, text="Submit", font=("times new roman", 15), command=chat)
submitbtn.grid(row=2, column=1)

bottext = Label(holder, text="Devi:", font=("times new roman", 15), height=3)
bottext.grid(row=1, column=0)

botoutput = Entry(holder, textvariable=botsaid, font=("times new roman", 15))
botoutput.grid(row=1, column=1)
root.mainloop()
