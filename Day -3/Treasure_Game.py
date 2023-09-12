print('''
                 __
                       ____               /._\
                       \__<---____________X__/  A R I F
                   .-^"~___~Z"^-._`'_____ ___~-.______
      ___,.---==='~[~~7^___^\"-._ 7~_____H__||"-. \__.^~""~"-------...,__
  .--^---+-----------Y /\_/\ Y--^Y [_____H__||   ^._______/"~~~~"^------^---,-
  |______|___________l [/ \] !___l       H  "^----z^------^----------------{
   "~^----....________\^---^/_____\      H    _.-~_____________,...---------^
                      ~"---"~     ~"-----"---^~~~"

                      "Millenium Falcon"
                      
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

place = input("Where do you want to go? Sun or Moon\n")
lowercase_place = place.lower()

if lowercase_place == "sun":
    print('''As you approach the blazing sun, the intense heat becomes unbearable. Your spacecraft's temperature gauge spikes to dangerous levels, and the protective shields start failing. You desperately attempt to veer away, but it's too late.

The searing heat engulfs your spacecraft, melting its hull and engulfing it in flames. The last thing you see is the blinding, fiery surface of the sun as your vessel disintegrates into nothingness.

Game Over!!!

You have been incinerated by the sun's unforgiving wrath. Try again and steer clear of the fiery demise next time!
 Game Over !!!''')
    exit(1)
elif lowercase_place == "moon":
    print("You have reached the moon. Wanna go the outside?\n")
    moon_adventure = input("Type Yes or No\n")
    if moon_adventure.lower() == "no":
        print("Attacked by trout. Game over")
        exit(1)
        
    elif moon_adventure.lower() == "yes":
        print('''You find yourself on the moon's surface, standing before three mysterious doors - one red, one blue, and one green. Each door seems to radiate an otherworldly glow, casting eerie shadows on the lunar soil beneath your feet.

You can't stay on the moon forever, and a sense of urgency grips you. It's clear that one of these doors holds the key to your escape, but choosing the wrong one could lead to an unknown fate.

The red door beckons with an unsettling crimson hue, hinting at possible danger. The green door, on the other hand, emanates an almost unnatural vibrancy, leaving you to wonder what lies beyond.

But it's the blue door that seems the most inviting. Its cool, cerulean glow appears strangely reassuring against the stark lunar backdrop, and you sense that safety might lie just beyond its threshold.

Time is running out. Which door will you choose to lead you back to Earth, and which will you leave behind? The fate of your journey rests on your decision.
''')
        center_adventure = input("Choose a door Red, Blue, Green \n")
        if center_adventure.lower() == "blue":
            print('''With a deep breath and a sense of determination, you reach for the blue door's handle. It opens smoothly, revealing a passage bathed in a soft, calming light. You step through, your heart pounding with anticipation.

As you venture deeper, the passage seems to stretch on endlessly, but a growing feeling of reassurance accompanies you. Finally, you reach the end and find yourself standing in a spacecraft, its control panel indicating a safe return trajectory to Earth.

With a sense of relief and accomplishment, you take your seat, strap in, and initiate the return sequence. The lunar surface slowly recedes, and the vastness of space surrounds you once more.

Hours later, Earth comes into view, a beautiful blue orb hanging in the void. You re-enter the planet's atmosphere and soon touch down safely, greeted by the cheers and applause of mission control.

Congratulations! You've successfully returned from the moon, having chosen the right door and completed your lunar adventure. You are a hero of space exploration!
''')
            
        elif center_adventure.lower() == "red" or center_adventure.lower() == "green":
            print("Game Over")
            exit(1)
            