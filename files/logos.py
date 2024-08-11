import random
from files.colors import text_color, bg_color

W = text_color('white')
C = text_color('cyan')
Y = text_color('yellow')
R = text_color('red')
M = text_color('blue')
G = text_color('green')
B = text_color('blue')
RB = bg_color('red')
GB = bg_color('green')
RES = bg_color('reset')

L1 = f"""{Y}
⢸⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡷⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇ {W}Are ya winning son?{Y}
⢸⠀⠀⠀⠀⠀⠖⠒⠒⠒⢤⠀⠀⠀⡇
⢸⠀⠀⣀⢤⣼⣀⡠⠤⠤⠼⠤⡄⠀⡇⠀
⢸⠀⠀⠑⡤⠤⡒⠒⠒⡊⠙⡏⠀⢀⡇⠀
⢸⠀⠀⠀⠇⠀⣀⣀⣀⣀⢀⠧⠟⠁⡇
⢸⠀⠀⠀⠸⣀⠀⠀⠈⢉⠟⠓⠀⠀⡇
⢸⠀⠀⠀⠀⠈⢱⡖⠋⠁⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⣠⢺⠧⢄⣀⠀⠀⣀⣀⡇
⢸⠀⠀⠀⣠⠃⢸⠀⠀⠈⠉⡽⠿⠯⡆
⢸⠀⠀⣰⠁⠀⢸⠀⠀⠀⠀⠉⠉⠉⡇
⢸⠀⠀⠣⠀⠀⢸⢄⠀⠀⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⠀⢸⠀⢇⠀⠀⠀⠀⠀⡇
.................

                {RB}{W} A U T H O R : K R I S H N A && N I T H I S H{RES}{W}


"""


def render():
    selected = L1
    return selected
