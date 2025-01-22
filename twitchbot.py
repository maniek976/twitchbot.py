import tkinter as tk
import random
import pyautogui
import time

messages_valorant = [
    "Nice shockdarts, Sova!",
    "Clean headshot!",
    "GG EZ Ace!",
    "Clutch or kick!",
    "Insane flicks!",
    "Cypher cams on point!",
    "Jett diff right there!",
    "Solid comms, team!",
    "You’re cracked with the Phantom!",
    "Omen TP plays are wild!",
    "Spike planted!",
    "That was a nasty wallbang!",
    "Amazing spray control!",
    "Reyna with the hard carry!",
    "Sage heals are lifesavers!",
    "Great post-plant setup!",
    "Clutch king!",
    "Watch out for flanks!",
    "Viper ult is terrifying!",
    "Smooth Operator plays!",
    "What a lineup!",
    "Nice eco round win!",
    "Let’s gooo, full buy!",
    "That Ace was insane!",
    "Your crosshair placement is on point!",
    "Amazing utility usage!",
    "Don’t peek, they’re holding!",
    "Wallhack moments lol!",
    "RIP enemy team",
    "Outplayed and outsmarted!",
    "Quick reflexes!",
    "The enemy team is molding!",
    "Clean retake strategy!",
    "Great prefire angle!",
    "Your aim is so satisfying to watch!",
    "Nice lurk plays!",
    "Tactical timeout vibes!",
    "They didn’t stand a chance!",
    "GG WP!",
    "That’s some 200 IQ gameplay!",
    "You’re carrying so hard!",
    "Nice entry fragging!",
    "Did that actually work?!",
    "The lineups are crazy good!",
    "What a spray transfer!",
    "Those knives were on point!",
    "Nice clutch, Sova main!",
    "Why are you so good?!",
    "Unstoppable Jett plays!",
    "That’s a Valorant highlight moment!",
    "Great shot, Sova!",
    "Clean headshot!",
    "GG, easy play!",
    "Cypher set up the cams perfectly!",
    "Jett is on fire!",
    "Solid comms, team!",
    "You're carrying with the Phantom!",
    "Omen's TP plays are wild!",
    "Spike planted!",
    "That was an incredible wallbang!",
    "Perfect spray control!",
    "Reyna’s hard carry is unreal!",
    "Sage’s heals are lifesaving!",
    "Great post-plant setup!",
    "Clutch king!",
    "Watch for flanks!",
    "Viper’s ult is terrifying!",
    "Operator plays are on point!",
    "What a lineup!",
    "Eco round win!",
    "Let’s go, full buy!",
    "That Ace was insane!",
    "Your crosshair placement is fire!",
    "Awesome utility usage!",
    "Don’t peek, they’re holding!",
    "Wallhack moments, lol!",
    "RIP, enemy team!",
    "Outplayed and outsmarted!",
    "Quick reflexes!",
    "The enemy team is tilting!",
    "Clean retake strategy!",
    "Great prefire angle!",
    "Your aim is so satisfying to watch!",
    "Nice lurk plays!",
    "Tactical timeout vibes!",
    "They didn’t stand a chance!",
    "GG WP!",
    "That’s some 200 IQ gameplay!",
    "You’re carrying so hard!",
    "Nice entry fragging!",
    "Did that really work?!",
    "Lineups are crazy good!",
    "What a spray transfer!",
    "Those knives were on point!",
    "Nice clutch, Sova main!",
    "Why are you so good?!",
    "Unstoppable Jett plays!",
    "That’s a Valorant highlight moment!",
    "That’s some insane gameplay!",
    "Clutch moments for the win!",
    "Can’t stop, won’t stop!",
    "Amazing trade, well done!",
    "Unbelievable clutch!",
    "Absolutely cracked!",
    "Sage’s wall saves the day!",
    "Unstoppable aim!",
    "Great job, team!",
    "That was fire!",
    "Epic shot!",
    "You’re an absolute legend!",
    "That was too good!",
    "Clutch play of the century!",
    "Clean kills all round!",
    "Nice job, everyone!",
    "Perfectly executed plan!",
    "Epic clutch, you saved us!",
    "Headshot king!",
    "Nice positioning!",
    "This is too good!",
    "Such good teamwork!",
    "Amazing comeback!",
    "You’re a beast!",
    "That was insane, GG!",
    "You’ve got this!",
    "Nice, let’s go!",
    "That was epic!",
    "Clean play, GG!",
    "You carried that round!",
    "So clean, wow!",
    "Incredible round!",
    "Fantastic play, team!",
    "You’re a pro!",
    "Great entry frag!",
    "Solid retake!",
    "Best play of the match!",
    "Absolutely savage plays!",
    "You’re dominating!",
    "Flawless round!",
    "Epic win, great job!",
    "Unbelievable plays!",
    "Best clutch ever!",
    "You’re unstoppable!",
    "What’s your favorite map?",
    "What’s your go-to gun?",
    "Do you have a favorite skin?",
    "Which agent do you prefer to play?",
    "What’s your opinion on Icebox?",
    "Do you prefer Phantom or Vandal?",
    "What skin are you rocking today?",
    "Do you have a favorite Valorant weapon skin?",
    "What’s your highest rank?",
    "How do you feel about split in competitive?",
    "What’s the most difficult map for you?",
    "How do you feel about the new agent?",
    "What’s your favorite ult to use?",
    "Do you have a favorite clutch moment?"
]

