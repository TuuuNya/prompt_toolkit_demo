# 输出简单文本
# coding: utf-8
from prompt_toolkit import print_formatted_text, HTML

print_formatted_text("a normal Hello World!")
print_formatted_text(HTML("<b>a bold Hello World!</b>"))
print_formatted_text(HTML("<i>a italic Hello World!</i>"))
print_formatted_text(HTML("<u>a underline Hello World!</u>"))
print_formatted_text(HTML("<ansired>a red foreground Hello World!</ansired>"))
print_formatted_text(HTML("<ansigreen>a green foreground Hello World!</ansigreen>"))
print_formatted_text(HTML("<skyblue>a skyblue Hello World!</skyblue>"))
print_formatted_text(HTML("<seagreen>a seagreen Hello World!</seagreen>"))
print_formatted_text(HTML("<violet>a violet Hello World!</violet>"))
print_formatted_text(HTML('<text fg="ansiwhite" bg="ansigreen">a colors Hello World!</text>'))

