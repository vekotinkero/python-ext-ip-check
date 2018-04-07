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
