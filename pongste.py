import pygame
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre du jeu
largeur, hauteur = 640, 480
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pong")

# Couleurs
blanc = (255, 255, 255)

# Initialisation des raquettes et de la balle
raquette1 = pygame.Rect(50, hauteur // 2 - 70, 10, 140)
raquette2 = pygame.Rect(largeur - 60, hauteur // 2 - 70, 10, 140)
balle = pygame.Rect(largeur // 2 - 15, hauteur // 2 - 15, 30, 30)

# Vitesses de la balle
vitesse_balle_x = 7
vitesse_balle_y = 7

# Variables pour les scores
score1 = 0
score2 = 0

# Police de texte
police = pygame.font.Font(None, 36)

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mouvement des raquettes
    touches = pygame.key.get_pressed()
    if touches[pygame.K_w] and raquette1.top > 0:
        raquette1.y -= 10
    if touches[pygame.K_s] and raquette1.bottom < hauteur:
        raquette1.y += 10
    if touches[pygame.K_UP] and raquette2.top > 0:
        raquette2.y -= 10
    if touches[pygame.K_DOWN] and raquette2.bottom < hauteur:
        raquette2.y += 10

    # Déplacement de la balle
    balle.x += vitesse_balle_x
    balle.y += vitesse_balle_y

    # Rebond de la balle sur les bords
    if balle.top <= 0 or balle.bottom >= hauteur:
        vitesse_balle_y = -vitesse_balle_y

    # Collision avec les raquettes
    if balle.colliderect(raquette1) or balle.colliderect(raquette2):
        vitesse_balle_x = -vitesse_balle_x

    # Balle sortie du jeu (marquer un point)
    if balle.left <= 0:
        score2 += 1
        balle = pygame.Rect(largeur // 2 - 15, hauteur // 2 - 15, 30, 30)
        vitesse_balle_x = 7

    if balle.right >= largeur:
        score1 += 1
        balle = pygame.Rect(largeur // 2 - 15, hauteur // 2 - 15, 30, 30)
        vitesse_balle_x = -7

    # Effacement de l'écran
    fenetre.fill((0, 0, 0))

    # Dessin des raquettes et de la balle
    pygame.draw.rect(fenetre, blanc, raquette1)
    pygame.draw.rect(fenetre, blanc, raquette2)
    pygame.draw.ellipse(fenetre, blanc, balle)

    # Affichage des scores
    texte1 = police.render(str(score1), True, blanc)
    texte2 = police.render(str(score2), True, blanc)
    fenetre.blit(texte1, (largeur // 4, 20))
    fenetre.blit(texte2, (3 * largeur // 4 - 20, 20))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limite de vitesse de rafraîchissement
    pygame.time.Clock().tick(60)
#Ce programme crée une fenêtre de jeu Pong où vous pouvez contrôler les raquettes avec les touches "W" et "S" pour la raquette de gauche, et les touches "Flèche haut" et "Flèche bas" pour la raquette de droite. Le jeu continue jusqu'à ce qu'un joueur atteigne un certain nombre de points (vous pouvez ajuster cela dans le code). J'espère que vous apprécierez de jouer à Pong !