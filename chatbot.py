import nltk
from nltk.chat.util import Chat, reflections
import random
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver


#FUNCTIONS:
#---------------------------

#Greg's editor mode code, for developers, not users

def editMode():
    '''if editor is ON: '''
    return False
    '''if editor is OFF: '''
    #return False

def highLow():
    print("You found the EASTER EGG, so you can guess which number I chose")
    number = random.randint(1,int(input("maximum number: ")))
    tries = 0
    while True:
        userIn = int(input("Your guess: "))
        if number > userIn:
            print("Higher")
        elif number < userIn:
            print("Lower")
        elif number == userIn:
            print("Congrats!")
            print(str(tries+1) + " tries made.")
            input("")
            break
        tries+=1
    
#Mihaela's code:
def entryRequirments():
  choice = input("Do you need information about postgraduate, undergraduate, full time, part time, sandwich course, condensed first year or online courses, part time UK/EU only?? Please type the keyword below")
  if choice == ("Undergraduate") or choice == ("undergraduate"):
     print("Here's a link that may help you with any enquiry you have! ")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=140")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Postgraduate") or choice == ("postgraduate"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=299")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("full time") or choice == ("Full time"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=140&location=143&method=122")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Part time") or choice == ("part time"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=140&location=143&method=123")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Sandwich course") or choice == ("sandwich course"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=140&location=143&method=444")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Condensed first year") or choice == ("condensed first year"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&level=140&location=143&method=1442")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Online/blended courses") or choice == ("online/blended courses"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&location=143&method=126")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("Part time UK/EU") or choice == ("par time UK/EU"):
     print("Here's a link that may help you with any enquiry you have!")
     print("https://www.coventry.ac.uk/study-at-coventry/course-finder-search-results/?startdate=1308&location=143&method=854")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
    
  else:
     print("I'm sorry, I don't understand")
#entryRequirments() 


#shouldhave
#Mihaela's code:


def accomodationStudents():
  choice = input("Are you interested in accomodation, residence life, short-term lets or private letting?")
  if choice == ("Accomodation") or choice == ("accomodation"):
     print("Here's whar I found for accomodation for Coventry University students. I hope that helps!")
     print("https://www.coventry.ac.uk/life-on-campus/accommodation/accommodation-choices/")
     choice = input("Are you interested into postgraduate or undergraduate accomodation?'")
     if choice == ("Postgraduate") or choice == ("postgraduate"):
           print("Here's what I found for postgraduate accomodation. I hope that helps!")
           print("https://www.coventry.ac.uk/life-on-campus/accommodation/accommodation-choices/postgraduate-choices/")
     elif choice == ("Undergraduate") or choice == ("undergraduate"):
           print("Here's what I found for undergraduate accomodation. I hope that helps!")
           print("https://www.coventry.ac.uk/life-on-campus/accommodation/accommodation-choices/undergraduate-choices/")
           choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
           if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print("  ")
           elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("residence life") or choice == ("Residence life"):
     print("Here's what I found about residence life at Coventry University! I hope that helps")
     print("https://www.coventry.ac.uk/life-on-campus/accommodation/accommodation-choices/residence-life/")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the Residence life team.")
           print("ResLife@futurelets.co.uk  +44 (0)24 76 158 158")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("short-term") or choice == ("Short-term"):
     print("Here's what I found about short term lets at Coventry University!")
     print("https://www.coventry.ac.uk/life-on-campus/accommodation/short-term-and-summer-bookings/")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("private letting") or choice == ("Private letting"):
     print("Here's what I found about private lettings for Coventry University students! I hope that helps!")
     print("https://www.futurelets.co.uk/")
     choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
     if choice == ("Yes") or choice == ("yes"):
           print("If you need further details please contact the University directly.")
           print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
     elif choice == ("No") or choice == ("no"):
           print("I'm glad I was useful today, hope you have a nice day!")
  else:
     print("I'm sorry, I don't understand")
accomodationStudents()

#shouldhave
#Mihaela's code:


