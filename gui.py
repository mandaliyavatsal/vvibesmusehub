import tkinter as tk
from tkinter import filedialog, messagebox
import os
import app
import config

class MusicGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Music Generator App")

        self.model_dir = tk.StringVar(value=config.MODEL_DIR)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="AI Music Generator App", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Model Directory:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.model_dir, width=50).pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_directory).pack(pady=5)

        tk.Button(self.root, text="Generate Music", command=self.generate_music).pack(pady=20)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.model_dir.set(directory)

    def generate_music(self):
        model_name = "gpt2"  # Example model name
        model_dir = self.model_dir.get()

        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        app.download_model(model_name, model_dir)

        prompt = "Generate a music piece based on this prompt: "
        length = 100  # Example length

        music = app.generate_music(model_name, prompt, length, model_dir)
        messagebox.showinfo("Generated Music", music)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicGeneratorApp(root)
    root.mainloop()
