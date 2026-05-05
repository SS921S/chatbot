import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# Chat loop
print("Grammar Bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break
    
    corrected = correct_grammar(user_input)
    print("Bot:", corrected)
