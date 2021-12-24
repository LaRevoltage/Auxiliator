# Auxiliator
Auxiliator is telegram bot for basic web-application analysis
# What for?
Sometimes there is no access to your main PC, where you can scan web-site and search for exploits, and you only have for e.g your phone.
Some people would say, that you can just connect with ssh, but is is not really easy to type on small screen.
That is why, i created this telegram bot, where it is simpler to analyse the website for further testing.
# What can it do?
1. Testing if site uses WAF.
2. Search for real IP via Censys if site uses WAF to hide it.
3. Scan IP for open ports.
4. Get additional info about services and network
5. SearchSploit right in your telegram, to look up some exploits for further testing
# How to use it?
Unfortunately, bot is not hosted at the moment, because it is made for personal use. But if will be usefull to people, i will host it.
To set up the bot, you need to:
1. Create a new bot at FatherBot and get the token.
2. Place the token in Auxiliator.py
3. Run Auxiliator.py
4. Use the bot!
There are following command for bot:
1. /searchbyip IP — Gets information from search.censys.io about the IP.
2. /searchbydomain DOMAIN — Searches for IPS by given domain, can be usefull when site is behind WAF.
3. /scan IP/DOMAIN — Scan targets for opened ports, by default it scans from port 1, to 65535 with 5000 threads, you should test diffrent numbers of threads to get fastest scan time on your server.
4. /searchsploit — Searches for exploits in exploit-db by name.
# Contacts:
@LaRevoltage — Telegram
@evoltage#2077 — Discord
