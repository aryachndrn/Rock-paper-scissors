import random
    
def play(x,y):
    
    if(x==y):
        return "It's a tie"
    elif(x=='r' and y=='p')or(x=='p'and y=='s') or (x=='s' and y=='r'):
        return "The computer won!, better luck next time"
    else:
        return "Woohoo You won!"

user=input("Choose 'r' for rock,'p' for paper and 's' for scissor\n")
comp=random.choice(['r','p','s'])
print(f"You chose {user} and computer chose {comp}")
print(play(user,comp))
