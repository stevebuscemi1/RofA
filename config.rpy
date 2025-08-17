# game/config.rpy
init python:
    # =============================================================================
    # GAME CONSTANTS - CENTRALIZED CONFIGURATION
    # =============================================================================
    # =============================================================================
    # GAME IDENTIFICATION
    # =============================================================================
    
    # Game information
    GAME_ID = "heroes_of_the_realm"
    GAME_TITLE = "Heroes of the Realm"
    GAME_VERSION = "1.0"
    GAME_AUTHOR = "Your Name"
    GAME_WEBSITE = "https://yourwebsite.com"
    
    # =============================================================================
    # SCREEN AND DISPLAY SETTINGS
    # =============================================================================
    
    # Screen dimensions
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_FULLSCREEN = False
    
    # Text settings
    TEXT_SIZE_SMALL = 16
    TEXT_SIZE_NORMAL = 20
    TEXT_SIZE_LARGE = 30
    TEXT_SIZE_XLARGE = 40
    
    # Text colors
    TEXT_COLOR_NORMAL = "#FFFFFF"
    TEXT_COLOR_HIGHLIGHT = "#FFFF00"
    TEXT_COLOR_DISABLED = "#808080"
    TEXT_COLOR_ERROR = "#FF6666"
    TEXT_COLOR_SUCCESS = "#66FF66"
    TEXT_COLOR_WARNING = "#FFFF66"
    TEXT_COLOR_INFO = "#66FFFF"
    
    # UI spacing and padding
    UI_PADDING = 20
    UI_SPACING = 10
    UI_MARGIN = 10
    UI_BUTTON_WIDTH = 200
    UI_BUTTON_HEIGHT = 50
    UI_BUTTON_SMALL_WIDTH = 150
    UI_BUTTON_SMALL_HEIGHT = 40
    
    # =============================================================================
    # CHARACTER CONSTANTS
    # =============================================================================
    
    # Character identifiers
    CHAR_WARRIOR = "warrior"
    CHAR_MAGE = "mage"
    CHAR_ROGUE = "rogue"
    CHAR_CLERIC = "cleric"
    CHAR_RANGER = "ranger"
    
    # Character display names
    DISPLAY_NAME_WARRIOR = "Warrior"
    DISPLAY_NAME_MAGE = "Mage"
    DISPLAY_NAME_ROGUE = "Rogue"
    DISPLAY_NAME_CLERIC = "Cleric"
    DISPLAY_NAME_RANGER = "Ranger"
    
    # Character stats
    STAT_STRENGTH = "strength"
    STAT_AGILITY = "agility"
    STAT_INTELLIGENCE = "intelligence"
    STAT_CHARISMA = "charisma"
    STAT_ENDURANCE = "endurance"
    STAT_LUCK = "luck"
    
    # Stat limits
    MIN_STAT_VALUE = 1
    MAX_STAT_VALUE = 10
    STAT_POINTS_PER_LEVEL = 3
    
    # =============================================================================
    # ITEM CONSTANTS
    # =============================================================================
    
    # Item types
    ITEM_TYPE_WEAPON = "weapon"
    ITEM_TYPE_ARMOR = "armor"
    ITEM_TYPE_CONSUMABLE = "consumable"
    ITEM_TYPE_QUEST = "quest"
    ITEM_TYPE_MISC = "misc"
    
    # Item rarities
    RARITY_COMMON = "common"
    RARITY_UNCOMMON = "uncommon"
    RARITY_RARE = "rare"
    RARITY_EPIC = "epic"
    RARITY_LEGENDARY = "legendary"
    
    # Inventory settings
    MAX_INVENTORY_SLOTS = 20
    MAX_ABILITIES = 6
    
    # Basic items
    ITEM_STEEL_SWORD = "Steel Sword"
    ITEM_WOODEN_SHIELD = "Wooden Shield"
    ITEM_HEALTH_POTION = "Health Potion"
    ITEM_MAGIC_STAFF = "Magic Staff"
    ITEM_SPELLBOOK = "Spellbook"
    ITEM_MANA_POTION = "Mana Potion"
    ITEM_DAGGER = "Dagger"
    ITEM_LOCKPICKS = "Lockpicks"
    ITEM_SMOKE_BOMB = "Smoke Bomb"
    ITEM_MACE = "Mace"
    ITEM_HOLY_SYMBOL = "Holy Symbol"
    ITEM_HEALING_POTION = "Healing Potion"
    ITEM_BOW = "Bow"
    ITEM_ARROWS = "Arrows"
    ITEM_HERBS = "Herbs"
    
    # Advanced items (used in story)
    ITEM_STEEL_SWORD_UPGRADED = "Upgraded Steel Sword"
    ITEM_IRON_SHIELD = "Iron Shield"
    ITEM_SPELLBOOK_ADVANCED = "Advanced Spellbook"
    ITEM_ENCHANTED_AMULET = "Enchanted Amulet"
    ITEM_HOLY_WATER = "Holy Water"
    ITEM_MAP_TREASURE = "Treasure Map"
    ITEM_CHILDREN_DOLL = "Children's Doll"
    ITEM_HERBS_RARE = "Rare Herbs"
    ITEM_LOCKPICKS_MASTER = "Master Lockpicks"
    ITEM_ANCIENT_RELIC = "Ancient Relic"
    ITEM_LEGENDARY_WEAPON = "Legendary Weapon"
    
    # =============================================================================
    # ASSET PATHS
    # =============================================================================
    
    # Character images
    IMG_WARRIOR_SMALL = "images/characters/warrior_small.png"
    IMG_WARRIOR_LARGE = "images/characters/warrior_large.png"
    IMG_MAGE_SMALL = "images/characters/mage_small.png"
    IMG_MAGE_LARGE = "images/characters/mage_large.png"
    IMG_ROGUE_SMALL = "images/characters/rogue_small.png"
    IMG_ROGUE_LARGE = "images/characters/rogue_large.png"
    IMG_CLERIC_SMALL = "images/characters/cleric_small.png"
    IMG_CLERIC_LARGE = "images/characters/cleric_large.png"
    IMG_RANGER_SMALL = "images/characters/ranger_small.png"
    IMG_RANGER_LARGE = "images/characters/ranger_large.png"
    
    # Background images
    BG_BLACK = "images/backgrounds/black.jpg"
    BG_CITY = "images/backgrounds/city.jpg"
    BG_FOREST = "images/backgrounds/forest.jpg"
    BG_TEMPLE = "images/backgrounds/temple.jpg"
    BG_DUNGEON = "images/backgrounds/dungeon.jpg"
    BG_CASTLE = "images/backgrounds/castle.jpg"
    BG_MARKET = "images/backgrounds/market.jpg"
    BG_TAVERN = "images/backgrounds/tavern.jpg"
    BG_LIBRARY = "images/backgrounds/library.jpg"
    BG_BLACKSMITH = "images/backgrounds/blacksmith.jpg"
    
    # UI elements
    UI_BUTTON_NORMAL = "images/ui/button_normal.png"
    UI_BUTTON_HOVER = "images/ui/button_hover.png"
    UI_BUTTON_DISABLED = "images/ui/button_disabled.png"
    UI_FRAME = "images/ui/frame.png"
    UI_ICON = "images/ui/icon.png"
    UI_BAR_LEFT = "images/ui/bar_left.png"
    UI_BAR_RIGHT = "images/ui/bar_right.png"
    UI_BAR_THUMB = "images/ui/bar_thumb.png"
    UI_SCROLLBAR_BASE = "images/ui/scrollbar_base.png"
    UI_SCROLLBAR_THUMB = "images/ui/scrollbar_thumb.png"
    UI_SLIDER_BASE = "images/ui/slider_base.png"
    UI_SLIDER_THUMB = "images/ui/slider_thumb.png"
    
    # Sound effects
    SFX_CLICK = "sounds/effects/click.wav"
    SFX_SUCCESS = "sounds/effects/success.wav"
    SFX_FAILURE = "sounds/effects/failure.wav"
    SFX_INVENTORY = "sounds/effects/inventory.wav"
    SFX_BATTLE = "sounds/effects/battle.wav"
    SFX_LEVEL_UP = "sounds/effects/level_up.wav"
    SFX_QUEST_COMPLETE = "sounds/effects/quest_complete.wav"
    SFX_ACHIEVEMENT_UNLOCK = "sounds/effects/achievement_unlock.wav"
    
    # Music tracks
    MUSIC_MAIN_THEME = "music/main_theme.ogg"
    MUSIC_BATTLE = "music/battle.ogg"
    MUSIC_PEACEFUL = "music/peaceful.ogg"
    MUSIC_MYSTICAL = "music/mystical.ogg"
    MUSIC_VICTORY = "music/victory.ogg"
    MUSIC_DEFEAT = "music/defeat.ogg"
    MUSIC_CHARACTER_THEME_WARRIOR = "music/themes/warrior.ogg"
    MUSIC_CHARACTER_THEME_MAGE = "music/themes/mage.ogg"
    MUSIC_CHARACTER_THEME_ROGUE = "music/themes/rogue.ogg"
    MUSIC_CHARACTER_THEME_CLERIC = "music/themes/cleric.ogg"
    MUSIC_CHARACTER_THEME_RANGER = "music/themes/ranger.ogg"
    
    # =============================================================================
    # STORY AND NARRATIVE CONSTANTS
    # =============================================================================
    
    # Chapter names
    CHAPTER_PROLOGUE = "Prologue"
    CHAPTER_1 = "The Awakening"
    CHAPTER_2 = "The Journey"
    CHAPTER_3 = "The Confrontation"
    CHAPTER_EPILOGUE = "Epilogue"
    
    # Story flags
    FLAG_MET_MAGE = "met_mage"
    FLAG_MET_WARRIOR = "met_warrior"
    FLAG_MET_ROGUE = "met_rogue"
    FLAG_MET_CLERIC = "met_cleric"
    FLAG_MET_RANGER = "met_ranger"
    FLAG_TRADED_ITEMS = "traded_items"
    FLAG_COMPLETED_QUEST = "completed_quest"
    FLAG_FOUND_TREASURE = "found_treasure"
    FLAG_DEFEATED_BOSS = "defeated_boss"
    FLAG_DISCOVERED_SECRET = "discovered_secret"
    FLAG_ALLIED_WITH_FACTION = "allied_with_faction"
    FLAG_LEARNED_SECRET_ABILITY = "learned_secret_ability"
    
    # =============================================================================
    # LOCATION CONSTANTS
    # =============================================================================
    
    # Location identifiers
    LOC_CITY = "city"
    LOC_FOREST = "forest"
    LOC_TEMPLE = "temple"
    LOC_DUNGEON = "dungeon"
    LOC_CASTLE = "castle"
    LOC_MARKET = "market"
    LOC_TAVERN = "tavern"
    LOC_LIBRARY = "library"
    LOC_BLACKSMITH = "blacksmith"
    LOC_CEMETERY = "cemetery"
    LOC_MOUNTAINS = "mountains"
    LOC_RUINS = "ruins"
    LOC_CAVES = "caves"
    LOC_SHORE = "shore"
    LOC_BRIDGE = "bridge"
    LOC_CAMP = "camp"
    
    # =============================================================================
    # QUEST CONSTANTS
    # =============================================================================
    
    # Quest identifiers
    QUEST_MAIN = "main_quest"
    QUEST_SIDE_1 = "side_quest_1"
    QUEST_SIDE_2 = "side_quest_2"
    QUEST_SIDE_3 = "side_quest_3"
    QUEST_SIDE_4 = "side_quest_4"
    QUEST_SIDE_5 = "side_quest_5"
    QUEST_HIDDEN = "hidden_quest"
    QUEST_DAILY = "daily_quest"
    QUEST_REPEATABLE = "repeatable_quest"
    
    # Quest types
    QUEST_TYPE_MAIN = "main"
    QUEST_TYPE_SIDE = "side"
    QUEST_TYPE_HIDDEN = "hidden"
    QUEST_TYPE_DAILY = "daily"
    QUEST_TYPE_REPEATABLE = "repeatable"
    
    # Quest statuses
    QUEST_STATUS_AVAILABLE = "available"
    QUEST_STATUS_ACTIVE = "active"
    QUEST_STATUS_COMPLETED = "completed"
    QUEST_STATUS_FAILED = "failed"
    QUEST_STATUS_LOCKED = "locked"
    
    # Quest rewards
    QUEST_REWARD_EXPERIENCE_MULTIPLIER = 1.0
    QUEST_REWARD_GOLD_MULTIPLIER = 1.0
    QUEST_REWARD_ITEM_CHANCE = 0.3
    
    # Quest difficulty levels
    QUEST_DIFFICULTY_TRIVIAL = "trivial"
    QUEST_DIFFICULTY_EASY = "easy"
    QUEST_DIFFICULTY_MEDIUM = "medium"
    QUEST_DIFFICULTY_HARD = "hard"
    QUEST_DIFFICULTY_EPIC = "epic"
    
    # Quest time limits
    QUEST_TIME_LIMIT_NONE = 0
    QUEST_TIME_LIMIT_SHORT = 300  # 5 minutes
    QUEST_TIME_LIMIT_MEDIUM = 600  # 10 minutes
    QUEST_TIME_LIMIT_LONG = 1800  # 30 minutes
    
    # =============================================================================
    # ACHIEVEMENT CONSTANTS
    # =============================================================================
    
    # Achievement identifiers
    ACHIEVEMENT_FIRST_BLOOD = "first_blood"
    ACHIEVEMENT_TREASURE_HUNTER = "treasure_hunter"
    ACHIEVEMENT_MASTER_TRADER = "master_trader"
    ACHIEVEMENT_FRIENDSHIP = "friendship"
    ACHIEVEMENT_COMPLETIONIST = "completionist"
    ACHIEVEMENT_EXPLORER = "explorer"
    ACHIEVEMENT_WARRIOR_PATH = "warrior_path"
    ACHIEVEMENT_MAGE_PATH = "mage_path"
    ACHIEVEMENT_ROGUE_PATH = "rogue_path"
    ACHIEVEMENT_CLERIC_PATH = "cleric_path"
    ACHIEVEMENT_RANGER_PATH = "ranger_path"
    ACHIEVEMENT_SPEEDRUNNER = "speedrunner"
    ACHIEVEMENT_PERFECTIONIST = "perfectionist"
    
    # Achievement categories
    ACHIEVEMENT_CATEGORY_COMBAT = "combat"
    ACHIEVEMENT_CATEGORY_EXPLORATION = "exploration"
    ACHIEVEMENT_CATEGORY_SOCIAL = "social"
    ACHIEVEMENT_CATEGORY_QUEST = "quest"
    ACHIEVEMENT_CATEGORY_CHARACTER = "character"
    ACHIEVEMENT_CATEGORY_SPECIAL = "special"
    
    # Achievement thresholds
    ACHIEVEMENT_THRESHOLD_FRIEND = 2
    ACHIEVEMENT_THRESHOLD_ALLY = 3
    ACHIEVEMENT_THRESHOLD_COMPANION = 4
    
    # Achievement notification settings
    ACHIEVEMENT_NOTIFICATION_DURATION = 5.0
    ACHIEVEMENT_NOTIFICATION_SOUND = SFX_ACHIEVEMENT_UNLOCK
    ACHIEVEMENT_UNLOCK_SOUND = "sounds/effects/achievement_unlock.wav"  # Sound for achievement unlock
    ACHIEVEMENT_UNLOCK_EFFECT_DURATION = 2.0  # Duration of unlock effect
    ACHIEVEMENT_PROGRESS_NOTIFICATION = True  # Show progress notifications for achievements
    
    # =============================================================================
    # RELATIONSHIP CONSTANTS
    # =============================================================================
    
    # Relationship levels
    RELATIONSHIP_STRANGER = 0
    RELATIONSHIP_ACQUAINTANCE = 1
    RELATIONSHIP_FRIEND = 2
    RELATIONSHIP_ALLY = 3
    RELATIONSHIP_COMPANION = 4
    RELATIONSHIP_SOULMATE = 5
    
    # Relationship modifiers
    RELATIONSHIP_MODIFIER_POSITIVE = 1
    RELATIONSHIP_MODIFIER_NEGATIVE = -1
    RELATIONSHIP_MODIFIER_NEUTRAL = 0
    
    # Relationship thresholds
    RELATIONSHIP_THRESHOLD_FRIEND = 2
    RELATIONSHIP_THRESHOLD_ALLY = 3
    RELATIONSHIP_THRESHOLD_COMPANION = 4
    
    # =============================================================================
    # ABILITY CONSTANTS
    # =============================================================================
    
    # Ability types
    ABILITY_TYPE_COMBAT = "combat"
    ABILITY_TYPE_MAGIC = "magic"
    ABILITY_TYPE_SKILL = "skill"
    ABILITY_TYPE_PASSIVE = "passive"
    
    # Ability levels
    ABILITY_LEVEL_MIN = 1
    ABILITY_LEVEL_MAX = 5
    
    # Ability cooldowns (in seconds)
    ABILITY_COOLDOWN_SHORT = 1.0
    ABILITY_COOLDOWN_MEDIUM = 3.0
    ABILITY_COOLDOWN_LONG = 5.0
    ABILITY_COOLDOWN_VERY_LONG = 10.0
    
    # Ability ranges
    ABILITY_RANGE_MELEE = 1.0
    ABILITY_RANGE_SHORT = 3.0
    ABILITY_RANGE_MEDIUM = 5.0
    ABILITY_RANGE_LONG = 10.0
    ABILITY_RANGE_VERY_LONG = 20.0
    
    # Ability effects
    ABILITY_EFFECT_DURATION_SHORT = 2.0
    ABILITY_EFFECT_DURATION_MEDIUM = 5.0
    ABILITY_EFFECT_DURATION_LONG = 10.0
    ABILITY_EFFECT_DURATION_VERY_LONG = 30.0
    
    # =============================================================================
    # SAVE/LOAD CONSTANTS
    # =============================================================================
    
    # Save settings
    SAVE_SLOTS = 10
    AUTOSAVE_SLOTS = 3
    QUICKSAVE_SLOTS = 1
    SAVE_DIRECTORY = "saves"
    SAVE_FILE_PREFIX = "save-"
    SAVE_FILE_EXTENSION = ".save"
    SAVE_ENABLE_QUICK_SAVE = True
    
    # Save compression settings
    SAVE_COMPRESSION_ENABLED = True
    SAVE_COMPRESSION_LEVEL = 6  # 1-9, where 9 is maximum compression
    
    # Save validation
    SAVE_VALIDATE_ON_LOAD = True
    SAVE_VALIDATE_CHECKSUM = True
    SAVE_VALIDATE_VERSION = True
    
    # Save backup settings
    SAVE_AUTO_BACKUP = True
    SAVE_BACKUP_INTERVAL = 10  # Create backup every 10 saves
    SAVE_MAX_BACKUPS = 5
    
    # Save metadata
    SAVE_METADATA_INCLUDE_SCREENSHOT = True
    SAVE_METADATA_INCLUDE_PLAYTIME = True
    SAVE_METADATA_INCLUDE_CHARACTER = True
    SAVE_METADATA_INCLUDE_LOCATION = True
    
    # =============================================================================
    # LOCALIZATION CONSTANTS
    # =============================================================================
    
    # Supported languages
    LANG_ENGLISH = "en"
    LANG_SPANISH = "es"
    LANG_FRENCH = "fr"
    LANG_GERMAN = "de"
    LANG_JAPANESE = "ja"
    LANG_CHINESE = "zh"
    
    # Language names
    LANGUAGE_NAMES = {
        LANG_ENGLISH: "English",
        LANG_SPANISH: "Espanol",
        LANG_FRENCH: "Francais",
        LANG_GERMAN: "Deutsch",
        LANG_JAPANESE: "Japanese",
        LANG_CHINESE: "Chinese"
    }
    
    # Font paths
    FONT_DEFAULT = "fonts/DejaVuSans.ttf"
    FONT_JAPANESE = "fonts/NotoSansCJKjp-Regular.otf"
    FONT_CHINESE = "fonts/NotoSansCJKsc-Regular.otf"
    
    # =============================================================================
    # INPUT CONSTANTS
    # =============================================================================
    
    # Input types
    INPUT_KEYBOARD = "keyboard"
    INPUT_MOUSE = "mouse"
    INPUT_CONTROLLER = "controller"
    INPUT_TOUCH = "touch"
    
    # Input repeat settings
    INPUT_REPEAT_DELAY = 0.5
    INPUT_REPEAT_INTERVAL = 0.05
        
    # Key bindings (defaults)
    KEY_ADVANCE = ["space", "return", "KP_Enter"]
    KEY_BACK = ["escape", "backspace"]
    KEY_MENU = ["escape", "rightshift"]
    KEY_SAVE = ["f5", "KP_Add"]
    KEY_LOAD = ["f9", "KP_Subtract"]
    KEY_QUICK_SAVE = ["f6"]
    KEY_QUICK_LOAD = ["f7"]
    KEY_SKIP = ["ctrl", "KP_Multiply"]
    KEY_AUTO_MODE = ["a"]
    KEY_HIDE_UI = ["h"]
    KEY_LOG = ["l"]
    KEY_INVENTORY = ["i"]
    KEY_CHARACTER_INFO = ["c"]
    KEY_MAP = ["m"]
    KEY_JOURNAL = ["j"]
    KEY_UP = ["up", "w", "KP_Up"]
    KEY_DOWN = ["down", "s", "KP_Down"]
    KEY_LEFT = ["left", "a", "KP_Left"]
    KEY_RIGHT = ["right", "d", "KP_Right"]
    KEY_PAGE_UP = ["pageup", "KP_Page_Up"]
    KEY_PAGE_DOWN = ["pagedown", "KP_Page_Down"]
    KEY_HOME = ["home", "KP_Home"]
    KEY_END = ["end", "KP_End"]
    
    # Mouse bindings
    MOUSE_LEFT = "mouse_left"
    MOUSE_RIGHT = "mouse_right"
    MOUSE_MIDDLE = "mouse_middle"
    MOUSE_WHEEL_UP = "mouse_wheel_up"
    MOUSE_WHEEL_DOWN = "mouse_wheel_down"
    
    # =============================================================================
    # ACCESSIBILITY CONSTANTS
    # =============================================================================
    
    # Text size multipliers
    TEXT_SIZE_SMALL_MULTIPLIER = 0.8
    TEXT_SIZE_NORMAL_MULTIPLIER = 1.0
    TEXT_SIZE_LARGE_MULTIPLIER = 1.2
    TEXT_SIZE_XLARGE_MULTIPLIER = 1.5
    TEXT_SIZE_XXLARGE_MULTIPLIER = 2.0
    
    # Color blind modes
    COLOR_BLIND_NONE = "none"
    COLOR_BLIND_PROTANOPIA = "protanopia"
    COLOR_BLIND_DEUTERANOPIA = "deuteranopia"
    COLOR_BLIND_TRITANOPIA = "tritanopia"
    
    # Subtitle sizes
    SUBTITLE_SIZE_SMALL = "small"
    SUBTITLE_SIZE_NORMAL = "normal"
    SUBTITLE_SIZE_LARGE = "large"
    
    # Accessibility settings
    ACCESSIBILITY_ENABLE_TEXT_TO_SPEECH = False  # Enable text-to-speech
    ACCESSIBILITY_SPEECH_RATE = 1.0  # Speech rate (0.5 to 2.0)
    ACCESSIBILITY_SPEECH_PITCH = 1.0  # Speech pitch (0.5 to 2.0)
    ACCESSIBILITY_ENABLE_HIGH_CONTRAST_MODES = True  # Enable multiple contrast modes
    ACCESSIBILITY_ENABLE_DALTONISM_FILTER = False  # Enable color blindness filter
    ACCESSIBILITY_ENABLE_MONOCHROME_MODE = False  # Enable monochrome mode
    ACCESSIBILITY_KEYBOARD_NAVIGATION_TIMEOUT = 5.0  # Timeout for keyboard navigation
    ACCESSIBILITY_FOCUS_INDICATOR_SIZE = 3  # Size of focus indicators
    ACCESSIBILITY_UI_SCALE_MIN = 0.5  # Minimum UI scale
    ACCESSIBILITY_UI_SCALE_MAX = 2.0  # Maximum UI scale
    ACCESSIBILITY_UI_SCALE_STEP = 0.1  # UI scale step size
    
    # =============================================================================
    # DEBUG SETTINGS
    # =============================================================================
    
    # Debug mode settings
    DEBUG_MODE = True
    DEBUG_SHOW_FPS = False
    DEBUG_SHOW_MEMORY = False
    DEBUG_SHOW_STATS = True
    DEBUG_ENABLE_CONSOLE = True
    DEBUG_ENABLE_VARIABLE_INSPECTOR = True
    DEBUG_ENABLE_PERFORMANCE_MONITOR = True
    DEBUG_ENABLE_TEST_RUNNER = True
    
    # Debug key bindings
    DEBUG_KEY_CONSOLE = "f2"
    DEBUG_KEY_VARIABLES = "f3"
    DEBUG_KEY_PERFORMANCE = "f4"
    DEBUG_KEY_TESTS = "f5"
    DEBUG_KEY_LOG = "f6"
    DEBUG_KEY_TOGGLE_DEBUG = "f12"
    
    # Debug log settings
    DEBUG_LOG_TO_FILE = True
    DEBUG_LOG_FILE_PATH = "debug_log.txt"
    DEBUG_LOG_MAX_ENTRIES = 1000
    DEBUG_LOG_TO_CONSOLE = True  # Whether to log to console
    DEBUG_SHOW_PERFORMANCE_OVERLAY = True  # Show FPS and memory usage
    DEBUG_ENABLE_PROFILER = False  # Enable performance profiler
    DEBUG_ENABLE_MEMORY_TRACKING = True  # Enable memory tracking
    DEBUG_ENABLE_FRAME_TIME_TRACKING = True  # Enable frame time tracking
    
    # =============================================================================
    # PERFORMANCE SETTINGS
    # =============================================================================
    
    # Performance settings
    PERFORMANCE_TARGET_FPS = 60  # Target frames per second
    PERFORMANCE_MAX_FRAME_TIME = 0.05  # Maximum acceptable frame time (20 FPS minimum)
    PERFORMANCE_CACHE_SIZE = 64  # Image cache size in MB
    PERFORMANCE_PREDICTIVE_IMAGES = 10  # Number of predictive images to load
    PERFORMANCE_TEXTURE_CACHE_SIZE = 64  # Texture cache size in MB
    PERFORMANCE_ENABLE_HARDWARE_ACCELERATION = True  # Enable hardware acceleration
    PERFORMANCE_ENABLE_TEXTURE_COMPRESSION = True  # Enable texture compression
    
    # =============================================================================
    # GAMEPLAY SETTINGS
    # =============================================================================
    
    # Gameplay settings
    GAME_STARTING_LEVEL = 1
    GAME_MAX_LEVEL = 20
    GAME_STARTING_GOLD = 50
    GAME_STARTING_HEALTH = 100
    GAME_STARTING_MANA = 50
    GAME_EXPERIENCE_PER_LEVEL = 100
    GAME_EXPERIENCE_MULTIPLIER = 1.0
    
    # Difficulty settings
    DIFFICULTY_EASY = "easy"
    DIFFICULTY_NORMAL = "normal"
    DIFFICULTY_HARD = "hard"
    DIFFICULTY_EXPERT = "expert"
    
    # Difficulty multipliers
    DIFFICULTY_MULTIPLIERS = {
        DIFFICULTY_EASY: {
            "experience": 1.5,
            "gold": 1.5,
            "damage_taken": 0.8,
            "damage_dealt": 1.2
        },
        DIFFICULTY_NORMAL: {
            "experience": 1.0,
            "gold": 1.0,
            "damage_taken": 1.0,
            "damage_dealt": 1.0
        },
        DIFFICULTY_HARD: {
            "experience": 0.8,
            "gold": 0.8,
            "damage_taken": 1.2,
            "damage_dealt": 0.9
        },
        DIFFICULTY_EXPERT: {
            "experience": 0.6,
            "gold": 0.6,
            "damage_taken": 1.5,
            "damage_dealt": 0.8
        }
    }
    
    # =============================================================================
    # AUDIO/VISUAL SETTINGS
    # =============================================================================
    
    # Audio settings
    AUDIO_MASTER_VOLUME_DEFAULT = 0.8
    AUDIO_MUSIC_VOLUME_DEFAULT = 0.8
    AUDIO_SOUND_VOLUME_DEFAULT = 0.8
    AUDIO_VOICE_VOLUME_DEFAULT = 0.8
    AUDIO_AMBIENT_VOLUME_DEFAULT = 0.5
    
    # Visual settings
    VISUAL_TRANSITIONS_ENABLED = True
    VISUAL_EFFECTS_ENABLED = True
    VISUAL_PARTICLES_ENABLED = True
    VISUAL_ANIMATIONS_ENABLED = True
    
    # =============================================================================
    # UI/UX SETTINGS
    # =============================================================================
    
    # UI settings
    UI_AUTO_ADVANCE_ENABLED = False
    UI_AUTO_ADVANCE_DELAY = 3.0
    UI_TEXT_SPEED_DEFAULT = 50
    UI_TEXT_SPEED_FAST = 150
    UI_SKIP_UNREAD_TEXT = False
    UI_SHOW_EMPTY_WINDOW = True
    
    # Quick menu settings
    QUICK_MENU_ENABLED = True
    QUICK_MENU_AUTO_HIDE = True
    QUICK_MENU_HIDE_DELAY = 3.0
    
    UI_TOOLTIP_DELAY = 0.5  # Seconds before tooltip appears
    UI_NOTIFICATION_DURATION = 3.0  # Seconds for notification display
    UI_LOADING_BAR_WIDTH = 300  # Width of loading bars
    UI_LOADING_BAR_HEIGHT = 20  # Height of loading bars
    
    # =============================================================================
    # INITIALIZATION
    # =============================================================================
    
    # Initialize game state
    persistent.game_state = {
        "selected_character": None,
        "inventory": {},
        "relationships": {},
        "flags": {},
        "achievements": [],
        "current_chapter": CHAPTER_PROLOGUE,
        "completed_quests": [],
        "current_location": LOC_CITY,
        "game_time": 0,
        "play_time": 0,
        "difficulty": DIFFICULTY_NORMAL,
        "audio_settings": {
            "master_volume": AUDIO_MASTER_VOLUME_DEFAULT,
            "music_volume": AUDIO_MUSIC_VOLUME_DEFAULT,
            "sound_volume": AUDIO_SOUND_VOLUME_DEFAULT,
            "voice_volume": AUDIO_VOICE_VOLUME_DEFAULT,
            "ambient_volume": AUDIO_AMBIENT_VOLUME_DEFAULT
        },
        "visual_settings": {
            "transitions_enabled": VISUAL_TRANSITIONS_ENABLED,
            "effects_enabled": VISUAL_EFFECTS_ENABLED,
            "particles_enabled": VISUAL_PARTICLES_ENABLED,
            "animations_enabled": VISUAL_ANIMATIONS_ENABLED
        },
        "accessibility_settings": {
            "text_size_multiplier": TEXT_SIZE_NORMAL_MULTIPLIER,
            "high_contrast_mode": False,
            "color_blind_mode": COLOR_BLIND_NONE,
            "screen_reader_enabled": False,
            "subtitles_enabled": True,
            "subtitle_size": SUBTITLE_SIZE_NORMAL,
            "captions_enabled": True,
            "visual_cues_enabled": True,
            "audio_cues_enabled": True,
            "simplified_ui": False,
            "reduced_motion": False,
            "focus_indicators_enabled": True,
            "keyboard_navigation_enabled": True
        },
        "input_settings": {
            "key_bindings": {},
            "mouse_sensitivity": 1.0,
            "controller_enabled": True
        },
        "preferred_language": LANG_ENGLISH
    }
    
    # Initialize character relationships
    for char_id in [CHAR_WARRIOR, CHAR_MAGE, CHAR_ROGUE, CHAR_CLERIC, CHAR_RANGER]:
        for other_id in [CHAR_WARRIOR, CHAR_MAGE, CHAR_ROGUE, CHAR_CLERIC, CHAR_RANGER]:
            if char_id != other_id:
                key = f"{char_id}_{other_id}"
                persistent.game_state["relationships"][key] = RELATIONSHIP_STRANGER
    
    # Initialize flags
    for flag in [FLAG_MET_MAGE, FLAG_MET_WARRIOR, FLAG_MET_ROGUE, FLAG_MET_CLERIC, 
                 FLAG_MET_RANGER, FLAG_TRADED_ITEMS, FLAG_COMPLETED_QUEST, 
                 FLAG_FOUND_TREASURE, FLAG_DEFEATED_BOSS, FLAG_DISCOVERED_SECRET,
                 FLAG_ALLIED_WITH_FACTION, FLAG_LEARNED_SECRET_ABILITY]:
        persistent.game_state["flags"][flag] = False
    
    # Initialize achievements
    persistent.game_state["achievements"] = []
    
    # Initialize input bindings
    persistent.game_state["input_settings"]["key_bindings"] = {
        "advance": KEY_ADVANCE,
        "back": KEY_BACK,
        "menu": KEY_MENU,
        "save": KEY_SAVE,
        "load": KEY_LOAD,
        "quick_save": KEY_QUICK_SAVE,
        "quick_load": KEY_QUICK_LOAD,
        "skip": KEY_SKIP,
        "auto_mode": KEY_AUTO_MODE,
        "hide_ui": KEY_HIDE_UI,
        "log": KEY_LOG,
        "inventory": KEY_INVENTORY,
        "character_info": KEY_CHARACTER_INFO,
        "map": KEY_MAP,
        "journal": KEY_JOURNAL,
        "up": KEY_UP,
        "down": KEY_DOWN,
        "left": KEY_LEFT,
        "right": KEY_RIGHT,
        "page_up": KEY_PAGE_UP,
        "page_down": KEY_PAGE_DOWN,
        "home": KEY_HOME,
        "end": KEY_END
    }