print("Title of program: Not_exactly_encouraging_encouragement_bot")
print()
while True:
  description = input("Could you describe how you feel in a word?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("it's not gonna get better if you don't do anything about it. I suggest a game of Among Us that could maybe make you happy instead of sad. Having a victory once in a while can help!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Doing great so far, then. Keep it up, but don't get too happy over it becuase there will be problems later on. I suggest a game of Among Us as a reward, go make a new friend and hopefully not an enemy. You probably wouldnt find them anywhere else though, so don't take them seriously if you dont like them.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think. You might want to take a nap, though. I suggest a game of Among Us to make you feel energised. It is easy to be energised when you are angry, but hopefully not. A change of emotions would be good, though.")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Are you typing in English? I only accept answers in English. "

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
