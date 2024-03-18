import tkinter as tk
from tkinter import simpledialog, messagebox, Menu, filedialog
import openai
import datetime
from tkinter import ttk
import webbrowser  # Importing webbrowser module

global_model = "gpt-3.5-turbo"  # Initial global model

def ask_gpt(question, api_key):
    try:
        openai.api_key = api_key  # Set the API key for each request
        response = openai.ChatCompletion.create(
            model=global_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        print(global_model)
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def send(api_key):
    send_text = "You: " + e.get()
    txt.insert(tk.END, "\n" + send_text)
    user_input = e.get().strip()
    e.delete(0, tk.END)
    answer = ask_gpt(user_input, api_key)
    txt.insert(tk.END, "\n" + "GPT " + global_model +" : " + answer)

def get_api_key():
    api_key = api_entry.get().strip()
    if api_key:
        return api_key
    else:
        messagebox.showerror("Error", "Please enter your OpenAI API key.")

def clear_chat():
    txt.delete(1.0, tk.END)

def save_chat(global_model):
    # Get the chat history from the text widget
    chat_history = txt.get("1.0", tk.END)

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the HTML content with the timestamp and current model as the header
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat History</title>
        <style>
            .container {{
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }}
            .message-container {{
                margin-bottom: 20px;
            }}
            .user-message {{
                background-color: #d3e9d3;
                padding: 10px;
                border-radius: 10px;
                float: right;
            }}
            .gpt-message {{
                background-color: #e3e3e3;
                padding: 10px;
                border-radius: 10px;
                float: left;
            }}
            .clearfix {{
                clear: both;
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Chat History</h1>
            <div class="header">
                <h2>Model: {global_model}</h2>
                <h3>{timestamp}</h3>
            </div>
    """

    # Split the chat history into individual messages
    messages = chat_history.split("\n")

    # Iterate over each message and format it as a conversation in HTML
    for i, message in enumerate(messages):
        if message.startswith("You:"):
            html_content += f"""
            <div class="message-container">
                <div class="user-message">{message}</div>
                <div class="clearfix"></div>
            </div>
            """
        else:
            html_content += f"""
            <div class="message-container">
                <div class="gpt-message">{message}</div>
                <div class="clearfix"></div>
            </div>
            """

    # Close the HTML content
    html_content += """
        </div>
    </body>
    </html>
    """

    # Ask the user to select file location for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])

    if file_path:
        # Save the HTML content to the selected file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)

        messagebox.showinfo("Save Chat History", f"Chat history saved to {file_path}")


def change_model():
    # Define available models or configurations along with descriptions
    models = {
        "gpt-3.5-turbo": "This is the GPT-3.5 model with turbo mode enabled.",
        "gpt-4-turbo-preview": "This is the GPT-4 model with turbo mode enabled.",
        # Add more models along with descriptions as needed
    }

    # Create a dropdown menu for selecting models
    model_var = tk.StringVar(window)
    model_combobox = ttk.Combobox(window, textvariable=model_var, values=list(models.keys()))
    model_combobox.set("GPT-3.5 Turbo")  # Set the initial value

    # Function to display the description of the selected model
    def display_model_description():
        selected_model = model_var.get()
        model_description = models.get(selected_model, "Description not available")
        messagebox.showinfo(selected_model, model_description)

    # Function to update the global_model variable based on the selected model
    def update_global_model():
        global global_model
        selected_model = model_var.get()
        if selected_model in models:
            global_model = selected_model.replace(" ", "").lower()  # Adjust global_model variable
            messagebox.showinfo("Model Changed", f"Global model set to {selected_model}")
        else:
            messagebox.showwarning("Invalid Model", "Please select a valid model.")

    # Combine creation and packing of widgets into a single line with horizontal alignment
    ttk.Combobox(window, textvariable=model_var, values=list(models.keys())).pack(side=tk.LEFT, padx=5)
    tk.Button(window, text="Update Model", command=update_global_model).pack(side=tk.LEFT, padx=5)
    tk.Button(window, text="Model Info", command=display_model_description).pack(side=tk.LEFT, padx=5)

def open_pricing_page():
    # Open the specified URL in a web browser
    webbrowser.open("https://openai.com/pricing")

def voice_io():
    pass  # Placeholder for voice input/output functionality

def emoji_support():
    pass  # Placeholder for emoji support

def multilingual_support():
    pass  # Placeholder for multilingual support

def customization():
    pass  # Placeholder for customization functionality

def error_handling():
    pass  # Placeholder for error handling

def other_api_integration():
    pass  # Placeholder for other API integration

def show_about_me_info():
    about_window = tk.Toplevel()
    about_window.title("About GPT Chat")
    about_window.resizable(False, False)  # Disable both horizontal and vertical resizing
    
    about_text = """
    About This Application:
    
    - Application Name: GPT Chat
    - Version: 1.0
    - Description: A chat application powered by OpenAI's GPT models.

    Developer Information:
    
    - Developer: Karthik Kannaiyan
    - Email: erakkarthik@hotmail.com
    - Website: www.karthikkannaiyan.com

    Acknowledgments:
    
    - OpenAI: For providing the GPT models.
    - tkinter: For the GUI framework.
    - Python: For the programming language.
    - 'image: Flaticon.com'. This cover has been designed using images from Flaticon.com

    License Information:
    
    This application is licensed under the MIT License.

    Additional Information:
    
    - Release Notes:
      - Version 1.0: Initial release with basic chat functionality.

    - Future Plans:
      - Local LLM model which will analyse and process data locally.
      - Version 1.1: Added support for emoji input.
      - Improve multilingual support.
      - Integrate voice recognition feature.
    """
    
    about_label = tk.Label(about_window, text=about_text, justify=tk.LEFT)
    about_label.pack(padx=10, pady=10)

# Setting up the window
window = tk.Tk()
window.title("Open AI GPT Chat interface")

# Setting window icon
window.iconbitmap(r'D:\gptchat\chat.ico')

# Color scheme
bg_color = "#f0f0f0"  # Light gray
button_color = "#4CAF50"  # Green
button_fg_color = "white"  # White

# Placeholder for API Key entry
api_frame = tk.Frame(window, bg=bg_color)
api_label = tk.Label(api_frame, text="OpenAI API Key:", bg=bg_color)
api_label.pack(side=tk.LEFT)

# Entry widget for API key
api_entry = tk.Entry(api_frame, width=30, show="*")  # Display entered characters as asterisks
api_entry.pack(side=tk.LEFT)

# Function to toggle between showing stars and actual characters in the API key entry
def toggle_show_chars():
    if show_button.cget("text") == "Show":
        api_entry.config(show="")
        show_button.config(text="Hide")
    else:
        api_entry.config(show="*")
        show_button.config(text="Show")

# Button to toggle showing/hiding characters in the API key entry
show_button = tk.Button(api_frame, text="Show", command=toggle_show_chars)
show_button.pack(side=tk.LEFT)

api_frame.pack(pady=10)

# Creating a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Adding menu items
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear Chat", command=clear_chat)
file_menu.add_command(label="Save Chat", command=lambda: save_chat(global_model))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Change Model", command=change_model)
edit_menu.add_command(label="OpenAI API Pricing", command=open_pricing_page)

tools_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Voice I/O", command=voice_io)
tools_menu.add_command(label="Emoji Support", command=emoji_support)
tools_menu.add_command(label="Multilingual Support", command=multilingual_support)

settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Customization", command=customization)
settings_menu.add_command(label="Error Handling", command=error_handling)

#help_menu = Menu(menu_bar, tearoff=0)
#menu_bar.add_cascade(label="Help", menu=help_menu)
#help_menu.add_command(label="API Integration", command=other_api_integration)

# Adding About Me option directly to the main menu bar
menu_bar.add_command(label="About", command=show_about_me_info)

frame = tk.Frame(window, bg=bg_color)
scroll = tk.Scrollbar(frame)
txt = tk.Text(frame, width=50, height=20, yscrollcommand=scroll.set, wrap='word')
scroll.pack(side=tk.RIGHT, fill=tk.Y)
txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack()

e = tk.Entry(window, width=50)
e.pack(pady=10)

# Configure the send button to use the API key
send_button = tk.Button(window, text="Send", bg=button_color, fg=button_fg_color, command=lambda: send(get_api_key()))
send_button.pack()

window.mainloop()
