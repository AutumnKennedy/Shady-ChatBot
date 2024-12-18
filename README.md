# Shady Chatbot

Welcome to the **Shady Chatbot** repository! This chatbot doesn't just answer your questions—it answers them with *attitude*. Perfect for beginners who want to learn about chatbots while keeping things fun and spicy.

## Features
- **Retrieval-Based Model**: Matches your questions to pre-written responses in a knowledge base.
- **Speech Recognition**: Listens to your questions using `speech_recognition`.
- **Text-to-Speech**: Roasts you out loud using `pyttsx3`.
- **Expandable Knowledge Base**: Teach the bot new responses if it doesn't know an answer.
- **Built-in Sass**: Responses come with a side of humor and shade!

## How It Works
The chatbot uses a JSON file (`knowledge_base.json`) to store pre-written questions and their snarky answers. Here’s how it works:
1. **Listens to Your Question**: The bot uses `speech_recognition` to convert your voice input into text.
2. **Finds the Best Match**: Using `difflib`, it matches your question to the closest one in its knowledge base.
3. **Responds with Shade**: The bot reads its answer out loud using `pyttsx3`. If no match is found, you can teach it a new response.

## Installation
To get started, clone this repository and install the required Python libraries:

```bash
# Clone the repo
git clone https://github.com/yourusername/shady-chatbot.git
cd shady-chatbot

# Install dependencies
pip install -r requirements.txt
```

### Required Libraries
- `json`: For storing and managing the knowledge base.
- `difflib`: To find the best match for user input.
- `speech_recognition`: For converting speech to text.
- `pyttsx3`: For text-to-speech functionality.

## Usage
Run the chatbot by executing the `chat_bot` function in the main script:

```bash
python chatbot.py
```

### Commands
- Speak a question into your microphone. For example: "What’s your favorite color?"
- Say **"goodbye"** to exit the chatbot.
- If the bot doesn't know an answer, type a response to teach it or skip by typing "skip."

## Knowledge Base
The chatbot's responses are stored in `knowledge_base.json`. Here’s a sample entry:

```json
{
  "question": "What’s your favorite color?",
  "answer": "My favorite color? The shade of your audacity for asking me that."
}
```

You can edit this file to add your own shady questions and answers.

## License
This project is licensed under the MIT License. Feel free to use and modify it as you like—just remember to keep the shade alive!

## Questions or Feedback?
Got questions, feedback, or just want to share your favorite shady responses? Open an issue or reach out to me!

Enjoy the sass! 😎

