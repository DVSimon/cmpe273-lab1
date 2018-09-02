import grequests

f = open("output.txt", "a+")
f.write('\nAsynchronous calls to webpage: https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39 \n')

urls = [
    'https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39',
    'https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39',
    'https://webhook.site/f54abbd8-09ae-463b-805b-a4ff1d947c39'
]

r = (grequests.get(u) for u in urls)
rs = grequests.map(r)
for response in rs:
    f.write(response.headers['Date'] + '\n')