def isPalindrome(text):
  if len(text) < 2:
    return True
  elif text[len(text) - 1] != text[0]:
    return False
  else:
    return isPalindrome(text[1:-1])

print(is_palindrome("hello"))