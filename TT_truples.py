def stringcases(string):
  a = string.upper()
  b = string.lower()
  c = string.title()
  d = string[::-1]
  print d
  #split = d[::-1]
  #print split
  e = "".join(d)
  print e
  f = a, b, c, e
  print f
  return e
  
stringcases("I am who I am")