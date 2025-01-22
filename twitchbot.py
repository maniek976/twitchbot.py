import random
import time
import pyautogui

print("""
████████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗██████╗  ██████╗ ████████╗
╚══██╔══╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║ █╗ ██║██║   ██║   ██║     ███████║██████╔╝██║   ██║   ██║   
   ██║   ██║███╗██║██║   ██║   ██║     ██╔══██║██╔══██ ██║   ██║   ██║   
   ██║   ╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║██████  ╚██████╔╝   ██║   
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═══╝    ╚═════╝    ╚═╝     
                                                                         

MADE BY MANIEK976

Version: Alpha 1.0

Instruction Manual: How to Use the Bot // Instrukcja obsługi: Jak korzystać z bota
ENG: The bot automatically selects a message from the list,
 types it into the active chat window, and sends it 
by pressing 'Enter'. Make sure the Twitch chat window
 is active while the program is running

 To change a game just restart a program :)

Come to my discord:
discord.com/invite/pcaWuXfmA9
""")

print("""Wybierz gre//Choose a game
1 - Valorant
2 - CS2
""")

game_choice = input("Wybierz grę (1 lub 2)//Choose a game (1 or 2): ")

messages_valorant = [
    "Nice shockdarts, Sova!",
    "Clean headshot! 🔥",
    "GG EZ Ace! 😎",
    "Clutch or kick! 😅",
    "Insane flicks! 😮",
    "Cypher cams on point! 📸",
    "Jett diff right there!",
    "Solid comms, team! 🎧",
    "You’re cracked with the Phantom!",
    "Omen TP plays are wild! 😳",
    "Spike planted! 💣",
    "That was a nasty wallbang!",
    "Amazing spray control!",
    "Reyna with the hard carry! 💜",
    "Sage heals are lifesavers! 💉",
    "Great post-plant setup!",
    "Clutch king/queen! 👑",
    "Watch out for flanks! 👀",
    "Viper ult is terrifying! 🐍",
    "Smooth Operator plays! 🎯",
    "What a lineup! 🎯",
    "Nice eco round win! 💰",
    "Let’s gooo, full buy! 💵",
    "That Ace was insane! 🤯",
    "Your crosshair placement is 🔥!",
    "Amazing utility usage!",
    "Don’t peek, they’re holding! 😬",
    "Wallhack moments lol! 😂",
    "RIP enemy team 😅",
    "Outplayed and outsmarted! 🧠",
    "Quick reflexes! 👏",
    "The enemy team is molding! 😆",
    "Clean retake strategy!",
    "Great prefire angle!",
    "Your aim is so satisfying to watch!",
    "Nice lurk plays!",
    "Tactical timeout vibes! ⏱️",
    "They didn’t stand a chance!",
    "GG WP! 👏",
    "That’s some 200 IQ gameplay! 🤯",
    "You’re carrying so hard! 🏋️",
    "Nice entry fragging! 🔥",
    "Did that actually work?! 😂",
    "The lineups are crazy good!",
    "What a spray transfer!",
    "Those knives were on point! ✨",
    "Nice clutch, Sova main!",
    "Why are you so good?! 😳",
    "Unstoppable Jett plays! 🌪️",
    "That’s a Valorant highlight moment! 🌟",
    "Great shot, Sova!",
    "Clean headshot! 🔥",
    "GG, easy play! 😎",
    "Clutch or kick! 😅",
    "Amazing flicks! 😮",
    "Cypher set up the cams perfectly! 📸",
    "Jett is on fire!",
    "Solid comms, team! 🎧",
    "You're carrying with the Phantom!",
    "Omen's TP plays are wild! 😳",
    "Spike planted! 💣",
    "That was an incredible wallbang!",
    "Perfect spray control!",
    "Reyna’s hard carry is unreal! 💜",
    "Sage’s heals are lifesaving! 💉",
    "Great post-plant setup!",
    "Clutch king/queen! 👑",
    "Watch for flanks! 👀",
    "Viper’s ult is terrifying! 🐍",
    "Operator plays are on point! 🎯",
    "What a lineup! 🎯",
    "Eco round win! 💰",
    "Let’s go, full buy! 💵",
    "That Ace was insane! 🤯",
    "Your crosshair placement is 🔥!",
    "Awesome utility usage!",
    "Don’t peek, they’re holding! 😬",
    "Wallhack moments, lol! 😂",
    "RIP, enemy team! 😅",
    "Outplayed and outsmarted! 🧠",
    "Quick reflexes! 👏",
    "The enemy team is tilting! 😆",
    "Clean retake strategy!",
    "Great prefire angle!",
    "Your aim is so satisfying to watch!",
    "Nice lurk plays!",
    "Tactical timeout vibes! ⏱️",
    "They didn’t stand a chance!",
    "GG WP! 👏",
    "That’s some 200 IQ gameplay! 🤯",
    "You’re carrying so hard! 🏋️",
    "Nice entry fragging! 🔥",
    "Did that really work?! 😂",
    "Lineups are crazy good!",
    "What a spray transfer!",
    "Those knives were on point! ✨",
    "Nice clutch, Sova main!",
    "Why are you so good?! 😳",
    "Unstoppable Jett plays! 🌪️",
    "That’s a Valorant highlight moment! 🌟",
    "That’s some insane gameplay! 😱",
    "Clutch moments for the win! 👑",
    "Can’t stop, won’t stop! 🔥",
    "Amazing trade, well done! 💪",
    "Unbelievable clutch! 🤯",
    "Absolutely cracked! 🔥",
    "Sage’s wall saves the day! 💉",
    "Unstoppable aim! 🎯",
    "Great job, team! 👏",
    "That was fire! 🔥",
    "Epic shot! 💥",
    "You’re an absolute legend! 🤩",
    "That was too good! 🔥",
    "Clutch play of the century! 👑",
    "Clean kills all round! 💥",
    "Nice job, everyone! 👏",
    "Perfectly executed plan! 🎯",
    "Epic clutch, you saved us! 👑",
    "Headshot king! 👑",
    "Nice positioning! 🎯",
    "This is too good! 🔥",
    "Such good teamwork! 👏",
    "Amazing comeback! 💪",
    "You’re a beast! 🦁",
    "That was insane, GG! 😱",
    "You’ve got this! 🔥",
    "Nice, let’s go! 🎯",
    "That was epic! 💥",
    "Clean play, GG! 👏",
    "You carried that round! 💪",
    "So clean, wow! 🤩",
    "Incredible round! 🔥",
    "Fantastic play, team! 👏",
    "You’re a pro! 🎯",
    "Great entry frag! 💥",
    "Solid retake! 🔥",
    "Best play of the match! 🎯",
    "Absolutely savage plays! 💥",
    "You’re dominating! 🔥",
    "Flawless round! 👑",
    "Epic win, great job! 💥",
    "Unbelievable plays! 😱",
    "Best clutch ever! 👑",
    "You’re unstoppable! 🌪️"
]


