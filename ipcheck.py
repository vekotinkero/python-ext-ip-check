import requests
import yagmail

# Get the current IP from web
r = requests.get('https://dynamicdns.park-your-domain.com/getip')
currentip = r.text

# Get the saved IP
with open('savedip') as file:
    savedip = file.readline()

if (savedip == currentip):
    print "IP unchanged. It's " + savedip
else:
    print "IP HAS BEEN CHANGED!"
    print "Old IP is: "
    print savedip
    print "Current IP is: "
    print currentip

    # Save new ip to file
    with open('savedip','r+') as file:
        file.write(currentip)

    # Notify via email
    yag = yagmail.SMTP("[ INSERT YOUR EMAIL HERE ]", oauth2_file="~/oauth2_creds.json")
    yag.send(to="[ INSERT EMAIL YOU WANT TO SPAM HERE ]",
             subject="[ EMAIL SUBJECT ]",
             contents =" [ EMAIL CONTENTS ]"
             )

        
file.close()
