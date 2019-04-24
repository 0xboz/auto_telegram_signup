# Auto Telegram Signup
Automated telegram account signup script. :smirk:

## Prerequisite
* Phone verification code API. Sign up an account at [getsmscode.com](https://www.getsmscode.com/) and top up a few dollars.
* A Telegram account with *api_id* and *api_hash*. Visit https://my.telegram.org/apps and fill out the forms.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## How-to
* Create an configuration file named *config.ini* in the root directory

```
touch config.ini
```
* Add your username and token

> [pyrogram]  
> api_id = YOUR_TELEGRAM_API_ID  
> api_hash = YOUR_TELEGRAM_API_HASH  

> [GetSMSCode.com]  
> username = YOUR_USERNAME  
> token = YOUR_TOKEN  
> api_url = http://www.getsmscode.com/do.php  

* Run
```
python main.py
```

