import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime

qa_pairs = [
    ("hi", "Hello! How can I help you today?"),
    ("hello", "Hi there!"),
    ("hey", "Hi there!"),
    ("hii", "Hello! How can I help you today?"),
    ("hiii", "Hello! How can I help you today?"),
    ("what is your name", "I am CodeAlphaBot, your internship assistant."),
    ("how are you", "I'm doing well, thank you!"),
    ("help", "Sure, I'm here to help. What do you need assistance with?"),
    ("tell me a joke", "Why do programmers prefer dark mode? Because light attracts bugs!"),
    ("project", "This chatbot is part of the CodeAlpha internship project."),
    ("internship", "This chatbot is part of the CodeAlpha internship project."),
    ("time", f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"),
    ("date", f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"),
    ("bye", "Bye! Have a great day."),
]

questions = [q for q, a in qa_pairs]
answers = [a for q, a in qa_pairs]
vectorizer = TfidfVectorizer().fit(questions)

def get_response(user_input):
    user_input = user_input.lower().strip()
    if user_input.startswith("calculate"):
        try:
            expr = user_input[10:]
            result = eval(expr, {"__builtins__": {}})
            return f"The answer is: {result}"
        except Exception:
            return "Sorry, I couldn't calculate that."
    X = vectorizer.transform([user_input])
    sims = cosine_similarity(X, vectorizer.transform([q.lower() for q in questions]))
    idx = sims.argmax()
    if sims[0, idx] > 0.3:
        return answers[idx]
    return "Sorry, I didn't understand that. Can you rephrase?"

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("CodeAlphaBot")
        master.geometry("450x600")
        master.configure(bg="#f7f7f8")

        # Header
        header = tk.Frame(master, bg="#9500ff", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="🤖 LeadBot", font=("Segoe UI", 13, "bold"), fg="white", bg="#9500ff").pack(side=tk.LEFT, padx=10, pady=15)
        tk.Label(header, text="● Online Now", font=("Segoe UI", 9), fg="lightgreen", bg="#9500ff").pack(side=tk.LEFT, padx=5, pady=15)

        # Chat area
        self.text_area = scrolledtext.ScrolledText(
            master, wrap=tk.WORD, font=("Segoe UI", 10),
            bg="white", fg="#000000", state='disabled', bd=0, relief="flat"
        )
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input area
        input_frame = tk.Frame(master, bg="#f7f7f8", highlightbackground="#b57edc", highlightthickness=2)
        input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.entry = tk.Entry(
            input_frame, font=("Segoe UI", 12),
            bg="#ffffff", fg="#000000", bd=0
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(10, 5))
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            input_frame, text="Send", command=self.send_message,
            font=("Segoe UI", 10, "bold"), bg="#b57edc", fg="white",
            activebackground="#a64dd8", relief="flat", padx=15
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 10))


        self.insert_message("CodeAlphaBot", "Hi! I'm CodeAlphaBot. Type 'bye' to exit.")

    def insert_message(self, sender, message, align="left"):
        self.text_area.config(state='normal')
        tag_name = f"{sender}_{align}"
        self.text_area.tag_config(tag_name, justify=align, foreground="#000000", lmargin1=10, lmargin2=10, rmargin=10)
        color = "#eae6f8" if sender == "CodeAlphaBot" else "#d4a5ff"
        bubble = f"{sender}: {message}\n\n"
        self.text_area.insert(tk.END, bubble, tag_name)
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.insert_message("You", user_input, align="right")
        self.entry.delete(0, tk.END)

        if user_input.lower() in ["bye", "quit", "exit"]:
            self.insert_message("CodeAlphaBot", "Bye! Have a great day.", align="left")
            self.master.after(1000, self.master.destroy)
            return

        response = get_response(user_input)
        self.insert_message("CodeAlphaBot", response, align="left")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatBotGUI(root)
    root.mainloop()
