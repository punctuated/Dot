import fusionengine as engine

from fusionengine.files.window import Window


def draw_object(window: Window, image, x, y, width, height):
    img = engine.Image(window, image, x, y, width, height)
    img.draw()
