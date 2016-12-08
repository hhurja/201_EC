###Description
* Sample Mad Libs project written in/for python by Hunter Hurja and Adam Moffitt

###Lets Get Started
Hello, lets learn a little bit about python Have you ever played Mad Libs? Well, either way, we are going to make our own version today Our program will deal with some simple concepts such as variables and user input A variable is a name assigned to some value User Input is when you tell the computer what to do Today we will be using words you type from your keyboard This will make more sense as we go along

###Instructions

1. Step 1: Find a fun story -- here is a link that you can use to start searching: 
	* http://www.teach-nology.com/worksheets/language_arts/madlibs/

2. Step 2: Count how many and the order of the nouns, adjectives, adverbs, etc there are.
	*  *Note* The order matters here

3. Step 3: Lets tell our user what to do.
	* Look up how to accept text input from the command line, *hint* use "raw_input()"
	* Try a test; ask the user what his/her name is.
	* name = raw_input("Please Enter Your name: ")
	* print "Hello", name

4. Step 4: Make a variable (or an array of variables) for each off the word types that you counted earlier

5. Step 5: Using this same template, ask the user to enter a word type for each of the ones you counted
	* *Example:*
	* adj1 = raw_input("Please enter an adjective: ")

6. Step 6: Once the user has unput all of his/her words, print out your Mad Libs template, replacing each underlined section with the corresponding word
	* *Note* look up string concatenation and how it works
	* *Example:*
	* adj1 = 'fun'
	* concatenated_string = 'This exercise is so ' + adj1+ '!'
	* print concated_string
