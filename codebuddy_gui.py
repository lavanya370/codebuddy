import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("CodeBuddy")
root.geometry("400x400")

# Responses dictionary
responses = {
    "loop": ["Loops repeat tasks", "Try printing 1 to 10", "Use for loop"],
    "list": ["Lists store values", "Find max number", "Use max()"],
    "function": ["Functions reuse code", "Create add function", "Use def"],
    "error": ["Read error carefully", "Check line number", "Fix step by step"]
}

# Function when button clicked
def get_response():
    user_input = entry.get().lower()
    
    for key in responses:
        if key in user_input:
            result = f"Explanation: {responses[key][0]}\n"
            result += f"Task: {responses[key][1]}\n"
            result += f"Tip: {responses[key][2]}"
            output_label.config(text=result)
            return
    
    output_label.config(text="Keep practicing!")

# Input box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Get Help", command=get_response)
button.pack(pady=10)

# Output
output_label = tk.Label(root, text="", wraplength=300, justify="left")
output_label.pack(pady=20)

# Run app
root.mainloop()