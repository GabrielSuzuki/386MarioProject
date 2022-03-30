import tkinter as tk
import os, random

import pygame.display

from settings import Settings
import pygame as pg
class Display:
    def __init__(self, screen, stats,game):
        self.screen = screen
        self.stats = stats
        self.settings = Settings()
        self.w = self.settings.screen_width
        self.h = self.settings.screen_height

        self.root = tk.Tk()
        self.embed = tk.Frame(self.root,width=self.w,height=self.h)

        os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.root.update()

    def move(self,r_w,r_h):
        if self.stats.moveFoward == True:
            r_w += 1
            self.root.geometry("+"+str(r_w)+"+"+str(r_h))
        #pg.display.flip()

    def quit(self):
        self.root.destroy()
