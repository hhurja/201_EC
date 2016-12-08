class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'





instruction = "Please enter a(n) "

print "\n****  Welcome to Mad Libs!  ****\n"

words = []


words.append(raw_input(instruction + "adjective: "))
words.append(raw_input(instruction + "noun: "))
words.append(raw_input(instruction + "verb past tense: "))
words.append(raw_input(instruction + "adverb: "))
words.append(raw_input(instruction + "adjective: "))
words.append(raw_input(instruction + "noun: "))
words.append(raw_input(instruction + "noun: "))
words.append(raw_input(instruction + "adjective: "))
words.append(raw_input(instruction + "verb: "))
words.append(raw_input(instruction + "adverb: "))
words.append(raw_input(instruction + "verb past tense: "))
words.append(raw_input(instruction + "adjective: "))

print "\n****  Your story is:  ****\n"


print "Today I went to the zoo. I saw a _"+ color.UNDERLINE +words[0]+ color.END + "_"
print "_"+ color.UNDERLINE +words[1]+ color.END + "_ jumping up and down in its tree. He"
print "_"+ color.UNDERLINE +words[2]+ color.END + "_ _"+ color.UNDERLINE +words[3]+ color.END + "_ through"
print "the large tunnel that led to its _"+ color.UNDERLINE +words[4]+ color.END + "_"
print "_"+ color.UNDERLINE +words[5]+ color.END + "_. I got some peanuts and passed them"
print "through the cage to a gigantic gray _"+ color.UNDERLINE +words[6]+ color.END + "_"
print "towering above my head. Feeding that animal made me"
print "hungry. I went to get a _"+ color.UNDERLINE +words[7]+ color.END + "_ scoop of ice"
print "cream. It filled my stomach. Afterwards I had to"
print "_"+ color.UNDERLINE +words[8]+ color.END + "_ _"+ color.UNDERLINE +words[9]+ color.END + "_  to catch our bus. When"
print "I got home I _"+ color.UNDERLINE +words[10]+ color.END + "_ my mom for a"
print "_"+ color.UNDERLINE +words[11]+ color.END + "_ day at the zoo."

print "\n   Thanks For Playing!\n"