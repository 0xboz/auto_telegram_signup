#!/usr/bin/env python
from pyrogram import Client
from modules.configuration import Configuration
from modules.sms import GetSMSCode
from time import sleep

cfg_obj = Configuration()
config = cfg_obj.load()
sms = GetSMSCode(config)


def phone_code_callback(mobile_number):
    sleep(30)
    code = sms.get_code(mobile_number)
    return code


def main():
    mobile_number = sms.get_mobile_number()
    # Get current account balance before signup
    print(sms.account_info)
    try:
        app = Client(
            session_name=mobile_number,
            phone_number=mobile_number,
            phone_code=phone_code_callback,
            first_name="John",
            last_name="Doe"
        )

        with app:
            print(app.get_me())

        return mobile_number

    except Exception as e:
        print(e)
        print(sms.blacklist(mobile_number))
        return None


if __name__ == '__main__':
    main()
