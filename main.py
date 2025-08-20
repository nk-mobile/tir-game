# Ветка: cycle-code
# Реализован игровой цикл, обработка выхода и обновление экрана
# Ветка: const-code
# Добавлены константы, экран, иконка, цель и случайный цвет фона

import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра Тир")

# Фиксированный цвет фона (для демонстрации)
color = (135, 206, 235)  # Светло-голубой

# Переменная для управления циклом

# Константы размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Установка иконки окна
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Случайное начальное положение цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Пустой игровой цикл (заглушка)
running = True
while running:
    # Заливка фона
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()