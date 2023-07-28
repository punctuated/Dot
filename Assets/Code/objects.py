import fusionengine as engine

from fusionengine.files.window import _CustomRenderer as Renderer  # NOQA


def draw_object(window: Renderer, image, x, y, width, height, main: engine.Main):
    img = main.image.open_image(window, image, x, y, width, height)
    main.image.draw_image(img)
