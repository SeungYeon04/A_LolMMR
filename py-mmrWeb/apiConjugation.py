from flask import Flask, render_template, request
import requests
from ApiKeyfile import API_KEY

appInput = Flask(__name__)

def get_account_info(game_name, tag_line):
    url = f'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"API Error: {response.status_code} - {response.text}"

@appInput.route('/', methods=['GET', 'POST'])
def index():
    account_info = None
    if request.method == 'POST':
        game_name = request.form['game_name']
        tag_line = request.form['tag_line']
        account_info = get_account_info(game_name, tag_line)
    return render_template('index.html', account_info=account_info)

if __name__ == '__main__':
    appInput.run(debug=True)
