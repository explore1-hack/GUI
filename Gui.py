# Import the tkinter library - this gives us GUI tools
# import tkinter as tk


import tensorflow as tf

a = tf.constant(5)
b = tf.constant(3)

c = a + b
print(c)



# # STEP 1: Create the main window
# # This is the foundation of your app
# window = tk.Tk()

# # STEP 2: Set the window title (appears at the top)
# window.title("My First GUI App")

# # STEP 3: Set the window size (width x height in pixels)
# window.geometry("400x300")

# # STEP 4: Create a label to display messages
# # This is where we'll show text to the user
# welcome_label = tk.Label(
#     window,                           # Put it in the main window
#     text="Welcome! Enter your name below.",  # Initial message
#     font=("Arial", 14),              # Font style and size
#     fg="blue"                        # Text color (foreground)
# )
# # Place the label in the window using pack() - it auto-arranges widgets
# welcome_label.pack(pady=20)  # pady adds space above and below

# # STEP 5: Create a text input box (Entry widget)
# # This is where users can type
# name_entry = tk.Entry(
#     window,              # Put it in the main window
#     width=30,           # Width in characters
#     font=("Arial", 12)  # Font size
# )
# name_entry.pack(pady=10)  # Add some spacing

# # STEP 6: Define what happens when the "Greet Me" button is clicked
# def greet_user():
#     """This function runs when the button is clicked"""
#     # Get whatever the user typed in the text box
#     user_name = name_entry.get()
    
#     # Check if they actually typed something
#     if user_name:
#         # Update the label with a personalized message
#         welcome_label.config(text=f"Hello, {user_name}! Nice to meet you!")
#     else:
#         # If the box is empty, show a reminder
#         welcome_label.config(text="Please enter your name first!")

# # STEP 7: Create the "Greet Me" button
# greet_button = tk.Button(
#     window,                    # Put it in the main window
#     text="Greet Me",          # Text on the button
#     command=greet_user,       # Function to call when clicked
#     font=("Arial", 12),       # Font size
#     bg="green",               # Background color
#     fg="white",               # Text color
#     width=15                  # Button width
# )
# greet_button.pack(pady=10)  # Add spacing

# # STEP 8: Define what happens when the "Exit" button is clicked
# def exit_app():
#     """This function closes the app"""
#     window.destroy()  # Close the window and end the program

# # STEP 9: Create the "Exit" button
# exit_button = tk.Button(
#     window,                # Put it in the main window
#     text="Exit",          # Text on the button
#     command=exit_app,     # Function to call when clicked
#     font=("Arial", 12),   # Font size
#     bg="red",             # Background color
#     fg="white",           # Text color
#     width=15              # Button width
# )
# exit_button.pack(pady=10)  # Add spacing

# # STEP 10: Start the app - this keeps the window open and responsive
# # This line must always be at the end!
# window.mainloop()