def scholarshipCU():
  choice = input("Are you interested in scholarships related to  BUCS Sport, Olympic Sports or Paralympic Sports?")
  if choice == ("Yes") or choice == ("yes"):
     print("Ok, I need more details!")
     choice = input("What kind of scholarship are you interested in?BUCS Sport, Olympic Sports or Paralympic Sports?")
     if choice == ("BUCS Sport") or choice == ("bucs sport"):
         print("Here's what I found about the BUCS Sport bursary! I hope that helps!")
         print("https://www.bucs.org.uk/compete/sports.html")
         choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
         if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print(" Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
         elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
     elif choice == ("Olympic Sports") or choice == ("olympic sports"):
          print("Here's what I found about Olympic Sports. I hope that helps")
          print("https://www.olympic.org/sports")
          choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
          if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print(" Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
          elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
     elif choice == ("Paralympic Sports") or choice == ("paralympic sports"):
           print("Here's what I found about Paralympic Sports. I hope that helps!")
           print("https://www.paralympic.org/sports")
           choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
           if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print(" Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
           elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
     choice = input("Are you interested into The Academic Merit Scholarship?")
     if choice == ("yes") or choice == ("Yes"):
           print("For  The Academic Merit Scholarship you need to Achieve at least 160 UCAS points or above and to start the first year of an undergraduate course in 2020 at Coventry University (CU) or CU London Campus (CULC). You can calculate your UCAS points here.")
           print("https://www.ucas.com/ucas/tariff-calculator")
           choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
           if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print(" Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
           elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
     choice = input("Are you a care leaver? If so, you might be eligible for the Care leavers accommodation scheme")
     if choice == ("yes") or choice == ("Yes"):
          print("Please contact welfare.ss@coventry.ac.uk to arrange an informal chat")
          choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
          if choice == ("Yes") or choice == ("yes"):
                print("If you need further details please contact University directly!")
                print(" Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
          elif choice == ("No") or choice == ("no"):
                print("I'm glad I was useful today, hope you have a nice day!")
  elif choice == ("No") or choice == ("no"):
          print("Take a look at our other scholarships, you may be eligible for one of them")
          print("https://www.coventry.ac.uk/study-at-coventry/finance/scholarships/")
scholarshipCU()

#Javeria's Code:

def qAnswered():
   if editMode() == True:
       print("qAnswered function")
   question = str(input("\nMK JAG: Does that answer your question?\n"+user_name+":"))

   #If the Bot cannot answer the question it will print relevant contact information for the user to use.
   ans1 = ["no", "NO", "No"]
   ans2 = ["yes", "YES", "Yes"]
   if question in ans1:
          print ("\nMK JAG: Contact Coventry University by phone on +44(0)24 7765 7688", "\nOR",
                 "\nIf you are a national student email us at https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=dom", "\nOR",
                 "\nIf you are an international student email us at https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=int", 
                 "\nOR", "\nWrite to us by letter to", "\nCoventry University", "\nPriory Street", "\nCoventry","\nUnited Kingdom", "\nCV1 5FB")
                 
          botq = ["\nMK JAG: Do you have another question?\n"+user_name+":",
                  "\nMK JAG: Can I assist you with anything else?\n"+user_name+":"]
          question = str(input(random.choice(botq)))
          ans1 = ["no", "NO", "No"]
          ans2 = ["yes", "YES", "Yes"]
          if question in ans2:
             inputRequests()        #should go to input for question again
          elif question in ans1:
              print("\nMK JAG: Goodbye "+user_name+".")
              what_to_do()  #Alarick's (R. Job) exit function.
          else:
              print("\nMK JAG: Sorry, I don't understand. \nPlease contact Coventry University "
                    "by phone on +44(0)24 7765 7688", "\nOR",
                 "\nIf you are a national student email us at"
                 " https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=dom", "\nOR",
                 "\nIf you are an international student email us at"
                 " https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=int",
                 "\nOR", "\nWrite to us by letter to", "\nCoventry University", "\nPriory Street", "\nCoventry",
                    "\nUnited Kingdom", "\nCV1 5FB", "\n Goodbye.")
              what_to_do()     #Alarick's (R. Job) exit function. 
   elif question in ans2:
          botq = ["\nMK JAG: Do you have another question?\n"+user_name+":",
                  "\nMK JAG: Can I assist you with anything else?\n"+user_name+":"]
          question = str(input(random.choice(botq)))
          ans1 = ["no", "NO", "No"]
          ans2 = ["yes", "YES", "Yes"]
          if question in ans2:
             inputRequests() #should go to input for question again
          elif question in ans1:
              print("\nMK JAG: Goodbye "+user_name+".")
              what_to_do()  #Alarick's (R. Job) exit function.
          else:
              print("\nMK JAG: Sorry, I don't understand. "
                    "\nPlease contact Coventry University by phone on +44(0)24 7765 7688", "\nOR",
                 "\nIf you are a national student email us at "
                 "https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=dom", "\nOR",
                 "\nIf you are an international student email us at "
                 "https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=int",
                 "\nOR", "\nWrite to us by letter to", "\nCoventry University", "\nPriory Street", "\nCoventry",
                    "\nUnited Kingdom", "\nCV1 5FB", "\n Goodbye.")
              what_to_do()  #Alarick's (R. Job) exit function.
   else:
       print("\nMK JAG: Sorry, I don't understand. "
             "\nPlease contact Coventry University by phone on +44(0)24 7765 7688", "\nOR",
                 "\nIf you are a national student email us at "
                 "https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=dom", "\nOR",
                 "\nIf you are an international student email us at "
                 "https://coventry-university.secure.force.com/CU_ChatOfflineSupport?queue=int",
                 "\nOR", "\nWrite to us by letter to", "\nCoventry University", "\nPriory Street", "\nCoventry",
                 "\nUnited Kingdom", "\nCV1 5FB", "\n Goodbye.")
       what_to_do()    #Alarick's (R. Job) exit function.   

#Javeria's Code:
def learnMatrl():
      userInput = input("What would you like help with? \nMicrosoft Teams \nAula \nCodio \nPadlet \nGithub \nCU Moodle \nBibliU \nOr if you would like to exit type 'exit'.\n").lower()
      if userInput == "microsoft teams" or userInput == "teams"or userInput == "microsoft":
          print("\nYou can sign into Microsoft Teams from: "
                "https://www.microsoft.com/en-GB/microsoft-365/microsoft-teams/group-chat-software using your "
                "Coventry University email: YOURUSERNAME@uni.coventry.ac.uk e.g. BobH@uni.coventry.ac.uk. "
                "You can also install Microsoft Teams on your desktop, mobile or tablet. \n")
      elif userInput == "aula":
          print("\nYou can sign into Aula from: https://aula.education/ using your Coventry University email:"
                " YOURUSERNAME@coventry.ac.uk e.g. BobH@coventry.ac.uk."
                "You can also install Aula on your mobile or tablet. \n")
      elif userInput == "codio":
          print("\nYou can sign-up for Codio from: https://tinyurl.com/codiosignup?token=vanilla-cement "
                "using your Coventry University email: YOURUSERNAME@coventry.ac.uk e.g. BobH@coventry.ac.uk. "
                "You can then sign-in to Codio from https://codio.co.uk Please use .co.uk NOT .com \n")
      elif userInput == "padlet":
          print("\nYou can sign into Padlet from https://coventryunionline.padlet.org/auth/login using your "
                "Coventry University Microsoft email account: YOURUSERNAME@uni.coventry.ac.uk e.g. BobH@uni.coventry.ac.uk \n")
      elif userInput == "github":
          print("\nYou can sign into Github Coventry with the following link https://github.coventry.ac.uk/ "
                "using your Coventry University email address @coventry.ac.uk e.g. BobH@coventry.ac.uk \n")
      elif userInput == "cu moodle" or userInput == "moodle":
          print("\nYou can sign into CU Moodle from: https://cumoodle.coventry.ac.uk/ using your Coventry University "
                "username: YOURUSERNAME e.g. BobH You can also install CU Moodle on your mobile or tablet. \n")
      elif userInput == "bibliu":
          print("\nYou can access BibliU from https://bibliu.com/ "
                "using your Coventry University email address; @coventry.ac.uk e.g. BobH@coventry.ac.uk \n") 
      elif userInput == "exit":
          print ("\n")
          what_to_do()         #Alarick's (R. Job) exit function.
      else:
          print("\nI don't understand. \n")
          learnMatrl()



'''
LinksToPages shorter version

def linksToPages():
    places = ["africa", "china", "america", "europe and central asia", "middle east", "south asia", "south east asia", "uk", "north east asia"]
    placesLinks = ["africa", "china", "america", "europe-russia-and-central-asia", "middle-east", "south-and-south-east-asia", "south-east-asia", "uk", "north-east-asia"]
    choice = input("Where are you from?\n").lower()
    for i in range(len(places)):
        if choice == places[i]:
            print("Here's a link that may help you with any enquiry you have! ")
            print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/" + placesLinks[i] + "-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice.lower() == ("yes"):
            print("If you need further details please contact the University directly.")
            print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice.lower() == ("no"):
            print("I'm glad I was useful today, hope you have a nice day!")
'''
#Mihaela's code:

def linksToPages():
 choice = input("Where are you from? Please type:Africa, China, America, Europe and Central Asia, Middle East, South Asia, South East Asia, UK, North East Asia")
 if choice == ("Africa") or choice == ("africa"):
    print("Here's a link that may help you with any enquiry you have! ")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/africa-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("China") or choice == ("china"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/china-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("America") or choice == ("america"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/americas-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("Europe and Central Asia") or choice == ("europe and central asia"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/europe-russia-and-central-asia-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("Middle East") or choice == ("middle east"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/middle-east-international-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("South Asia") or choice == ("south asia"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/south-and-south-east-asia-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("South East Asia") or choice == ("south east asia"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/south-east-asia-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("UK") or choice == ("uk"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/uk-regional-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 elif choice == ("North East Asia") or choice == ("north east asia"):
    print("Here's a link that may help you with any enquiry you have!")
    print("https://www.coventry.ac.uk/international-students-hub/new-students/find-your-region/north-east-asia-information/")
    choice = input("Is there anything else I can do for you? Please type 'Yes' or 'No'")
    if choice == ("Yes") or choice == ("yes"):
        print("If you need further details please contact the University directly.")
        print("Coventry University Priory Street Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688 ")
    elif choice == ("No") or choice == ("no"):
        print("I'm glad I was useful today, hope you have a nice day!")
 else:
   print("I'm sorry, I don't understand")
#linksToPages()

#Karam's Code:

conversations = [
    [
        r"my name is (.*)",
        ["Hello %1, Good to see you, How can I help?", ]
    ],
    [
        r"what is your name?",
        ["My name is Karam And I am a Coventry University chatbot", ]
    ],
    [
        r"how are you?",
        ["I am good\nHow are you?", ]
    ],
    [
        r"I am Fine|I am Good|I am Very good|i am Not bad|Fine|Good|Very good|Not Bad",
        ["That's Great :)", ]
    ],
    [
        r"I am bad|I am not good|Bad",
        ["How can I help you?", ]
    ],
    [
        r"Where i can get information about international students?",
        ["You can visit this webpage, https://www.coventry.ac.uk/international-students-hub/", ]
    ],
    [
        # Greeting
        r"Hi|How are you|Is anyone there?|Hello|Good day|Whats up",
        ["Hello! How can I help?", ]
    ],
    [
        # GoodBye
        r"see ya|See you later|Goodbye|I am Leaving|Have a Good day|bye",
        ["Goodbye, talk to you later", ]
    ],
    [
        # How to apply
        r"How to Apply?|How do i apply?|How to apply|how do i apply|1",
        ["There are many easy ways to apply...\n1 Online application form, (https://webapp.coventry.ac.uk/CUapply/) \n2 Downloadable application form, Once completed, please email the form to (applications.io@coventry.ac.uk).Please ensure any attachments sent with your email and application form are less than 10MB, otherwise your application email may not reach us. \n3 Through UCAS. If you are an undergraduate student from the EU, you must apply through UCAS. \n4 Through a local office, or local representative.", ]
    ],
    [
        # How to pay
        r"How to pay fees?|How to pay tuition fees?|how to pay fee?|how to pay?|How to pay fees|how to pay|how to pay fee|2",
        ["As an International student, we may have asked you to pay a deposit. We’ll need this deposit before we send you the Confirmation of Acceptance to Study (CAS letter) that you will need to get a visa to study in the UK. We’ll apply your deposit to any tuition fees that you owe for your course. To avoid delays in arranging your travel, accommodation and enrolment, we recommend that you pay your deposit at least three months before your course starts. \n1 Pay online from your bank. \n2 Pay online by credit or debit card. \n3 Pay offline by bank transfer. \n Account Name: Coventry University\n Bank Name: Barclays Bank\n Bank Address: High Street, Coventry, CV1 1ZZ\n Sort Code: 20-23-78\n Account Number: 20786675\n IBAN Number: GB56 BARC 202378 20786675\n Swift Code: BARCGB22", ]
    ],
    [
        # International and EU scholarships
        r"How to apply scholarships?|how to get scholarships?|how to get scholarship?|international scholarships|international scholarship|3",
        ["About our scholarships \nWe want the best and brightest students to fulfil their potential when they study with us. We are supporting students from all across the world with these valuable and prestigious financial awards. \nThere are different types of scholarships...\nInternational academic excellence awards, Territory awards, Coventry entrepreneurship award and Coventry university sports scholarships. For more information please visit this link.\nhttps://www.coventry.ac.uk/international-students-hub/new-students/international-scholarships-and-discounts/international-scholarships/apply-for-a-scholarship-/.", ]
    ],
    [
        # Coming to the UK
        r"Applying for visa|Student visa|Student visa information|Visas for students|4",
        ["The International Student Support Team offers help and advice to international students coming to study at Coventry University. As part of the application process you will need to obtain the relevant entry clearance before you can travel, ensure you have sufficient funds and pass any necessary health checks before your arrival in the UK. For more information, you can download our visa guide. For more information please go to (https://www.coventry.ac.uk/international-students-hub/new-students/coming-to-the-uk/your-visa/)", ]
    ],
    [
        # Travelling to the UK
        r"Travelling to the UK|Travel to the UK|Travel information|Travel to UK|Travelling information|5",
        ["If you have accepted your offer, received your CAS and applied for, and received your visa, you can now start to plan your arrival in Coventry. If you need any further information, please contact the International Student Support team via email welfare.io@coventry.ac.uk or call +44 (0) 24 7765 3546.", ]
    ],
    [
        # Living costs in the UK
        r"Living costs in the UK|what is the living costs in the UK?|Living cost|Living costs|6",
        ["You will need to book your accommodation and arrange your finances before you arrive at University. It is vital that you have sufficient funding in place before starting your course of study, and this will need to cover your tuition fees, accommodation, books, stationery, food and of course social costs. \n  \nBelow is an approximate guide to the minimum amount you should expect for living expenses in the UK per month. These costs are for one person only, so students with children and dependents should keep this in mind when working out a budget. \n\nAccommodation (halls of residence, usually including bills) £400 - £600 per month \nFood / Housekeeping £160 - £200 per month \nMobile phone £15 - £50 per month \nTravel / Transport (Based on the monthly cost of a student bus pass) £32 per month \nChildcare (if needed) £656 per month.", ]
    ],

]

def InternationalStudent() :
    if editMode() == True:
         print("InternationalStudent function")
    print ( "Hi I am MKJAG Coventry University chatbot. How can I help?" )
    print("Choose a number from list...\n1 How to apply? \n2 How to pay fees? \n3 How to apply scholarships? \n4 Coming to the UK. \n5 Travelling to the UK. \n6 Living cost in the UK")
    chat = Chat ( conversations, reflections )
    chat.converse ()

    if __name__ == "__main__" :
        InternationalStudent()
    chat.converse()
    
    
 #Karam 
 
conversations = [
    [
        r"my name is (.*)",
        ["Hello %1, Good to see you, How can I help?",]
    ],
    [
        r"what is your name?",
        ["My name is MKJAG And I am a Coventry University chatbot",]
    ],
    [
        r"how are you?",
        ["I am good\nHow are you?", ]
    ],
    [
        r"I am Fine|I am Good|I am Very good|i am Not bad|Fine|Good|Very good|Not Bad|i'm good|i'm fine|i'm very good|i'm not bad",
        ["That's Great :)",]
    ],
    [
        r"I am bad|I am not good|Bad",
        ["How can I help you?",]
    ],
    [
        #Staff Parking
        r"Staff Parking|Staff car parking|Staff parking permit|Staff car parking permit|1|Staff motorcycle parking|staff disabled parking",
        ["All staff need to display a blue University Parking Permit when they park in University Staff Car Parks – even when they have used their staff ID card to enter the car park or pay for parking.Permits can be collected from Alan Berry, Portal House or Alma reception between 10am-12pm and 1.30pm-3pm. For electric car parking passes or disabled parking passes please contact Alan Berry reception.If you change cars or bring in a different car, you should email estates@coventry.ac.uk.\n* Car Parking \nStaff parking is charged at £3 per day in all University car parks. There is an option to park for up to 4 hours in the Multi-Storey car park for £1 with no return the same day. You will need to present your Staff ID card at the card reader next to the ticket machines to purchase a ticket. Please ensure that you display your blue University Parking Permit as well as your valid Pay & Display ticket.\n* Motorcycle Parking\n There is parking for motorbikes in the Multi-Storey Car Park, at Singer Hall, and at the front of the Alma Building. Parking for motorcycles is free, and does not require a parking permit. \n*Disabled Parking for Staff \nStaff using disabled parking should display both their blue University Parking Permit and their Blue Badge. They should also pay the usual fee for the car park they are using. Temporary passes are available for staff who need to use disabled parking on medical grounds. To get one of these passes, staff members should contact their People Partner for their department or faculty.\n For information about sites and timing please visit https://www.coventry.ac.uk/life-on-campus/parking-coventry-university/staff-parking/",]
    ],
    [
        #Student Parking
        r"Student car parking|Student motorcycle parking|student parking|student disabled parking|2",
        ["* Student Car Parking \n Student parking is charged at £2 per day in all University car parks. There is also an option to park for up to 4 for £1 with no return the same day. Staff are not permitted to park in the student Abandon Car Park on the corner of Cox Street, or the student area of the Mile Lane car park; these car parks are solely for the use of our students.\n* Student Motorcycle Parking \nThere is parking for motorbikes in the Multi-Storey Car Park, at Singer Hall, and at the front of the Alma Building. Parking for motorcycles is free, and does not require a parking permit. \n* Student Disabled Parking\n Students using disabled parking should display their Blue Badge and a red Student Permit. Permits are available from the Disability Support Team.\n There are other options like other car parks, public tranport and liftshare\n For information about sites, timing and other options please visit https://www.coventry.ac.uk/life-on-campus/parking-coventry-university/student-parking/",]
    ],
    [
        #Visitor Parking
        r"Visitor parking|visitor car parking|visitor|3",
        ["*Visitor Parking \nLimited parking spaces in the Multi Storey Car Park are available for professional visitors to the University. Permits must be arranged by the staff member who is receiving the visitor.\nTo request a visitor car parking space, staff members should email us at visitorparking.mc@coventry.ac.uk with the following information: \n* Name of visitor \n* Time of expected arrival and departure \n* Visitor's vehicle registration number \n* The name and telephone extension number of the staff member they are visiting. \n An electronic pass will be sent by email to the member of staff requesting it. This pass needs to be sent to the visitor. They will need to present the pass when entering the car park and then display the pass in their vehicle whilst parked. \n All visitor car parking is free, subject to the correct procedure being followed. Visitor parking is only available in the Multi Storey Car Park. If you have any queries about this process, please contact: \n Alan Berry Reception team \n Telephone: 024 77 658788.",]
    ],

]

def Parking() :
    if editMode() == True:
         print("Parking function")
    print("Hi I am MKJAG Coventry University chatbot. I am here to help you with car parking.\nChoose one option.\n1 Staff Parking\n2 Student Parking\n3 Visitor Parking")
    chat = Chat(conversations, reflections)
    chat.converse ()


if __name__ == "__main__" :
    Parking()
chat.converse()


#Karam


def BuildingsCU():
    input("Hi I am here to help you with Coventry University Buildings...Choose one number from the list.\n1 Business Development.\n2 Science and Health Building.\n3 Estates and ITS.\n4 Faculty of Health and Life Sciences.\n5 Faculty of Arts and Humanities.\n6 Engineering, Environment and Computing Building.\n7 Coventry Law School and the Faculty of Arts and Humanities.\n8 Social space for our students.\n9 Jaguar Land Rover.\n10 Faculty of Engineering, Environment and Computing.\n11 The main university library.\n12 New bespoke campus for CU Coventry.\n13 Multi-storey car park.\n14 Coventry foundation campus.\n15 Faculty of Health and Life Sciences.\n16 New students help centre.\n17 The hub of offices and shops.\n18 Student Engagement Centre team and small research units.\n19 Coventry Business School.")

    choice=input()

    if choice==("1") or choice==("Business Development") or choice==("business development"):
        print("Alan Berry")
        print("This was constructed in 1963 and has a prominent position on our campus overlooking University Square and Coventry Cathedral. It is used by Business Development, Registry and the Vice Chancellor’s Office. The building is named after Alan Berry, who was the Director and Chief Executive for the West Midlands Engineering Employers’ Association.")
        print("Post Code for the building is CV1 5FB.")

    elif choice==("2") or choice==("Science and Health Building") or choice==("science and health building"):
        print("Alison Gingell Building")
        print("Opened by the Duke and Duchess of Cambridge in January 2018, this is a modern multidisciplinary facility housing new healthcare simulation, research and ‘super-lab’ environments. It enables students to learn to care for patients at every stage of their healthcare experience; from ambulance and hospital treatment, through to physical and mental rehabilitation. It is named in memory of Alison Gingell, a city councillor who was at the forefront of health and social care in Coventry and Warwickshire for more than 40 years.")
        print("Post Code for the building is CV1 2DS.")

    elif choice==("3") or choice==("Estates and ITS") or choice==("estates and its"):
        print("Alma")
        print("This was built in the 1920s and is used by Estates and ITS. It is the former site of the Singer Works, from which both the Singer Penny Farthing and Coventry City Football Club can trace their origins.")
        print("Post Code for the building is CV1 5QA.")

    elif choice==("4") or choice==("Faculty of Health and Life Sciences"):
        print("Charles Ward")
        print("Built in the 1950s, this is used mainly by our Faculty of Health and Life Sciences. The building was named after a key figure for the university, Charles Ward, who became Vice Chair of the Board of Governors in 1982.")
        print("Post Code for the building is CV1 5FD.")

    elif choice==("5") or choice==("Faculty of Arts and Humanities"):
        print("There are 3 buildings...")
        print("Ellen Terry")
        print("This is used by our Faculty of Arts and Humanities, specifically for the performing arts, media and music courses. Built in 1880, the art deco building underwent a major refurbishment in 2000. Fittingly, it was previously a cinema, and is named after Dame Ellen Terry, a star of the Victorian stage and a leading Shakespearean actress.")
        print("Post Code for the building is CV1 5RW.")
        print("\n")
        print("Graham Sutherland")
        print("Built in 1959, this building is currently undergoing an extensive internal redevelopment. Once completed, it will continue to be used by the Faculty of Arts and Humanities, predominantly by design and visual art students. It is aptly named after the painter and printmaker Graham Sutherland, who created the world-famous tapestry ‘Christ in Glory’ in Coventry Cathedral which, at 23x12m, is reputedly the largest continuously woven tapestry in the world.")
        print("Post Code for the building is CV1 5PH.")
        print("\n")
        print("Maurice Foss")
        print("Built in 1978, this building is currently undergoing an extensive internal redevelopment. Once completed, it will continue to be used by the Faculty of Arts and Humanities, primarily for industrial design courses. The building is named after Maurice Foss, the former Deputy Director of Coventry Polytechnic and one of the university’s Honorary Life Fellows.")
        print("Post Code for the building is CV1 5PH.")

    elif choice==("6") or choice==("Engineering, Environment and Computing Building"):
        print("Engineering and Computing Building")
        print("Our Engineering, Environment and Computing Building (EEC), was completed in 2012. It uses a range of sustainable technologies, including rainwater harvesting, solar thermal energy and biomass boilers. Facilities include a precision wind-tunnel, a high-performance engineering centre, a Harrier Jump Jet and three flight simulators.")
        print("Post Code for the building is CV1 2JH.")

    elif choice==("7") or choice==("Coventry Law School and the Faculty of Arts and Humanities"):
        print("George Eliot")
        print("Built in 1960 and fully refurbished in recent years, this building provides modern teaching and learning spaces for both Coventry Law School and the Faculty of Arts and Humanities. It is named after George Eliot, which was the pen name of the novelist Mary Anne Evans, one of the leading writers of the Victorian era.")
        print("Post Code for the building is CV1 5FB.")

    elif choice==("8") or choice==("Social space for our students"):
        print("TheHub")
        print("Completed in 2011, TheHub is a modern, hi-tech building providing a welcoming social space for our students. Facilities in the building include a doctors’ surgery, a multi-cultural faith centre, employment services and catering services, as well as a hairdresser, food court and the Students’ Union offices. It has fully licensed function spaces and bars, a multi-purpose venue hosting regular music and film events, and a new restaurant, The Courtyard, which opened in 2019. The building holds a BREEAM status of Excellent – the world’s leading sustainability assessment method.")
        print("Post Code for the building is CV1 5FB.")

    elif choice==("9") or choice==("Jaguar Land Rover"):
        print("Jaguar")
        print("Built in the late 1970s, this building is sponsored by Jaguar Land Rover, the Coventry-based car manufacturer, and recently underwent a significant refurbishment.  It is home to our postgraduate students, as well as our researchers within the Centre for Business in Society (CBiS).")
        print("Post Code for the building is CV1 5DL.")

    elif choice==("10") or choice==("Faculty of Engineering, Environment and Computing"):
        print("John Laing")
        print("This building is primarily used by the Faculty of Engineering, Environment and Computing, offering courses relating to the construction sector. It was built in 1970, and is named after Sir John Laing, a British entrepreneur in the construction industry.")
        print("Post Code for the building is CV1 2LT.")

    elif choice==("11") or choice==("12 The main university library."):
        print("Frederick Lanchester Library")
        print("This striking building houses the main university library. It was opened in 2001, and in 2019 was upgraded to bring together all elements of academic support into one location, with a new entrance, café and collaboration spaces on the ground floor. It is named after Frederick Lanchester, the Coventry-based designer of the first British petrol-driven car. It is equipped with more than 350 computers, group and individual study rooms, books, journals, and electronic resources across five floors. It also includes the the Lanchester Interactive Archive, the largest and fully digitalised archive of the life and work of Frederick Lanchester.")
        print("Post Code for the building is CV1 5DD.")

    elif choice==("12") or choice==("New bespoke campus for CU Coventry"):
        print("Mile Lane")
        print("This is a new bespoke campus for CU Coventry, which offers Coventry University degrees through a unique and flexible education model designed to fit around the lives of students. It opened in 2019 and provides a cutting-edge learning environment for collaboration, creativity and innovation. The building has energy-efficient features, with student having access to on-site parking and catering facilities.")
        print("Post Code for the building is CV1 2TU.")

    elif choice==("13") or choice==("Multi-storey car park") or choice==("Car park"):
        print("Multi-Storey Car Park")
        print("This is our impressive multi-storey car park, opened for staff and visitors in 2010. It has 457 spaces over 15 floors, including spaces for electric vehicles.")
        print("Post Code for the building is CV1 5DE.")

    elif choice==("14") or choice==("Coventry foundation campus"):
        print("Priory Building")
        print("Built in 1964, this is occupied by the Cambridge Education Group, which runs its Coventry foundation campus from here, offering university pathway courses for overseas students who wish to gain entry to UK universities. The building also houses a large sports hall.")
        print("Post Code for the building is CV1 5FB.")

    elif choice==("15") or choice==("Faculty of Health and Life Sciences"):
        print("Richard Crossman")
        print("This was built in 1971 and is named after the political journalist and Labour politician Richard Crossman, who represented Coventry East from 1945 to 1974. It is used by the Faculty of Health and Life Sciences, primarily for psychology, criminology and social sciences subjects, and includes mock prison cells and psychology labs.")
        print("Post Code for the building is CV1 5RW.")

    elif choice==("16") or choice==("Help centre for new students"):
        print("Student Centre")
        print("Opened in 2006, the centre is home to many of our key student services as well as our International Office. This is where our students enrol and is also a main information point for student accommodation and finance queries.")
        print("Post Code for the building is CV1 2JH.")

    elif choice==("17") or choice==("The hub of offices and shops"):
        print("Whitefriars")
        print("This is a hub of offices and shops, and includes the Inkwell, the Printshop, as well as the Enterprise Hub. There is a suite of small offices above these units Built in 1922, its name is drawn from the Carmelite Friary founded in 1342 in Coventry.")
        print("Post Code for the building is CV1 2DS.")

    elif choice==("18") or choice==("Student Engagement Centre team and small research units"):
        print("William Lyons")
        print("Constructed in 1980, this building is currently the home of the Student Engagement Centre team and a few small research units. It is named after Sir William Lyons, the co-founder of the Swallow Sidecar Company, which subsequently became Jaguar Cars.")
        print("Post Code for the building is CV1 5DL.")

    elif choice==("19") or choice==("Coventry Business School"):
        print("William Morris")
        print("Built by French company Hotchkiss and Cie in 1917 to make machine guns, this building was later bought by the Morris car company for engine works. Coventry pioneered car production and this building, now the William Morris, is home to our Coventry Business School.")
        print("Post Code for the building is CV1 5DL.")

    else:
        print("Please select a number so i can help you.")
        print("Thank you")
BuildingsCU()

#Karam


def PartTimejobsCU():
    input("Hi At Coventry University we realise that working part-time while studying is a necessity for many students – be it to cover living and academic expenses or to just to earn a bit of extra spending money.Please select one...\n1 Home and EU Students.\n2 International Students.")
    select=input()

    if select==("1") or select==("Home") or select==("home") or select==("EU") or select==("Eu") or select==("eu") or select==("UK") or select==("Home student") or select==("UK student") or select==("EU studnet"):
        print("Based in theHub, thefutureworks is the University’s own commercial recruitment agency, which provides a choice of flexible temporary opportunities for students.")
        print("Here is a link of thefutureworks http://www.thefutureworks.org.uk/")
        print("From the link you will be to apply for flexible temporary opportunities with Coventry University.")



    elif select==("2") or select==("International Student") or select==("International student") or select==("international student") or select==("international") or select==("International"):
        print("If you are an international student and have had to obtain entry clearance before you arrived in the UK your visa stamp will include the words ‘work (and any changes) must be authorised’, this means you can work up to 20 hours per week during term-time and full-time during your vacation period. Please be aware that, as an international student working in the UK, there are certain restrictions on the activities that you are allowed to undertake.")
        print("You are allowed to work if your student visa or biometric ID card states.")
        print("Able to work as authorised by The Secretary of State.")
        print("Work (and any changes) must be authorised.")
        print("Here is a link from where you will be able to apply jobs with Coventry University http://www.thefutureworks.org.uk/")
        print("\n")
        print("You are not allowed to work if your student visa or sticker states.")
        print("No work or recourse to public funds.")
        print("No work or engaging in business.")
        print("Restricted work term-time.")

    select=input("Do you need more help?")
    if select==("yes") or select==("yes"):
        print("Please contact to Coventry University.")
        print("Contact details are Priory Street, Coventry United Kingdom CV1 5FB Tel: +44(0)24 7765 7688")
    elif select==("No") or select==("no"):
        print("I am very happy to help you out.")
        print("Thank You for chatting with me.")


    else:
        print("I do not understand. Please type or select correctly.")
        print("Thank You")


PartTimejobsCU()
   

#Alarick (R.Job) code:
finereply = ["yes", "yeah", "please", "ok", "okay", "k", "sure", "y"]

def what_to_do() :
    print("Are you lost or stuck friend?")
    print("You can ask me to take you to certain parts of information.")
    print("You can restart the bot by typing 'try again'")

    try_again=input("Do you wish to return to the beginning? \n").lower()
    if try_again in finereply:
        inputRequests()

    else:
        print("Hope I could be of service. \n")
        exit() 

def Clearing_Info() :
    print("Clearing information has been divided into 3 options to choose from; \n 0. What is Clearing? \n 1. Clearing time period? \n 2. How to Apply? \n 3. Is clearing open now?")
    clearing_choice = input('') 
    if input == '1':
        result_clearing_period = requests.get("https://www.coventry.ac.uk/news/2020/clearing-2020-explainer/").text
        soup = BeautifulSoup(result_clearing_period, 'lxml')
        clearing_time = soup.find('div' , class_ = 'col-sm-12')
        clearing_timeA = clearing_time.find('p', 'span')
        print(clearing_timeA)

    elif input == '3':
        result_clearing1 = requests.get("https://www.coventry.ac.uk/clearing/").text
        soup = BeautifulSoup(result_clearing1, 'lxml')
        clearing_yes_or_no = soup.find('div', class_ = 'clearing-text-overlay')
        yes_or_no = clearing_yes_or_no.find('h1')
        print(clearing_yes_or_no)

    elif input == '2':
        results_how_to_apply = requests.get("https://www.coventry.ac.uk/news/2020/clearing-2020-explainer/").text
        soup = BeautifulSoup(results_how_to_apply, 'lxml')
        how_to_apply = soup.find('div' , class_ = 'col-sm-12')
        apply = how_to_apply.find('br')
        print(how_to_apply)

    elif input == '0':
        results_what_is_clearing = requests.get('https://www.coventry.ac.uk/news/2020/clearing-2020-explainer/').text
        soup = BeautifulSoup(results_what_is_clearing, 'lxml')
        what_is_clearing = soup.find('div' , class_ = 'col-sm-12')
        is_this_clearing = what_is_clearing.find('p')
        print(what_is_clearing)

    else:
        pass

def timing_details() :

    print("So you want to know about things like; semester starting dates, when they end, exams that are scheduled, and similar things?")
    print("\nWell.. you have come to the right place friend.")
    print("\n I have a list of a number of things you can start from;\n 1. Semester start dates. \n 2. Semester end dates. \n 3. Exams (may vary depending on course). \n 4. Gradutaion. \n 5. Holidays in the years, for students. \n 6. none of the above...")
    
    timingdecision1=input("")
    
    while (timingdecision1):
        if timingdecision1 == "1":
            print("So you want to know about semester start dates huh? \n")
            print("For those starting in 2020, the first semester started on 14/09/2020. 14th of september 2020 (this includes both undergraduates and postgraduates). \n Semester 2 starts on the 18th of January 2021, 18/01/2020 (this also includes both undergraduates and postgraduates). \n September 2020, postgraduate students, will have their third semester start on 17/05/2021. \n")
            print("There will also people who will be joining us in January 2021: both post & undergraduates will be starting on the 18/01/2021. \n January 2021 students will also have their second semeter on the 17/05/2021, and third semester will be 13/09/2021 for postgraduates. \n")
            print("Last but not least, May 2021, 17/05/2021, will be the starting date for any students planning to study from May. \n Second semester for May 2021 students will be 13/09/2021, for both postgraduates and undergraduates. \n May 2021, postgraduate students, will have their third semester on 17/01/2022. \n")
            print("if you'd like to choose another part, you are more than welcome to choose another from the list;\n 2. Semester end dates. \n 3. Exams (May vary depending on course). \n 4. Gradutaion. \n 5. Holidays in the years, for students. \n 6. none of the above...")
            timingdecision1=input("")

        elif timingdecision1 == "2":
            print("Want to know when the semester ends, have you even started one yet?")
            print("September 2020 students, both postgraduates and undergraduates, first semester will end on 12/12/2020 \n Second semester, for september 2020 students, will end on 17/04/2021 (both undergraduates and postgrads), and third semester will end on 14/08/2021 for postgraduates who started 2020 september. \n")
            print("Undergraduates and post graduates starting January 2021 will have their first semester end on 17/04/2021 and their second semester will end on 14/08/2021. \n Postgraduates stating in January 2021 will have their third semester ending 11/12/2021. \n ")
            print("Postgrads and undergrads, who start in May 2021, will have their first semester end on 14/08/2021... and their second semester will end 11/12/2021. \n Post graduates starting in May 2021 will have their third semester end on 16/04/2022.")
            print("if you'd like to choose another part, you are more than welcome to choose another from the list;\n 1. Semester start dates. \n 3. Exams (may vary depending on course). \n 4. Gradutaion. \n 5. Holidays in the years, for students. \n 6. none of the above...")

            timingdecision1=input("")

        elif timingdecision1 == "3":
            print("Exams, nobody likes them but we have to have ways to determine who is right for jobs. \n I'd just like to let you know now that exams, coursework and tests vary based on subjects... if you have been given a different time frame than what is posted here, i'd reccomend checking with your lecturer as their may have been unforseen circumstances. \n")
            print("Students who start in September 2020 should have their first semester exams between 5/12/2020 - 12/12/2020. Second semester 10/4/2021 - 17/4/2021 and third semeter, postgraduates only, between 7/8/2021 - 14/8/2021. \n")
            print("Postgraduates and undergraduates who start in January 2021 have their first examinations around 10/4/2021 - 17/4/2021 and their second semester exams should be 7/8/2021 - 14/8/2021. \n Postgraduates, on their third semester, should have theirs just before christmas 4/12/2021 - 11/12/2021. \n")
            print("Finally, those who start in May 2021, have a time frame of  7/8/2021 - 14/8/2021	for the first semester and 4/12/2021 - 11/12/2021 for the second semster. \n Postgraduates third semester examinations should be around 9/4/2022 - 16/11/2022. \n ")
            print("if you'd like to choose another part, you are more than welcome to choose another from the list;\n 1. Semester start dates. \n 2. Semester end dates. \n 4. Gradutaion. \n 5. Holidays in the years, for students. \n 6. none of the above...")
            timingdecision1=input("")

        elif timingdecision1 == "4":
            print("Graduation... Remember graduation only applies to those who pass their course. \n")
            print("September 2020 undergraduates will have their graduation sometime in the summer of 2021. \n September 2020 postgraduates have their planned graduation in Autumn 2021. \n")
            print("January 2021 undergraduate students are planned to have the graduation period within Autumn 2021. \n Postgraduates for January 2021 will have thier graduation within spring 2022. \n")
            print("May 2021 undergrads will have their graduation within Spring 2022. \n Postgraduates for May 2021 will have their graduation period during the summer of 2022. \n")
            print("if you'd like to choose another part, you are more than welcome to choose another from the list;\n 1. Semester start dates. \n 2. Semester end dates. \n 3. Exams (may vary depending on course). \n 5. Holidays in the years, for students. \n 6. none of the above...")
            timingdecision1=input("")

        elif timingdecision1 == "5":
            print("Holidays, everyone loves the time to have a break. \n Honestly, you could work out the holidays by just seeing the end date of your current semester and the start date of your next one. However, i'm here to make your life easier so here you go; \n")
            print("Study breaks for September 2020 students will be 13/12/2020 - 17/01/2021 for their transition between first and second semester. Second semester break will be 18/04/2021 - 16/05/2021. \n Third semester study break for September 2020, postgraduates only, will be 15/08/2021 - 12/09/2021. \n")
            print("January 2021 students have their first study break18/04/2021 - 16/05/2021 and the second holidays are between 15/08/2021 - 12/09/2021. \n Post grads have the third semester study break 12/12/2021 - 16/01/2022, \n ")
            print("May 2021 postgraduates and undergraduates have their first study periods from 15/08/2021 to 12/09/2021, and the second semester break between 12/12/2021 - 16/01/2022. \n Postgrads have the semester 3 study break from 17/04/2022 - 15/05/2022. \n ")
            print("if you'd like to choose another part, you are more than welcome to choose another from the list;\n 1. Semester start dates. \n 2. Semester end dates. \n 3. Exams (may vary depending on course). \n 4. Gradutaion.  \n 6. none of the above...")
            timingdecision1=input("")
            
        elif timingdecision1 == "6":
            what_to_do()
        
        else:
            print("You have failed to follow simple instructions to get help from a little bot... how do you plan to survive university? \n I will give you another chance and restart \n press enter to continue.")
            break

def req_Docs() :
    if editMode() == True:
         print("req_Docs function")
    pairs = [
        ['my name is (.*)', ['Hey there %1']],
        ['(Yeah|Yes|yes|yeah|yes please|please|would you|how kind|thank you)' , ['I will try my best, lets start with your required documents.', 'Great, lets start with your required documents.']],
        ['(thanks|thank you|great|sweet)', ["You're welcome", "Anytime", "No problem"]],
        ['(hi|hello|hey|sup|whats good|hiya)', ['Hello there', 'Hiya', 'Yo, whats up?']],
        ['(creators|created|who created|creation)', ['My creators are; Miheala, Karam, Javaria, Alarick & Greg... Hence MkJag :)']],
        ['(what do you do?)', ['I am a chatbot: created to help with documents required for university. ']],
        ['(what is required?)', ['Very broad question... You need to have necessary documents to enroll, there are also a few absolutes that are not just documents.']],
        ['(what documents?)', ['Usually you will need; identity photo / card / birth certificate / adoption certificate / passport,\n your secondary school and college certificates,\n student finance proof if you plan to borrow money,\n A reccomendation letter and a personal statement.\n Medical, and dental, students are required to also pass a dbs check to start their program. ']],
        ['(absolutes|other than documents)', ['Other than the documents there are a few things you must complete before actually enrolling. If you plan to study on campus be sure to order your student ID\n If you plan on living in the student halls: make sure you have secured your accommodation and have placed your deposit if there is one, \n Check your student fees, and finance if you are borrowing money,\nensure any disabilities and mental health support arrangements are sorted and confirmed\nmake a note of any contact details you will need if you are unable to attend classes,\n Make sure you have completed and received a qualifying grade for any required prerequisite courses. ']],
        ['(student ID)' , ['This will allow you to access the building(s),other facilities and resources provided']],
        ['(disabilities)' , ['If you have any disabilities that require certian help, please let the university know so they can do their best to help you any way they can. \n If you dont have any disabilities you dont need to worry about that section.']]
    ]
    
    chat = Chat(pairs)
    chat.converse()

   
#Greg's Code:    
    
def eventGet():
    if editMode() == True:
         print("eventGet function")
    print('As you are looking for events, type in a keyword for searching:')
    userIn01 = input("Keyword: ")
    url_1 = 'https://www.coventry.ac.uk/search/?searchText='
    url_2 = userIn01
    url_3 = '&contentType=EventPage'

    #URL = 'https://www.coventry.ac.uk/search/?contentType=EventPage'
    URL = str(url_1+url_2+url_3)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(role='main')

    elements = results.find_all(class_='col-sm-12')

    #print('---------\n START\n')

    for elements in elements:
        title_elem = elements.find('a')
        time_elem = elements.find(class_='entry-label mls')
        descr_elem = elements.find('p')
        if None in (title_elem, time_elem, descr_elem):
            continue
        print('TITLE: ', end='')
        print(title_elem.text)
        print('TIME: ', end='')
        
        #ADD RELEVANCY CHECK - IF DATE EXPIRED
        
        print(time_elem.text)
        print('DESCRIPTION: ', end='')
        print(descr_elem.text)
        print('\n')

def appGet():
    if editMode() == True:
         print("appGet function")
    print('As you are looking for an application, type in a keyword for searching:')
    userIn01 = input("Keyword: ")
    url_1 = 'https://www.coventry.ac.uk/search/?searchText='
    url_2 = userIn01
    url_3 = '&contentType=NewsPage'

    #URL = 'https://www.coventry.ac.uk/search/?contentType=NewsPage'
    URL = str(url_1+url_2+url_3)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(role='main')

    elements = results.find_all(class_='col-sm-12')

    #print('---------\n START\n')

    for elements in elements:
        title_elem = elements.find('a')
        time_elem = elements.find(class_='entry-label mls')
        descr_elem = elements.find('p')
        if None in (title_elem, time_elem, descr_elem):
            continue
        print('TITLE: ', end='')
        print(title_elem.text)
        #print('TIME: ', end='')
        #print(time_elem.text)
        print('DESCRIPTION: ', end='')
        print(descr_elem.text)
        print('\n')


def enrolInfoGet():
    if editMode() == True:
         print("enrolInfoGet function")
    URL = 'https://www.coventry.ac.uk/international-students-hub/new-students/pre-arrival-information/enrolment'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.find("strong")
    optionTitles = soup.find_all("span", class_="text-left") 
    optionDescription = soup.find_all("div", class_="collapse")

    titleList=[]
    descrList=[]
    bigTitle = titles.get_text()

    for optionTitles in optionTitles:
        titleList.append(optionTitles.get_text())

    for optionDescription in optionDescription:
        descrList.append(optionDescription.get_text())
    
    for i in range(4):
        print(str(i+1)+" - "+titleList[i])
    userIn02 = int(input("You are "))
    print(descrList[userIn02-1])
    
    
def inputRequests():
    if editMode() == True:
         print("inputRequests function")
    print("\nAre you looking for: \n0 An event \n1 An app \n2 Enrollment \n3 Links to pages \n4 Information about learning material like Aula and Codio. \n5 Term Details. \n6 Doc info for enrolment. \n7 Clearing Info. \n8 International Student. \n9 Coventry University Buildings. \n10 Coventry University Parking. \n11 Part time jobs with Coventry University. Entry requirments \n12. Accomodation Students \n13. Scholarship \n14. ")
    userAnswer = int(input("\nChoose a number please: \n"))
    if userAnswer == 0:
      eventGet()
      print ("\n")
      qAnswered()
    elif userAnswer == 1:
      appGet()
      print ("\n")
      qAnswered()
    elif userAnswer== 2:
      enrolInfoGet()
      print ("\n")
      qAnswered()
    elif userAnswer ==3:
      linksToPages()
      print ("\n")
      qAnswered()
    elif userAnswer ==4:
      learnMatrl()
      print ("\n")
      qAnswered()
    elif userAnswer ==5:
      timing_details()
      print ("\n")
      qAnswered() 
    elif userAnswer ==6:
      req_Docs()
      print ("\n")
      qAnswered()
    elif userAnswer ==7:
      Clearing_Info()
      print ("\n")
      qAnswered()
    elif userAnswer ==8:
      InternationalStudent()
      print("\n")
      qAnswered()
    elif userAnswer ==9:
      BuildingsCU()
      print("\n")
      qAnswered()
    elif userAnswer ==10:
      Parking()
      print ( "\n" )
      qAnswered ()
    elif userAnswer ==11:
      PartTimeJobsCU()
      print ( "\n" )
      qAnswered ()
    elif userAnswer ==12
      entryRequirments()
      print ( "\n" )
      qAnswered ()
    elif userAnswer ==13
      accomodationStudents()
      print ( "\n" )
      qAnswered ()
    elif userAnswer ==14
      scholarshipCU()
      print ( "\n" )
      qAnswered ()
    elif userAnswer ==42:
      highLow()
      
#Alarick's code:

#First, the following code consists of assigning a username to the user, and the bot, to make the chatbot feel more realistic when chatting.
if editMode() == True:
    print("START function")
bots_name = "Mk Jag"
print("\n\nHello I am " + bots_name + ".\n")
print("Mk Jag are the initials of my creators.")
print("\nMy main function is to help with any questions you have regarding studying at Coventry University.")
user_name = input("\nWhat's your name?\n")
print("Okay great, thanks " + user_name + ".\n")
    
inputRequests()