import tkinter as tk
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog. This is a sample text for typing speed assessment."

        self.label = tk.Label(root, text="Type the following text:")
        self.label.pack()

        self.text_to_type = tk.Label(root, text=self.sample_text, wraplength=400)
        self.text_to_type.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def start_typing_test(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.bind("<Return>", self.calculate_typing_speed)

    def calculate_typing_speed(self, event):
        typed_text = self.entry.get()
        end_time = time.time()
        time_taken = end_time - self.start_time

        words_per_minute = len(typed_text.split()) / (time_taken / 60)

        result_text = f"Your typing speed: {words_per_minute:.2f} words per minute."

        if words_per_minute < 40:
            result_text += " Keep practicing!"
        elif words_per_minute >= 100:
            result_text += " Excellent! You are a fast typist."

        self.result_label.config(text=result_text)
        self.start_button.config(state=tk.NORMAL)
        self.entry.unbind("<Return>")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
