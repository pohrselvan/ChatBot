from collections import deque 

class ChatHistory:
  def __init__(self,max_len=3):
    self.history = deque(maxlen=max_len)

  def add(self,user,ai):
    self.history.append((user,ai))

  def get_context(self):
    messages = []
    for chat in self.history:
      user = f"User:{chat[0]}"
      ai = f"AI:{chat[1]}"
      messages.append(user)
      messages.append(ai)
    return messages 
  
  def length(self):
    return len(self.history)