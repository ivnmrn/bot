# Daily bot

Daily bot is a Python telegram bot for multiple things like search for imdb movie information, picture of the day of NASA, and Zelda breath of the wild finder items.

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install Daily bot.

```bash
pip3 install python-telegram-bot==10.1.0
```

## Usage

First of all, be sure that you have a telegram bot [token](https://core.telegram.org/bots) and a IMDb [token](http://www.omdbapi.com/).

In bot/src/config/auth.py change the parameters for your token.

```python
TOKEN_TELEGRAM='YOUR_TOKEN'
TOKEN_IMDB='YOUR_TOKEN'
```

Then in bot/src/ run 
```bash
python3 main.py
```

## License

