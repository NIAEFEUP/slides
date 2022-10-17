answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

sword = False

def intro():
  print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")

  print("A. Grab a nearby rock and throw it at the orc")
  print("B. Lie down and wait to be mauled")
  print("C. Run")

  choice = str(input())

  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print("Welp, that was quick. You died!")
  elif choice in answer_C:
    option_run()

def option_rock():
  print("The orc is stunned, but regains control. He begins running towards you again.")

  print("A. Run")
  print("B. Throw another rock")
  print("C. Run towards a nearby cave")

  choice = str(input())
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print("The rock flew well over the orcs head. You missed. You died!")
  elif choice in answer_C:
    option_cave()

def option_cave():
  print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")

  choice = str(input())
  if choice in yes:
    sword = True
  elif choice in no:
    sword = False

  print("What do you do next?")

  print("A. Hide in silence")
  print("B. Fight")
  print("C. Run")

  choice = str(input())
  if choice in answer_A:
    print("I think orcs can see very well in the dark, right? You died!")
  elif choice in answer_B:
    if sword == False:
      print("You're defenseless. You died!")
    elif sword == True:
      print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
  elif choice in answer_C:
    print("The orc turns around and sees you running.")
    option_run()

def option_run():
  print("You run as quickly as possible.")

  print("A. Hide behind boulder")
  print("B. Trapped, so you fight")
  print("C. Run towards an abandoned town")

  choice = str(input())

  if choice in answer_A:
    print("You're easily spotted. You died!")
  elif choice in answer_B:
    print("You're no match for an orc. You died!")
  elif choice in answer_C:
    option_town()

def option_town():
  print("You notice a purple flower near your foot. Do you pick it up? Y/N")

  choice = str(input())

  if choice in yes:
    print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
  elif choice in no:
    print("Maybe you should have picked up the flower. You died!")

intro()