messages_cs2 = [
    "Nice shot, bro!",
    "Clean headshot!",
    "GG, easy clutch!",
    "Great spray control!",
    "Bomb planted!",
    "Perfect A site hold!",
    "Nice eco round win!",
    "Fantastic smoke play!",
    "Flawless round!",
    "Nice wallbang!",
    "Amazing trade frag!",
    "You’re carrying hard!",
    "Incredible flick shot!",
    "That’s a CS2 highlight moment!",
    "Great team play, guys!",
    "Clutch or kick!",
    "Nice flash assist!",
    "Good job with the bomb!",
    "Outplayed, well done!",
    "Great positioning on site!",
    "That was an epic round!",
    "Perfect timing!",
    "You’re on fire today!",
    "Nice entry fragging!",
    "Smooth AWP shots!",
    "One tap wonder!",
    "Great trade, let’s go!",
    "Flank secured!",
    "Well played, team!",
    "Nice rotation!",
    "Epic comeback!",
    "You’re a clutch master!",
    "Solid utility usage!",
    "The enemy team didn’t stand a chance!",
    "Nice retake strategy!",
    "Great prefire angles!",
    "Clean B site hold!",
    "You’re a CS2 legend!",
    "Epic clutch moment!",
    "Nice aim, bro!",
    "How’s your aim so smooth?",
    "That was sick!",
    "You’re on fire today!",
    "What’s your rank?",
    "You’re cracked, no cap!",
    "Nice flick, bro!",
    "Are you in a team?",
    "GG, carry us!",
    "That clutch was insane!",
    "How long have you been playing CS2?",
    "That spray control tho!",
    "You’re literally popping off!",
    "You got this!",
    "Who taught you that flick?",
    "What mouse are you using?",
    "That was a textbook play!",
    "Big plays, big wins!",
    "How many kills you got so far?",
    "You make it look easy!",
    "That was a beautiful headshot!",
    "What’s your favorite gun?",
    "I need to learn those moves!",
    "Do you play other FPS games?",
    "I swear you’re a wallhack god!",
    "That was a fast reaction!",
    "How much FPS do you get?",
    "You're carrying the whole team!",
    "Let’s win this, easy!",
    "Best play of the game right there!",
    "What’s your elo right now?",
    "Do you stream often?",
    "How do you pre-aim like that?",
    "That was dirty shot!",
    "You’re literally god-tier!",
    "What’s your secret to aiming?",
    "How do you do that with pistols?",
    "Can I join you next round?",
    "I love how you play!",
    "What's your setup like?",
    "That was insane, dude!",
    "How do you have so much game sense?",
    "That flick was ridiculous!",
    "Let’s get that MVP!",
    "Can you teach me some tricks?",
    "Your positioning is so good!",
    "You always have the best timing!",
    "How do you handle pressure like that?",
    "Can I get some coaching?",
    "How do you keep calm in clutch situations?",
    "Nice entry frag!",
    "You’re popping off today!",
    "That flick was on point!",
    "Nice trade frag!",
    "That’s how it’s done!",
    "Sick wallbang!",
    "You’re a beast!",
    "Pog play!",
    "No way you just hit that!",
    "Good rotation!",
    "Clutch king!",
    "Keep it up, we’re winning this!",
    "You’ve got this in the bag!",
    "Great awareness!",
    "That was a perfect prefire!",
    "Unstoppable!",
    "Let’s keep this momentum going!",
    "Solid plays all round!",
    "So clean, bro!",
    "Big brain plays!",
    "That’s how you carry!",
    "Best round yet!",
    "Let’s push A!",
    "Nice, we’re getting better!",
    "That was dirty!",
    "So much skill!",
    "Great teamwork, guys!",
    "Fast reactions, love it!",
    "Nice job holding B!",
    "Keep it going, team!",
    "That was an insane retake!",
    "Perfect smoke, well done!",
    "Amazing teamwork!",
    "You’re unstoppable!",
    "Sick flick shot!",
    "Amazing round, guys!",
    "Nice retake!",
    "Great teamwork in that clutch!",
    "You’re carrying me, bro!",
    "Epic game, let’s win this!",
    "You’re making it look easy!",
    "That was beautiful!",
    "No way you just did that!",
    "Nice wallbang on A!",
    "Nice flank, bro!",
    "Clutch or nothing!",
    "Best clutch I’ve ever seen!",
    "You’re on a whole other level!",
    "You’re so quick!",
    "Best team player right here!",
    "You make this look so easy!",
    "That’s how you do it!",
    "What a round!",
    "Unreal game sense!"
]


