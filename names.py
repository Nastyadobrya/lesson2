names = ["Вася", "Маша", "Петя", 'Валера', "Саша", "Даша"]
#while names:
 #   if names.pop()!="Валера":
  #      print("Валера не здесь")
   # else:
    #    print("Валера нашелся")
    #    break

name = str(input('Напиши имя, которое хотите проверить по списку :  '))
def  find_person(name):
    while names:
        if names.pop()!=name:
            print(name," не здесь")
        else:
            print(name," нашелся")
            break
find_person(name)

