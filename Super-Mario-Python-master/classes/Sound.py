from pygame import mixer


class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.soundtrack = mixer.Sound("./sfx/main_theme.wav")
        self.coin = mixer.Sound("./sfx/coin.wav")
        self.bump = mixer.Sound("./sfx/bump.wav")
        self.stomp = mixer.Sound("./sfx/stomp.wav")
        self.jump = mixer.Sound("./sfx/small_jump.wav")
        self.death = mixer.Sound("./sfx/death.wav")

    def play_sfx(self, sfx):
        if self.allowSFX:
            self.sfx_channel.play(sfx)

    def play_music(self, music):
        self.music_channel.play(music)
