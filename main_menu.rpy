# game/main_menu.rpy

init python:
    # =============================================================================
    # MAIN MENU AND UI MANAGEMENT SYSTEM
    # =============================================================================
    
    class MainMenuManager:
        """
        Manages the main menu, navigation, and user interface elements.
        Handles menu transitions, settings, and user interactions.
        """
        
        def __init__(self):
            """Initialize the main menu manager."""
            self.current_menu = "main"
            self.menu_history = []
            self.menu_stack = []
            self.menu_animations = True
            self.menu_sounds = True
            self.menu_background = BG_BLACK
            self.menu_music = MUSIC_MAIN_THEME
            self.menu_items = self._initialize_menu_items()
            self.settings_menu = self._initialize_settings_menu()
            self.credits_data = self._initialize_credits_data()
            self.help_data = self._initialize_help_data()
            self.menu_transitions = {
                "fade": Fade(0.5, 0.0, 0.5),
                "slide": MoveTransition(0.5),
                "zoom": ZoomTransition(0.5)
            }
        
        def _initialize_menu_items(self):
            """Initialize main menu items."""
            return {
                "main": [
                    {
                        "text": "New Game",
                        "action": "start_new_game",
                        "icon": "images/ui/icons/new_game.png",
                        "tooltip": "Start a new adventure"
                    },
                    {
                        "text": "Load Game",
                        "action": "show_load_menu",
                        "icon": "images/ui/icons/load.png",
                        "tooltip": "Load a saved game"
                    },
                    {
                        "text": "Settings",
                        "action": "show_settings",
                        "icon": "images/ui/icons/settings.png",
                        "tooltip": "Configure game settings"
                    },
                    {
                        "text": "Credits",
                        "action": "show_credits",
                        "icon": "images/ui/icons/credits.png",
                        "tooltip": "View game credits"
                    },
                    {
                        "text": "Help",
                        "action": "show_help",
                        "icon": "images/ui/icons/help.png",
                        "tooltip": "Get help and instructions"
                    },
                    {
                        "text": "Quit",
                        "action": "quit_game",
                        "icon": "images/ui/icons/quit.png",
                        "tooltip": "Exit the game"
                    }
                ],
                "settings": [
                    {
                        "text": "Audio Settings",
                        "action": "show_audio_settings",
                        "icon": "images/ui/icons/audio.png",
                        "tooltip": "Configure audio options"
                    },
                    {
                        "text": "Visual Settings",
                        "action": "show_visual_settings",
                        "icon": "images/ui/icons/visual.png",
                        "tooltip": "Configure visual options"
                    },
                    {
                        "text": "Game Settings",
                        "action": "show_game_settings",
                        "icon": "images/ui/icons/game.png",
                        "tooltip": "Configure game options"
                    },
                    {
                        "text": "Controls",
                        "action": "show_controls",
                        "icon": "images/ui/icons/controls.png",
                        "tooltip": "Configure control settings"
                    },
                    {
                        "text": "Language",
                        "action": "show_language",
                        "icon": "images/ui/icons/language.png",
                        "tooltip": "Select language"
                    },
                    {
                        "text": "Back",
                        "action": "back_to_main",
                        "icon": "images/ui/icons/back.png",
                        "tooltip": "Return to main menu"
                    }
                ]
            }
        
        def _initialize_settings_menu(self):
            """Initialize settings menu structure."""
            return {
                "audio": {
                    "title": "Audio Settings",
                    "options": [
                        {
                            "name": "Master Volume",
                            "type": "slider",
                            "min": 0,
                            "max": 100,
                            "default": 80,
                            "current": 80,
                            "action": "set_master_volume"
                        },
                        {
                            "name": "Music Volume",
                            "type": "slider",
                            "min": 0,
                            "max": 100,
                            "default": 80,
                            "current": 80,
                            "action": "set_music_volume"
                        },
                        {
                            "name": "Sound Effects Volume",
                            "type": "slider",
                            "min": 0,
                            "max": 100,
                            "default": 80,
                            "current": 80,
                            "action": "set_sound_volume"
                        },
                        {
                            "name": "Voice Volume",
                            "type": "slider",
                            "min": 0,
                            "max": 100,
                            "default": 80,
                            "current": 80,
                            "action": "set_voice_volume"
                        },
                        {
                            "name": "Audio Enabled",
                            "type": "toggle",
                            "default": True,
                            "current": True,
                            "action": "toggle_audio"
                        }
                    ]
                },
                "visual": {
                    "title": "Visual Settings",
                    "options": [
                        {
                            "name": "Screen Resolution",
                            "type": "dropdown",
                            "options": ["1280x720", "1920x1080", "2560x1440"],
                            "default": "1280x720",
                            "current": "1280x720",
                            "action": "set_resolution"
                        },
                        {
                            "name": "Fullscreen",
                            "type": "toggle",
                            "default": False,
                            "current": False,
                            "action": "toggle_fullscreen"
                        },
                        {
                            "name": "Visual Effects",
                            "type": "toggle",
                            "default": True,
                            "current": True,
                            "action": "toggle_visual_effects"
                        },
                        {
                            "name": "Transitions",
                            "type": "toggle",
                            "default": True,
                            "current": True,
                            "action": "toggle_transitions"
                        },
                        {
                            "name": "Text Speed",
                            "type": "slider",
                            "min": 1,
                            "max": 10,
                            "default": 5,
                            "current": 5,
                            "action": "set_text_speed"
                        }
                    ]
                },
                "game": {
                    "title": "Game Settings",
                    "options": [
                        {
                            "name": "Auto-Save Interval",
                            "type": "dropdown",
                            "options": ["Off", "1 Minute", "5 Minutes", "10 Minutes", "30 Minutes"],
                            "default": "5 Minutes",
                            "current": "5 Minutes",
                            "action": "set_autosave_interval"
                        },
                        {
                            "name": "Difficulty",
                            "type": "dropdown",
                            "options": ["Easy", "Normal", "Hard", "Expert"],
                            "default": "Normal",
                            "current": "Normal",
                            "action": "set_difficulty"
                        },
                        {
                            "name": "Show Hints",
                            "type": "toggle",
                            "default": True,
                            "current": True,
                            "action": "toggle_hints"
                        },
                        {
                            "name": "Show Tutorial",
                            "type": "toggle",
                            "default": True,
                            "current": True,
                            "action": "toggle_tutorial"
                        },
                        {
                            "name": "Debug Mode",
                            "type": "toggle",
                            "default": DEBUG_MODE,
                            "current": DEBUG_MODE,
                            "action": "toggle_debug"
                        }
                    ]
                }
            }
        
        def _initialize_credits_data(self):
            """Initialize credits data."""
            return {
                "title": "Credits",
                "sections": [
                    {
                        "title": "Development",
                        "entries": [
                            "Game Design: Your Name",
                            "Programming: Your Name",
                            "Writing: Your Name",
                            "Art: Your Name",
                            "Music: Your Name"
                        ]
                    },
                    {
                        "title": "Special Thanks",
                        "entries": [
                            "Ren'Py Development Team",
                            "Beta Testers",
                            "Community Supporters",
                            "Friends and Family"
                        ]
                    },
                    {
                        "title": "Technologies",
                        "entries": [
                            "Ren'Py Engine",
                            "Python",
                            "PyGame",
                            "OpenAL"
                        ]
                    }
                ]
            }
        
        def _initialize_help_data(self):
            """Initialize help data."""
            return {
                "title": "Help & Instructions",
                "sections": [
                    {
                        "title": "Getting Started",
                        "content": [
                            "1. Select a character from the main menu",
                            "2. Read the story and make choices",
                            "3. Explore different paths and endings",
                            "4. Save your progress regularly"
                        ]
                    },
                    {
                        "title": "Controls",
                        "content": [
                            "Left Click: Advance text/Select option",
                            "Right Click: Open menu/Go back",
                            "Spacebar: Advance text",
                            "Escape: Open menu",
                            "F1: Take screenshot",
                            "F5: Quick save",
                            "F9: Quick load"
                        ]
                    },
                    {
                        "title": "Tips",
                        "content": [
                            "Different characters have unique stories",
                            "Your choices affect the outcome",
                            "Build relationships with other characters",
                            "Manage your inventory wisely",
                            "Explore all paths for the full experience"
                        ]
                    }
                ]
            }
        
        def show_menu(self, menu_name):
            """
            Show a specific menu.
            
            Args:
                menu_name (str): The name of the menu to show
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if menu_name not in self.menu_items:
                    return False
                
                # Add to history
                self.menu_history.append(self.current_menu)
                self.current_menu = menu_name
                
                # Play menu sound
                if self.menu_sounds:
                    audio_visual_manager.play_sound_effect(SFX_CLICK)
                
                # Apply menu transition
                if self.menu_animations:
                    audio_visual_manager.apply_transition("fade")
                
                if DEBUG_MODE:
                    print(f"Showing menu: {menu_name}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error showing menu {menu_name}: {e}")
                return False
        
        def go_back(self):
            """
            Go back to the previous menu.
            
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.menu_history:
                    return False
                
                # Get previous menu
                previous_menu = self.menu_history.pop()
                self.current_menu = previous_menu
                
                # Play menu sound
                if self.menu_sounds:
                    audio_visual_manager.play_sound_effect(SFX_CLICK)
                
                # Apply menu transition
                if self.menu_animations:
                    audio_visual_manager.apply_transition("fade")
                
                if DEBUG_MODE:
                    print(f"Going back to menu: {previous_menu}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error going back in menu: {e}")
                return False
        
        def get_current_menu_items(self):
            """
            Get items for the current menu.
            
            Returns:
                list: List of menu items
            """
            try:
                return self.menu_items.get(self.current_menu, [])
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting current menu items: {e}")
                return []
        
        def execute_menu_action(self, action):
            """
            Execute a menu action.
            
            Args:
                action (str): The action to execute
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Play menu sound
                if self.menu_sounds:
                    audio_visual_manager.play_sound_effect(SFX_CLICK)
                
                # Execute action
                if action == "start_new_game":
                    renpy.jump("start")
                elif action == "show_load_menu":
                    renpy.show_screen("load_screen")
                elif action == "show_settings":
                    self.show_menu("settings")
                elif action == "show_credits":
                    renpy.show_screen("credits_screen")
                elif action == "show_help":
                    renpy.show_screen("help_screen")
                elif action == "quit_game":
                    renpy.quit()
                elif action == "show_audio_settings":
                    renpy.show_screen("audio_visual_settings")
                elif action == "show_visual_settings":
                    renpy.show_screen("audio_visual_settings")
                elif action == "show_game_settings":
                    renpy.show_screen("game_settings_screen")
                elif action == "show_controls":
                    renpy.show_screen("controls_screen")
                elif action == "show_language":
                    renpy.show_screen("language_screen")
                elif action == "back_to_main":
                    self.current_menu = "main"
                    self.menu_history = []
                else:
                    if DEBUG_MODE:
                        print(f"Unknown menu action: {action}")
                    return False
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error executing menu action {action}: {e}")
                return False
        
        def update_setting(self, category, setting_name, value):
            """
            Update a setting value.
            
            Args:
                category (str): The setting category
                setting_name (str): The name of the setting
                value: The new value
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if category not in self.settings_menu:
                    return False
                
                category_settings = self.settings_menu[category]["options"]
                
                for setting in category_settings:
                    if setting["name"] == setting_name:
                        setting["current"] = value
                        
                        # Execute setting action
                        action = setting.get("action")
                        if action:
                            self.execute_setting_action(action, value)
                        
                        if DEBUG_MODE:
                            print(f"Updated setting {setting_name} to {value}")
                        
                        return True
                
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error updating setting {setting_name}: {e}")
                return False
        
        def execute_setting_action(self, action, value):
            """
            Execute a setting action.
            
            Args:
                action (str): The action to execute
                value: The value to apply
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if action == "set_master_volume":
                    audio_visual_manager.set_music_volume(value / 100.0)
                    audio_visual_manager.set_sound_effects_volume(value / 100.0)
                    audio_visual_manager.set_ambient_volume(value / 100.0)
                    audio_visual_manager.set_voice_volume(value / 100.0)
                elif action == "set_music_volume":
                    audio_visual_manager.set_music_volume(value / 100.0)
                elif action == "set_sound_volume":
                    audio_visual_manager.set_sound_effects_volume(value / 100.0)
                elif action == "set_voice_volume":
                    audio_visual_manager.set_voice_volume(value / 100.0)
                elif action == "toggle_audio":
                    audio_visual_manager.toggle_audio()
                elif action == "set_resolution":
                    # Resolution setting would be implemented here
                    pass
                elif action == "toggle_fullscreen":
                    # Fullscreen toggle would be implemented here
                    pass
                elif action == "toggle_visual_effects":
                    audio_visual_manager.toggle_visual_effects()
                elif action == "toggle_transitions":
                    audio_visual_manager.toggle_transitions()
                elif action == "set_text_speed":
                    # Text speed setting would be implemented here
                    pass
                elif action == "set_autosave_interval":
                    # Auto-save interval setting would be implemented here
                    pass
                elif action == "set_difficulty":
                    # Difficulty setting would be implemented here
                    pass
                elif action == "toggle_hints":
                    # Hints toggle would be implemented here
                    pass
                elif action == "toggle_tutorial":
                    # Tutorial toggle would be implemented here
                    pass
                elif action == "toggle_debug":
                    global DEBUG_MODE
                    DEBUG_MODE = value
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error executing setting action {action}: {e}")
                return False
        
        def get_setting_value(self, category, setting_name):
            """
            Get the current value of a setting.
            
            Args:
                category (str): The setting category
                setting_name (str): The name of the setting
                
            Returns:
                The current value or None if not found
            """
            try:
                if category not in self.settings_menu:
                    return None
                
                category_settings = self.settings_menu[category]["options"]
                
                for setting in category_settings:
                    if setting["name"] == setting_name:
                        return setting["current"]
                
                return None
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting setting value for {setting_name}: {e}")
                return None
        
        def initialize_main_menu(self):
            """Initialize the main menu with proper background and music."""
            try:
                # Set menu background
                renpy.scene(self.menu_background)
                
                # Play menu music
                audio_visual_manager.play_music(self.menu_music, fadein=1.0, loop=True)
                
                # Reset menu state
                self.current_menu = "main"
                self.menu_history = []
                
                if DEBUG_MODE:
                    print("Main menu initialized")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error initializing main menu: {e}")
                return False
        
        def show_tooltip(self, tooltip_text):
            """
            Show a tooltip with the given text.
            
            Args:
                tooltip_text (str): The text to show in the tooltip
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not tooltip_text:
                    return False
                
                # Show tooltip screen
                renpy.show_screen("tooltip_screen", tooltip_text)
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error showing tooltip: {e}")
                return False
        
        def hide_tooltip(self):
            """
            Hide the current tooltip.
            
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                renpy.hide_screen("tooltip_screen")
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error hiding tooltip: {e}")
                return False

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the main menu manager
    main_menu_manager = MainMenuManager()

# =============================================================================
# MAIN MENU SCREEN
# =============================================================================

screen main_menu():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Game title
            text SCREEN_TITLE size TEXT_SIZE_LARGE + 10 color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Menu items
            for item in main_menu_manager.get_current_menu_items():
                frame:
                    xsize 600
                    ysize 60
                    background Frame(UI_FRAME, 10, 10)
                    hover_background Frame(UI_BUTTON_HOVER, 10, 10)
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        yalign 0.5
                        
                        # Menu icon
                        if "icon" in item:
                            add item["icon"] size (40, 40)
                        
                        # Menu text
                        text item["text"] size TEXT_SIZE_NORMAL xalign 0.5
                        
                        # Action
                        if "action" in item:
                            textbutton "" action [
                                Function(main_menu_manager.execute_menu_action, item["action"]),
                                Function(main_menu_manager.show_tooltip, item.get("tooltip", "")),
                                Function(main_menu_manager.hide_tooltip)
                            ] xsize 600 ysize 60 background None
            
            # Version info
            text "Version 1.0" size TEXT_SIZE_SMALL color screen_manager.ui_theme["text_color"] xalign 0.5

# =============================================================================
# SETTINGS SCREENS
# =============================================================================

screen game_settings_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 700
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Game Settings" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Settings categories
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                # Audio settings
                frame:
                    xsize 250
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Audio" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for setting in main_menu_manager.settings_menu["audio"]["options"]:
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text setting["name"] size TEXT_SIZE_SMALL
                                
                                if setting["type"] == "slider":
                                    bar value setting["current"] range setting["max"] xsize 200
                                    text "{current}/{max}".format(
                                        current=setting["current"],
                                        max=setting["max"]
                                    ) size TEXT_SIZE_SMALL
                                elif setting["type"] == "toggle":
                                    textbutton (setting["current"] ? "On" : "Off") action [
                                        Function(main_menu_manager.update_setting, "audio", setting["name"], not setting["current"]),
                                        Function(renpy.play, SFX_CLICK)
                                    ] xsize 80
                
                # Visual settings
                frame:
                    xsize 250
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Visual" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for setting in main_menu_manager.settings_menu["visual"]["options"]:
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text setting["name"] size TEXT_SIZE_SMALL
                                
                                if setting["type"] == "dropdown":
                                    textbutton setting["current"] action [
                                        Function(main_menu_manager.update_setting, "visual", setting["name"], setting["current"])
                                    ] xsize 150
                                elif setting["type"] == "toggle":
                                    textbutton ("On" if setting["current"] else "Off") action [
                                        Function(main_menu_manager.update_setting, "visual", setting["name"], not setting["current"])
                                    ] xsize 80
                                elif setting["type"] == "slider":
                                    bar value setting["current"] range setting["max"] xsize 200
                                    text "{current}/{max}".format(
                                        current=setting["current"],
                                        max=setting["max"]
                                    ) size TEXT_SIZE_SMALL
                
                # Game settings
                frame:
                    xsize 250
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Game" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for setting in main_menu_manager.settings_menu["game"]["options"]:
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text setting["name"] size TEXT_SIZE_SMALL
                                
                                if setting["type"] == "dropdown":
                                    textbutton setting["current"] action [
                                        Function(main_menu_manager.update_setting, "game", setting["name"], setting["current"])
                                    ] xsize 150
                                elif setting["type"] == "toggle":
                                    textbutton ("On" if setting["current"] else "Off") action [
                                        Function(main_menu_manager.update_setting, "game", setting["name"], not setting["current"])
                                    ] xsize 80
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Apply" action [
                    Function(renpy.play, SFX_SUCCESS),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH
                textbutton "Cancel" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH

# =============================================================================
# CREDITS SCREEN
# =============================================================================

screen credits_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text main_menu_manager.credits_data["title"] size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Credits sections
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 700
                ysize 400
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for section in main_menu_manager.credits_data["sections"]:
                        frame:
                            xsize 650
                            background Frame(UI_FRAME, 10, 10)
                            
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text section["title"] size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                                
                                for entry in section["entries"]:
                                    text entry size TEXT_SIZE_SMALL
            
            # Close button
            textbutton "Close" action Hide("credits_screen") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# HELP SCREEN
# =============================================================================

screen help_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text main_menu_manager.help_data["title"] size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Help sections
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 700
                ysize 400
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for section in main_menu_manager.help_data["sections"]:
                        frame:
                            xsize 650
                            background Frame(UI_FRAME, 10, 10)
                            
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text section["title"] size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                                
                                for content in section["content"]:
                                    text content size TEXT_SIZE_SMALL
            
            # Close button
            textbutton "Close" action Hide("help_screen") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# TOOLTIP SCREEN
# =============================================================================

screen tooltip_screen(tooltip_text):
    zorder 100
    modal False
    
    frame:
        background Frame(UI_FRAME, 10, 10)
        xalign 0.5
        yalign 0.1
        
        text tooltip_text size TEXT_SIZE_SMALL

# =============================================================================
# CONTROLS SCREEN
# =============================================================================

screen controls_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Controls" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Controls list
            frame:
                xsize 700
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Keyboard Controls" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    grid 2 1:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        vbox:
                            spacing UI_SPACING
                            text "Left Click - Advance text/Select option" size TEXT_SIZE_SMALL
                            text "Right Click - Open menu/Go back" size TEXT_SIZE_SMALL
                            text "Spacebar - Advance text" size TEXT_SIZE_SMALL
                            text "Escape - Open menu" size TEXT_SIZE_SMALL
                        
                        vbox:
                            spacing UI_SPACING
                            text "F1 - Take screenshot" size TEXT_SIZE_SMALL
                            text "F5 - Quick save" size TEXT_SIZE_SMALL
                            text "F9 - Quick load" size TEXT_SIZE_SMALL
                            text "Ctrl - Skip text" size TEXT_SIZE_SMALL
                    
                    text "Mouse Controls" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    text "Left Click - Interact with objects and make choices" size TEXT_SIZE_SMALL
                    text "Right Click - Access context menu" size TEXT_SIZE_SMALL
                    text "Scroll Wheel - Navigate menus and text" size TEXT_SIZE_SMALL
            
            # Close button
            textbutton "Close" action Hide("controls_screen") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# LANGUAGE SCREEN
# =============================================================================

screen language_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 600
        ysize 400
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Language Selection" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Language options
            vbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "English" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH
                textbutton "Spanish" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH
                textbutton "French" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH
                textbutton "German" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(main_menu_manager.go_back)
                ] xsize UI_BUTTON_WIDTH
            
            # Close button
            textbutton "Close" action Hide("language_screen") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# INITIALIZATION
# =============================================================================

init python:
    # Initialize main menu when game starts
    main_menu_manager.initialize_main_menu()