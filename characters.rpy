# game/characters.rpy

init python:
    # =============================================================================
    # CHARACTER MANAGEMENT SYSTEM
    # =============================================================================
    
    class CharacterManager:
        """
        Manages all character-related data and operations including stats,
        abilities, inventory, and relationships.
        """
        
        def __init__(self):
            """Initialize the character manager with default data."""
            self.characters = self._initialize_characters()
            self.selected_character = None
            self.inventory_manager = InventoryManager()
            self.relationship_manager = RelationshipManager()
            
        def _initialize_characters(self):
            """Initialize all character data with default values."""
            # Import constants from config if they exist
            global CHAR_WARRIOR, CHAR_MAGE, CHAR_ROGUE, CHAR_CLERIC, CHAR_RANGER
            global DISPLAY_NAME_WARRIOR, DISPLAY_NAME_MAGE, DISPLAY_NAME_ROGUE, DISPLAY_NAME_CLERIC, DISPLAY_NAME_RANGER
            global IMG_WARRIOR_SMALL, IMG_WARRIOR_LARGE, IMG_MAGE_SMALL, IMG_MAGE_LARGE
            global IMG_ROGUE_SMALL, IMG_ROGUE_LARGE, IMG_CLERIC_SMALL, IMG_CLERIC_LARGE
            global IMG_RANGER_SMALL, IMG_RANGER_LARGE
            global STAT_STRENGTH, STAT_AGILITY, STAT_INTELLIGENCE, STAT_CHARISMA, STAT_ENDURANCE, STAT_LUCK
            global ABILITY_TYPE_COMBAT, ABILITY_TYPE_MAGIC, ABILITY_TYPE_SKILL, ABILITY_TYPE_PASSIVE
            global ITEM_STEEL_SWORD, ITEM_WOODEN_SHIELD, ITEM_HEALTH_POTION
            global ITEM_MAGIC_STAFF, ITEM_SPELLBOOK, ITEM_MANA_POTION
            global ITEM_DAGGER, ITEM_LOCKPICKS, ITEM_SMOKE_BOMB
            global ITEM_MACE, ITEM_HOLY_SYMBOL, ITEM_HEALING_POTION
            global ITEM_BOW, ITEM_ARROWS, ITEM_HERBS
            global MAX_INVENTORY_SLOTS, MAX_ABILITIES, MAX_STAT_VALUE
            global LOC_CITY, LOC_TEMPLE, LOC_FOREST
            
            # Check if constants exist, if not create default values
            try:
                CHAR_WARRIOR
            except NameError:
                CHAR_WARRIOR = "warrior"
                CHAR_MAGE = "mage"
                CHAR_ROGUE = "rogue"
                CHAR_CLERIC = "cleric"
                CHAR_RANGER = "ranger"
                DISPLAY_NAME_WARRIOR = "Warrior"
                DISPLAY_NAME_MAGE = "Mage"
                DISPLAY_NAME_ROGUE = "Rogue"
                DISPLAY_NAME_CLERIC = "Cleric"
                DISPLAY_NAME_RANGER = "Ranger"
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
                STAT_STRENGTH = "strength"
                STAT_AGILITY = "agility"
                STAT_INTELLIGENCE = "intelligence"
                STAT_CHARISMA = "charisma"
                STAT_ENDURANCE = "endurance"
                STAT_LUCK = "luck"
                ABILITY_TYPE_COMBAT = "combat"
                ABILITY_TYPE_MAGIC = "magic"
                ABILITY_TYPE_SKILL = "skill"
                ABILITY_TYPE_PASSIVE = "passive"
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
                MAX_INVENTORY_SLOTS = 20
                MAX_ABILITIES = 6
                MAX_STAT_VALUE = 10
                LOC_CITY = "city"
                LOC_TEMPLE = "temple"
                LOC_FOREST = "forest"
                
            return {
                CHAR_WARRIOR: {
                    "id": CHAR_WARRIOR,
                    "name": DISPLAY_NAME_WARRIOR,
                    "image_small": IMG_WARRIOR_SMALL,
                    "image_large": IMG_WARRIOR_LARGE,
                    "bio": "A brave warrior from the Northern Kingdoms, skilled in combat and leadership.",
                    "stats": {
                        STAT_STRENGTH: 9,
                        STAT_AGILITY: 5,
                        STAT_INTELLIGENCE: 4,
                        STAT_CHARISMA: 6,
                        STAT_ENDURANCE: 8,
                        STAT_LUCK: 4
                    },
                    "abilities": [
                        {
                            "name": "Sword Mastery",
                            "type": ABILITY_TYPE_COMBAT,
                            "description": "Increases damage with sword weapons",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Shield Block",
                            "type": ABILITY_TYPE_COMBAT,
                            "description": "Improves defense when using shields",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Battle Cry",
                            "type": ABILITY_TYPE_SKILL,
                            "description": "Boosts party morale in combat",
                            "level": 1,
                            "max_level": 3
                        }
                    ],
                    "inventory": [ITEM_STEEL_SWORD, ITEM_WOODEN_SHIELD, ITEM_HEALTH_POTION],
                    "level": 1,
                    "experience": 0,
                    "health": 100,
                    "max_health": 100,
                    "mana": 0,
                    "max_mana": 0,
                    "gold": 50,
                    "location": LOC_CITY,
                    "quests": [],
                    "achievements": []
                },
                CHAR_MAGE: {
                    "id": CHAR_MAGE,
                    "name": DISPLAY_NAME_MAGE,
                    "image_small": IMG_MAGE_SMALL,
                    "image_large": IMG_MAGE_LARGE,
                    "bio": "A powerful mage from the Academy of Arcane Arts, master of elemental magic.",
                    "stats": {
                        STAT_STRENGTH: 3,
                        STAT_AGILITY: 4,
                        STAT_INTELLIGENCE: 9,
                        STAT_CHARISMA: 5,
                        STAT_ENDURANCE: 4,
                        STAT_LUCK: 6
                    },
                    "abilities": [
                        {
                            "name": "Fireball",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Launches a ball of fire at enemies",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Ice Shard",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Shoots sharp ice projectiles",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Teleport",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Instantly move to a nearby location",
                            "level": 1,
                            "max_level": 3
                        }
                    ],
                    "inventory": [ITEM_MAGIC_STAFF, ITEM_SPELLBOOK, ITEM_MANA_POTION],
                    "level": 1,
                    "experience": 0,
                    "health": 70,
                    "max_health": 70,
                    "mana": 100,
                    "max_mana": 100,
                    "gold": 30,
                    "location": LOC_TEMPLE,
                    "quests": [],
                    "achievements": []
                },
                CHAR_ROGUE: {
                    "id": CHAR_ROGUE,
                    "name": DISPLAY_NAME_ROGUE,
                    "image_small": IMG_ROGUE_SMALL,
                    "image_large": IMG_ROGUE_LARGE,
                    "bio": "A cunning rogue from the Shadow Guild, expert in stealth and deception.",
                    "stats": {
                        STAT_STRENGTH: 5,
                        STAT_AGILITY: 9,
                        STAT_INTELLIGENCE: 6,
                        STAT_CHARISMA: 4,
                        STAT_ENDURANCE: 6,
                        STAT_LUCK: 8
                    },
                    "abilities": [
                        {
                            "name": "Stealth",
                            "type": ABILITY_TYPE_SKILL,
                            "description": "Become invisible to enemies",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Lockpicking",
                            "type": ABILITY_TYPE_SKILL,
                            "description": "Open locked doors and containers",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Backstab",
                            "type": ABILITY_TYPE_COMBAT,
                            "description": "Deal massive damage from behind",
                            "level": 1,
                            "max_level": 5
                        }
                    ],
                    "inventory": [ITEM_DAGGER, ITEM_LOCKPICKS, ITEM_SMOKE_BOMB],
                    "level": 1,
                    "experience": 0,
                    "health": 80,
                    "max_health": 80,
                    "mana": 20,
                    "max_mana": 20,
                    "gold": 40,
                    "location": LOC_CITY,
                    "quests": [],
                    "achievements": []
                },
                CHAR_CLERIC: {
                    "id": CHAR_CLERIC,
                    "name": DISPLAY_NAME_CLERIC,
                    "image_small": IMG_CLERIC_SMALL,
                    "image_large": IMG_CLERIC_LARGE,
                    "bio": "A devoted cleric from the Temple of Light, healer and protector of the innocent.",
                    "stats": {
                        STAT_STRENGTH: 4,
                        STAT_AGILITY: 3,
                        STAT_INTELLIGENCE: 7,
                        STAT_CHARISMA: 8,
                        STAT_ENDURANCE: 6,
                        STAT_LUCK: 5
                    },
                    "abilities": [
                        {
                            "name": "Heal",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Restore health to yourself or allies",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Bless",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Increase party's combat effectiveness",
                            "level": 1,
                            "max_level": 3
                        },
                        {
                            "name": "Turn Undead",
                            "type": ABILITY_TYPE_MAGIC,
                            "description": "Repel or destroy undead creatures",
                            "level": 1,
                            "max_level": 5
                        }
                    ],
                    "inventory": [ITEM_MACE, ITEM_HOLY_SYMBOL, ITEM_HEALING_POTION],
                    "level": 1,
                    "experience": 0,
                    "health": 85,
                    "max_health": 85,
                    "mana": 80,
                    "max_mana": 80,
                    "gold": 35,
                    "location": LOC_TEMPLE,
                    "quests": [],
                    "achievements": []
                },
                CHAR_RANGER: {
                    "id": CHAR_RANGER,
                    "name": DISPLAY_NAME_RANGER,
                    "image_small": IMG_RANGER_SMALL,
                    "image_large": IMG_RANGER_LARGE,
                    "bio": "A skilled ranger from the Forest of Whispers, master of archery and survival.",
                    "stats": {
                        STAT_STRENGTH: 6,
                        STAT_AGILITY: 8,
                        STAT_INTELLIGENCE: 5,
                        STAT_CHARISMA: 5,
                        STAT_ENDURANCE: 7,
                        STAT_LUCK: 7
                    },
                    "abilities": [
                        {
                            "name": "Archery",
                            "type": ABILITY_TYPE_COMBAT,
                            "description": "Improved accuracy and damage with bows",
                            "level": 1,
                            "max_level": 5
                        },
                        {
                            "name": "Animal Companion",
                            "type": ABILITY_TYPE_PASSIVE,
                            "description": "Summon an animal ally to fight alongside you",
                            "level": 1,
                            "max_level": 3
                        },
                        {
                            "name": "Track",
                            "type": ABILITY_TYPE_SKILL,
                            "description": "Follow tracks and find hidden paths",
                            "level": 1,
                            "max_level": 5
                        }
                    ],
                    "inventory": [ITEM_BOW, ITEM_ARROWS, ITEM_HERBS],
                    "level": 1,
                    "experience": 0,
                    "health": 90,
                    "max_health": 90,
                    "mana": 30,
                    "max_mana": 30,
                    "gold": 45,
                    "location": LOC_FOREST,
                    "quests": [],
                    "achievements": []
                }
            }
        
        def get_character(self, character_id):
            """
            Get character data by ID.
            
            Args:
                character_id (str): The ID of the character to retrieve
                
            Returns:
                dict: Character data or None if not found
            """
            try:
                return self.characters.get(character_id)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting character {character_id}: {e}")
                return None
        
        def select_character(self, character_id):
            """
            Select a character as the player character.
            
            Args:
                character_id (str): The ID of the character to select
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id in self.characters:
                    self.selected_character = character_id
                    persistent.game_state["selected_character"] = character_id
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error selecting character {character_id}: {e}")
                return False
        
        def get_selected_character(self):
            """
            Get the currently selected character data.
            
            Returns:
                dict: Selected character data or None if none selected
            """
            try:
                if self.selected_character:
                    return self.characters.get(self.selected_character)
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting selected character: {e}")
                return None
        
        def update_character_stat(self, character_id, stat_name, value):
            """
            Update a character's stat.
            
            Args:
                character_id (str): The ID of the character
                stat_name (str): The name of the stat to update
                value (int): The new value of the stat
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id in self.characters and stat_name in self.characters[character_id]["stats"]:
                    self.characters[character_id]["stats"][stat_name] = max(0, min(value, MAX_STAT_VALUE))
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error updating stat {stat_name} for character {character_id}: {e}")
                return False
        
        def add_experience(self, character_id, amount):
            """
            Add experience to a character and handle level up.
            
            Args:
                character_id (str): The ID of the character
                amount (int): The amount of experience to add
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id in self.characters:
                    character = self.characters[character_id]
                    character["experience"] += amount
                    
                    # Check for level up
                    exp_needed = character["level"] * 100
                    while character["experience"] >= exp_needed:
                        character["experience"] -= exp_needed
                        character["level"] += 1
                        self._level_up_character(character_id)
                        exp_needed = character["level"] * 100
                    
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error adding experience to character {character_id}: {e}")
                return False
        
        def _level_up_character(self, character_id):
            """
            Handle character level up.
            
            Args:
                character_id (str): The ID of the character
            """
            try:
                character = self.characters[character_id]
                
                # Increase stats based on character type
                if character_id == CHAR_WARRIOR:
                    character["stats"][STAT_STRENGTH] += 2
                    character["stats"][STAT_ENDURANCE] += 2
                    character["max_health"] += 20
                elif character_id == CHAR_MAGE:
                    character["stats"][STAT_INTELLIGENCE] += 2
                    character["max_mana"] += 20
                elif character_id == CHAR_ROGUE:
                    character["stats"][STAT_AGILITY] += 2
                    character["stats"][STAT_LUCK] += 1
                elif character_id == CHAR_CLERIC:
                    character["stats"][STAT_CHARISMA] += 2
                    character["stats"][STAT_INTELLIGENCE] += 1
                    character["max_health"] += 10
                    character["max_mana"] += 10
                elif character_id == CHAR_RANGER:
                    character["stats"][STAT_AGILITY] += 1
                    character["stats"][STAT_STRENGTH] += 1
                    character["stats"][STAT_LUCK] += 1
                
                # Restore health and mana
                character["health"] = character["max_health"]
                character["mana"] = character["max_mana"]
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error leveling up character {character_id}: {e}")
        
        def get_character_abilities(self, character_id):
            """
            Get all abilities for a character.
            
            Args:
                character_id (str): The ID of the character
                
            Returns:
                list: List of character abilities
            """
            try:
                if character_id in self.characters:
                    return self.characters[character_id]["abilities"]
                return []
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting abilities for character {character_id}: {e}")
                return []
        
        def upgrade_ability(self, character_id, ability_name):
            """
            Upgrade a character's ability.
            
            Args:
                character_id (str): The ID of the character
                ability_name (str): The name of the ability to upgrade
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id in self.characters:
                    for ability in self.characters[character_id]["abilities"]:
                        if ability["name"] == ability_name and ability["level"] < ability["max_level"]:
                            ability["level"] += 1
                            return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error upgrading ability {ability_name} for character {character_id}: {e}")
                return False
        
        def set_character_location(self, character_id, location):
            """
            Set a character's location.
            
            Args:
                character_id (str): The ID of the character
                location (str): The new location
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id in self.characters:
                    self.characters[character_id]["location"] = location
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting location for character {character_id}: {e}")
                return False
        
        def get_character_location(self, character_id):
            """
            Get a character's location.
            
            Args:
                character_id (str): The ID of the character
                
            Returns:
                str: Character location or None if not found
            """
            try:
                if character_id in self.characters:
                    return self.characters[character_id]["location"]
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting location for character {character_id}: {e}")
                return None
        
        def validate_character_data(self, character_id):
            """
            Validate character data integrity.
            
            Args:
                character_id (str): The ID of the character to validate
                
            Returns:
                bool: True if valid, False otherwise
            """
            try:
                if character_id not in self.characters:
                    return False
                
                character = self.characters[character_id]
                
                # Check required fields
                required_fields = ["id", "name", "stats", "abilities", "inventory", "level", "experience"]
                for field in required_fields:
                    if field not in character:
                        return False
                
                # Check stats
                for stat_name, value in character["stats"].items():
                    if not isinstance(value, int) or value < 0 or value > MAX_STAT_VALUE:
                        return False
                
                # Check inventory
                if len(character["inventory"]) > MAX_INVENTORY_SLOTS:
                    return False
                
                # Check abilities
                if len(character["abilities"]) > MAX_ABILITIES:
                    return False
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error validating character {character_id}: {e}")
                return False

    # =============================================================================
    # INVENTORY MANAGEMENT SYSTEM
    # =============================================================================
    
    class InventoryManager:
        """
        Manages character inventory operations including adding, removing, and trading items.
        """
        
        def __init__(self):
            """Initialize the inventory manager."""
            self.item_database = self._initialize_item_database()
        
        def _initialize_item_database(self):
            """Initialize the item database with all possible items."""
            # Import constants from config if they exist
            global ITEM_TYPE_WEAPON, ITEM_TYPE_ARMOR, ITEM_TYPE_CONSUMABLE, ITEM_TYPE_MISC, ITEM_TYPE_QUEST
            global RARITY_COMMON, RARITY_UNCOMMON, RARITY_RARE, RARITY_EPIC, RARITY_LEGENDARY
            
            # Check if constants exist, if not create default values
            try:
                ITEM_TYPE_WEAPON
            except NameError:
                ITEM_TYPE_WEAPON = "weapon"
                ITEM_TYPE_ARMOR = "armor"
                ITEM_TYPE_CONSUMABLE = "consumable"
                ITEM_TYPE_MISC = "misc"
                ITEM_TYPE_QUEST = "quest"
                RARITY_COMMON = "common"
                RARITY_UNCOMMON = "uncommon"
                RARITY_RARE = "rare"
                RARITY_EPIC = "epic"
                RARITY_LEGENDARY = "legendary"
                
            return {
                ITEM_STEEL_SWORD: {
                    "name": ITEM_STEEL_SWORD,
                    "type": ITEM_TYPE_WEAPON,
                    "rarity": RARITY_COMMON,
                    "value": 50,
                    "description": "A well-crafted steel sword",
                    "effects": {"damage": 10}
                },
                ITEM_WOODEN_SHIELD: {
                    "name": ITEM_WOODEN_SHIELD,
                    "type": ITEM_TYPE_ARMOR,
                    "rarity": RARITY_COMMON,
                    "value": 30,
                    "description": "A basic wooden shield",
                    "effects": {"defense": 5}
                },
                ITEM_HEALTH_POTION: {
                    "name": ITEM_HEALTH_POTION,
                    "type": ITEM_TYPE_CONSUMABLE,
                    "rarity": RARITY_COMMON,
                    "value": 20,
                    "description": "Restores 50 health points",
                    "effects": {"health_restore": 50}
                },
                ITEM_MAGIC_STAFF: {
                    "name": ITEM_MAGIC_STAFF,
                    "type": ITEM_TYPE_WEAPON,
                    "rarity": RARITY_UNCOMMON,
                    "value": 80,
                    "description": "A staff imbued with magical energy",
                    "effects": {"magic_power": 15}
                },
                ITEM_SPELLBOOK: {
                    "name": ITEM_SPELLBOOK,
                    "type": ITEM_TYPE_MISC,
                    "rarity": RARITY_UNCOMMON,
                    "value": 60,
                    "description": "Contains ancient magical knowledge",
                    "effects": {"intelligence": 2}
                },
                ITEM_MANA_POTION: {
                    "name": ITEM_MANA_POTION,
                    "type": ITEM_TYPE_CONSUMABLE,
                    "rarity": RARITY_COMMON,
                    "value": 25,
                    "description": "Restores 50 mana points",
                    "effects": {"mana_restore": 50}
                },
                ITEM_DAGGER: {
                    "name": ITEM_DAGGER,
                    "type": ITEM_TYPE_WEAPON,
                    "rarity": RARITY_COMMON,
                    "value": 25,
                    "description": "A sharp dagger for close combat",
                    "effects": {"damage": 5, "agility": 1}
                },
                ITEM_LOCKPICKS: {
                    "name": ITEM_LOCKPICKS,
                    "type": ITEM_TYPE_MISC,
                    "rarity": RARITY_COMMON,
                    "value": 15,
                    "description": "Tools for opening locks",
                    "effects": {"lockpick_skill": 10}
                },
                ITEM_SMOKE_BOMB: {
                    "name": ITEM_SMOKE_BOMB,
                    "type": ITEM_TYPE_CONSUMABLE,
                    "rarity": RARITY_UNCOMMON,
                    "value": 30,
                    "description": "Creates a cloud of smoke for escape",
                    "effects": {"escape_chance": 50}
                },
                ITEM_MACE: {
                    "name": ITEM_MACE,
                    "type": ITEM_TYPE_WEAPON,
                    "rarity": RARITY_COMMON,
                    "value": 40,
                    "description": "A heavy mace for crushing blows",
                    "effects": {"damage": 8, "stun_chance": 10}
                },
                ITEM_HOLY_SYMBOL: {
                    "name": ITEM_HOLY_SYMBOL,
                    "type": ITEM_TYPE_MISC,
                    "rarity": RARITY_RARE,
                    "value": 100,
                    "description": "A symbol of divine power",
                    "effects": {"holy_power": 20, "charisma": 3}
                },
                ITEM_HEALING_POTION: {
                    "name": ITEM_HEALING_POTION,
                    "type": ITEM_TYPE_CONSUMABLE,
                    "rarity": RARITY_COMMON,
                    "value": 20,
                    "description": "Restores 50 health points",
                    "effects": {"health_restore": 50}
                },
                ITEM_BOW: {
                    "name": ITEM_BOW,
                    "type": ITEM_TYPE_WEAPON,
                    "rarity": RARITY_UNCOMMON,
                    "value": 60,
                    "description": "A well-crafted wooden bow",
                    "effects": {"ranged_damage": 12}
                },
                ITEM_ARROWS: {
                    "name": ITEM_ARROWS,
                    "type": ITEM_TYPE_MISC,
                    "rarity": RARITY_COMMON,
                    "value": 10,
                    "description": "A quiver of arrows",
                    "effects": {"ammo": 20}
                },
                ITEM_HERBS: {
                    "name": ITEM_HERBS,
                    "type": ITEM_TYPE_MISC,
                    "rarity": RARITY_COMMON,
                    "value": 15,
                    "description": "Medicinal herbs for healing",
                    "effects": {"health_restore": 25}
                }
            }
        
        def add_item(self, character_id, item_name, quantity=1):
            """
            Add an item to a character's inventory.
            
            Args:
                character_id (str): The ID of the character
                item_name (str): The name of the item to add
                quantity (int): The quantity to add (default: 1)
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id not in character_manager.characters:
                    return False
                
                character = character_manager.characters[character_id]
                
                # Check if inventory is full
                if len(character["inventory"]) >= MAX_INVENTORY_SLOTS:
                    return False
                
                # Check if item exists in database
                if item_name not in self.item_database:
                    return False
                
                # Add item to inventory
                for _ in range(quantity):
                    if len(character["inventory"]) < MAX_INVENTORY_SLOTS:
                        character["inventory"].append(item_name)
                    else:
                        break
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error adding item {item_name} to character {character_id}: {e}")
                return False
        
        def remove_item(self, character_id, item_name, quantity=1):
            """
            Remove an item from a character's inventory.
            
            Args:
                character_id (str): The ID of the character
                item_name (str): The name of the item to remove
                quantity (int): The quantity to remove (default: 1)
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id not in character_manager.characters:
                    return False
                
                character = character_manager.characters[character_id]
                
                # Remove item from inventory
                removed = 0
                for _ in range(quantity):
                    if item_name in character["inventory"]:
                        character["inventory"].remove(item_name)
                        removed += 1
                    else:
                        break
                
                return removed > 0
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error removing item {item_name} from character {character_id}: {e}")
                return False
        
        def has_item(self, character_id, item_name):
            """
            Check if a character has a specific item.
            
            Args:
                character_id (str): The ID of the character
                item_name (str): The name of the item to check
                
            Returns:
                bool: True if character has the item, False otherwise
            """
            try:
                if character_id not in character_manager.characters:
                    return False
                
                character = character_manager.characters[character_id]
                return item_name in character["inventory"]
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error checking item {item_name} for character {character_id}: {e}")
                return False
        
        def get_item_count(self, character_id, item_name):
            """
            Get the count of a specific item in a character's inventory.
            
            Args:
                character_id (str): The ID of the character
                item_name (str): The name of the item to count
                
            Returns:
                int: The count of the item
            """
            try:
                if character_id not in character_manager.characters:
                    return 0
                
                character = character_manager.characters[character_id]
                return character["inventory"].count(item_name)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error counting item {item_name} for character {character_id}: {e}")
                return 0
        
        def exchange_items(self, char1_id, char2_id, item1, item2):
            """
            Exchange items between two characters.
            
            Args:
                char1_id (str): The ID of the first character
                char2_id (str): The ID of the second character
                item1 (str): The item from the first character
                item2 (str): The item from the second character
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Check if both characters exist
                if char1_id not in character_manager.characters or char2_id not in character_manager.characters:
                    return False
                
                # Check if both characters have the items
                if not self.has_item(char1_id, item1) or not self.has_item(char2_id, item2):
                    return False
                
                # Remove items from both characters
                if not self.remove_item(char1_id, item1) or not self.remove_item(char2_id, item2):
                    return False
                
                # Add items to the other characters
                if not self.add_item(char1_id, item2) or not self.add_item(char2_id, item1):
                    # Rollback on failure
                    self.add_item(char1_id, item1)
                    self.add_item(char2_id, item2)
                    return False
                
                # Set flag for item trading
                persistent.game_state["flags"][FLAG_TRADED_ITEMS] = True
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error exchanging items between {char1_id} and {char2_id}: {e}")
                return False
        
        def get_item_info(self, item_name):
            """
            Get information about an item.
            
            Args:
                item_name (str): The name of the item
                
            Returns:
                dict: Item information or None if not found
            """
            try:
                return self.item_database.get(item_name)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting item info for {item_name}: {e}")
                return None
        
        def use_item(self, character_id, item_name):
            """
            Use an item from a character's inventory.
            
            Args:
                character_id (str): The ID of the character
                item_name (str): The name of the item to use
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if character_id not in character_manager.characters:
                    return False
                
                character = character_manager.characters[character_id]
                item_info = self.get_item_info(item_name)
                
                if not item_info:
                    return False
                
                # Apply item effects
                for effect, value in item_info["effects"].items():
                    if effect == "health_restore":
                        character["health"] = min(character["health"] + value, character["max_health"])
                    elif effect == "mana_restore":
                        character["mana"] = min(character["mana"] + value, character["max_mana"])
                    # Add more effect types as needed
                
                # Remove the item if it's consumable
                if item_info["type"] == ITEM_TYPE_CONSUMABLE:
                    self.remove_item(character_id, item_name)
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error using item {item_name} for character {character_id}: {e}")
                return False

    # =============================================================================
    # RELATIONSHIP MANAGEMENT SYSTEM
    # =============================================================================
    
    class RelationshipManager:
        """
        Manages character relationships and interactions.
        """
        
        def __init__(self):
            """Initialize the relationship manager."""
            self.relationships = persistent.game_state["relationships"]
        
        def get_relationship(self, char1_id, char2_id):
            """
            Get the relationship level between two characters.
            
            Args:
                char1_id (str): The ID of the first character
                char2_id (str): The ID of the second character
                
            Returns:
                int: Relationship level
            """
            try:
                relationship_key = f"{char1_id}_{char2_id}"
                return self.relationships.get(relationship_key, RELATIONSHIP_STRANGER)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting relationship between {char1_id} and {char2_id}: {e}")
                return RELATIONSHIP_STRANGER
        
        def set_relationship(self, char1_id, char2_id, level):
            """
            Set the relationship level between two characters.
            
            Args:
                char1_id (str): The ID of the first character
                char2_id (str): The ID of the second character
                level (int): The relationship level to set
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                relationship_key = f"{char1_id}_{char2_id}"
                self.relationships[relationship_key] = max(RELATIONSHIP_STRANGER, min(level, RELATIONSHIP_COMPANION))
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting relationship between {char1_id} and {char2_id}: {e}")
                return False
        
        def modify_relationship(self, char1_id, char2_id, modifier):
            """
            Modify the relationship level between two characters.
            
            Args:
                char1_id (str): The ID of the first character
                char2_id (str): The ID of the second character
                modifier (int): The modifier to apply
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                current_level = self.get_relationship(char1_id, char2_id)
                new_level = current_level + modifier
                return self.set_relationship(char1_id, char2_id, new_level)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error modifying relationship between {char1_id} and {char2_id}: {e}")
                return False
        
        def has_met(self, char1_id, char2_id):
            """
            Check if two characters have met.
            
            Args:
                char1_id (str): The ID of the first character
                char2_id (str): The ID of the second character
                
            Returns:
                bool: True if they have met, False otherwise
            """
            try:
                relationship_key = f"{char1_id}_{char2_id}"
                return relationship_key in self.relationships
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error checking if {char1_id} and {char2_id} have met: {e}")
                return False
        
        def get_relationship_description(self, level):
            """
            Get a description of a relationship level.
            
            Args:
                level (int): The relationship level
                
            Returns:
                str: Description of the relationship level
            """
            descriptions = {
                RELATIONSHIP_STRANGER: "Stranger",
                RELATIONSHIP_ACQUAINTANCE: "Acquaintance",
                RELATIONSHIP_FRIEND: "Friend",
                RELATIONSHIP_ALLY: "Ally",
                RELATIONSHIP_COMPANION: "Companion"
            }
            return descriptions.get(level, "Unknown")

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instances of the managers
    character_manager = CharacterManager()
    inventory_manager = InventoryManager()
    relationship_manager = RelationshipManager()