messages_cs2 = [
    "Nice shot, bro!",
    "GG, well played!",
    "POG moment!",
    "That flick was insane!",
    "Headshot!",
    "Let’s goooo!",
    "Wooo, that was close!",
    "Clutch or kick!",
    "Epic play!",
    "You got this!",
    "Nice aim!",
    "Lucky shot!",
    "Pure skill!",
    "Big brain play!",
    "Keep it up!",
    "Easy clap!",
    "Nice spray control!",
    "That was fire!",
    "Monster kill!",
    "10/10 aim!",
    "So smooth!",
    "Good job, teammate!",
    "POGChamp!",
    "Oof, unlucky!",
    "You’re on fire!",
    "Big poggers!",
    "Good round!",
    "That was filthy!",
    "You’re a beast!",
    "Lmao, nice try!",
    "Let’s go team!",
    "Mad respect!",
    "Clean shot!",
    "Super clutch!",
    "Let’s win this!",
    "You’re carrying us!",
    "That was nuts!",
    "GG, let’s go again!",
    "Big pog!",
    "Carry us, pls!",
    "What a play!",
    "That flick tho!",
    "You’re cracked!",
    "Epic kill!",
    "Let’s get this dub!",
    "That was insane!",
    "You’re insane!",
    "Nice one, bro!",
    "So clean!",
    "You’re too good!",
    "Just too good!",
    "GG, nice effort!",
    "Big plays, big wins!",
    "I’m dead lol!",
    "Such a good round!",
    "That was wild!",
    "Let’s push!",
    "Get those headshots!",
    "One more, we got this!",
    "Full focus!",
    "Clutch God!",
    "Nice teamwork!",
    "I believe in you!",
    "Let's go for the win!",
    "POGgers!",
    "That was epic!",
    "Clean win!",
    "Go, go, go!",
    "On point, bro!",
    "Let’s smash this!",
    "You’re a pro!",
    "That’s a W!",
    "So slick!",
    "Let’s crush it!",
    "GG, let’s go again!",
    "Keep those kills coming!",
    "Nice round!",
    "Almost there!",
    "Let’s make this comeback!",
    "Big brain moves!",
    "Great teamwork!",
    "Full focus now!",
    "I see you!",
    "Nice trade!",
    "That’s a dub!",
    "Game changer!",
    "Keep it up, team!",
    "Another round, let’s go!",
    "Impressive play!",
    "You’re on fire today!",
    "Smooth operator!",
    "Best play!",
    "Big plays incoming!",
    "Crazy game!",
    "You're cracked today!",
    "That shot was deadly!",
    "Carrying the team!",
    "Let's clutch this!",
    "Win this for us!",
    "Nice kill!"
]


if game_choice == "1":
    messages = messages_valorant
    print("Tryb Valorant został wybrany.")
elif game_choice == "2":
    messages = messages_cs2
    print("Tryb CS2 został wybrany.")
else:
    print("Niepoprawny wybór, domyślnie uruchamiany tryb Valorant.")
    messages = messages_valorant

while True:
    message = random.choice(messages)
    pyautogui.typewrite(message)  
    pyautogui.press("enter")  
    wait_time = random.randint(15, 45)  
    time.sleep(wait_time)  
