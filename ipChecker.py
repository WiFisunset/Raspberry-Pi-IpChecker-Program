# Python Program to Get the IP Address & Email you the IP Address if it changes.
# Note: The variable that checks if the IP has changed is named: ipaddrConstant. 
import socket
import os
import smtplib

# This finds and define's the IP Address that Dynamically will change every so often.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddrDynamic = s.getsockname()[0]
print ("IP:", ipaddrDynamic)

# Function: ipChecker(ipaddrDynamic)
# Function Definition:   Checks the Device's Dynamic IP against an IP Checker; 
# If they differ, the program makes the variables match, 
# and sends off an email notifying of the change. 
# Paramaters: ipaddrDynamic
def ipChecker(ipaddrDynamic):

  # Variables that keep the while loop in a constant run to always check for IP Address Changes.
  test1 = 1
  test2 = 2

  # The Variable that the Dynamic IP checks against
  ipaddrConstant = 8
  
  # While loop
  while (test1 != test2):

    # If the Dynamic and Constant IP match; Do Nothing.
    if (ipaddrDynamic == ipaddrConstant):
      nothing = 1

    # If the Dynamic IP and Constant IP mismatch; Make them match, and email the changed IP.
    if (ipaddrDynamic != ipaddrConstant):
      
      print(ipaddrDynamic)
      print(ipaddrConstant)

      # Sets the programs IP Checker to match the changed Dynamic IP Address.
      ipaddrConstant = ipaddrDynamic

      # Creates a SMTP session 
      s = smtplib.SMTP('smtp.gmail.com', 587) 
  
      # Starts TLS for security 
      s.starttls() 
  
      # Authentication for logging into the email
      # Note: You'll have to follow the link below to allow the program to send gmail's.
      # https://myaccount.google.com/lesssecureapps
      s.login("placeSenderEmailAddressHere", "placeSenderEmailPasswordHere") 
  
      # Emails the changed IP Address so remote ssh can be configured to match.
      message = ipaddrDynamic
  
      # Sends the mail out after validating the email login credentials
      s.sendmail("placeSenderEmailAddressHere", "placeRecipientEmailAddressHere", message) 
  
      # Terminates the session 
      s.quit()

      # Prints out the IP Checker for validation
      print(ipaddrConstant)

  # Returns the Dynamic IP Address
  return ipaddrDynamic


#Catch when script is interrupted, cleanup correctly
try:
    #Main loop
    while True:
        # Function: ipChecker(ipaddrDynamic)
        # Function Definition:   Checks the Device's Dynamic IP against an IP Checker; 
        # If they differ, the program makes the variables match, 
        # and sends off an email notifying of the change.
        # Paramaters: ipaddrDynamic
        ipChecker(ipaddrDynamic)
except KeyboardInterrupt:
    pass
finally:
    print("Program Has Terminated.")
