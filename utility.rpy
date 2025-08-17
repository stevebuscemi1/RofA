# game/utility.rpy

init python:
    # =============================================================================
    # UTILITY SYSTEMS - LOCALIZATION, INPUT, ACCESSIBILITY
    # =============================================================================
    
    class LocalizationManager:
        """
        Manages game localization, translations, and multi-language support.
        Handles text translation, date/time formatting, and cultural adaptations.
        """
        
        def __init__(self):
            """Initialize the localization manager."""
            self.current_language = "en"
            self.fallback_language = "en"
            self.supported_languages = {
                "en": {"name": "English", "flag": "images/flags/en.png"},
                "es": {"name": "Español", "flag": "images/flags/es.png"},
                "fr": {"name": "Français", "flag": "images/flags/fr.png"},
                "de": {"name": "Deutsch", "flag": "images/flags/de.png"},
                "ja": {"name": "???", "flag": "images/flags/ja.png"},
                "zh": {"name": "??", "flag": "images/flags/zh.png"}
            }
            self.translations = self._load_translations()
            self.fonts = {
                "en": "fonts/DejaVuSans.ttf",
                "es": "fonts/DejaVuSans.ttf",
                "fr": "fonts/DejaVuSans.ttf",
                "de": "fonts/DejaVuSans.ttf",
                "ja": "fonts/NotoSansCJKjp-Regular.otf",
                "zh": "fonts/NotoSansCJKsc-Regular.otf"
            }
            self.text_direction = "ltr"  # left-to-right or right-to-left
            self.number_format = {
                "decimal": ".",
                "thousands": ","
            }
            self.date_format = "%Y-%m-%d"
            self.time_format = "%H:%M:%S"
            
        def _load_translations(self):
            """Load translation data for all supported languages."""
            translations = {}
            
            # English (base language)
            translations["en"] = {
                # UI Elements
                "ui_new_game": "New Game",
                "ui_load_game": "Load Game",
                "ui_save_game": "Save Game",
                "ui_settings": "Settings",
                "ui_quit": "Quit",
                "ui_back": "Back",
                "ui_close": "Close",
                "ui_cancel": "Cancel",
                "ui_confirm": "Confirm",
                "ui_yes": "Yes",
                "ui_no": "No",
                
                # Character Selection
                "char_select_title": "Choose Your Character",
                "char_warrior": "Warrior",
                "char_mage": "Mage",
                "char_rogue": "Rogue",
                "char_cleric": "Cleric",
                "char_ranger": "Ranger",
                
                # Stats
                "stat_strength": "Strength",
                "stat_agility": "Agility",
                "stat_intelligence": "Intelligence",
                "stat_charisma": "Charisma",
                "stat_endurance": "Endurance",
                "stat_luck": "Luck",
                
                # Items
                "item_steel_sword": "Steel Sword",
                "item_wooden_shield": "Wooden Shield",
                "item_health_potion": "Health Potion",
                "item_mana_potion": "Mana Potion",
                
                # Locations
                "loc_city": "City",
                "loc_forest": "Forest",
                "loc_temple": "Temple",
                "loc_dungeon": "Dungeon",
                "loc_castle": "Castle",
                
                # Common Phrases
                "common_level": "Level",
                "common_experience": "Experience",
                "common_health": "Health",
                "common_mana": "Mana",
                "common_gold": "Gold",
                "common_inventory": "Inventory",
                "common_abilities": "Abilities",
                "common_stats": "Stats",
                
                # Story Text
                "story_intro": "Once upon a time, in a world far away, an ancient evil awakened. Five heroes from different walks of life must rise to face the challenge.",
                
                # Error Messages
                "error_save_failed": "Failed to save game",
                "error_load_failed": "Failed to load game",
                "error_invalid_character": "Invalid character selected",
                "error_item_not_found": "Item not found",
                "error_quest_not_found": "Quest not found"
            }
            
            # Spanish translations
            translations["es"] = {
                "ui_new_game": "Nuevo Juego",
                "ui_load_game": "Cargar Juego",
                "ui_save_game": "Guardar Juego",
                "ui_settings": "Configuración",
                "ui_quit": "Salir",
                "ui_back": "Atrás",
                "ui_close": "Cerrar",
                "ui_cancel": "Cancelar",
                "ui_confirm": "Confirmar",
                "ui_yes": "Sí",
                "ui_no": "No",
                
                "char_select_title": "Elige tu Personaje",
                "char_warrior": "Guerrero",
                "char_mage": "Mago",
                "char_rogue": "Pícaro",
                "char_cleric": "Clérigo",
                "char_ranger": "Guardabosques",
                
                "stat_strength": "Fuerza",
                "stat_agility": "Agilidad",
                "stat_intelligence": "Inteligencia",
                "stat_charisma": "Carisma",
                "stat_endurance": "Resistencia",
                "stat_luck": "Suerte",
                
                "item_steel_sword": "Espada de Acero",
                "item_wooden_shield": "Escudo de Madera",
                "item_health_potion": "Poción de Salud",
                "item_mana_potion": "Poción de Maná",
                
                "loc_city": "Ciudad",
                "loc_forest": "Bosque",
                "loc_temple": "Templo",
                "loc_dungeon": "Mazmorra",
                "loc_castle": "Castillo",
                
                "common_level": "Nivel",
                "common_experience": "Experiencia",
                "common_health": "Salud",
                "common_mana": "Maná",
                "common_gold": "Oro",
                "common_inventory": "Inventario",
                "common_abilities": "Habilidades",
                "common_stats": "Estadísticas",
                
                "story_intro": "Érase una vez, en un mundo lejano, un mal ancestral despertó. Cinco héroes de diferentes caminos de la vida deben levantarse para enfrentar el desafío.",
                
                "error_save_failed": "Error al guardar el juego",
                "error_load_failed": "Error al cargar el juego",
                "error_invalid_character": "Personaje no válido seleccionado",
                "error_item_not_found": "Objeto no encontrado",
                "error_quest_not_found": "Misión no encontrada"
            }
            
            # French translations
            translations["fr"] = {
                "ui_new_game": "Nouveau Jeu",
                "ui_load_game": "Charger Partie",
                "ui_save_game": "Sauvegarder",
                "ui_settings": "Paramètres",
                "ui_quit": "Quitter",
                "ui_back": "Retour",
                "ui_close": "Fermer",
                "ui_cancel": "Annuler",
                "ui_confirm": "Confirmer",
                "ui_yes": "Oui",
                "ui_no": "Non",
                
                "char_select_title": "Choisissez votre Personnage",
                "char_warrior": "Guerrier",
                "char_mage": "Mage",
                "char_rogue": "Voleur",
                "char_cleric": "Clerc",
                "char_ranger": "Ranger",
                
                "stat_strength": "Force",
                "stat_agility": "Agilité",
                "stat_intelligence": "Intelligence",
                "stat_charisma": "Charisme",
                "stat_endurance": "Endurance",
                "stat_luck": "Chance",
                
                "item_steel_sword": "Épée en Acier",
                "item_wooden_shield": "Bouclier en Bois",
                "item_health_potion": "Potion de Santé",
                "item_mana_potion": "Potion de Mana",
                
                "loc_city": "Ville",
                "loc_forest": "Forêt",
                "loc_temple": "Temple",
                "loc_dungeon": "Donjon",
                "loc_castle": "Château",
                
                "common_level": "Niveau",
                "common_experience": "Expérience",
                "common_health": "Santé",
                "common_mana": "Mana",
                "common_gold": "Or",
                "common_inventory": "Inventaire",
                "common_abilities": "Compétences",
                "common_stats": "Statistiques",
                
                "story_intro": "Il était une fois, dans un monde lointain, un mal ancien s'est réveillé. Cinq héros de différents horizons doivent se lever pour relever le défi.",
                
                "error_save_failed": "Échec de la sauvegarde",
                "error_load_failed": "Échec du chargement",
                "error_invalid_character": "Personnage invalide sélectionné",
                "error_item_not_found": "Objet non trouvé",
                "error_quest_not_found": "Quête non trouvée"
            }
            
            # German translations
            translations["de"] = {
                "ui_new_game": "Neues Spiel",
                "ui_load_game": "Spiel Laden",
                "ui_save_game": "Spiel Speichern",
                "ui_settings": "Einstellungen",
                "ui_quit": "Beenden",
                "ui_back": "Zurück",
                "ui_close": "Schließen",
                "ui_cancel": "Abbrechen",
                "ui_confirm": "Bestätigen",
                "ui_yes": "Ja",
                "ui_no": "Nein",
                
                "char_select_title": "Wähle deinen Charakter",
                "char_warrior": "Krieger",
                "char_mage": "Magier",
                "char_rogue": "Schurke",
                "char_cleric": "Kleriker",
                "char_ranger": "Waldläufer",
                
                "stat_strength": "Stärke",
                "stat_agility": "Beweglichkeit",
                "stat_intelligence": "Intelligenz",
                "stat_charisma": "Charisma",
                "stat_endurance": "Ausdauer",
                "stat_luck": "Glück",
                
                "item_steel_sword": "Stahlschwert",
                "item_wooden_shield": "Holzschild",
                "item_health_potion": "Gesundheitstrank",
                "item_mana_potion": "Manatrank",
                
                "loc_city": "Stadt",
                "loc_forest": "Wald",
                "loc_temple": "Tempel",
                "loc_dungeon": "Verlies",
                "loc_castle": "Burg",
                
                "common_level": "Stufe",
                "common_experience": "Erfahrung",
                "common_health": "Gesundheit",
                "common_mana": "Mana",
                "common_gold": "Gold",
                "common_inventory": "Inventar",
                "common_abilities": "Fähigkeiten",
                "common_stats": "Statistiken",
                
                "story_intro": "Es war einmal in einer fernen Welt, als ein altes Böse erwachte. Fünf Helden aus verschiedenen Lebenswegen müssen sich erheben, um der Herausforderung zu begegnen.",
                
                "error_save_failed": "Speichern fehlgeschlagen",
                "error_load_failed": "Laden fehlgeschlagen",
                "error_invalid_character": "Ungültiger Charakter ausgewählt",
                "error_item_not_found": "Gegenstand nicht gefunden",
                "error_quest_not_found": "Quest nicht gefunden"
            }
            
            return translations
        
        def set_language(self, language_code):
            """
            Set the current language.
            
            Args:
                language_code (str): Language code (e.g., "en", "es", "fr")
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if language_code in self.supported_languages:
                    self.current_language = language_code
                    
                    # Update font
                    if language_code in self.fonts:
                        style.default.font = self.fonts[language_code]
                    
                    # Update text direction for RTL languages
                    if language_code in ["ar", "he"]:
                        self.text_direction = "rtl"
                    else:
                        self.text_direction = "ltr"
                    
                    # Update number format based on locale
                    if language_code == "de":
                        self.number_format = {"decimal": ",", "thousands": "."}
                    elif language_code == "fr":
                        self.number_format = {"decimal": ",", "thousands": " "}
                    else:
                        self.number_format = {"decimal": ".", "thousands": ","}
                    
                    # Save language preference
                    persistent.game_state["preferred_language"] = language_code
                    
                    if DEBUG_MODE:
                        print(f"Language set to: {language_code}")
                    
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting language to {language_code}: {e}")
                return False
        
        def get_text(self, key, **kwargs):
            """
            Get translated text for a key.
            
            Args:
                key (str): Translation key
                **kwargs: Format arguments
                
            Returns:
                str: Translated text or key if not found
            """
            try:
                # Try current language first
                if self.current_language in self.translations:
                    text = self.translations[self.current_language].get(key)
                    if text:
                        return text.format(**kwargs) if kwargs else text
                
                # Try fallback language
                if self.fallback_language in self.translations:
                    text = self.translations[self.fallback_language].get(key)
                    if text:
                        return text.format(**kwargs) if kwargs else text
                
                # Return key if no translation found
                return key
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting translation for {key}: {e}")
                return key
        
        def format_number(self, number):
            """
            Format a number according to current locale.
            
            Args:
                number (int/float): Number to format
                
            Returns:
                str: Formatted number string
            """
            try:
                if isinstance(number, int):
                    return "{:,}".format(number).replace(",", self.number_format["thousands"])
                else:
                    return "{:,.2f}".format(number).replace(",", self.number_format["thousands"]).replace(".", self.number_format["decimal"])
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error formatting number {number}: {e}")
                return str(number)
        
        def format_date(self, timestamp):
            """
            Format a date according to current locale.
            
            Args:
                timestamp (int/float): Unix timestamp
                
            Returns:
                str: Formatted date string
            """
            try:
                date_obj = datetime.datetime.fromtimestamp(timestamp)
                return date_obj.strftime(self.date_format)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error formatting date {timestamp}: {e}")
                return str(timestamp)
        
        def format_time(self, timestamp):
            """
            Format a time according to current locale.
            
            Args:
                timestamp (int/float): Unix timestamp
                
            Returns:
                str: Formatted time string
            """
            try:
                time_obj = datetime.datetime.fromtimestamp(timestamp)
                return time_obj.strftime(self.time_format)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error formatting time {timestamp}: {e}")
                return str(timestamp)
        
        def get_supported_languages(self):
            """
            Get list of supported languages.
            
            Returns:
                dict: Supported languages with metadata
            """
            return self.supported_languages
        
        def get_current_language(self):
            """
            Get current language code.
            
            Returns:
                str: Current language code
            """
            return self.current_language
        
        def add_translation(self, language_code, key, text):
            """
            Add or update a translation.
            
            Args:
                language_code (str): Language code
                key (str): Translation key
                text (str): Translated text
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if language_code not in self.translations:
                    self.translations[language_code] = {}
                
                self.translations[language_code][key] = text
                
                if DEBUG_MODE:
                    print(f"Added translation: {language_code}.{key} = {text}")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error adding translation {language_code}.{key}: {e}")
                return False

    class InputManager:
        """
        Manages input handling, keyboard shortcuts, and control customization.
        Provides accessible input options and customizable controls.
        """
        
        def __init__(self):
            """Initialize the input manager."""
            self.key_bindings = self._initialize_key_bindings()
            self.mouse_bindings = self._initialize_mouse_bindings()
            self.controller_bindings = self._initialize_controller_bindings()
            self.input_history = []
            self.repeat_delay = 0.5  # Delay before key repeat starts
            self.repeat_interval = 0.05  # Interval between key repeats
            self.last_key_time = {}
            self.key_states = {}
            self.accessibility_mode = False
            self.simplified_controls = False
            self.auto_advance = False
            self.auto_advance_delay = 3.0  # Seconds before auto-advance
            
        def _initialize_key_bindings(self):
            """Initialize default keyboard bindings."""
            return {
                "advance": ["space", "return", "KP_Enter"],
                "back": ["escape", "backspace"],
                "menu": ["escape", "rightshift"],
                "save": ["f5", "KP_Add"],
                "load": ["f9", "KP_Subtract"],
                "screenshot": ["f1"],
                "debug_console": ["f2"],
                "quick_save": ["f6"],
                "quick_load": ["f7"],
                "skip": ["ctrl", "KP_Multiply"],
                "auto_mode": ["a"],
                "hide_ui": ["h"],
                "log": ["l"],
                "inventory": ["i"],
                "character_info": ["c"],
                "map": ["m"],
                "journal": ["j"],
                "up": ["up", "w", "KP_Up"],
                "down": ["down", "s", "KP_Down"],
                "left": ["left", "a", "KP_Left"],
                "right": ["right", "d", "KP_Right"],
                "page_up": ["pageup", "KP_Page_Up"],
                "page_down": ["pagedown", "KP_Page_Down"],
                "home": ["home", "KP_Home"],
                "end": ["end", "KP_End"]
            }
        
        def _initialize_mouse_bindings(self):
            """Initialize default mouse bindings."""
            return {
                "advance": ["mouse_left"],
                "back": ["mouse_right"],
                "hover": ["mouse_motion"],
                "scroll_up": ["mouse_wheel_up"],
                "scroll_down": ["mouse_wheel_down"]
            }
        
        def _initialize_controller_bindings(self):
            """Initialize default controller bindings."""
            return {
                "advance": ["button_a", "button_start"],
                "back": ["button_b", "button_back"],
                "menu": ["button_y", "button_select"],
                "up": ["dpad_up", "left_stick_up"],
                "down": ["dpad_down", "left_stick_down"],
                "left": ["dpad_left", "left_stick_left"],
                "right": ["dpad_right", "left_stick_right"],
                "page_up": ["left_shoulder"],
                "page_down": ["right_shoulder"]
            }
        
        def handle_key_down(self, key):
            """
            Handle key down events.
            
            Args:
                key (str): The key that was pressed
                
            Returns:
                str: Action triggered by the key, or None
            """
            try:
                current_time = time.time()
                
                # Check for key repeat
                if key in self.last_key_time:
                    time_since_last = current_time - self.last_key_time[key]
                    if time_since_last < self.repeat_delay:
                        return None
                    if time_since_last < self.repeat_interval:
                        return None
                
                self.last_key_time[key] = current_time
                self.key_states[key] = True
                
                # Find action for key
                action = self._get_action_for_key(key)
                if action:
                    self.input_history.append({
                        "type": "key_down",
                        "key": key,
                        "action": action,
                        "timestamp": current_time
                    })
                    
                    if DEBUG_MODE:
                        print(f"Key pressed: {key} -> {action}")
                    
                    return action
                
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error handling key down {key}: {e}")
                return None
        
        def handle_key_up(self, key):
            """
            Handle key up events.
            
            Args:
                key (str): The key that was released
            """
            try:
                self.key_states[key] = False
                del self.last_key_time[key]
                
                self.input_history.append({
                    "type": "key_up",
                    "key": key,
                    "timestamp": time.time()
                })
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error handling key up {key}: {e}")
        
        def handle_mouse_down(self, button, x, y):
            """
            Handle mouse down events.
            
            Args:
                button (str): Mouse button
                x (int): Mouse X position
                y (int): Mouse Y position
                
            Returns:
                str: Action triggered by the mouse button, or None
            """
            try:
                action = self._get_action_for_mouse_button(button)
                if action:
                    self.input_history.append({
                        "type": "mouse_down",
                        "button": button,
                        "x": x,
                        "y": y,
                        "action": action,
                        "timestamp": time.time()
                    })
                    
                    if DEBUG_MODE:
                        print(f"Mouse pressed: {button} at ({x}, {y}) -> {action}")
                    
                    return action
                
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error handling mouse down {button}: {e}")
                return None
        
        def handle_mouse_motion(self, x, y, dx, dy):
            """
            Handle mouse motion events.
            
            Args:
                x (int): Mouse X position
                y (int): Mouse Y position
                dx (int): Mouse X delta
                dy (int): Mouse Y delta
            """
            try:
                self.input_history.append({
                    "type": "mouse_motion",
                    "x": x,
                    "y": y,
                    "dx": dx,
                    "dy": dy,
                    "timestamp": time.time()
                })
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error handling mouse motion: {e}")
        
        def handle_mouse_wheel(self, direction):
            """
            Handle mouse wheel events.
            
            Args:
                direction (int): Wheel direction (1 for up, -1 for down)
                
            Returns:
                str: Action triggered by the mouse wheel, or None
            """
            try:
                action = "scroll_up" if direction > 0 else "scroll_down"
                
                self.input_history.append({
                    "type": "mouse_wheel",
                    "direction": direction,
                    "action": action,
                    "timestamp": time.time()
                })
                
                if DEBUG_MODE:
                    print(f"Mouse wheel: {direction} -> {action}")
                
                return action
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error handling mouse wheel: {e}")
                return None
        
        def _get_action_for_key(self, key):
            """
            Get the action associated with a key.
            
            Args:
                key (str): The key to check
                
            Returns:
                str: Action name or None
            """
            for action, keys in self.key_bindings.items():
                if key in keys:
                    return action
            return None
        
        def _get_action_for_mouse_button(self, button):
            """
            Get the action associated with a mouse button.
            
            Args:
                button (str): The mouse button to check
                
            Returns:
                str: Action name or None
            """
            for action, buttons in self.mouse_bindings.items():
                if button in buttons:
                    return action
            return None
        
        def bind_key(self, action, key):
            """
            Bind a key to an action.
            
            Args:
                action (str): Action name
                key (str): Key to bind
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if action not in self.key_bindings:
                    return False
                
                # Remove key from any existing bindings
                for existing_action, keys in self.key_bindings.items():
                    if key in keys:
                        keys.remove(key)
                
                # Add new binding
                self.key_bindings[action].append(key)
                
                # Save key bindings
                persistent.game_state["key_bindings"] = self.key_bindings
                
                if DEBUG_MODE:
                    print(f"Bound key {key} to action {action}")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error binding key {key} to action {action}: {e}")
                return False
        
        def unbind_key(self, key):
            """
            Unbind a key from any action.
            
            Args:
                key (str): Key to unbind
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                for action, keys in self.key_bindings.items():
                    if key in keys:
                        keys.remove(key)
                
                # Save key bindings
                persistent.game_state["key_bindings"] = self.key_bindings
                
                if DEBUG_MODE:
                    print(f"Unbound key {key}")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error unbinding key {key}: {e}")
                return False
        
        def get_key_bindings(self):
            """
            Get current key bindings.
            
            Returns:
                dict: Current key bindings
            """
            return self.key_bindings
        
        def reset_key_bindings(self):
            """
            Reset key bindings to defaults.
            
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                self.key_bindings = self._initialize_key_bindings()
                
                # Save key bindings
                persistent.game_state["key_bindings"] = self.key_bindings
                
                if DEBUG_MODE:
                    print("Key bindings reset to defaults")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error resetting key bindings: {e}")
                return False
        
        def is_key_pressed(self, key):
            """
            Check if a key is currently pressed.
            
            Args:
                key (str): Key to check
                
            Returns:
                bool: True if key is pressed, False otherwise
            """
            return self.key_states.get(key, False)
        
        def get_input_history(self, limit=100):
            """
            Get recent input history.
            
            Args:
                limit (int): Maximum number of entries to return
                
            Returns:
                list: Input history entries
            """
            return self.input_history[-limit:]
        
        def clear_input_history(self):
            """Clear input history."""
            self.input_history = []
        
        def enable_accessibility_mode(self):
            """Enable accessibility mode with simplified controls."""
            try:
                self.accessibility_mode = True
                self.simplified_controls = True
                self.auto_advance = True
                
                # Simplified key bindings
                self.key_bindings = {
                    "advance": ["space", "return", "mouse_left"],
                    "back": ["escape", "mouse_right"],
                    "menu": ["m"],
                    "save": ["s"],
                    "load": ["l"]
                }
                
                if DEBUG_MODE:
                    print("Accessibility mode enabled")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error enabling accessibility mode: {e}")
                return False
        
        def disable_accessibility_mode(self):
            """Disable accessibility mode."""
            try:
                self.accessibility_mode = False
                self.simplified_controls = False
                self.auto_advance = False
                
                # Restore default key bindings
                self.key_bindings = self._initialize_key_bindings()
                
                if DEBUG_MODE:
                    print("Accessibility mode disabled")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error disabling accessibility mode: {e}")
                return False

    class AccessibilityManager:
        """
        Manages accessibility features including text size, contrast,
        screen reader support, and other accessibility options.
        """
        
        def __init__(self):
            """Initialize the accessibility manager."""
            self.text_size_multiplier = 1.0
            self.high_contrast_mode = False
            self.color_blind_mode = False
            self.screen_reader_enabled = False
            self.subtitles_enabled = True
            self.subtitle_size = "normal"
            self.captions_enabled = True
            self.visual_cues_enabled = True
            self.audio_cues_enabled = True
            self.simplified_ui = False
            self.reduced_motion = False
            self.focus_indicators_enabled = True
            self.keyboard_navigation_enabled = True
            self.announcements = []
            
        def set_text_size(self, size_multiplier):
            """
            Set text size multiplier.
            
            Args:
                size_multiplier (float): Text size multiplier (0.5 to 2.0)
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                size_multiplier = max(0.5, min(2.0, size_multiplier))
                self.text_size_multiplier = size_multiplier
                
                # Update text styles
                style.default.size = int(TEXT_SIZE_NORMAL * size_multiplier)
                style.large.size = int(TEXT_SIZE_LARGE * size_multiplier)
                style.small.size = int(TEXT_SIZE_SMALL * size_multiplier)
                
                # Save preference
                persistent.game_state["accessibility_text_size"] = size_multiplier
                
                if DEBUG_MODE:
                    print(f"Text size set to {size_multiplier}x")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting text size: {e}")
                return False
        
        def toggle_high_contrast(self):
            """
            Toggle high contrast mode.
            
            Returns:
                bool: New high contrast state
            """
            try:
                self.high_contrast_mode = not self.high_contrast_mode
                
                if self.high_contrast_mode:
                    # Set high contrast colors
                    style.default.color = "#FFFFFF"
                    style.window.background = "#000000"
                    style.frame.background = "#000000"
                    style.button.background = "#FFFFFF"
                    style.button.text_color = "#000000"
                else:
                    # Restore normal colors
                    style.default.color = TEXT_COLOR_NORMAL
                    style.window.background = None
                    style.frame.background = None
                    style.button.background = None
                    style.button.text_color = TEXT_COLOR_NORMAL
                
                # Save preference
                persistent.game_state["accessibility_high_contrast"] = self.high_contrast_mode
                
                if DEBUG_MODE:
                    print(f"High contrast mode: {'enabled' if self.high_contrast_mode else 'disabled'}")
                
                return self.high_contrast_mode
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling high contrast: {e}")
                return not self.high_contrast_mode
        
        def set_color_blind_mode(self, mode):
            """
            Set color blind mode.
            
            Args:
                mode (str): Color blind mode ("none", "protanopia", "deuteranopia", "tritanopia")
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                valid_modes = ["none", "protanopia", "deuteranopia", "tritanopia"]
                if mode not in valid_modes:
                    return False
                
                self.color_blind_mode = mode
                
                # Apply color blind filters (this would require additional implementation)
                # For now, we just store the setting
                
                # Save preference
                persistent.game_state["accessibility_color_blind"] = mode
                
                if DEBUG_MODE:
                    print(f"Color blind mode set to: {mode}")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting color blind mode: {e}")
                return False
        
        def toggle_screen_reader(self):
            """
            Toggle screen reader support.
            
            Returns:
                bool: New screen reader state
            """
            try:
                self.screen_reader_enabled = not self.screen_reader_enabled
                
                # Enable/disable screen reader announcements
                if self.screen_reader_enabled:
                    self.announce("Screen reader enabled")
                else:
                    self.announce("Screen reader disabled")
                
                # Save preference
                persistent.game_state["accessibility_screen_reader"] = self.screen_reader_enabled
                
                if DEBUG_MODE:
                    print(f"Screen reader: {'enabled' if self.screen_reader_enabled else 'disabled'}")
                
                return self.screen_reader_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling screen reader: {e}")
                return not self.screen_reader_enabled
        
        def announce(self, text, priority="normal"):
            """
            Announce text for screen readers.
            
            Args:
                text (str): Text to announce
                priority (str): Announcement priority ("low", "normal", "high")
            """
            try:
                if not self.screen_reader_enabled:
                    return
                
                announcement = {
                    "text": text,
                    "priority": priority,
                    "timestamp": time.time()
                }
                
                self.announcements.append(announcement)
                
                # In a real implementation, this would interface with screen reader APIs
                # For now, we just log it
                if DEBUG_MODE:
                    print(f"Screen reader announcement: {text}")
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error making announcement: {e}")
        
        def toggle_subtitles(self):
            """
            Toggle subtitles.
            
            Returns:
                bool: New subtitles state
            """
            try:
                self.subtitles_enabled = not self.subtitles_enabled
                
                # Save preference
                persistent.game_state["accessibility_subtitles"] = self.subtitles_enabled
                
                if DEBUG_MODE:
                    print(f"Subtitles: {'enabled' if self.subtitles_enabled else 'disabled'}")
                
                return self.subtitles_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling subtitles: {e}")
                return not self.subtitles_enabled
        
        def set_subtitle_size(self, size):
            """
            Set subtitle size.
            
            Args:
                size (str): Subtitle size ("small", "normal", "large")
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                valid_sizes = ["small", "normal", "large"]
                if size not in valid_sizes:
                    return False
                
                self.subtitle_size = size
                
                # Save preference
                persistent.game_state["accessibility_subtitle_size"] = size
                
                if DEBUG_MODE:
                    print(f"Subtitle size set to: {size}")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting subtitle size: {e}")
                return False
        
        def toggle_captions(self):
            """
            Toggle captions.
            
            Returns:
                bool: New captions state
            """
            try:
                self.captions_enabled = not self.captions_enabled
                
                # Save preference
                persistent.game_state["accessibility_captions"] = self.captions_enabled
                
                if DEBUG_MODE:
                    print(f"Captions: {'enabled' if self.captions_enabled else 'disabled'}")
                
                return self.captions_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling captions: {e}")
                return not self.captions_enabled
        
        def toggle_visual_cues(self):
            """
            Toggle visual cues.
            
            Returns:
                bool: New visual cues state
            """
            try:
                self.visual_cues_enabled = not self.visual_cues_enabled
                
                # Save preference
                persistent.game_state["accessibility_visual_cues"] = self.visual_cues_enabled
                
                if DEBUG_MODE:
                    print(f"Visual cues: {'enabled' if self.visual_cues_enabled else 'disabled'}")
                
                return self.visual_cues_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling visual cues: {e}")
                return not self.visual_cues_enabled
        
        def toggle_audio_cues(self):
            """
            Toggle audio cues.
            
            Returns:
                bool: New audio cues state
            """
            try:
                self.audio_cues_enabled = not self.audio_cues_enabled
                
                # Save preference
                persistent.game_state["accessibility_audio_cues"] = self.audio_cues_enabled
                
                if DEBUG_MODE:
                    print(f"Audio cues: {'enabled' if self.audio_cues_enabled else 'disabled'}")
                
                return self.audio_cues_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling audio cues: {e}")
                return not self.audio_cues_enabled
        
        def toggle_simplified_ui(self):
            """
            Toggle simplified UI mode.
            
            Returns:
                bool: New simplified UI state
            """
            try:
                self.simplified_ui = not self.simplified_ui
                
                # Save preference
                persistent.game_state["accessibility_simplified_ui"] = self.simplified_ui
                
                if DEBUG_MODE:
                    print(f"Simplified UI: {'enabled' if self.simplified_ui else 'disabled'}")
                
                return self.simplified_ui
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling simplified UI: {e}")
                return not self.simplified_ui
        
        def toggle_reduced_motion(self):
            """
            Toggle reduced motion mode.
            
            Returns:
                bool: New reduced motion state
            """
            try:
                self.reduced_motion = not self.reduced_motion
                
                # Apply reduced motion settings
                if self.reduced_motion:
                    # Disable or reduce animations
                    config.transition_frequency = 0
                    config.transition_screens = False
                else:
                    # Restore normal animations
                    config.transition_frequency = 1
                    config.transition_screens = True
                
                # Save preference
                persistent.game_state["accessibility_reduced_motion"] = self.reduced_motion
                
                if DEBUG_MODE:
                    print(f"Reduced motion: {'enabled' if self.reduced_motion else 'disabled'}")
                
                return self.reduced_motion
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling reduced motion: {e}")
                return not self.reduced_motion
        
        def toggle_focus_indicators(self):
            """
            Toggle focus indicators.
            
            Returns:
                bool: New focus indicators state
            """
            try:
                self.focus_indicators_enabled = not self.focus_indicators_enabled
                
                # Save preference
                persistent.game_state["accessibility_focus_indicators"] = self.focus_indicators_enabled
                
                if DEBUG_MODE:
                    print(f"Focus indicators: {'enabled' if self.focus_indicators_enabled else 'disabled'}")
                
                return self.focus_indicators_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling focus indicators: {e}")
                return not self.focus_indicators_enabled
        
        def toggle_keyboard_navigation(self):
            """
            Toggle keyboard navigation.
            
            Returns:
                bool: New keyboard navigation state
            """
            try:
                self.keyboard_navigation_enabled = not self.keyboard_navigation_enabled
                
                # Save preference
                persistent.game_state["accessibility_keyboard_navigation"] = self.keyboard_navigation_enabled
                
                if DEBUG_MODE:
                    print(f"Keyboard navigation: {'enabled' if self.keyboard_navigation_enabled else 'disabled'}")
                
                return self.keyboard_navigation_enabled
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling keyboard navigation: {e}")
                return not self.keyboard_navigation_enabled
        
        def get_accessibility_settings(self):
            """
            Get current accessibility settings.
            
            Returns:
                dict: Current accessibility settings
            """
            return {
                "text_size_multiplier": self.text_size_multiplier,
                "high_contrast_mode": self.high_contrast_mode,
                "color_blind_mode": self.color_blind_mode,
                "screen_reader_enabled": self.screen_reader_enabled,
                "subtitles_enabled": self.subtitles_enabled,
                "subtitle_size": self.subtitle_size,
                "captions_enabled": self.captions_enabled,
                "visual_cues_enabled": self.visual_cues_enabled,
                "audio_cues_enabled": self.audio_cues_enabled,
                "simplified_ui": self.simplified_ui,
                "reduced_motion": self.reduced_motion,
                "focus_indicators_enabled": self.focus_indicators_enabled,
                "keyboard_navigation_enabled": self.keyboard_navigation_enabled
            }
        
        def load_accessibility_settings(self):
            """Load accessibility settings from persistent data."""
            try:
                if "accessibility_text_size" in persistent.game_state:
                    self.set_text_size(persistent.game_state["accessibility_text_size"])
                
                if "accessibility_high_contrast" in persistent.game_state:
                    if persistent.game_state["accessibility_high_contrast"] != self.high_contrast_mode:
                        self.toggle_high_contrast()
                
                if "accessibility_color_blind" in persistent.game_state:
                    self.set_color_blind_mode(persistent.game_state["accessibility_color_blind"])
                
                if "accessibility_screen_reader" in persistent.game_state:
                    if persistent.game_state["accessibility_screen_reader"] != self.screen_reader_enabled:
                        self.toggle_screen_reader()
                
                if "accessibility_subtitles" in persistent.game_state:
                    if persistent.game_state["accessibility_subtitles"] != self.subtitles_enabled:
                        self.toggle_subtitles()
                
                if "accessibility_subtitle_size" in persistent.game_state:
                    self.set_subtitle_size(persistent.game_state["accessibility_subtitle_size"])
                
                if "accessibility_captions" in persistent.game_state:
                    if persistent.game_state["accessibility_captions"] != self.captions_enabled:
                        self.toggle_captions()
                
                if "accessibility_visual_cues" in persistent.game_state:
                    if persistent.game_state["accessibility_visual_cues"] != self.visual_cues_enabled:
                        self.toggle_visual_cues()
                
                if "accessibility_audio_cues" in persistent.game_state:
                    if persistent.game_state["accessibility_audio_cues"] != self.audio_cues_enabled:
                        self.toggle_audio_cues()
                
                if "accessibility_simplified_ui" in persistent.game_state:
                    if persistent.game_state["accessibility_simplified_ui"] != self.simplified_ui:
                        self.toggle_simplified_ui()
                
                if "accessibility_reduced_motion" in persistent.game_state:
                    if persistent.game_state["accessibility_reduced_motion"] != self.reduced_motion:
                        self.toggle_reduced_motion()
                
                if "accessibility_focus_indicators" in persistent.game_state:
                    if persistent.game_state["accessibility_focus_indicators"] != self.focus_indicators_enabled:
                        self.toggle_focus_indicators()
                
                if "accessibility_keyboard_navigation" in persistent.game_state:
                    if persistent.game_state["accessibility_keyboard_navigation"] != self.keyboard_navigation_enabled:
                        self.toggle_keyboard_navigation()
                
                if DEBUG_MODE:
                    print("Accessibility settings loaded")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error loading accessibility settings: {e}")

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instances of utility managers
    localization_manager = LocalizationManager()
    input_manager = InputManager()
    accessibility_manager = AccessibilityManager()

