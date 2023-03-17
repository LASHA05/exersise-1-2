
def run():
   dict = {}
   count = int(input(""))
   for i in range(count):
       word = input("")
       if word in dict:
           dict[word] = dict.get(word) + 1
       else:
           dict[word] = 1
   for i,j in dict.items():
       print(j,end=" ")
if __name__ == '__main__':
    run()