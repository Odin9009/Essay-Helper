
import tkinter as tk
from tkinter import messagebox
import datetime

def save_essay():
    subject = subject_var.get()
    essay_title = title_entry.get()
    essay_author = author_entry.get()
    essay_intro = intro_text.get("1.0", tk.END).strip()
    essay_paragraphs = [p.get("1.0", tk.END).strip() for p in paragraph_entries]
    essay_conclusion = conclusion_text.get("1.0", tk.END).strip()

    # Build the essay structure
    essay_text = f"{essay_title}\nby {essay_author}\n\n"
    essay_text += essay_intro + "\n"
    essay_text += "_" * 40 + "\n\n"

    for i, paragraph in enumerate(essay_paragraphs):
        essay_text += f"Paragraph {i+1}\n{paragraph}\n"
        essay_text += "_" * 40 + "\n\n"

    essay_text += "Conclusion\n\n"
    essay_text += essay_conclusion

    # Save the essay
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"essay_{subject}_{current_time}.txt"
    with open(filename, "w") as file:
        file.write(essay_text)
    messagebox.showinfo("Essay Saved", f"The essay has been saved as {filename}")

def clear_text():
    intro_text.delete("1.0", tk.END)
    for p in paragraph_entries:
        p.delete("1.0", tk.END)
    conclusion_text.delete("1.0", tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)

def add_paragraph():
    new_paragraph_label = tk.Label(window, text=f"Paragraph {len(paragraph_entries)+1}:", bg=label_bg)
    new_paragraph_entry = tk.Text(window, height=5, width=50, bg=text_bg)

    # Insert the new paragraph entry and label into the lists at the correct position
    new_index = len(paragraph_labels) - 1
    paragraph_labels.insert(new_index, new_paragraph_label)
    paragraph_entries.insert(new_index, new_paragraph_entry)

    # Pack the new paragraph entry and label
    new_paragraph_label.pack(side="top")
    new_paragraph_entry.pack()

# Create the main window
window = tk.Tk()
window.title("Essay Writer")

# Configure colors and styles for the smooth theme
window.configure(bg="#F0F0F0")
window.geometry("600x600")

button_bg = "#4CAF50"  # Green
button_fg = "#FFFFFF"  # White
label_bg = "#E0E0E0"   # Light Gray
text_bg = "#FFFFFF"    # White
border_radius = 10

# Create a frame for buttons
button_frame = tk.Frame(window, bg=label_bg)
button_frame.pack(pady=10)

# Create a button to save the essay
save_button = tk.Button(button_frame, text="Save", command=save_essay, bg=button_bg, fg=button_fg, relief=tk.FLAT,
                        padx=10, pady=5, bd=0, font=("Arial", 12), borderwidth=0, highlightthickness=0)
save_button.pack(side="left", padx=10)

# Create a button to clear the text areas
clear_button = tk.Button(button_frame, text="Clear", command=clear_text, bg=button_bg, fg=button_fg, relief=tk.FLAT,
                         padx=10, pady=5, bd=0, font=("Arial", 12), borderwidth=0, highlightthickness=0)
clear_button.pack(side="left", padx=10)

# Create a label for the subject
subject_label = tk.Label(window, text="Subject:", bg=label_bg, font=("Arial", 14, "bold"))
subject_label.pack(pady=10)

# Create a dropdown menu for the subject
subjects = ["Science", "History", "Literature", "Technology", "Politics", "Other"]
subject_var = tk.StringVar()
subject_dropdown = tk.OptionMenu(window, subject_var, *subjects)
subject_dropdown.config(bg=text_bg, relief=tk.FLAT, font=("Arial", 12), borderwidth=0, highlightthickness=0)
subject_dropdown.pack()

# Create a label for the title
title_label = tk.Label(window, text="Title:", bg=label_bg, font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Create an entry for the title
title_entry = tk.Entry(window, bg=text_bg, font=("Arial", 12), relief=tk.FLAT, bd=0, highlightthickness=0)
title_entry.pack()

# Create a label for the author
author_label = tk.Label(window, text="Author:", bg=label_bg, font=("Arial", 14, "bold"))
author_label.pack(pady=10)

# Create an entry for the author
author_entry = tk.Entry(window, bg=text_bg, font=("Arial", 12), relief=tk.FLAT, bd=0, highlightthickness=0)
author_entry.pack()

# Create a label for the introduction
intro_label = tk.Label(window, text="Introduction:", bg=label_bg, font=("Arial", 14, "bold"))
intro_label.pack(pady=10)

# Create a text area for the introduction
intro_text = tk.Text(window, height=5, width=50, bg=text_bg, relief=tk.FLAT, bd=0, highlightthickness=0,
                     font=("Arial", 12))
intro_text.pack()

# Create lists for paragraph labels and entries
paragraph_labels = []
paragraph_entries = []

# Create a button to add a new paragraph
add_paragraph_button = tk.Button(window, text="+ Add Paragraph", command=add_paragraph, bg=button_bg, fg=button_fg,
                                 relief=tk.FLAT, padx=10, pady=5, bd=0, font=("Arial", 12), borderwidth=0,
                                 highlightthickness=0)
add_paragraph_button.pack(pady=10)

# Create a frame for conclusion
conclusion_frame = tk.Frame(window, bg=label_bg)
conclusion_frame.pack(pady=10)

# Create a label for the conclusion
conclusion_label = tk.Label(conclusion_frame, text="Conclusion:", bg=label_bg, font=("Arial", 14, "bold"))
conclusion_label.pack(side="top", pady=5)

# Create a text area for the conclusion
conclusion_text = tk.Text(conclusion_frame, height=5, width=50, bg=text_bg, relief=tk.FLAT, bd=0, highlightthickness=0,
                          font=("Arial", 12))
conclusion_text.pack(side="bottom")

# Allow resizing of the window
window.resizable(True, True)

# Start the GUI event loop
window.mainloop()
