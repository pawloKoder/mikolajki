# Mikołajki

To run script copy **secrets.py.example** as **secrets.py** and fill with your Mailgun settings.
Copy also **data.py.example** as **data.py**.
Fill it with mails and names of people taking part in the draw.
Text in *SECRET_MESSAGE* will be ciphered and distributed along people form the list.
 
## Usage

Fill *secrets.py* and *data.py* with data.

Run `python mail.py` to send the mails. 

## Dependencies 

All dependencies are listed in *requirements.txt*. To install them just type `pip install -r requirements.txt`.
We recommend using virtualenv.