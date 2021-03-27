from model.drawable import Drawable


class DefeatHeader(Drawable):
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, view):
        first_line = view.font_72.render("You Lose", True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 2 - first_line.get_width() // 2, view.height // 4))
