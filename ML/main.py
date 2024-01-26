import numpy as np
from PIL import Image  #이미지 보여주는 라이브러리 
import matplotlib.pyplot as plt

color_img = Image.open('./images/fruits.jpg')
plt.imshow(color_img)
plt.show()

# import game.sound.echo 
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# from game import *
# echo.echo_test()
# render.render_test()

# import game.graphic.render
# game.graphic.render.render_test()

# from game.graphic import render
# render.render_test()

# from game.graphic.render import render_test
# render_test()

# from game import *
# render.render_test()