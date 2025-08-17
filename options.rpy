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
    config.skip_unseen = False
    
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
    # =============================================================================
    
    # Transition settings
    config.enter_transition = None
    config.exit_transition = None
    config.intra_transition = None
    config.main_game_transition = None
    config.game_main_transition = None
    config.end_game_transition = None
    config.after_load_transition = None
    config.default_transition = dissolve
    
    # Visual effects
    config.transition_frequency = 1 if VISUAL_TRANSITIONS_ENABLED else 0
    config.transition_screens = VISUAL_TRANSITIONS_ENABLED
    config.enable_effects = VISUAL_EFFECTS_ENABLED
    config.enable_particles = VISUAL_PARTICLES_ENABLED
    config.enable_animations = VISUAL_ANIMATIONS_ENABLED
    
    # =============================================================================
    # LAYER CONFIGURATION
    # =============================================================================
    
    # Layer order
    config.layers = [
        'master',
        'transient',
        'screens',
        'overlay'
    ]
    
    # Top layers
    config.top_layers = ['overlay']
    
    # LayeredImage configuration
    config.layeredimage = "auto"
    
    # =============================================================================
    # PERFORMANCE CONFIGURATION
    # =============================================================================
    
    # Hardware acceleration
    config.hw_accelerate = True
    config.use_cpickle = True
    config.gl_texture = True
    config.gl_resize = True
    config.gl_scale = True
    
    # Cache settings
    config.image_cache_size = PERFORMANCE_CACHE_SIZE
    config.image_cache_size_garbage_collection_threshold = 1.2
    config.predictive_images = PERFORMANCE_PREDICTIVE_IMAGES
    config.texture_cache_size = 64
    config.texture_cache_size_garbage_collection_threshold = 1.2
    
    # =============================================================================
    # DEBUG CONFIGURATION
    # =============================================================================
    
    # Debug mode settings
    config.developer = DEBUG_MODE
    config.debug_image_cache = DEBUG_MODE
    config.debug_sound = DEBUG_MODE
    config.debug_texture = DEBUG_MODE
    config.debug_draw = DEBUG_MODE
    
    # Debug options
    config.debug = DEBUG_MODE
    config.debug_image_skip = True
    config.suppress_overlay = True
    config.hide_transient = True
    
    # Debug logging
    config.log = None if not DEBUG_MODE else "debug_log.txt"
    config.log_width = 200
    
    # =============================================================================
    # LOCALIZATION CONFIGURATION
    # =============================================================================
    
    # Translation settings
    config.translate_utf8 = True
    config.translate_stripping_tags = True
    
    # Language settings
    config.language = None
    config.locales = [LANG_ENGLISH, LANG_SPANISH, LANG_FRENCH, LANG_GERMAN, LANG_JAPANESE, LANG_CHINESE]
    
    # Font fallback
    config.font_fallback = True
    config.font_fallback_size = 1.0
    
    # =============================================================================
    # NARRATIVE CONFIGURATION
    # =============================================================================
    
    # NVL mode transitions
    config.nvl_adv_transition = dissolve
    config.adv_nvl_transition = dissolve
    
    # Say menu settings
    config.say_menu_text_limit = 200
    config.say_menu_include_thought = True
    
    # NVL mode settings
    config.nvl_mode = False
    config.nvl_height = None
    
    # Name box settings
    config.show_name_box = True
    config.name_box_placement = "left"
    
    # =============================================================================
    # MENU CONFIGURATION
    # =============================================================================
    
    # Menu layer settings
    config.menu_clear_layers = ["screens"]
    config.menu_include_layers = []
    
    # Menu display settings
    config.menu_include_disabled = True
    config.menu_disabled_prefix = "#"
    
    # Button settings
    config.button_disabled_prefix = "#"
    config.button_disabled_text_color = TEXT_COLOR_DISABLED
    
    # =============================================================================
    # GUI CONFIGURATION
    # =============================================================================
    
    # Screen settings
    config.screen_width = SCREEN_WIDTH
    config.screen_height = SCREEN_HEIGHT
    config.screen_background = None
    
    # Name box settings
    config.gui.show_name = True
    config.gui.show_name_box = True
    
    # Quick menu settings
    config.quick_menu = True
    config.quick_menu_text = False
    config.quick_menu_image = True
    
    # =============================================================================
    # PREFERENCES
    # =============================================================================
    
    config.preferences = {
        # Display preferences
        "display": {
            "fullscreen": [False, True],
            "transitions": [True, False],
            "text speed": 50,
        },
        
        # Sound preferences
        "sound": {
            "master volume": 0.8,
            "music volume": 0.8,
            "sound volume": 0.8,
            "voice volume": 0.8,
        },
        
        # Control preferences
        "controls": {
            "joystick": [True, False],
            "mouse sensitivity": 1.0,
            "controller": [True, False],
            "quick_menu": [True, False],
        },
        
        # Gameplay preferences
        "gameplay": {
            "difficulty": ["easy", "normal", "hard", "expert"],
            "auto-forward enabled": [True, False],
            "auto-forward time": 10,
            "skip": [True, False],
            "show empty window": [True, False],
        },
        
        # Accessibility preferences
        "accessibility": {
            "text size multiplier": 1.0,
            "high contrast mode": [True, False],
            "color blind mode": ["none", "protanopia", "deuteranopia", "tritanopia"],
            "screen reader enabled": [True, False],
            "subtitles enabled": [True, False],
            "reduced motion": [True, False],
        },
    }
    
    # =============================================================================
    # DEFAULT PREFERENCES
    # =============================================================================
    
    config.default_preferences = {
        # Display preferences
        "display": {
            "fullscreen": False,
            "transitions": True,
            "text speed": 50,
        },
        
        # Sound preferences
        "sound": {
            "master volume": 0.8,
            "music volume": 0.8,
            "sound volume": 0.8,
            "voice volume": 0.8,
        },
        
        # Control preferences
        "controls": {
            "joystick": True,
            "mouse sensitivity": 1.0,
            "controller": True,
            "quick_menu": True,
        },
        
        # Gameplay preferences
        "gameplay": {
            "difficulty": "normal",
            "auto-forward enabled": False,
            "auto-forward time": 10,
            "skip": False,
            "show empty window": True,
        },
        
        # Accessibility preferences
        "accessibility": {
            "text size multiplier": 1.0,
            "high contrast mode": False,
            "color blind mode": "none",
            "screen reader enabled": False,
            "subtitles enabled": True,
            "reduced motion": False,
        },
    }
    
    # =============================================================================
    # THEME
    # =============================================================================
    
    config.theme = {
        # Colors
        "colors": {
            "background": "#000000",
            "foreground": "#FFFFFF",
            "accent": "#FFFF00",
            "disabled": "#808080",
            "error": "#FF6666",
            "success": "#66FF66",
            "warning": "#FFFF66",
            "info": "#66FFFF",
        },
        
        # Fonts
        "fonts": {
            "default": "fonts/DejaVuSans.ttf",
            "japanese": "fonts/NotoSansCJKjp-Regular.otf",
            "chinese": "fonts/NotoSansCJKsc-Regular.otf",
        },
        
        # UI elements
        "ui": {
            "frame": "images/ui/frame.png",
            "button_normal": "images/ui/button_normal.png",
            "button_hover": "images/ui/button_hover.png",
            "button_disabled": "images/ui/button_disabled.png",
            "bar_left": "images/ui/bar_left.png",
            "bar_right": "images/ui/bar_right.png",
            "bar_thumb": "images/ui/bar_thumb.png",
            "scrollbar_base": "images/ui/scrollbar_base.png",
            "scrollbar_thumb": "images/ui/scrollbar_thumb.png",
            "slider_base": "images/ui/slider_base.png",
            "slider_thumb": "images/ui/slider_thumb.png",
        },
    }
    
    # =============================================================================
    # INITIALIZATION
    # =============================================================================
    
    try:
        # Load theme colors
        config.theme.colors["background"]
        config.theme.colors["foreground"]
        config.theme.colors["accent"]
        config.theme.colors["disabled"]
        config.theme.colors["error"]
        config.theme.colors["success"]
        config.theme.colors["warning"]
        config.theme.colors["info"]
        
        # Load theme fonts
        config.theme.fonts["default"]
        config.theme.fonts["japanese"]
        config.theme.fonts["chinese"]
        
        # Load theme UI elements
        config.theme.ui["frame"]
        config.theme.ui["button_normal"]
        config.theme.ui["button_hover"]
        config.theme.ui["button_disabled"]
        config.theme.ui["bar_left"]
        config.theme.ui["bar_right"]
        config.theme.ui["bar_thumb"]
        config.theme.ui["scrollbar_base"]
        config.theme.ui["scrollbar_thumb"]
        config.theme.ui["slider_base"]
        config.theme.ui["slider_thumb"]
        
    except Exception as e:
        print(f"Error loading theme: {e}")
    
    # =============================================================================
    # STYLES
    # =============================================================================
    
    # Default text style
    style.default.font = FONT_DEFAULT
    style.default.size = TEXT_SIZE_NORMAL
    style.default.color = TEXT_COLOR_NORMAL
    style.default.outlines = [(1, "#000000", 0, 0)]
    style.default.kerning = 0.5
    style.default.line_leading = 1.2
    
    # Button styles
    style.button.font = FONT_DEFAULT
    style.button.size = TEXT_SIZE_NORMAL
    style.button.color = TEXT_COLOR_NORMAL
    style.button.outlines = [(1, "#000000", 0, 0)]
    style.button.hover_color = TEXT_COLOR_HIGHLIGHT
    style.button.insensitive_color = TEXT_COLOR_DISABLED
    
    style.button_text.font = FONT_DEFAULT
    style.button_text.size = TEXT_SIZE_NORMAL
    style.button_text.color = TEXT_COLOR_NORMAL
    style.button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.button_text.insensitive_color = TEXT_COLOR_DISABLED
    
    # Label style
    style.label.font = FONT_DEFAULT
    style.label.size = TEXT_SIZE_NORMAL
    style.label.color = TEXT_COLOR_NORMAL
    style.label.outlines = [(1, "#000000", 0, 0)]
    
    # Input style
    style.input.font = FONT_DEFAULT
    style.input.size = TEXT_SIZE_NORMAL
    style.input.color = TEXT_COLOR_NORMAL
    style.input.outlines = [(1, "#000000", 0, 0)]
    style.input.caret_color = TEXT_COLOR_HIGHLIGHT
    style.input.selected_color = TEXT_COLOR_HIGHLIGHT
    style.input.insensitive_color = TEXT_COLOR_DISABLED
    
    # Prompt style
    style.prompt.font = FONT_DEFAULT
    style.prompt.size = TEXT_SIZE_NORMAL
    style.prompt.color = TEXT_COLOR_NORMAL
    style.prompt.outlines = [(1, "#000000", 0, 0)]
    
    # Frame style
    style.frame.background = Frame(UI_FRAME, 20, 20)
    style.frame.padding = UI_PADDING
    style.frame.margin = UI_MARGIN
    
    # Window style
    style.window.background = Frame(UI_FRAME, 20, 20)
    style.window.padding = UI_PADDING
    style.window.margin = UI_MARGIN
    
    # Box style
    style.box_spacing = UI_SPACING
    style.box_wrap = False
    
    # Grid style
    style.grid_spacing = UI_SPACING
    
    # Say window style
    style.say_window.background = Frame(UI_FRAME, 20, 20)
    style.say_window.padding = UI_PADDING
    style.say_window.margin = UI_PADDING
    style.say_window.xalign = 0.5
    style.say_window.yalign = 0.9
    style.say_window.xminimum = 800
    style.say_window.ymax = 200
    
    # Name box style
    style.namebox.background = Frame(UI_FRAME, 10, 10)
    style.namebox.padding = 5
    style.namebox.margin = 5
    style.namebox.xalign = 0.0
    style.namebox.yalign = 0.5
    
    # Menu window style
    style.menu_window.background = Frame(UI_FRAME, 20, 20)
    style.menu_window.padding = UI_PADDING
    style.menu_window.margin = UI_PADDING
    style.menu_window.xalign = 0.5
    style.menu_window.yalign = 0.5
    
    # Choice button style
    style.choice_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.choice_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.choice_button.size_group = "choice"
    style.choice_button.xalign = 0.5
    style.choice_button.xminimum = 600
    style.choice_button.ymax = 50
    
    style.choice_button_text.font = FONT_DEFAULT
    style.choice_button_text.size = TEXT_SIZE_NORMAL
    style.choice_button_text.color = TEXT_COLOR_NORMAL
    style.choice_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.choice_button_text.insensitive_color = TEXT_COLOR_DISABLED
    
    # Navigation button style
    style.navigation_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.navigation_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.navigation_button.size_group = "navigation"
    style.navigation_button.xsize = UI_BUTTON_WIDTH
    style.navigation_button.ysize = UI_BUTTON_HEIGHT
    
    style.navigation_button_text.font = FONT_DEFAULT
    style.navigation_button_text.size = TEXT_SIZE_NORMAL
    style.navigation_button_text.color = TEXT_COLOR_NORMAL
    style.navigation_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.navigation_button_text.insensitive_color = TEXT_COLOR_DISABLED
    
    # Quick button style
    style.quick_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.quick_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.quick_button.insensitive_background = Frame(UI_BUTTON_DISABLED, 10, 10)
    style.quick_button.size_group = "quick_button"
    style.quick_button.xsize = 100
    style.quick_button.ysize = 30
    style.quick_button.yoffset = 0
    
    style.quick_button_text.font = FONT_DEFAULT
    style.quick_button_text.size = TEXT_SIZE_SMALL
    style.quick_button_text.color = TEXT_COLOR_NORMAL
    style.quick_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.quick_button_text.insensitive_color = TEXT_COLOR_DISABLED
    
    # Bar style
    style.bar.xmaximum = 200
    style.bar.ymax = 20
    style.bar.left_bar = Frame("images/ui/bar_left.png", 10, 10)
    style.bar.right_bar = Frame("images/ui/bar_right.png", 10, 10)
    style.bar.thumb = Frame("images/ui/bar_thumb.png", 10, 10)
    style.bar.thumb_offset = 5
    style.bar.thumb_shadow = None
    
    # VBar style
    style.vbar.xmaximum = 20
    style.vbar.ymax = 200
    style.vbar.top_bar = Frame("images/ui/bar_top.png", 10, 10)
    style.vbar.bottom_bar = Frame("images/ui/bar_bottom.png", 10, 10)
    style.vbar.thumb = Frame("images/ui/bar_thumb.png", 10, 10)
    style.vbar.thumb_offset = 5
    style.vbar.thumb_shadow = None
    
    # Scrollbar style
    style.scrollbar.xmaximum = 20
    style.scrollbar.ymax = 200
    style.scrollbar.base_bar = Frame("images/ui/scrollbar_base.png", 10, 10)
    style.scrollbar.thumb = Frame("images/ui/scrollbar_thumb.png", 10, 10)
    style.scrollbar.thumb_offset = 5
    style.scrollbar.thumb_shadow = None
    
    # Slider style
    style.slider.xmaximum = 200
    style.slider.ymax = 30
    style.slider.base_bar = Frame("images/ui/slider_base.png", 10, 10)
    style.slider.thumb = Frame("images/ui/slider_thumb.png", 10, 10)
    style.slider.thumb_offset = 5
    style.slider.thumb_shadow = None
    
    # Tooltip style
    style.tooltip.background = Frame(UI_FRAME, 10, 10)
    style.tooltip.padding = 5
    style.tooltip.margin = 5
    style.tooltip.xalign = 0.5
    style.tooltip.yalign = 0.0
    
    style.tooltip_text.font = FONT_DEFAULT
    style.tooltip_text.size = TEXT_SIZE_SMALL
    style.tooltip_text.color = TEXT_COLOR_NORMAL
    style.tooltip_text.outlines = [(1, "#000000", 0, 0)]
    
    # Viewport style
    style.viewport.background = "#000000"
    style.viewport.xsize = 800
    style.viewport.ysize = 600
    style.viewport.clip = True
    
    # Hyperlink style
    style.hyperlink_text.font = FONT_DEFAULT
    style.hyperlink_text.size = TEXT_SIZE_NORMAL
    style.hyperlink_text.color = "#0080FF"
    style.hyperlink_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.hyperlink_text.insensitive_color = TEXT_COLOR_DISABLED
    style.hyperlink_text.underline = True
    
    
    # =============================================================================
    # PLATFORM-SPECIFIC CONFIGURATION
    # =============================================================================
    
    # Android configuration
    if config.android:
        config.orientation = "landscape"
        config.enter_transition = None
        config.exit_transition = None
        config.mouse = None
        config.touch_show_quickmenu = True
        config.touch_hide_quickmenu_time = 3.0
    
    # iOS configuration
    if config.ios:
        config.enter_transition = None
        config.exit_transition = None
        config.mouse = None
    
    # Web configuration
    if config.web:
        config.enter_transition = None
        config.exit_transition = None
        config.mouse = None
        config.touch_show_quickmenu = True
        config.touch_hide_quickmenu_time = 3.0
    
    # =============================================================================
    # OVERLAY SCREENS
    # =============================================================================
    
    # Initialize overlay screens
    config.overlay_screens = []
    
    # Add quick menu to overlay screens
    config.overlay_screens.append("quick_menu")
    
    # Add debug screens if debug mode is enabled
    if DEBUG_MODE:
        config.overlay_screens.extend(["debug_console", "debug_variables", "debug_performance"])
