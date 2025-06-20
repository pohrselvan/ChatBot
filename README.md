# ChatBot using Qwen 0.6B (4-bit Quantized)
I have created a chatbot using Qwen 0.6B model with window memory ranging from 3-5.

# Features
Uses Qwen 0.6B Base model (4-bit quantized for low memory)
Maintains windowed conversation history (3–5 turns)
Built with Hugging Face transformers + bitsandbytes
Simple CLI-based interface for chatting

# Instruction for setup 
1. git clone the repo \b
`git clone https://github.com/pohrselvan/ChatBot
cd chatbot`
3. Create a virtual environment
`python3 -m venv chatbot`
4. Enable the virtual env
`source chatbot/bin/activate`
5. Install Requriments
`pip install transformers bitsandbytes`
6. Run the Interface file
`python interface.py`
