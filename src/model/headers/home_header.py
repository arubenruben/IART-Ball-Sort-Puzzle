from src.model.drawable import Drawable


class HomeHeader(Drawable):
    def update(self):
        super().update()

    def draw(self, view):
        first_line = view.font_72.render("Ball Sort Puzzle", True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 2 - first_line.get_width() // 2, view.height // 8))
