import base64, tempfile


# Sorting
def sort_elements_from_top(el_list):
    el_list.sort(key=getylocation)


def sort_elements_from_bottom(el_list):
    el_list.sort(key=getylocation, reverse=True)


def sort_elements_from_right(el_list):
    el_list.sort(key=getxlocation)


def sort_elements_from_left(el_list):
    el_list.sort(key=getxlocation, reverse=True)


def getylocation(el):
    return el.location["y"]


def getxlocation(el):
    return el.location["x"]


# screenshot element
def screen_element(el, path=None):
    img_data = el.screenshot_as_base64

    if path is None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as image:
            image.write(base64.b64decode(img_data))
        image.close()
        return image.name
    else:
        with open(path, "wb") as image:
            image.write(base64.b64decode(img_data))
        image.close()
        return path


# MAYBE TODO:
# [ ] els under el
# [ ] els ontop of el
# [ ] els at right of el
# [ ] els left of el
# [ ] tesseract on base64 screenshot
# [ ] opencv on base64 screenshot
