import pygame as pygame

class Farben:
    SCHWARZ = 0, 0, 0
    WEISS = 255, 255, 255


def mainloop():
    pygame.init()

    # Variablen definieren
    breite, hoehe = 800, 600
    fps = 60
    
    # Definieren und Öffnen eines Fenters
    fenster = pygame.display.set_mode( (breite, hoehe) )
    pygame.display.set_caption("Titel für Fensterkopf")
    taktgeber = pygame.time.Clock()


    # Schleife für das Hauptprogramm
    spiel_aktiv = True
    while spiel_aktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                spiel_aktiv = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        fenster.fill(Farben.WEISS)
        pygame.display.flip()
        taktgeber.tick(fps)

    pygame.quit()

    return 'Fertig'

if __name__ == "__main__":
    print (mainloop())