import pygame
import threading
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienie rozmiaru okna gry
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Semaphore Example")

# Kolor tła
background_color = (255, 255, 255)

# Semafor do kontrolowania dostępu do rysowania
draw_semaphore = threading.Semaphore()


# Funkcja rysująca koła
def draw_circle():
    with draw_semaphore:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        radius = random.randint(10, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rysowanie tła
        screen.fill(background_color)

        # Rysowanie kół w dwóch wątkach
        thread1 = threading.Thread(target=draw_circle)
        thread2 = threading.Thread(target=draw_circle)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        pygame.display.flip()
        clock.tick(5)  # Ustawienie opóźnienia na 5 klatek na sekundę

    pygame.quit()


if __name__ == "__main__":
    main()
