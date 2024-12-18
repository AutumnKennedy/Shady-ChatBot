import json
from difflib import get_close_matches
import speech_recognition as sr
import pyttsx3

def load_knoledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str| None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def chat_bot():
    knowledge_base: dict = load_knoledge_base('knowledge_base.json')
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while True:
        try:
            with sr.Microphone() as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic, duration= 0.2)
                audio = recognizer.listen(mic)

                user_input = recognizer.recognize_google(audio)
                user_input = user_input.lower()

                print(f'You: {user_input}')

                if user_input == 'goodbye':
                    print("Bot: Goodbye big back!")
                    engine.say("Goodbye big back!")
                    engine.runAndWait()
                    break

            best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

            if best_match:
                answer: str = get_answer_for_question(best_match, knowledge_base)
                print(f'Bot: {answer}')
                engine.say(answer)
                engine.runAndWait()
            else:
                print('Bot: I don\'t know the answer. Can you teach me how to respond?')
                engine.say("I don't know the answer. Can you teach me how to respond?")
                engine.runAndWait()

                new_answer: str = input('Type the answer or "skip" to skip: ')

                if new_answer.lower() != 'skip':
                    knowledge_base['questions'].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Bot: I learned a new response!')
                    engine.say('I learned a new response!')
                    engine.runAndWait()

        except sr.UnknownValueError:
            print("Bot: Speak up Big Back!")
            engine.say("Speak up Big Back!")
            engine.runAndWait()
        except Exception as e:
            print(f"Bot: An error occurred: {e}")

            pass

if __name__ == '__main__':
    chat_bot()