# =============================================================================
    # ACCESSIBILITY SETTINGS SCREEN
    # =============================================================================

screen accessibility_settings():
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
            text "Accessibility Settings" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Text settings
            frame:
                xsize 800
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Text Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Text Size:" size TEXT_SIZE_SMALL
                        bar value accessibility_manager.text_size_multiplier range 2.0 xsize 200
                        text "{:.1f}x".format(accessibility_manager.text_size_multiplier) size TEXT_SIZE_SMALL
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "High Contrast:" size TEXT_SIZE_SMALL
                        textbutton (accessibility_manager.high_contrast_mode ? "On" : "Off") action [
                             Function(accessibility_manager.toggle_high_contrast),
                             Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Color Blind Mode:" size TEXT_SIZE_SMALL
                        textbutton accessibility_manager.color_blind_mode.capitalize() action [
                            Function(accessibility_manager.set_color_blind_mode, 
                                "protanopia" if accessibility_manager.color_blind_mode == "none" else "none"),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 120
            
            # Audio settings
            frame:
                xsize 800
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Audio Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Screen Reader:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.screen_reader_enabled else "Off") action [
                            Function(accessibility_manager.toggle_screen_reader),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Audio Cues:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.audio_cues_enabled else "Off") action [
                            Function(accessibility_manager.toggle_audio_cues),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
            
            # Visual settings
            frame:
                xsize 800
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Visual Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Subtitles:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.subtitles_enabled else "Off") action [
                            Function(accessibility_manager.toggle_subtitles),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Caption Size:" size TEXT_SIZE_SMALL
                        textbutton accessibility_manager.subtitle_size.capitalize() action [
                            Function(accessibility_manager.set_subtitle_size, 
                                "large" if accessibility_manager.subtitle_size == "normal" else 
                                "small" if accessibility_manager.subtitle_size == "large" else "normal"),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 120
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Visual Cues:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.visual_cues_enabled else "Off") action [
                            Function(accessibility_manager.toggle_visual_cues),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Reduced Motion:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.reduced_motion else "Off") action [
                            Function(accessibility_manager.toggle_reduced_motion),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
            
            # Navigation settings
            frame:
                xsize 800
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Navigation Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Simplified UI:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.simplified_ui else "Off") action [
                            Function(accessibility_manager.toggle_simplified_ui),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Focus Indicators:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.focus_indicators_enabled else "Off") action [
                            Function(accessibility_manager.toggle_focus_indicators),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Keyboard Navigation:" size TEXT_SIZE_SMALL
                        textbutton ("On" if accessibility_manager.keyboard_navigation_enabled else "Off") action [
                            Function(accessibility_manager.toggle_keyboard_navigation),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Apply" action [
                    Function(renpy.play, SFX_SUCCESS),
                    Hide("accessibility_settings")
                ] xsize UI_BUTTON_WIDTH
                textbutton "Reset to Defaults" action [
                    Function(accessibility_manager.set_text_size, 1.0),
                    Function(accessibility_manager.set_color_blind_mode, "none"),
                    Function(accessibility_manager.toggle_high_contrast) if accessibility_manager.high_contrast_mode else None,
                    Function(accessibility_manager.toggle_screen_reader) if accessibility_manager.screen_reader_enabled else None,
                    Function(accessibility_manager.toggle_subtitles) if not accessibility_manager.subtitles_enabled else None,
                    Function(accessibility_manager.set_subtitle_size, "normal"),
                    Function(accessibility_manager.toggle_captions) if not accessibility_manager.captions_enabled else None,
                    Function(accessibility_manager.toggle_visual_cues) if not accessibility_manager.visual_cues_enabled else None,
                    Function(accessibility_manager.toggle_audio_cues) if not accessibility_manager.audio_cues_enabled else None,
                    Function(accessibility_manager.toggle_simplified_ui) if accessibility_manager.simplified_ui else None,
                    Function(accessibility_manager.toggle_reduced_motion) if accessibility_manager.reduced_motion else None,
                    Function(accessibility_manager.toggle_focus_indicators) if not accessibility_manager.focus_indicators_enabled else None,
                    Function(accessibility_manager.toggle_keyboard_navigation) if not accessibility_manager.keyboard_navigation_enabled else None,
                    Function(renpy.play, SFX_CLICK)
                ] xsize UI_BUTTON_WIDTH
                textbutton "Cancel" action [
                    Function(renpy.play, SFX_CLICK),
                    Hide("accessibility_settings")
                ] xsize UI_BUTTON_WIDTH

# =============================================================================
    # KEY BINDINGS SCREEN
    # =============================================================================

screen key_bindings():
    tag menu
    use game_screen()
    
    default selected_action = None
    default waiting_for_key = False
    
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
            text "Key Bindings" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            if waiting_for_key:
                text "Press a key to bind to [selected_action]..." size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"] xalign 0.5
            else:
                text "Click on an action to change its key binding" size TEXT_SIZE_SMALL xalign 0.5
            
            # Key bindings list
            frame:
                xsize 750
                ysize 400
                background Frame(UI_FRAME, 10, 10)
                
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 730
                    ysize 380
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        for action, keys in input_manager.get_key_bindings().items():
                            frame:
                                xsize 700
                                background Frame(UI_FRAME, 5, 5)
                                hover_background Frame(UI_BUTTON_HOVER, 5, 5)
                                
                                hbox:
                                    spacing UI_SPACING
                                    xalign 0.5
                                    yalign 0.5
                                    
                                    text action.replace("_", " ").title() size TEXT_SIZE_SMALL xsize 200
                                    text ", ".join(keys) size TEXT_SIZE_SMALL xsize 200
                                    
                                    if not waiting_for_key:
                                        textbutton "Change" action [
                                            Function(setattr, selected_action, action),
                                            Function(setattr, waiting_for_key, True),
                                            Function(renpy.play, SFX_CLICK)
                                        ] xsize 80
                                        textbutton "Clear" action [
                                            Function(input_manager.unbind_key, keys[0]) if keys else None,
                                            Function(renpy.play, SFX_CLICK)
                                        ] xsize 80
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Reset to Defaults" action [
                    Function(input_manager.reset_key_bindings),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 150
                textbutton "Accessibility Mode" action [
                    Function(input_manager.enable_accessibility_mode),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 150
                textbutton "Close" action [
                    Function(renpy.play, SFX_CLICK),
                    Hide("key_bindings")
                ] xsize 100

# =============================================================================
    # LANGUAGE SELECTION SCREEN
    # =============================================================================

screen language_selection():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 600
        ysize 500
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Language Selection" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Language options
            frame:
                xsize 550
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for lang_code, lang_info in localization_manager.get_supported_languages().items():
                        frame:
                            xsize 500
                            background Frame(UI_FRAME, 5, 5)
                            hover_background Frame(UI_BUTTON_HOVER, 5, 5)
                            
                            hbox:
                                spacing UI_SPACING
                                xalign 0.5
                                yalign 0.5
                                
                                # Language flag
                                add lang_info["flag"] size (30, 30)
                                
                                # Language name
                                text lang_info["name"] size TEXT_SIZE_SMALL
                                
                                # Current language indicator
                                if lang_code == localization_manager.get_current_language():
                                    text "?" size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]

                                #Select button
                                $ button_width = 80 if lang_code != localization_manager.get_current_language() else None
                                textbutton "Select" action [
                                     Function(localization_manager.set_language, lang_code),
                                     Function(renpy.play, SFX_SUCCESS),
                                     Hide("language_selection")
                                ] xsize button_width

            # Current language info
            text "Current Language: [localization_manager.get_supported_languages()[localization_manager.get_current_language()]['name']]" size TEXT_SIZE_SMALL xalign 0.5
            
            # Close button
            textbutton "Close" action Hide("language_selection") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
    # INITIALIZATION
    # =============================================================================

init python:
    # Load saved preferences
    if "preferred_language" in persistent.game_state:
        localization_manager.set_language(persistent.game_state["preferred_language"])
    
    if "key_bindings" in persistent.game_state:
        input_manager.key_bindings = persistent.game_state["key_bindings"]
    
    # Load accessibility settings
    accessibility_manager.load_accessibility_settings()