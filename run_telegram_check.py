import requests

# Define your bot token
TOKEN = ''

# Define a function to read updates from Telegram
def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        updates = data['result']
        return updates
    else:
        print('Failed to get updates.')
        return []

# Define a function to handle incoming messages
def handle_message(message):
    text = message['text']
    chat_id = message['chat']['id']
    
    # Process the received message
    # You can add your own logic here
    
    # Reply to the message
    send_message(chat_id, f'You said: {text}')

# Define a function to send a message to a chat
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Message sent successfully.')
    else:
        print('Failed to send message.')

# Get and process incoming updates

updates = get_updates()
for update in updates:
    message = update.get('message')
    if message:
        handle_message(message)

print("finished...")

