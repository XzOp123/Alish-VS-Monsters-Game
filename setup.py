import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Alish VS Monsters",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["3d-movie.png", '176458889_208370900743684_7423843189261827827_n.png','background_1.png', 'balloons.ttf', 'bullet.png', 'cthulhu.png', 'enemy.png', 'explosion.wav', 'laser.wav', 'left.png', 'monster.ttf', 'monster shadow.ttf', 'music.wav', 'right.png', 'mario_sound_end.mp3']}},
    executables=executables

)
