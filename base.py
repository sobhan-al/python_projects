import time, random, re

print("Hi it is a little quize to measure your typing speed.\nlets do this😉")
print("\nWe have a test based on the number of sentences you choose.")

def speed(wpm, accuracy):
    return wpm * accuracy

data1 = ['The sun is bright today', 'I like to read books', 'She has a small cat',
          'We play every day', 'This is my house', 'He drinks cold water', 'The dog runs fast', 'Open the window please',
            'Close the door now', 'My friend is kind', 'I have a new pen', 'The sky is blue', 'They eat fresh fruit',
              'The baby is sleeping', 'Time goes very fast', 'Please write your name', 'The bird can fly', 'We love good music',
                'Today is a nice day', 'The phone is ringing', 'The tree is very tall', 'I need some help', 'The coffee is hot',
                  'My family is happy', 'The bus is coming', 'She wears a blue dress', 'The school is nearby', 'He likes to swim',
                    'We enjoy long walks', 'The food tastes good', 'Please keep it clean', 'I found my keys', 'The movie was funny', 'Everyone is ready',
                      'The train arrived early', 'This chair is comfortable', 'The room looks clean', 'He bought a new bag', 'The flowers smell nice',
                        'Learning is always useful', 'The child is smiling', 'I can solve this', 'The river is calm', 'We work as a team',
                          'Your answer is correct', 'The weather feels warm', 'Please speak slowly', 'The game is exciting', 'Every day is different',
                            'Success comes with practice']
data2 = ['The weather looks perfect for a long walk in the park.', 'I finished my homework before going out with my friends.', 'Please remember to lock the door before leaving the house.',
          'She enjoys reading novels while drinking a cup of hot coffee.', "The meeting will begin exactly at nine o'clock tomorrow morning.", 'Learning a new language takes patience, practice, and consistency.', 'We decided to travel by train instead of driving this weekend.', 'The computer suddenly restarted while I was saving my project.', 'My brother usually wakes up earlier than everyone else in the family.', 'A healthy breakfast gives you energy for the rest of the day.', 'The teacher explained the lesson in a simple and clear way.',
            'They watched the beautiful sunset from the top of the hill.', 'I forgot my wallet, so my friend paid for lunch.', 'The little girl smiled when she received her birthday gift.', 'Please check your email before submitting the final application.', 'The restaurant serves delicious food at a reasonable price.', 'Our team worked together to complete the project on time.', 'The library is quiet, making it a great place to study.', 'He bought a new laptop because his old one was slow.', 'The bus arrived late due to heavy traffic in the city.',
              'Everyone applauded after the musician finished the amazing performance.', 'She carefully organized all her files into separate folders.', 'The movie was interesting, but the ending was unexpected.', 'I always keep a bottle of water on my desk.', 'The manager thanked everyone for their hard work this month.', 'We spent the afternoon cleaning the garage and organizing tools.', 'The internet connection became unstable during the online meeting.', 'My grandmother tells wonderful stories about her childhood adventures.',
                'Please double-check your answers before clicking the submit button.', 'The airport was crowded because many flights were delayed today.', 'He practices playing the guitar for at least one hour daily.', 'The garden looks beautiful after the fresh spring rain.', 'Small improvements every day can lead to great success.', 'The customer politely asked for a refund after finding the problem.', 'She quickly packed her suitcase before leaving for the airport.', 'We ordered pizza because nobody wanted to cook dinner tonight.',
                  'The museum displayed ancient paintings from different parts of Europe.', 'My phone battery was almost empty before I reached home.', 'The coach encouraged every player to stay focused until the end.', 'The company introduced several new features in the latest update.', 'I enjoy listening to relaxing music while working on difficult tasks.', 'The children laughed loudly as they played outside together.', 'He forgot the meeting because his calendar reminder was disabled.', 'The coffee shop across the street opens very early every morning.',
                    'Taking short breaks can improve both focus and productivity.', 'She carefully followed the recipe and the cake turned out perfect.', 'The customer support team responded within a few minutes.', 'Every challenge is an opportunity to learn something valuable.', 'Please keep your password secure and never share it with anyone.', 'Success usually comes from dedication, effort, and continuous learning.']


ready = input("Are you ready?")
while ready == 'yes':
    sentences = int(input("How many sentence you want?(more than 3!)"))
    
    if sentences % 2 != 0:
        items1 = random.sample(data1, int(sentences/4*3)+1)
        items2 = random.sample(data2, int(sentences/4))
    else:
        items1 = random.sample(data1, sentences/4*3)
        items2 = random.sample(data2, sentences/4)
    items = items1 + items2
    matn = random.sample(items, sentences)
    text = ""
    for i in matn:
        text += i + " "

    print("Type this letter as fastest as you can:\n")

    start = time.time()
    letter = input(text+"\nAwnser:")
    end = time.time()
    
    timing = end - start   



