name = input("Your Name :  ")
words = name.split(name)
words = name.lower()

print(words)
emoji = {
    "a" : "😊",
    "b" : "😒",
    "c" : "😂",
    "d" : "😉",
    "e" : "😍",
    "f" : "🥴‍",
    "g" : "😋",
    "h" : "😣",
    "i" : "🤗",
    "j" : "😎",
    "k" : "😮",
    "l" : "😘",
    "m" : "‍🤑",
    "n" : "😵",
    "o" : "😢",
    "p" : "🤐",
    "q" : "🤔",
    "r" : "🙃",
    "s" : "🤪",
    "t" : "🥵",
    "u" : "🥳",
    "v" : "😇",
    "w" : "🤩",
    "x" : "🥰",
    "y" : "😴",
    "z" : "🤒"
}
op = "";
for ch in words:
    op += emoji.get(ch,ch) + " "
print(op)
