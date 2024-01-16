import pygame


class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Créer le plateau initial avec des pions
        # (À implémenter : positionner les pions blancs et noirs)
        pass

    def draw(self, screen):
        # Dessiner le plateau
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (col*100, row*100, 100, 100))
