'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

can't contain loops,
says nothing about defining global variables

'''


def count_th(word:str,result=0):
    print(word)
    if len(word) == 0:
        print(f"final final count = {result}")
        finalfinal=result
        print(f"result = {result} finalfinal ={finalfinal}")
        return int(f"{finalfinal}")
    if len(word) < 3:
        chunk = word[0:2]
        print(f"chunk = {chunk}")
        if chunk=="th":
            result+=1
        print(f"final count = {result}")
        return count_th(word[2:len(word)],result)
    else:
        chunk = word[0:2]
        chunk2 = word[1:3]
        print(f"chunk = {chunk}")
        if chunk=="th":
            result+=1
        elif chunk2=="th":
            result+=1
            return count_th(word[3:len(word)],result)
        return count_th(word[2:len(word)],result)


def count_th(word):
  if len(word) < 2:
    return 0
  else:
    if word[0:2] == "th":
      return 1 + count_th(word[2:])
    else:
      return count_th(word[1:])


