```python
import nltk
from nltk.chat.util import Chat, reflections

class IntelligentVirtualAssistant:
    def __init__(self):
        self.virtual_assistant_responses = {
            "greetings": ["Hello! How can I assist you today?"],
            "goodbye": ["Goodbye! Happy hacking!"],
            "default": ["I am sorry, but I do not understand that."]
        }
        self.pairs = [
            [
                r"hi|hey|hello",
                self.virtual_assistant_responses["greetings"]
            ],
            [
                r"bye|goodbye",
                self.virtual_assistant_responses["goodbye"]
            ],
            [
                r".*",
                self.virtual_assistant_responses["default"]
            ]
        ]

    def ask_virtual_assistant(self, message):
        chat = Chat(self.pairs, reflections)
        return chat.respond(message)

if __name__ == "__main__":
    assistant = IntelligentVirtualAssistant()
    while True:
        message = input("> ")
        if message.lower() == "quit":
            break
        print(assistant.ask_virtual_assistant(message))
```