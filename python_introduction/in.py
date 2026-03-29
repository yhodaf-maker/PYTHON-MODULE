# movies = {
#     "the matrix"
#     "parasite"
#     "inception"
# }
# user_movie = input("Enter a movie you have watched recently: ").lower()
# if user_movie in movies:
#     print("Great choice! That's a fantastic movie."

user_input = input("Enter Y if you would like to play: ").lower().strip()
if user_input == "y":
    print("Let's play!")
       
secret_number = 7
guess = int(input("Guess our number: "))
    
f guess == secret_number:
        print("You guessed correctly!")

elif guess == secret_number + 1 or guess == secret_number - 1:
        print("You were off by one.")

else:
          print("Sorry, that's not correct.")