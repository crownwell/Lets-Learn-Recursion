def writeBackward(word, reversed_word = ""):
  if len(word) < 2:
    print(reversed_word + word)
  else:
    new_word = reversed_word + word[len(word) - 1]
    writeBackward(word[:-1], new_word)


print(writeBackward("hello"))