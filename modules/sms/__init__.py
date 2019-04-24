#!/usr/bin/env python
import requests


class GetSMSCode:
    def __init__(self, config):
        self.username = config['GetSMSCode.com']['username']
        self.token = config['GetSMSCode.com']['token']
        self.api_url = config['GetSMSCode.com']['api_url']

    @property
    def account_info(self):
        payload = {
            'action': 'login',
            'username': self.username,
            'token': self.token,
        }
        r = requests.post(self.api_url, params=payload)
        r.encoding = 'utf-8'
        keys = ['username', 'balance', 'points', 'discount_rate', 'api_thread']
        values = r.text.split('|')
        return dict(zip(keys, values))

    def get_mobile_number(self):
        payload = {
            'action': 'getmobile',
            'username': self.username,
            'token': self.token,
            'pid': 10,
        }
        r = requests.post(self.api_url, params=payload)
        r.encoding = 'utf-8'
        return r.text

    def blacklist(self, mobile_number):
        payload = {
            'action': 'addblack',
            'username': self.username,
            'token': self.token,
            'pid': 10,
            'mobile': mobile_number,
        }
        r = requests.post(self.api_url, params=payload)
        r.encoding = 'utf-8'
        if r.text == 'Message|Had add black list':
            return '{} has been blacklisted.'.format(mobile_number)

    @property
    def mobile_list(self):
        payload = {
            'action': 'mobilelist',
            'username': self.username,
            'token': self.token,
        }
        r = requests.post(self.api_url, params=payload)
        r.encoding = 'utf-8'
        mobile_list = []
        for mobile in r.text.split(','):
            keys = ['mobile', 'pid']
            values = mobile.split('|')
            mobile_list.append(dict(zip(keys, values)))
        return mobile_list

    def get_code(self, mobile_number):
        payload = {
            'action': 'getsms',
            'username': self.username,
            'token': self.token,
            'pid': 10,
            'mobile': mobile_number,
            'author': self.username,
        }
        r = requests.post(self.api_url, params=payload)
        r.encoding = 'utf-8'
        code = ''.join([num for num in list(
            r.text.split('|')[1]) if num.isdigit()])
        return code
