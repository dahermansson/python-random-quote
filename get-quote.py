import random

def hepp():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  i = 0
  while i <3:
    rnd = random.randint(0, last)
    print(quotes[rnd].rstrip())
    i += 1

def add(newQuote):
  f = open("quotes.txt", "a")
  f.write(newQuote)
  f.close


if __name__== "__main__":
  hepp()
  newQuote = input()
  add(newQuote)