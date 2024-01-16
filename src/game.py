import pygame

from board import Board
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (800, 800))  # Définir la taille de la fenêtre
        pygame.display.set_caption("Jeu de Dames")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.player1 = Player('white')
        self.player2 = Player('black')
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Remplir l'écran de noir
            self.board.draw(self.screen)  # Dessiner le plateau
            pygame.display.flip()  # Mettre à jour l'affichage

            self.clock.tick(60)  # Limiter à 60 FPS

    def draw(self):
        # Dessiner l'état du jeu
        pass
