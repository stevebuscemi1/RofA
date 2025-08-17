# game/options.rpy
# =============================================================================
# TRANSITIONS
# =============================================================================

# Define transitions
define fade = Fade(0.5, 0.0, 0.5)
define dissolve = Dissolve(0.5)
define pixellate = Pixellate(0.5)
define moveinright = MoveIn(0.5, "right")
define moveinleft = MoveIn(0.5, "left")
define moveintop = MoveIn(0.5, "top")
define moveinbottom = MoveIn(0.5, "bottom")
define zoomin = ZoomIn(0.5)
define zoomout = ZoomOut(0.5)
define irisout = IrisOut(0.5)
define vpunch = VPunch(0.5)
define hpunch = HPunch(0.5)
define zoom = Zoom(0.5)  # Added zoom transition

init python:
    # =============================================================================
    # BASIC CONFIGURATION
    # =============================================================================

    # Screen settings
    config.screen_width = SCREEN_WIDTH
    config.screen_height = SCREEN_HEIGHT
    config.window_title = SCREEN_TITLE

    # Text positioning
    config.default_text_xpos = 0.5
    config.default_text_ypos = 0.9
    config.default_text_xanchor = 0.5
    config.default_text_yanchor = 0.5

    # Font settings
    config.font_replacement = [
        (None, None, None, None, "fonts/DejaVuSans.ttf")
    ]

    # Text display settings
    config.default_afm_time = 0.05
    config.default_afm_enable = False
    config.text_cps = 50
    config.fast_text_cps = 150

    # Skipping settings
    config.allow_skipping = True
    config.skip_indicator = True
    config.skip_unseen = False  # Ensure this is valid in your Ren'Py version

    # =============================================================================
    # AUDIO CONFIGURATION
    # =============================================================================

    # Audio availability
    config.has_sound = True
    config.has_music = True
    config.has_voice = True

    # Default volumes
    config.master_volume = 0.8
    config.music_volume = 0.8
    config.sound_volume = 0.8
    config.voice_volume = 0.8

    # Voice settings
    config.auto_voice = False
    config.enable_voice_replay = True
    config.voice_filename_format = "voice/{filename}.ogg"

    # =============================================================================
    # SAVE/LOAD CONFIGURATION
    # =============================================================================

    # Autosave settings
    config.has_autosave = True
    config.autosave_on_quit = True
    config.autosave_slots = AUTOSAVE_SLOTS
    config.autosave_on_choice = False

    # Quicksave settings
    config.quicksave_slots = QUICKSAVE_SLOTS

    # Save file settings
    config.save_directory = SAVE_DIRECTORY
    config.save_version = 1
    config.save_filename = "save-{slot}-{timestamp}"
    config.save_game = True

    # =============================================================================
    # INPUT CONFIGURATION
    # =============================================================================

    # Mouse settings
    config.mouse = {'hide': 2000}
    config.mouse_visible = True
    config.mouse_wheel_horizontal = False

    # Touch settings
    config.touch_show_quickmenu = True
    config.touch_hide_quickmenu_time = 3.0

    # Controller settings
    config.joystick = True
    config.controller = True

    # =============================================================================
    # TRANSITION CONFIGURATION