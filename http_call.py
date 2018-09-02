import requests
f = open("output.txt", "a+")
f.write('Synchronous calls to webpage: https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39 \n')
for x in range(3):
    r = requests.get('https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39')
    f.write(r.headers['Date'] + '\n')