def send_message(min_time, max_time):
    global messages
    message = random.choice(messages)  
    
    pyautogui.typewrite(message)  
    pyautogui.press('enter')  
    
    next_time = random.randint(min_time, max_time) * 1000  
    root.after(next_time, send_message, min_time, max_time)  

def choose_game_mode():
    global messages
    game_choice = game_mode.get()  
    if game_choice == "Valorant":
        messages = messages_valorant
        print("Valorant mode selected.")
    elif game_choice == "CS2":
        messages = messages_cs2
        print("CS2 mode selected.")
    else:
        messages = messages_valorant
        print("Invalid selection, defaulting to Valorant.")
    
    try:
        min_time = int(min_time_entry.get())
        max_time = int(max_time_entry.get())
        if min_time > max_time:
            print("Minimalny czas nie może być większy od maksymalnego.")
            return
    except ValueError:
        print("Proszę wpisać poprawne liczby.")
        return
    
    send_message(min_time, max_time)

root = tk.Tk()
root.title("Message Sender")

welcome_text = """
████████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗██████╗  ██████╗ ████████╗
╚══██╔══╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║ █╗ ██║██║   ██║   ██║     ███████║██████╔╝██║   ██║   ██║   
   ██║   ██║███╗██║██║   ██║   ██║     ██╔══██║██╔══██ ██║   ██║   ██║   
   ██║   ╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║██████  ╚██████╔╝   ██║   
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═══╝    ╚═════╝    ╚═╝     

MADE BY MANIEK976

Come to my discord:
discord.com/invite/pcaWuXfmA9
To change any settings pls restart program
"""
welcome_label = tk.Label(root, text=welcome_text, font=("Courier", 12), padx=10, pady=10)
welcome_label.pack()

game_mode = tk.StringVar(value="Valorant")  
valorant_radio = tk.Radiobutton(root, text="Valorant", variable=game_mode, value="Valorant")
cs2_radio = tk.Radiobutton(root, text="CS2", variable=game_mode, value="CS2")
valorant_radio.pack()
cs2_radio.pack()

min_time_label = tk.Label(root, text="Minimalny czas (sekundy):")
min_time_label.pack()

min_time_entry = tk.Entry(root)
min_time_entry.insert(0, "15")  
min_time_entry.pack()

max_time_label = tk.Label(root, text="Maksymalny czas (sekundy):")
max_time_label.pack()

max_time_entry = tk.Entry(root)
max_time_entry.insert(0, "45")  
max_time_entry.pack()

start_button = tk.Button(root, text="Start Sending Messages", command=choose_game_mode)
start_button.pack(pady=20)

root.mainloop()
