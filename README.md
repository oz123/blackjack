# blackjack

A network multiplayer blackjack game using Python

# Rules of the game

The rules are the american based version of black jack as described in [wikipedia](https://en.wikipedia.org/wiki/Blackjack).

# The game

Player one starts the blackjack server which deals the cards

```
blackjack serve
[listening to player on 192.168.1.122:8000]
```

Player two joins the server with

```
blackjack join 192.168.1.122:8000
```
