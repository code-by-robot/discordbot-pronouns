import math
import os
import random
import re
import sys
import string

pronounPresets = {"they": ["they", "them", "their", "theirself"], "she": ["she", "her", "hers", "herself"], 
                      "he": ["he", "him", "his", "himself"], "ze": ["ze", "hir", "hirs", "hirself"]}
oldPronounKey = ""
newPronounKey = ""
userPronouns = {}
validYesses = ["Y", "Yes", "y", "yes"]
initialCommand = ""
username = ""

def addPronounSet():
    # each pronoun is keyed by subjective case.
    # the order of the pronouns in the value is subjective, objective, possessive, reflexive.
    newnouns = pythonInput()
    try:
        if newnouns not in pronounPresets.values():
            key = newnouns[0]
            altCounter = 0
            while key in pronounPresets.keys():
                   key=key+string(altCounter)
                   altCounter +=1
            pronounPresets.update({key: newnouns})
            return 
        else:
            print("This pronoun set is already listed.\nAdd other pronoun set? ")
            input = input()
            if input in validYesses:
                pythonInput()
            else:
                return
    except: 
        return

def caseParser(word, replacement):
    shorterPronoun = word if len(word)<= len(replacement) else replacement
    longerPronoun = replacement if len(word)<= len(replacement) else word
    holdingList = []
    for index in range(len(shorterPronoun)):
        print(word[index])
        holdingList.append(replacement[index].upper() if word[index].isupper() ==True and word[index].isalpha() ==True else replacement[index])
    lengthShorter = len(shorterPronoun)
    if len(longerPronoun)> lengthShorter:
        holdingList.append(longerPronoun[lengthShorter:])
    return "".join(holdingList)

def changeUserPronouns(username):
    # want to draw username from the user accessing it & not allow them to change other people's pronouns
    userIn = -1
    while userIn == "LIST" or userIn == "ADD" or (userIn not in pronounPresets.keys() and userIn != -1):
        print("Type the label(s) for the pronoun set(s) you want to use (in order of preference and separated by space if more than one), \"LIST\" to show the existing pronoun list, \"ADD\" to add a new set to the list, or \"quit()\" to quit.")
        userIn = str(input().strip().split())
        if userIn == "LIST":
            showExistingPronouns()
        elif userIn == "ADD":
            addPronounSet(pronounPresets)
        else:
            print("I don't know that pronoun set yet. Type \"ADD\" to add it to my list.")
    if userIn == "quit()":
        return
    elif userIn in pronounPresets.keys():
        print("Your pronouns are now set to: ")
        for i in userIn:
            print(i)
        if len(userIn)>1:
            print("Do you want to have people swap between your pronoun sets?")
            swap = input().strip()
            if swap in validYesses:
                userPronouns.update({username: [userIn, 1]})
                print("I will swap between your pronouns randomly.")
            else:
                userPronouns.update({username: [userIn, 0]})
                print("I will only use the first pronoun of yours listed above.")
        else:
            userPronouns.update({username: [userIn, 0]})
    return

def findPronouns(username):
    try:
        for pronoun in userPronouns[username]:
            if pronoun.isnumeric():
                swapMessage = "User swaps between the above pronouns." if pronoun == 1 else "User prefers the first pronoun listed."
                print(swapMessage)
            else:
                print(pronounPresets[pronoun])
    except:
        print(f"{username} does not have listed pronouns or is not in this server.")

def nounSwap(word, oldPronounKey, newPronounKey):
    # each pronoun is keyed by subjective case.
    # the order of the pronouns in the value is subjective, objective, possessive, reflexive.
    # assume if oldPronounKey and newPronounKey in pronounPresets: is True
    try:
        index = pronounPresets[oldPronounKey].index(word)
        word = pronounPresets[newPronounKey][index]
        return word
    except ValueError:
        return word

def processMessage(oldPronounKey, newPronounKey, message):
    #message = input() - from command line prompt functionality
    newMessage = switcheroo(oldPronounKey, newPronounKey, message)
    return newMessage

def pythonInput():
    correct = False
    while correct == False:
        newnouns=[]
        print("Enter new pronouns and press enter, or enter \"quit()\" to quit without adding:\nSubjective (ex. they): ")
        newnouns.append(input())
        print("Objective (ex. them): ")
        newnouns.append(input())
        print("Possessive (ex. their): ")
        newnouns.append(input())
        print("Reflexive (ex. theirself): ")
        newnouns.append(input())
        print("The following pronoun set has been added to your list of pronouns:\nSubjective: "+newnouns[0]+"\nObjective: "+newnouns[1]+
          "\nPossessive: "+newnouns[2]+"\nReflexive: "+newnouns[3]+"\nIs this correct? Enter \"quit()\" to quit without adding.")
        check = input()
        if check in validYesses and check != "quit()":
            correct = True
        elif check == "quit()":
            return
    return newnouns

def showExistingPronouns():
    print("Choose from the following pronouns by typing the label(s) for the set(s) you want to use (in order of preference and separated by space if more than one)")
    for label in pronounPresets:
        print(label+": ")
        for pronoun in pronounPresets[label]:
            print("\t"+pronoun)   

def switcheroo(oldPronounKey, newPronounKey, message):
    newMessage = []
    words = message.split(' ')
    for word in words:
        lowerNoPunct = word.strip(string.punctuation).lower()
        replacement = nounSwap(lowerNoPunct, oldPronounKey, newPronounKey)
        if replacement != lowerNoPunct:
            noPunct = word.strip(string.punctuation)
            lowercaseWord = word.lower()
            if noPunct != word:
                index1 = word.find(noPunct)
                index2 = index1 + len(noPunct)
                if index1 == 0:
                    word = replacement + word[index2:]
                elif index2 == 0:
                    word = replacement + word[index2:]
                else:
                    word = word[:index1] + replacement + word[index2:]
            elif lowercaseWord != word:
                if noPunct.isupper() == True:
                    word = replacement.upper()
                elif noPunct[0].isupper() == True and noPunct[1:].islower() == True:
                    word = replacement[0].upper()+replacement[1:]
                else:
                    word = caseParser(word, replacement)
            else:
                word = replacement
        newMessage.append(word)
    output = " ".join(newMessage)
    return output

def userLoop():
    while initialCommand != "quit()":
        print("Choose one of the following commands:\nmessage: enter a message to swap pronouns\nadd: add pronouns to main list\nuser: check user's pronouns\nchange: change your own pronouns\nquit(): quit application")
        initialCommand = input()

        if initialCommand == "m" or initialCommand =="message":
            processMessage(oldPronounKey, newPronounKey)
        elif initialCommand == "add" or initialCommand =="a":
            addPronounSet(pronounPresets)
        elif initialCommand == "user" or initialCommand =="u":
            print("Enter username to find which pronouns to use:")
            username = input().strip()
            findPronouns(username)
        elif initialCommand == "change" or initialCommand =="c":
            changeUserPronouns()
        else:
            print("Invalid command.")
    



'''if __name__== "__main__":
    pronounPresets = {"they": ["they", "them", "their", "theirself"], "she": ["she", "her", "hers", "herself"], 
                      "he": ["he", "him", "his", "hisself"], "ze": ["ze", "hir", "hirs", "hirself"]}
    oldPronounKey = ""
    newPronounKey = ""
    userPronouns = {}
    validYesses = ["Y", "Yes", "y", "yes"]
    initialCommand = ""
    username = ""'''

    #Tesing variables
    #userPronouns = {"test1": ["ze", 0], "test2": ["he", "they", 1]}
    #oldPronounKey = "he"
    #newPronounKey = "ze"
    


