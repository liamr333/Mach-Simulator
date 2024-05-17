import pygame
import time
import random
import sys
pygame.init()


if len(sys.argv) != 3:
        print('Please enter mach velocity and acceleration for sprite')
        exit(1)


BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen_width = 1800
screen_height = 1000
screen_center = (screen_width / 2, screen_height / 2)
sound_wave_width = 1
sprite_radius = 10
rectangle_height = 100

sound_wave_color = BLUE
sprite_color = RED


sprite_x, sprite_y = 0, screen_center[1]
mach_1_velocity = 1
sprite_velocity = float(sys.argv[1]) * mach_1_velocity
sprite_acceleration = float(sys.argv[2]) * mach_1_velocity

frames_passed = 0
# how many frames pass before a new sound wave is generated
sound_wave_frequency = 50


sound_waves = []


def add_sound_wave():
        sound_wave = {}
        # render sound wave initially at front end of sprite
        sound_wave['x'] = sprite_x + sprite_radius
        sound_wave['y'] = sprite_y
        sound_wave['radius'] = 0
        sound_wave['color'] = sound_wave_color
        sound_waves.append(sound_wave)


def update_sound_waves():
        # get rid of sound waves that are out of frame for efficiency
        for sound_wave in sound_waves:
                if sound_wave['radius'] > screen_height or sound_wave['radius'] > screen_width:
                        sound_waves.remove(sound_wave)

        for sound_wave in sound_waves:
                sound_wave['radius'] += 1 * mach_1_velocity


def render_sound_waves():
        for sound_wave in sound_waves:
                sound_wave_center = (sound_wave['x'], sound_wave['y'])
                pygame.draw.circle(screen, sound_wave['color'], sound_wave_center, sound_wave['radius'], sound_wave_width)


def update_sprite():
        global sprite_x
        global sprite_y
        global sprite_velocity

        sprite_x += sprite_velocity
        sprite_position = (sprite_x, sprite_y)

        sprite_velocity += sprite_acceleration

        pygame.draw.circle(screen, sprite_color, sprite_position, sprite_radius)


screen = pygame.display.set_mode([screen_width, screen_height])
running = True



while running:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False


        screen.fill(BLACK)

        if frames_passed % sound_wave_frequency == 0:
                add_sound_wave()

        update_sprite()
        update_sound_waves()
        render_sound_waves()

        pygame.display.flip()

        frames_passed += 1


pygame.quit()
