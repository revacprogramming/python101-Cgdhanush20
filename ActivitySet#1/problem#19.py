def score():
  if a>=0 and a<=1:
    if a>=0.9 :
        print('A')
    elif a>=0.8 :
        print('B')
    elif a>=0.7 :
        print('C')
    elif a>=0.6 :
        print('D')
    elif a< 0.6 :
        print('F')
    else:
        print('Invalid input')
a=float(input('Enter the score: '))
score()