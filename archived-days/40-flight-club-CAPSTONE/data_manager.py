import json


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        try:
            with open('data.json') as data_file:
                self.data = json.load(data_file)
        except FileNotFoundError:
            print('Existing data not found, starting new db...')
            self.data = {}
        else:
            print('Loading Data...')
            print(self.data)

    def add_user(self, user_id):
        self.data.update({user_id: {}})

    def set_home(self, user_id, home_airport):
        print('Setting Home...')
        # if 'home' in self.data[user_id]:
        #     print('home found')
        #     self.data[user_id]['home'] = home_airport
        # else:
        self.data[user_id].update({'home': home_airport})

    def add_airport(self, user_id, airport):
        print('Adding Airport...')
        if 'airports' in self.data[user_id]:
            self.data[user_id]['airports'].append(airport)
        else:
            self.data[user_id].update({'airports': [airport]})
        self.write_file()

    def write_file(self):
        print('Saving Data...')
        print(self.data)
        with open('data.json', mode='w') as f:
            json.dump(self.data, f, indent=4)

