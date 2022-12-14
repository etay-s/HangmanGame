import requests

class Words:
    def __init__(self):
        self._url = "https://wordsapiv1.p.rapidapi.com/words/"
        self._headers = {
            # FIXME: Insert the new API KEY
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
            }
        self._words = []

    def random(self, length=None) -> str:
        payload = {'random': 'true'}
        if length:
            payload['letters'] = str(length)
        response = requests.get(f'{w._url}', headers=w._headers, params=payload)
        if response.status_code == 200:
            return response.json()['word']


if __name__ == '__main__':
    w = Words()
    # payload = {'random': 'true', 'letters': '4'}
    # response = requests.get(f'{w._url}', headers=w._headers, params=payload)
    # if response.status_code == 200:
    #     word = response.json()['word']
    word = w.random(5)
    print(word)
    mistakes = []
    checks = {l:False for l in [*word]}
    while(not all(checks.values())):
        letter = input('Guess:  ')
        if letter not in mistakes:
            if letter in word:
                print('GOOD JOB')
                checks[letter] = True
            else:
                mistakes.append(letter)
        else:
            print('Already tried this letter...')
    print('complete')
