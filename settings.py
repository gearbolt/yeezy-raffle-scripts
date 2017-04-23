import configparser
import os


c = configparser.ConfigParser()
configFilePath = os.path.join('', 'config.cfg')
c.read(configFilePath)


class Config:
    try:
        # Settings
        isThreaded = c.getboolean('settings', 'threaded')
        numberOfThreads = c.getint('settings', 'numberOfThreads')
        numberOfEntries = c.getint('settings', 'numberOfEntries')

        # Details
        firstName = c.get('details', 'lastName')
        lastName = c.get('details', 'lastName')
        email = c.get('details', 'email')
        phone = c.get('details', 'phone')
        address = c.get('details', 'address')
        city = c.get('details', 'city')
        state = c.get('details', 'state')
        zip = c.get('details', 'zip')
        country = c.get('details', 'country')
        size = c.get('details', 'size')
        birthday = c.get('details', 'birthday')
        validConfig = True

    except ValueError:
        validConfig = False

    def __init__(self, *args, **kwargs):
        pass

    def print_config(self):
        print('\n[Settings]')
        print('[Threaded]', self.isThreaded)
        print('[Number Of Threads]', self.numberOfThreads)
        print('[Number Of Entries]', self.numberOfEntries)
        print('\n[User Details]')
        print('[First Name]', self.firstName)
        print('[Last Name]', self.lastName)
        print('[Email]', self.email)
        print('[Phone Number]', self.phone)
        print('[Address]', self.address)
        print('[City]', self.city)
        print('[State / County]', self.state)
        print('[City]', self.zip)
        print('[Country]', self.country)
        print('[Size]', self.size)
        print('[Birthday]', self.birthday, '\n')


user_config = Config()
