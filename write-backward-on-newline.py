def writeBackwardNewline(word):
  if len(word) < 2:
    print(word)
  else:
    print(word[len(word) - 1])
    writeBackwardNewline(word[:-1])

print(write_backward_newline("hello"))