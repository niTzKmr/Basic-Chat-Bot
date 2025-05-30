# Basic ChatBot

A simple GUI-based chatbot using Python, Tkinter, and TF-IDF for conversational matching. This project is part of the CodeAlpha internship.

## Features

- Text-based chat interface with a modern look
- Answers greetings, project info, date, time, and jokes
- Can perform simple calculations (e.g., `calculate 2+2`)
- Uses TF-IDF and cosine similarity for flexible matching

## Requirements

- Python 3.x
- scikit-learn

## Installation

1. Clone or download this repository.
2. Install dependencies:
    ```
    pip install scikit-learn
    ```

## Usage

1. Run the chatbot:
    ```
    python BasicChatBot.py
    ```
2. Type your message and press Enter or click Send.
3. Type `bye` to exit.

## Example

```
You: hi
CodeAlphaBot: Hello! How can I help you today?
You: calculate 5*7
CodeAlphaBot: The answer is: 35
You: what is the date
CodeAlphaBot: Today's date is 2025-05-30
You: bye
CodeAlphaBot: Bye! Have a great day.
```
