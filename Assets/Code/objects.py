import fusionengine as engine


type winobj = engine.Window


def draw_object(window: winobj, image, x, y, width, height):
    img = engine.Image(window, image, x, y, width, height)
    img.draw()
