import csv
import random
import tkfontawesome
import tkinter as tk

with open('indian movies.csv', encoding='utf-8') as f:  # for csv file
    reader = csv.reader(f)
    next(reader)  # Skip header row
    val = [(row[0], row[1:]) for row in reader]

import json
with open("info.json", "r") as f:  # for JSON file
    greetings = json.load(f)

# Define function to generate response
def generate_response(input_text):

    # if it is something from json
    for intent in greetings["dataofall"]:
        if input_text.lower() in intent["patterns"]:
            return random.choice(intent["responses"])
    # for referring csv file
        for moviesname, values in val:
            if moviesname.lower() == input_text.lower():  # Check if input text contains the movie name
                response = "\n".join(values)
                return response

    return "Sorry! My work is limited here, I'm not sure which movie you're referring to."


# Define function to handle button click
def handle_click():
    input_text = entry.get()
    response = generate_response(input_text)
    text.insert('end', 'You: ' + input_text + '\n')
    text.insert('end', 'ChatBot101: ' + response + '\n')
    entry.delete(0, 'end')

# Create tkinter window

window = tk.Tk()
window.title('ChatBot101')
window.config(bg="aquamarine")

m= tkfontawesome.icon_to_image("film", fill="#4267B2", scale_to_width=64)
tk.Label(window, image=m).pack(padx=10, pady=10)
tk.Label(window,text="Movie Name??",font=("Times", "24", "bold italic"),bg='light cyan').pack(padx=10,pady=10)
# Create input field
entry = tk.Entry(window, width=50,bg='sky blue1',font=("Helvetica", "10"))
entry.pack(pady=10)

# Create submit button
button = tk.Button(window, text='SUBMIT', command=handle_click,bg='DarkSeaGreen2',activeforeground='green',foreground='purple')
button.pack(pady=10)

# Create chat history text area
text = tk.Text(window, height=10, width=50, bg='sky blue1',font=("Helvetica", "10"))
text.pack(pady=10)

# Start the tkinter event loop
window.mainloop()
