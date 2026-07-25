print("Namaste! Welcome to Your Chatbot")
print("You can ask me basic questions. Type 'bye' to exit.")

responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am a smart AI chatbot",          # fixed case
    "motivate me": "Keep going. Every line of code makes you a great developer!",
    "what is functions": "A function is a named block of code that performs a specific task. Write it once, reuse it anywhere!"  # fixed case
}

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to answer that yet. Mai jald hi ye sikh lunga!"




while True:
   
   
   
    user_Input = input("Please ask your question: ")
    
    if "bye" in user_Input.lower():          # check BEFORE getting bot response
        print("Bot Response: Goodbye! Have a great day!")
        break
    
    reply = getResponseBot(user_Input)
    print("Bot Response:", reply)