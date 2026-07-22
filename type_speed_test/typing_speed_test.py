import time, random, re

print("Hi it is a little quize to measure your typing speed.\nlets do this😉")
print("\nWe have a test based on the number of sentences you choose.✔️")

def speed(wpm, accuracy):
    return round((wpm * accuracy),1)

data1 = [
        "The sun is bright today.", "I like to read books.", "She has a small cat.", "We play every day.", "This is my house.",
        "He drinks cold water.", "The dog runs fast.", "Open the window please.", "Close the door now.", "My friend is kind.", 
        "The sky is blue.", "They eat fresh fruit.", "The baby is sleeping.", "Time goes very fast.", "Please write your name.",
        "The bird can fly.", "We love good music.", "Today is a nice day.", "The phone is ringing.", "The tree is very tall.",
        "My family is happy.", "The bus is coming.", "The school is nearby.", "He likes to swim.", "We enjoy long walks.",
        "The food tastes good.", "Please keep it clean.", "Everyone is ready.", "The train arrived early.", "This chair is comfortable.",
        "The flowers smell nice.", "The child is smiling.", "The river is calm.", "We work as a team.", "Your answer is correct.",
        "The room looks clean.", "The coffee is hot.","I have a new pen.", "Success comes with practice."]

data2 = [
    "I finished my homework before going out with my friends.","Please remember to lock the door before leaving the house.",
    "She enjoys reading novels while drinking a cup of hot coffee.","Learning a new language takes patience, practice, and consistency.",
    "We decided to travel by train instead of driving this weekend.","The computer suddenly restarted while I was saving my project.",
    "My brother usually wakes up earlier than everyone else in the family.","A healthy breakfast gives you energy for the rest of the day.",
    "The teacher explained the lesson in a simple and clear way.","They watched the beautiful sunset from the top of the hill.",
    "I forgot my wallet, so my friend paid for lunch.","The little girl smiled when she received her birthday gift.",
    "Please check your email before submitting the final application.","The restaurant serves delicious food at a reasonable price.",
    "The weather looks perfect for a long walk in the park."]

ready = input("Are you ready?(yes or no)")
while ready == "yes":
  def sentent():
    sentences = input("How many sentence you want?(between 4 and 50)")
    if sentences.isdigit():
      return sentences
    else:
      print("Wrong awnser!")
      sentent()

      
  sentences = sentent()
  sentences = int(sentences)
  items1 = random.sample(data1, int(sentences/4*3)+1)
  items2 = random.sample(data2, int(sentences/4))
  items = items1 + items2
  matn = random.sample(items, sentences)
  text = ""
  for i in matn:
    text += i + " "

  print("Type this letter as fastest as you can:\n")
  start = time.time()
  letter = input(text+"\nAwnser:")
  end = time.time()
  timing = round((end - start),2)   
  minet = round((timing/60),2)

  last_words = letter.split(" ")
  word_counter = 0
  for i in last_words:
    word_counter += 1
  wpm = round((word_counter/minet),2)
  #Words per minet

  text = text.split(" ")
  letter = letter.split(" ")
  number_of_wrong_letters = 0
  for i in range(word_counter):
    one =[]
    for j in text[i]:
      one.append(j)
    two =[]
    for k in letter[i]:
      two.append(k)

    for j,k in zip(one,two):
      if j == k:
        pass
      else:
        print(j,k)
        number_of_wrong_letters += 1

  all_letters = 0
  for i in text:
    for j in i:
      all_letters += 1
  accuracy = round(((all_letters - number_of_wrong_letters)/all_letters),2)
  #Percentage of correct writing of letters based on total letters

  score = speed(wpm,accuracy)
  print(f"wpm: {wpm}⭐")
  print(f"accuracy: {accuracy}⭐")
  print(f"\nSpeed: {score} words per minet💡")

  ready = input("Are you ready for more quize?😉(yes or no)")
