"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730612993"

character_input:str=input("Enter a 5-character word: ")
if len(character_input)>5 or len(character_input)<5: 
    print("Error: Word must contain 5 characters")
    exit()
single_character:str=input("Enter a single character: ")
if len(single_character)!=1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for "+single_character+" in "+character_input)
instance_counter:int=0
if character_input[0]==single_character:
    print(single_character+" found at index 0")
    instance_counter=instance_counter+1
if character_input[1]==single_character:
    print(single_character+" found at index 1")
    instance_counter=instance_counter+1
if character_input[2]==single_character:
    print(single_character+" found at index 2")
    instance_counter=instance_counter+1
if character_input[3]==single_character:
    print(single_character+" found at index 3")
    instance_counter=instance_counter+1
if character_input[4]==single_character:
    print(single_character+" found at index 4")
    instance_counter=instance_counter+1
if instance_counter==1:
    print(str(instance_counter)+" instance of "+single_character+" found in "+character_input)
if instance_counter>1:
    print(str(instance_counter)+" instances of "+single_character+" found in "+character_input)
if instance_counter==0:
    print("No instances of "+single_character+" found in "+character_input)


