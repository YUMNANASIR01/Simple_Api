from fastapi import FastAPI

import random

app = FastAPI()

#side hustle
# money_quotes
side_hustles = [
" Hustle is the bridge between a dream and its reality.",
"Talent gives you a head start, but hustle keeps you in the race.",
"The universe rewards consistent effort, not occasional inspiration.",
"Dont just chase success—build it with every step you take.",
"Your future is shaped by what you grind for today.",
"Every no brings you closer to the right yes—keep hustling.",
"Hustle is when your actions speak louder than your excuses.",
"You werent given this dream to quit halfway—keep pushing.",
"Obstacles arent stop signs; they are tests to see how bad you want it.",
"Hustle isnt about luck; its about persistence, discipline, and resilience.",
"The grind knows no shortcuts, only steps forward.",
"Your comfort zone is the enemy of your hustle.",
"Success is built in the early mornings, late nights, and in the moments no one sees.",
"What you do today defines where you will be tomorrow—so make it count.",
"A hustlers mindset: Work until your idols become your rivals.",
"The only competition that truly matters is the one in the mirror.",
"If you are not obsessed with your goals, someone else will be.",
"Hustle is when you turn pain into power and setbacks into comebacks.",
"Doubt kills more dreams than failure ever will, so keep moving.",
"You can have excuses, or you can have results—but never both.",
]

money_quotes = [
    "A wise person should have money in their head, but not in their heart.",
    "The secret to wealth is simple: Find a way to do more for others than anyone else does. Become more valuable. Do more. Give more. Be more. Serve more.",
    "Money often costs too much.",
    "The only way to permanently change your income is to change yourself.",
    "Dont tell me where your priorities are. Show me where you spend your money, and Ill tell you what they are.",
    "Its not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for.",
    "The more you learn, the more you earn.",
    "Formal education will make you a living; self-education will make you a fortune.",
    "If you dont find a way to make money while you sleep, you will work until you die.",
    "Money is a terrible master but an excellent servant.",
    "The best investment you can make is in yourself.",
    "Wealth consists not in having great possessions, but in having few wants.",
    "Compound interest is the eighth wonder of the world. He who understands it, earns it; he who doesnt, pays it.",
    "If you think nobody cares if youre alive, try missing a couple of car payments.",
    "Do not save what is left after spending; instead, spend what is left after saving.",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing.",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
    "Every time you borrow money, youre robbing your future self.",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work.",
    "Money is a universal passport to everywhere except heaven.",
]

@app.get("/side_hustles")
def get_side_hustle():
    """ Returns a random side hustle idea """
    return{"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
      """ Returns a random money quotes """
     
      return{"money_quote": random.choice(money_quotes)}
  