# Import the tkinter library - this gives us GUI tools
import tkinter as tk

# STEP 1: Create the main window
window = tk.Tk()

# STEP 2: Set the window title
window.title("My Beautiful GUI App")

# STEP 3: Set the window size
window.geometry("450x400")

# STEP 4: Set the background color of the entire window
# You can use color names or hex codes (like #2C3E50)
window.config(bg="#2C3E50")  # Dark blue-gray background

# STEP 5: Create a frame (container) for better organization
# Frames help group widgets together
main_frame = tk.Frame(
    window,
    bg="#2C3E50"  # Match the window background
)
main_frame.pack(pady=30, padx=30, fill="both", expand=True)

# STEP 6: Create a title label with attractive styling
title_label = tk.Label(
    main_frame,
    text="✨ Welcome! ✨",
    font=("Helvetica", 20, "bold"),  # Bigger, bold font
    bg="#2C3E50",                     # Background color
    fg="#ECF0F1"                      # Light text color
)
title_label.pack(pady=15)

# STEP 7: Create a label to display messages
welcome_label = tk.Label(
    main_frame,
    text="Enter your name below to get started",
    font=("Helvetica", 13),
    bg="#2C3E50",      # Dark background
    fg="#BDC3C7",      # Light gray text
    wraplength=350     # Wrap text if it's too long
)
welcome_label.pack(pady=10)

# STEP 8: Create a frame for the input box (for better styling)
entry_frame = tk.Frame(main_frame, bg="#34495E")  # Slightly lighter frame
entry_frame.pack(pady=15, padx=20, fill="x")

# STEP 9: Create a text input box with better styling
name_entry = tk.Entry(
    entry_frame,
    width=30,
    font=("Helvetica", 12),
    bg="#ECF0F1",           # Light background
    fg="#2C3E50",           # Dark text
    relief="flat",          # Flat style (no border)
    highlightthickness=2,   # Border thickness when selected
    highlightcolor="#3498DB" # Blue border when clicked
)
name_entry.pack(pady=10, padx=10, ipady=8)  # ipady makes it taller

# STEP 10: Define what happens when the "Greet Me" button is clicked
def greet_user():
    """This function runs when the button is clicked"""
    user_name = name_entry.get()
    
    if user_name:
        # Update with a colorful personalized message
        welcome_label.config(
            text=f"🎉 Hello, {user_name}! Nice to meet you! 🎉",
            fg="#2ECC71"  # Green color for success
        )
    else:
        # Show reminder in orange
        welcome_label.config(
            text="⚠️ Please enter your name first!",
            fg="#E74C3C"  # Red color for warning
        )

# STEP 11: Create the "Greet Me" button with modern styling
greet_button = tk.Button(
    main_frame,
    text="Greet Me",
    command=greet_user,
    font=("Helvetica", 12, "bold"),
    bg="#3498DB",              # Bright blue background
    fg="white",                # White text
    activebackground="#2980B9", # Darker blue when clicked
    activeforeground="white",
    relief="flat",             # Flat style
    width=18,
    height=2,
    cursor="hand2"             # Hand cursor on hover
)
greet_button.pack(pady=10)

# STEP 12: Define what happens when the "Exit" button is clicked
def exit_app():
    """This function closes the app"""
    window.destroy()

# STEP 13: Create the "Exit" button with contrasting style
exit_button = tk.Button(
    main_frame,
    text="Exit",
    command=exit_app,
    font=("Helvetica", 12, "bold"),
    bg="#E74C3C",              # Red background
    fg="white",                # White text
    activebackground="#C0392B", # Darker red when clicked
    activeforeground="white",
    relief="flat",
    width=18,
    height=2,
    cursor="hand2"
)
exit_button.pack(pady=5)

# STEP 14: Add a footer label
footer_label = tk.Label(
    main_frame,
    text="Made with ❤️ using Python",
    font=("Helvetica", 9),
    bg="#2C3E50",
    fg="#7F8C8D"  # Subtle gray
)
footer_label.pack(side="bottom", pady=10)

# STEP 15: Start the app
window.mainloop()