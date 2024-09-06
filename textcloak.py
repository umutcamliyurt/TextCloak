from gpt4all import GPT4All

# Initialize the model
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # Downloads / loads a 4.66GB LLM

def interact_with_model():
    with model.chat_session() as session:
        print("Welcome to the interactive LLM chat session!")
        print("Type 'exit' to end the session.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Ending session. Goodbye!")
                break
            
            # Generate a response
            response = session.generate("Convert this text to make it sound like from a random person: " + user_input, max_tokens=1024)
            print("Model:", response)

if __name__ == "__main__":
    interact_with_model()
