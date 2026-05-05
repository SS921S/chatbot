import language_tool_python

tool = language_tool_python.LanguageTool('en-US', remote_server='https://api.languagetool.org/')

def correct_grammar(text):
    return tool.correct(text)

# Chat loop
print("Grammar Bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break
    
    corrected = correct_grammar(user_input)
    print("Bot:", corrected)
