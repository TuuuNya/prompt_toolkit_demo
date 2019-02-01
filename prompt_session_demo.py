from prompt_toolkit import PromptSession

session = PromptSession()

text1 = session.prompt()
text2 = session.prompt()

print(text1)
print(text2)
