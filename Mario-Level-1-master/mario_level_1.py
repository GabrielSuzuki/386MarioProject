#!/usr/bin/env python
__author__ = 'justinarmstrong'

import pygame

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    pygame.init()
    main()
    pg.quit()
    sys.exit()