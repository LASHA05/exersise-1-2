def run():
   lst = []
   count = int(input(""))
   for i in range(count):
       word = input("")
       lst.append(word)
   for i in lst:
       if "".join(sorted(i)[::-1])==i:
           print("No answer")
       else:
           print("TODO")

if __name__ == '__main__':
    run()