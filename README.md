# Amazing Discord Snitching Bot

This bot snitches on the user for using a bad word in the given bad word database.
If the word is in the very bad word database, then the message is also deleted.

Additionally, it can check that LFG pings were not sent within 15 minutes of a previous LFG ping.

## Usage

### Configuration

To configurate the bot, copy `config.example` to `config` and edit it:

```sh
$ cp config.example config && vim config
```

### Defining bad words

The default bad word databases are `profanity.txt` and `strict-profanity.txt`, with the later containing the words which, when used, trigger message deletion. Words and word combinations need to be separated by newlines:

```
bad word 1
bad word 2
```

### Running

To run the snitch bot, you need to have a working Python environment with the `discord.py` module. Once these are set up, change directory to snitch bot's and run it with python:

```sh
$ cd discord-snitch-bot
$ python3 snitch-bot.py
```
