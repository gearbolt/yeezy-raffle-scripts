import requests, threading
from settings import user_config
from random import getrandbits


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
url = 'https://www.excelsiormilano.com/module/antcontactcustom/sendmail'


def raffle(thread):
    for i in range(1, user_config.numberOfEntries+1):
        email = user_config.email.split('@')[0] + \
                '+{}@'.format(getrandbits(40)) + \
                user_config.email.split('@')[1]

        payload = {
            'first_name': user_config.firstName,
            'last_name': user_config.lastName,
            'birth': birthday,
            'mail': email,
            'number': user_config.phone,
            'size': user_config.size,
            'country': user_config.country,
            'state': user_config.state,
            'city': user_config.city,
            'zip': user_config.zip,
            'street': user_config.address
        }

        r = requests.post(url,
                          data=payload,
                          headers=headers
                          )
                
        if r.status_code == 200:
            print('[Thread {}] - {}/{} completed. ({})'.format(
                thread,
                i,
                user_config.numberOfEntries,
                email
            ))
        else:
            print('[Thread {}] - {}/{} failed request. ({})'.format(
                thread,
                i,
                user_config.numberOfEntries,
                r.status_code
            ))

    print('[Thread {}] - all assigned entries completed!'.format(
        thread
    ))

if __name__ == "__main__":
    print('\n[EXCELSIOR MILANO RAFFLE SCRIPT]\n\n@BertieDent')

    if user_config.validConfig:
        user_config.print_config()

        # User detail sort specifically for this site.
        split_bday = user_config.birthday.split('/')
        birthday = split_bday[2] + '-' + split_bday[1] + '-' + split_bday[0]

        if user_config.isThreaded:
            thread_list = []
            for i in range(1, user_config.numberOfThreads+1):
                t = threading.Thread(target=raffle, args=(i,))
                thread_list.append(t)
                t.start()
        else:
            raffle(thread=1)
    else:
        print('\n[INVALID CONFIG FILE - CHECK IT AND TRY AGAIN!]')
