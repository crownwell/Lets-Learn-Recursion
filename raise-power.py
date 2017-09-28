def raisePower(number, p):
  if p == 0:
    return 1.0
  elif p < 0:
    print(p)
    return 1.0 / float(power(number, (p * -1) - 1) * float(number))
  else:
    return raisePower(number, p - 1) * number

print(raisePower(2, -7)) # negative power
print(raisePower(2, 7)) #positive power