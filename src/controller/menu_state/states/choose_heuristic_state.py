import pygame

from src.controller.ai.execution_template.a_star import AStar
from src.controller.ai.execution_template.greedy import Greedy
from src.controller.ai.heuristics.concrete_heuristics.distance import DistanceHeuristic
from src.controller.ai.heuristics.concrete_heuristics.entropy import EntropyHeuristic
from src.controller.ai.heuristics.concrete_heuristics.taboo_search_like import TabooSearchHeuristic
from src.controller.events.event_manager_strategy.home_event_manager import HomeEventManager
from src.controller.menu_state.menu_state import MenuState
from src.model.elements.button import Button
from src.model.menu_models.home_state_model import HomeStateModel
from src.model.menu_models.playing_state_model import PlayingStateModel


class ChooseHeuristicState(MenuState):
    def __init__(self, game, model, algorithm):
        super().__init__(game, model)
        self._algorithm = algorithm
        self._event_manager = HomeEventManager(model)

        button_h1 = Button(pygame.Rect(model.width // 6 - 200 // 2, 2 * model.height // 6, 200, 100),
                           "Entropy", self.change_state_heuristic_h1)
        button_h2 = Button(pygame.Rect(model.width // 2 - 300 // 2, 2 * model.height // 6, 300, 100),
                           "Distance Homogenous", self.change_state_heuristic_h2)

        if algorithm != "A_STAR":
            button_h3 = Button(pygame.Rect(model.width // 2 + 350 // 2, 2 * model.height // 6, 300, 100),
                               "Taboo Search Like", self.change_state_heuristic_h3)
            self.model.buttons.append(button_h3)

        button_back = Button(pygame.Rect(model.width // 2 - 400 // 2, 4 * model.height // 6, 400, 100),
                             "Back", self.change_state_bot_choose)

        self.model.buttons.append(button_back)
        self.model.buttons.append(button_h1)
        self.model.buttons.append(button_h2)
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

    def change_state_heuristic_h1(self):
        if self._algorithm == "A_STAR":
            self.game.menu_state = AStar(self.game,
                                         PlayingStateModel((self.game.view.width, self.game.view.height)),
                                         EntropyHeuristic())
        else:
            self.game.menu_state = Greedy(self.game,
                                          PlayingStateModel((self.game.view.width, self.game.view.height)),
                                          EntropyHeuristic())
        self.game.run()

    def change_state_heuristic_h2(self):

        if self._algorithm == "A_STAR":
            self.game.menu_state = AStar(self.game,
                                         PlayingStateModel((self.game.view.width, self.game.view.height)),
                                         DistanceHeuristic())
        else:
            self.game.menu_state = Greedy(self.game,
                                          PlayingStateModel((self.game.view.width, self.game.view.height)),
                                          DistanceHeuristic())
        self.game.run()

    def change_state_heuristic_h3(self):

        if self._algorithm == "A_STAR":
            self.game.menu_state = AStar(self.game,
                                         PlayingStateModel((self.game.view.width, self.game.view.height)),
                                         TabooSearchHeuristic())
        else:
            self.game.menu_state = Greedy(self.game,
                                          PlayingStateModel((self.game.view.width, self.game.view.height)),
                                          TabooSearchHeuristic())
        self.game.run()

    def change_state_bot_choose(self):
        from src.controller.menu_state.states.choose_bot_state import ChooseBotState
        self.game.menu_state = ChooseBotState(self.game,
                                              HomeStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()
