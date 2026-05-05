import language_tool_python

# Using the remote server to avoid the Java requirement
tool = language_tool_python.LanguageTool('en-US', remote_server='https://api.languagetool.org/')

# Chat loop
print("Grammar Bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    # 1. First, check for errors
    matches = tool.check(user_input)
    
    # 2. Decide what to print based on the number of matches
    if len(matches) == 0:
        print("Bot: The text is good!")
    else:
        corrected = tool.correct(user_input)
        print(f"Bot: The corrected version is: {corrected}")
