# python-ext-ip-check
External IP Monitor used to monitor external IP changes by your ISP if you don't have any Dynamic DNS service.
Written in Python 2, but should definitely upgrade someday to 3-point-something... But, I guess I'm too lazy for that.

# So what does it do?
It basically compares IP fetched from web (http://dynamicdns.park-your-domain.com/getip in this case) to a saved address saved into file called 'savedip'. If they match, all is well and you can relax. If they don't, it sends an email and updates the 'savedip'. So it doesn't even do much, either way you can relax. You can to do something for the IP change if you want. I'm updating my domains DNS records manually, because I'm old school and ah, so cool. That's right, I rhyme as well.

# Building Blocks I've used
- Raspberry Pi 3
- Python 2.7 (could definitely use more up-to-date versions)
- Requests Library http://docs.python-requests.org/en/master/
- Yagmail https://github.com/kootenpv/yagmail 
- crontab for scheduled checkups
- Beers for rudimentary coding

# Yagmail and Google
I've used my Gmail account for this. And for security reasons I used Oauth2 so I don't have to put my usernames and password in every garbage piece of code I happen to generate. If you want to set it up go ahead, grab a beer and read more about it from [here](https://github.com/kootenpv/yagmail). Read and follow the instructions and you shall be rewarded... after many beers and probably some frustration I mean. 

# Crontab
If you're familiar with RasPi and Linux, you're probably familiar with [Crontab](http://www.adminschoice.com/crontab-quick-reference). Anyway, this is what I added to sudo Crontab. This will run the ipcheck.py every month at 0:00. Remember to make your script executable and run it as sudo.

```
# Check the External IP Address and send email if it's changed (monthly at midnight)
0 0 1 * * sudo python /home/pi/ipcheck.py
```
# Shortcut for lazy people
After you've downloaded this project to your home folder (e.g. /home/pi) and if you're lazy like me, you can make necessary linux mambo jambo with the script [mambojambosetup.sh](https://github.com/vekotinkero/python-ext-ip-check/blob/master/mambojambosetup.sh). Make it executable and run it as sudo. It will install Yagmail for Python and make the changes to Crontab. If you want to run the ipcheck.py more or less frequently edit this script or edit crontab directly with ``` sudo crontab -e ```. But be warned, it has a rear light guarantee and it removes itself after it has run. 

