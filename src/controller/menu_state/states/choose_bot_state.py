import pygame

from src.controller.AI.execution_template.bfs import BFS
from src.controller.AI.execution_template.dfs import DFS
from src.controller.AI.execution_template.iterative_deepening import IterativeDeepening
from src.controller.events.event_manager_strategy.home_event_manager import HomeEventManager
from src.controller.menu_state.menu_state import MenuState
from src.controller.menu_state.states.choose_heuristic_state import ChooseHeuristicState
from src.model.elements.button import Button
from src.model.menu_models.home_state_model import HomeStateModel
from src.model.menu_models.playing_state_model import PlayingStateModel


class ChooseBotState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

        self._event_manager = HomeEventManager(model)
        button_dfs = Button(pygame.Rect(model.width // 4 - 200 // 2, 2 * model.height // 6, 200, 100),
                            "DFS", self.change_state_dfs)
        button_bfs = Button(pygame.Rect(model.width // 2 - 200 // 2, 2 * model.height // 6, 200, 100),
                            "BFS", self.change_state_bfs)

        button_iterative_deepening = Button(pygame.Rect(model.width // 2 + 300 // 2, 2 * model.height // 6, 300, 100),
                                            "Iterative Deepening", self.change_state_iterative_deepening)

        button_greedy = Button(pygame.Rect(model.width // 2 - 300, 3 * model.height // 6, 300, 100),
                               "Greedy", self.change_state_greedy)

        button_a_star = Button(pygame.Rect(model.width // 2 + 50, 3 * model.height // 6, 300, 100),
                               "A Star", self.change_state_a_star)

        button_back = Button(pygame.Rect(model.width // 2 - 400 // 2, 4 * model.height // 6, 400, 100),
                             "Back", self.change_state_home)

        self.model.buttons.append(button_dfs)
        self.model.buttons.append(button_bfs)
        self.model.buttons.append(button_iterative_deepening)
        self.model.buttons.append(button_greedy)
        self.model.buttons.append(button_a_star)
        self.model.buttons.append(button_back)

        self.running = True

    def run(self):

        while self.running:

            self.model.update()
            self.model.draw(self.game.view)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    button = self._event_manager.handle_mouse_event(event)
                    if button is not None:
                        self.running = False
                        return button.callback()


    def change_state_home(self):
        from src.controller.menu_state.states.home_state import HomeState
        from src.model.menu_models.home_state_model import HomeStateModel

        self.game.menu_state = HomeState(self.game,
                                         HomeStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()

    def change_state_dfs(self):
        self.game.menu_state = DFS(self.game, PlayingStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()

    def change_state_bfs(self):
        self.game.menu_state = BFS(self.game, PlayingStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()

    def change_state_iterative_deepening(self):
        self.game.menu_state = IterativeDeepening(self.game,
                                                  PlayingStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()

    def change_state_greedy(self):
        self.game.menu_state = ChooseHeuristicState(self.game,
                                                    HomeStateModel((self.game.view.width, self.game.view.height)),
                                                    "GREEDY")
        self.game.run()

    def change_state_a_star(self):

        self.game.menu_state = ChooseHeuristicState(self.game,
                                                    HomeStateModel((self.game.view.width, self.game.view.height)),
                                                    "A_STAR")
        self.game.run()
