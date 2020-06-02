import argparse
import pygame
# import tkinter as tk
# from tkinter import filedialog as fd

from chip8.chip import Chip
from chip8.pygame_gui import Screen

FONT_FILE = "FONTS.chip8"
GAME_NAME = 'My Game'

# Delay timer decrement interval (in ms)
DELAY_INTERVAL = 17

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Starts a Chip 8 emulator")
    parser.add_argument(
        "rom", help="the ROM file to load on startup")
    parser.add_argument(
        "-s", help="the scale factor to apply to the display "
        "(default is 5)", type=int, default=5, dest="scale")
    parser.add_argument(
        "-d", help="sets the CPU operation to take at least "
        "the specified number of milliseconds to execute (default is 1)",
        type=int, default=1, dest="op_delay")
    return parser.parse_args()

TIMER = pygame.USEREVENT + 1

def main_loop(args):
    game = args.rom.split('\\')
    GAME_NAME = game.pop()
    # root = tk.Tk()
    # root.withdraw()
    screen = Screen(scale_factor=args.scale, game=GAME_NAME)
    screen.init_display()
    cpu = Chip(screen)
    cpu.load_rom(FONT_FILE, 0)
    cpu.load_rom(args.rom)
    # cpu.load_rom(fd.askopenfilename())
    pygame.time.set_timer(TIMER, DELAY_INTERVAL)

    while cpu.running:
        pygame.time.wait(args.op_delay)
        cpu.execute_instruction()

        # Check for events
        for event in pygame.event.get():
            if event.type == TIMER:
                cpu.decrement_timers()
            if event.type == pygame.QUIT:
                cpu.running = False
            if event.type == pygame.KEYDOWN:
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_ESCAPE]:
                    cpu.running = False

if __name__ == "__main__":
    main_loop(parse_arguments())