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
                "zoom": zoom  # Updated to use the defined transition
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
