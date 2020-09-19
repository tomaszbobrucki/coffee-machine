text = input()

new_text = text.strip().replace("!", "").replace(",", "").replace("?", "").replace(".", "").lower()
print(new_text)
