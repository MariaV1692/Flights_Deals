# Flights_Deals
Find the most cheap flight deals and send yourself a message every time there is a great flight deal

## Installation

Install all the required packages from the requirements.txt

```bash
pip install -r requirements.txt
```

Rename the .env.example file to .env and change the values

```bash
 cp .env.example .env
```

## Usage

Fill/change all the required values in the .env file

```python
# Your Sheety Authentication Token
SHEETY_AUTH=""
# Sheety username
SHEETY_USERNAME=""
# Your Sheety project name
SHEETY_PROJECT_NAME=""
# Your Sheety flights sheet name
FLIGHTS_SHEETY_SHEET_NAME=""
# Your Sheety users sheet name
USERS_SHEETY_SHEET_NAME=""
# Your API key from KIWI
KIWI_API_KEY=""
# Your phone number
MY_NUM=""
# your Email password
EMAIL_PASS=""
# your Twilio SID key
TWILIO_SID_KEY=""
# Your Twilio authentication token
TWILIO_AUTH_TOKEN=""

```