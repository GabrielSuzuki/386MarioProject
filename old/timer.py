import pygame as pg


class Timer:
    def __init__(self, image_list, start_index=0, delay=100, is_loop=True):
        self.image_list = image_list
        self.start_index = start_index
        self.delay = delay
        self.is_loop = is_loop
        self.last_time_switched = pg.time.get_ticks()
        self.frames = len(image_list)
        self.index = start_index if start_index < len(image_list) - 1 else 0

    def next_frame(self):
        # if a one-pass timer that has finished
        if not self.is_loop and self.index == len(self.image_list) - 1: return
        now = pg.time.get_ticks()

        if now - self.last_time_switched > self.delay:
            self.index += 1
            if self.is_loop: self.index %= self.frames
            self.last_time_switched = now

    def is_expired(self):
        return not self.is_loop and self.index == len(self.image_list) - 1

    def reset(self):
        self.index = self.start_index

    def image(self):
        self.next_frame()
        return self.image_list[self.index]


class CommandTimer(Timer):
    def __init__(self, image_list, start_index=0, delay=100, is_loop=True):
        super().__init__(image_list, start_index, delay, is_loop)

    def next_frame(self):
        # if a one-pass timer that has finished
        if not self.is_loop and self.index == len(self.image_list) - 1: return
        now = pg.time.get_ticks()

        self.index += 1
        if self.is_loop: self.index %= self.frames
        self.last_time_switched = now

    def image(self):
        return self.image_list[self.index]


class DictionaryTimer(Timer):
    def __init__(self, image_list, start_index=0, delay=100, is_loop=True, position=0):
        super().__init__(image_list, start_index, delay, is_loop)
        self.dictionary_of_image_lists = image_list
        self.keylist = self.dictionary_of_image_lists.keys()
        # set the image list to position(automatically set to 0) in the dictionary
        self.image_list = self.dictionary_of_image_lists[(list(self.keylist)[position])]
        self.start_index = start_index
        self.delay = delay
        self.is_loop = is_loop
        self.last_time_switched = pg.time.get_ticks()
        self.frames = len(self.image_list)
        self.index = start_index if start_index < len(self.image_list) - 1 else 0

    def switch_to(self, name):
        self.image_list = self.dictionary_of_image_lists[name]
        self.frames = len(self.image_list)
        self.index = self.start_index if self.start_index < len(self.image_list) - 1 else 0

    def hasName(self, name):
        for key in self.dictionary_of_image_lists.keys():
            if key == name:
                return (True)
        return False

    def keys(self):
        list = []
        for key in self.dictionary_of_image_lists.keys():
            list.append(key)
        return (list)
