"""Test TCP communication for the board.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from minesweeper import MSGame

game = MSGame(10, 10, 5, port=5678, ip_add="127.0.0.1")

game.tcp_accept()

while True:
    data = game.tcp_receive()

    if data == "help\n":
        game.tcp_help()
        game.tcp_send("> ")
    elif data == "exit\n":
        game.tcp_close()
    elif data == "print\n":
        game.tcp_send(game.get_board())
        game.tcp_send("> ")
    elif data == "":
        game.tcp_send("> ")
    else:
        game.play_move_msg(data)
        game.tcp_send(game.get_board())
        game.tcp_send("> ")

    if game.game_status == 1:
        game.tcp_send("[MESSAGE] YOU WIN!\n")
        game.tcp_close()
    elif game.game_status == 0:
        game.tcp_send("[MESSAGE] YOU LOSE!\n")
        game.tcp_close()
