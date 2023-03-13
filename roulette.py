import random
black=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
red=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
green=[0,37]
def even(betmoney):
    global black, red, green
    trialvalue=random.randint(0,37)
    bets=["black","red"]
    bet=random.choice(bets)
    print("Bet ", bet)
    if trialvalue in red:
        if bet=="red":
            return betmoney
        return -1 * betmoney
    if trialvalue in black:
        if bet=="black":
            return betmoney
        return -1*betmoney
    if trialvalue in green:
        return -1*betmoney
def twoone(betmoney):
    global black, red, green
    trialvalue=random.randint(0,37)
    bets=[1,2,3]
    bet=random.choice(bets)
    print("Bet ", bet)
    if trialvalue>=1 and trialvalue<=12:
        if bet==1:
            return 2*betmoney
        return -1 * betmoney
    if trialvalue>=13 and trialvalue<=24:
        if bet==2:
            return 2*betmoney
        return -1 * betmoney
    if trialvalue>=25 and trialvalue<=36:
        if bet==3:
            return 2*betmoney
        return -1 * betmoney
    if trialvalue in green:
        return -1*betmoney
def thirtyfive(betmoney, input):
    global black, red, green
    trialvalue=random.randint(0,37)
    if trialvalue==input:
        return 35*betmoney
    return -1*betmoney
print("Enter your initial amount")
money=int(input())
print("Enter the number of trials (Or until you have nothing left)")
trials=int(input())
print("Type of bet: Even bet(1) Two to one bet(2) 35 to 1 bet(3)")
bettype=int(input())
auto='A'
if (auto == 'A'):
    print("Enter bet per trial")
    bet=int(input())
    if bet>money:
        print("Bet is greater than money")
        exit()
    if (bettype == 1):
        for i in range(trials):
            res=even(bet)
            # print(res)
            money=money+res
            if res>0:
                game="won"
            else:
                game="lost"
            print("Trial ", i, "Money ", money, "Game ", game)
            if money<=0:
                print("You are out of money")
                exit()
            # print("Trial ", i, "Money ", money)
    if (bettype == 2):
        for i in range(trials):
            res=twoone(bet)
            money=money+res
            if res>0:
                game="won"
            else: game="lost"
            print("Trial ", i, "Money ", money, "Game ", game)
            if money<=0:
                print("You are out of money")
                exit()
            # print("Trial ", i, "Money ", money)
    if (bettype == 3):
        for i in range(trials):
            # print("Enter the number you want to bet on")
            # input=10
            input=random.randint(0,37)
            # input=input()
            res=thirtyfive(bet, input)
            money=money+res
            if res>0:
                game="won"
            else: game="lost"
            print("Trial ", i,"Input ",input,  "Money ", money, "Game ", game)
            if money<=0:
                print("You are out of money")
                exit()
            # print("Trial No.: ", i, "  Money left", money)
    

