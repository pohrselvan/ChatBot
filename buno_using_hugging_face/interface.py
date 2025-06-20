from model_loader import model_loader
from memory import ChatHistory
import torch

def run_chat():
    model, tokenizer = model_loader()
    history = ChatHistory()
    messages = []
    print("chatbot is starting ...............")
    while True:
        user_input = input("User: ")

        if user_input.lower() == '/exit':
            print("Exiting chat bot ...........")
            break

        if history.length() > 0:
            # Join full history into a prompt
            past = "\n".join(history.get_context())
            prompt = f"{past}\nUser: {user_input}\nAI:"
        else:
            prompt = f"User: {user_input}\nAI:"
  

        # Tokenize prompt
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        # Generate response
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=150,
            do_sample=True,
            temperature=1.0,
            top_p=0.85,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id
        )


        # Decode only newly generated tokens
        generated = outputs[0][inputs.input_ids.shape[-1]:]
        response = tokenizer.decode(generated, skip_special_tokens=True)

        print("AI:", response)

        # Save to history
        history.add(user_input, response)

if __name__ == "__main__":
    run_chat()