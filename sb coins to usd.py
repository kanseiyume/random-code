'''

USD = US dollar
SBG = Skyblock Gems
SBC = Skyblock Coins
CK = booster cookie
$5 USD = 675 SBG
1 CK = 325 SBG
2.0769 CK = 675 SBG = $5 USD
'''

import os, time
os.system('cls' if os.name == 'nt' else 'clear')

while True:
        
        money = input("how much are you willing to spend on skyblock? ")
        money = float(money)
        if money < 5:
            print("gems packages start at $5, try again")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        if money >= 5:
            break

print("for " + str(int(money)) + " USD, you can buy:")
time.sleep(.75)
print(str(int(money/5*675)) + " skyblock gems")
time.sleep(.75)
print(str(int(money/5*675/325)) + " booster cookies")
time.sleep(.75)
print("roughly " + str(int(money/5*675/325*9500000)) + " sb coins (from selling the cookies at bazaar @ 9.5m coins per)")
time.sleep(3)
