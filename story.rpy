# game/story.rpy

init python:
    # =============================================================================
    # STORY MANAGEMENT SYSTEM
    # =============================================================================
    
    class StoryManager:
        """
        Manages all story content, branches, choices, and narrative flow.
        Handles character-specific stories, quests, and achievements.
        """
        
        def __init__(self):
            """Initialize the story manager with all story data."""
            self.story_data = self._initialize_story_data()
            self.quest_data = self._initialize_quest_data()
            self.achievement_data = self._initialize_achievement_data()
            self.current_chapter = CHAPTER_PROLOGUE
            self.story_flags = persistent.game_state["flags"]
            self.completed_quests = persistent.game_state["completed_quests"]
            self.achievements = persistent.game_state["achievements"]
        
        def _initialize_story_data(self):
            """Initialize all story branches and decision trees."""
            return {
                # Prologue story (common to all characters)
                CHAPTER_PROLOGUE: {
                    "intro": {
                        "text": "Once upon a time, in a world far away, an ancient evil awakened. Five heroes from different walks of life must rise to face the challenge. Each with their own unique skills and stories, they are the last hope for the realm.",
                        "background": BG_BLACK,
                        "music": MUSIC_MAIN_THEME,
                        "next": "character_selection"
                    },
                    "character_selection": {
                        "text": "The time has come to choose your path. Who will you become in this tale of heroism and adventure?",
                        "background": BG_BLACK,
                        "music": MUSIC_MAIN_THEME,
                        "choices": [
                            {
                                "text": "I shall be the Warrior",
                                "character": CHAR_WARRIOR,
                                "next": "warrior_intro"
                            },
                            {
                                "text": "I shall be the Mage",
                                "character": CHAR_MAGE,
                                "next": "mage_intro"
                            },
                            {
                                "text": "I shall be the Rogue",
                                "character": CHAR_ROGUE,
                                "next": "rogue_intro"
                            },
                            {
                                "text": "I shall be the Cleric",
                                "character": CHAR_CLERIC,
                                "next": "cleric_intro"
                            },
                            {
                                "text": "I shall be the Ranger",
                                "character": CHAR_RANGER,
                                "next": "ranger_intro"
                            }
                        ]
                    }
                },
                
                # Chapter 1: The Awakening
                CHAPTER_1: {
                    # Warrior story branches
                    "warrior_intro": {
                        "character": CHAR_WARRIOR,
                        "text": "You are the Warrior, a brave fighter from the Northern Kingdoms. Your journey begins at the gates of the capital, where rumors of strange creatures have been spreading.",
                        "background": BG_CITY,
                        "music": MUSIC_PEACEFUL,
                        "location": LOC_CITY,
                        "choices": [
                            {
                                "text": "Investigate the rumors in the city",
                                "requirements": [],
                                "consequences": {"relationship": {"guard_captain": 1}},
                                "next": "warrior_city_investigation"
                            },
                            {
                                "text": "Head directly to the outskirts where the creatures were seen",
                                "requirements": [],
                                "consequences": {"experience": 10, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "warrior_outskirts"
                            },
                            {
                                "text": "Visit the blacksmith to upgrade your equipment",
                                "requirements": [ITEM_GOLD >= 30],
                                "consequences": {"gold": -30, "items": [{"add": ITEM_STEEL_SWORD_UPGRADED, "remove": ITEM_STEEL_SWORD}]},
                                "next": "warrior_blacksmith"
                            }
                        ]
                    },
                    "warrior_city_investigation": {
                        "character": CHAR_WARRIOR,
                        "text": "You spend the day talking to citizens and guards about the strange creatures. The information you gather paints a disturbing picture of the threat.",
                        "background": BG_CITY,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Follow the lead to the tavern",
                                "requirements": [],
                                "consequences": {"relationship": {"tavern_keeper": 1}, "flags": [FLAG_MET_MAGE]},
                                "next": "warrior_tavern"
                            },
                            {
                                "text": "Check the city archives for historical information",
                                "requirements": [],
                                "consequences": {"intelligence": 1, "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "warrior_archives"
                            },
                            {
                                "text": "Visit the guard captain for official reports",
                                "requirements": [],
                                "consequences": {"relationship": {"guard_captain": 2}, "experience": 15},
                                "next": "warrior_guard_captain"
                            }
                        ]
                    },
                    "warrior_outskirts": {
                        "character": CHAR_WARRIOR,
                        "text": "You travel to the outskirts where the creatures were last seen. The area is eerily quiet, with signs of struggle and destruction everywhere.",
                        "background": BG_FOREST,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Set up camp and wait for nightfall",
                                "requirements": [],
                                "consequences": {"experience": 5, "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "warrior_camp"
                            },
                            {
                                "text": "Explore the nearby forest",
                                "requirements": [],
                                "consequences": {"items": [{"add": ITEM_HERBS}], "flags": [FLAG_FOUND_TREASURE]},
                                "next": "warrior_forest"
                            },
                            {
                                "text": "Follow the tracks leading north",
                                "requirements": [STAT_AGILITY >= 6],
                                "consequences": {"experience": 20, "relationship": {"ranger": 1}},
                                "next": "warrior_tracks"
                            }
                        ]
                    },
                    "warrior_blacksmith": {
                        "character": CHAR_WARRIOR,
                        "text": "You visit the blacksmith to upgrade your equipment. The smithy is filled with the sound of hammering steel and the heat of the forge.",
                        "background": BG_MARKET,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Upgrade your sword",
                                "requirements": [ITEM_GOLD >= 50],
                                "consequences": {"gold": -50, "items": [{"add": ITEM_STEEL_SWORD_UPGRADED, "remove": ITEM_STEEL_SWORD}]},
                                "next": "warrior_sword_upgrade"
                            },
                            {
                                "text": "Get a better shield",
                                "requirements": [ITEM_GOLD >= 40],
                                "consequences": {"gold": -40, "items": [{"add": ITEM_IRON_SHIELD, "remove": ITEM_WOODEN_SHIELD}]},
                                "next": "warrior_shield_upgrade"
                            },
                            {
                                "text": "Ask the blacksmith for information",
                                "requirements": [],
                                "consequences": {"relationship": {"blacksmith": 2}, "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "warrior_blacksmith_info"
                            }
                        ]
                    },
                    
                    # Mage story branches
                    "mage_intro": {
                        "character": CHAR_MAGE,
                        "text": "You are the Mage, a powerful spellcaster from the Academy of Arcane Arts. Your journey begins in your study, where you've sensed a disturbance in the magical energies of the realm.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_MYSTICAL,
                        "location": LOC_TEMPLE,
                        "choices": [
                            {
                                "text": "Consult the ancient tomes in the library",
                                "requirements": [],
                                "consequences": {"intelligence": 1, "experience": 10},
                                "next": "mage_library"
                            },
                            {
                                "text": "Visit the magical observatory",
                                "requirements": [STAT_INTELLIGENCE >= 7],
                                "consequences": {"mana": 20, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "mage_observatory"
                            },
                            {
                                "text": "Seek out other mages for their insights",
                                "requirements": [],
                                "consequences": {"relationship": {"archmage": 1}, "flags": [FLAG_MET_WARRIOR]},
                                "next": "mage_colleagues"
                            }
                        ]
                    },
                    "mage_library": {
                        "character": CHAR_MAGE,
                        "text": "You spend hours researching in the library, poring over ancient texts and magical theories. The knowledge you gain is both enlightening and concerning.",
                        "background": BG_LIBRARY,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Focus on elemental magic texts",
                                "requirements": [],
                                "consequences": {"abilities": [{"upgrade": "Fireball"}], "experience": 15},
                                "next": "mage_elemental"
                            },
                            {
                                "text": "Study ancient prophecies",
                                "requirements": [STAT_INTELLIGENCE >= 8],
                                "consequences": {"flags": [FLAG_COMPLETED_QUEST], "relationship": {"scholar": 2}},
                                "next": "mage_prophecies"
                            },
                            {
                                "text": "Research magical creatures",
                                "requirements": [],
                                "consequences": {"items": [{"add": ITEM_SPELLBOOK_ADVANCED}], "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "mage_creatures"
                            }
                        ]
                    },
                    "mage_observatory": {
                        "character": CHAR_MAGE,
                        "text": "You observe the magical phenomena from the observatory. The patterns in the magical energies reveal a source of great power and danger.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Analyze the magical patterns",
                                "requirements": [STAT_INTELLIGENCE >= 8],
                                "consequences": {"intelligence": 2, "experience": 20},
                                "next": "mage_patterns"
                            },
                            {
                                "text": "Attempt to locate the source",
                                "requirements": [],
                                "consequences": {"mana": -30, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "mage_source"
                            },
                            {
                                "text": "Perform a scrying ritual",
                                "requirements": [ITEM_MANA_POTION >= 1],
                                "consequences": {"items": [{"remove": ITEM_MANA_POTION}], "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "mage_scrying"
                            }
                        ]
                    },
                    "mage_colleagues": {
                        "character": CHAR_MAGE,
                        "text": "You consult with other mages about the disturbance. Their insights and concerns mirror your own, but they offer different perspectives on the situation.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Talk to the elemental specialist",
                                "requirements": [],
                                "consequences": {"abilities": [{"upgrade": "Ice Shard"}], "relationship": {"elementalist": 2}},
                                "next": "mage_elementalist"
                            },
                            {
                                "text": "Visit the divination master",
                                "requirements": [STAT_CHARISMA >= 5],
                                "consequences": {"flags": [FLAG_MET_CLERIC], "experience": 15},
                                "next": "mage_diviner"
                            },
                            {
                                "text": "Discuss with the enchantment professor",
                                "requirements": [],
                                "consequences": {"items": [{"add": ITEM_ENCHANTED_AMULET}], "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "mage_enchanter"
                            }
                        ]
                    },
                    
                    # Rogue story branches
                    "rogue_intro": {
                        "character": CHAR_ROGUE,
                        "text": "You are the Rogue, a cunning thief from the Shadow Guild. Your journey begins in the back alleys of the city, where you've overheard whispers of a great treasure.",
                        "background": BG_CITY,
                        "music": MUSIC_PEACEFUL,
                        "location": LOC_CITY,
                        "choices": [
                            {
                                "text": "Investigate the source of the rumors",
                                "requirements": [],
                                "consequences": {"relationship": {"informant": 1}, "experience": 10},
                                "next": "rogue_rumors"
                            },
                            {
                                "text": "Case the locations mentioned in the rumors",
                                "requirements": [STAT_AGILITY >= 7],
                                "consequences": {"gold": 20, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "rogue_locations"
                            },
                            {
                                "text": "Gather information from the underworld",
                                "requirements": [],
                                "consequences": {"relationship": {"guild_master": 1}, "flags": [FLAG_MET_ROGUE]},
                                "next": "rogue_underworld"
                            }
                        ]
                    },
                    "rogue_rumors": {
                        "character": CHAR_ROGUE,
                        "text": "You investigate the source of the rumors, following whispers and half-truths through the shadowy corners of the city.",
                        "background": BG_CITY,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Follow the nobleman who mentioned the treasure",
                                "requirements": [STAT_AGILITY >= 6],
                                "consequences": {"relationship": {"nobleman": 1}, "gold": 30},
                                "next": "rogue_nobleman"
                            },
                            {
                                "text": "Question the tavern keeper",
                                "requirements": [],
                                "consequences": {"flags": [FLAG_MET_MAGE], "experience": 15},
                                "next": "rogue_tavern_keeper"
                            },
                            {
                                "text": "Track down the merchant who spread the story",
                                "requirements": [],
                                "consequences": {"items": [{"add": ITEM_LOCKPICKS_MASTER}], "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "rogue_merchant"
                            }
                        ]
                    },
                    "rogue_locations": {
                        "character": CHAR_ROGUE,
                        "text": "You case the locations mentioned in the rumors, studying their layouts, security, and potential entry points.",
                        "background": BG_CITY,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Scout the abandoned mansion",
                                "requirements": [STAT_AGILITY >= 8],
                                "consequences": {"gold": 50, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "rogue_mansion"
                            },
                            {
                                "text": "Check the old catacombs",
                                "requirements": [ITEM_LOCKPICKS >= 1],
                                "consequences": {"items": [{"add": ITEM_ANCIENT_RELIC}], "experience": 20},
                                "next": "rogue_catacombs"
                            },
                            {
                                "text": "Survey the ruined temple",
                                "requirements": [],
                                "consequences": {"relationship": {"priest": 1}, "flags": [FLAG_MET_CLERIC]},
                                "next": "rogue_temple"
                            }
                        ]
                    },
                    "rogue_underworld": {
                        "character": CHAR_ROGUE,
                        "text": "You gather information from the criminal underworld, navigating the dangerous network of thieves, smugglers, and informants.",
                        "background": BG_TAVERN,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Visit the Thieves' Guild",
                                "requirements": [],
                                "consequences": {"relationship": {"guild_master": 2}, "abilities": [{"upgrade": "Stealth"}]},
                                "next": "rogue_thieves_guild"
                            },
                            {
                                "text": "Talk to the fence in the market",
                                "requirements": [],
                                "consequences": {"gold": 40, "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "rogue_fence"
                            },
                            {
                                "text": "Meet with the information broker",
                                "requirements": [ITEM_GOLD >= 20],
                                "consequences": {"gold": -20, "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "rogue_broker"
                            }
                        ]
                    },
                    
                    # Cleric story branches
                    "cleric_intro": {
                        "character": CHAR_CLERIC,
                        "text": "You are the Cleric, a devoted servant of the Temple of Light. Your journey begins in the temple halls, where you've received a vision of darkness spreading across the land.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_PEACEFUL,
                        "location": LOC_TEMPLE,
                        "choices": [
                            {
                                "text": "Consult with the high priest",
                                "requirements": [],
                                "consequences": {"relationship": {"high_priest": 2}, "experience": 10},
                                "next": "cleric_high_priest"
                            },
                            {
                                "text": "Perform a divination ritual",
                                "requirements": [STAT_INTELLIGENCE >= 6],
                                "consequences": {"mana": -20, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "cleric_divination"
                            },
                            {
                                "text": "Visit the afflicted areas",
                                "requirements": [],
                                "consequences": {"relationship": {"villagers": 1}, "flags": [FLAG_MET_RANGER]},
                                "next": "cleric_afflicted"
                            }
                        ]
                    },
                    "cleric_high_priest": {
                        "character": CHAR_CLERIC,
                        "text": "You consult with the high priest about your vision. His wisdom and experience provide valuable insights into the nature of the darkness you've foreseen.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Ask about ancient prophecies",
                                "requirements": [STAT_INTELLIGENCE >= 7],
                                "consequences": {"flags": [FLAG_COMPLETED_QUEST], "relationship": {"scholar": 1}},
                                "next": "cleric_prophecies"
                            },
                            {
                                "text": "Request guidance on how to combat the darkness",
                                "requirements": [],
                                "consequences": {"abilities": [{"upgrade": "Turn Undead"}], "experience": 15},
                                "next": "cleric_guidance"
                            },
                            {
                                "text": "Volunteer to lead a mission",
                                "requirements": [STAT_CHARISMA >= 7],
                                "consequences": {"relationship": {"high_priest": 3}, "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "cleric_mission"
                            }
                        ]
                    },
                    "cleric_divination": {
                        "character": CHAR_CLERIC,
                        "text": "You perform a divination ritual to seek more information. The divine insights you receive are both terrifying and enlightening.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Focus on the source of the darkness",
                                "requirements": [STAT_INTELLIGENCE >= 8],
                                "consequences": {"mana": -30, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "cleric_source"
                            },
                            {
                                "text": "Seek information on how to stop it",
                                "requirements": [],
                                "consequences": {"items": [{"add": ITEM_HOLY_WATER}], "experience": 20},
                                "next": "cleric_solution"
                            },
                            {
                                "text": "Look for allies in the fight",
                                "requirements": [STAT_CHARISMA >= 6],
                                "consequences": {"flags": [FLAG_MET_WARRIOR], "relationship": {"paladin": 2}},
                                "next": "cleric_allies"
                            }
                        ]
                    },
                    "cleric_afflicted": {
                        "character": CHAR_CLERIC,
                        "text": "You visit the areas affected by the darkness. The suffering of the people strengthens your resolve to fight against the spreading evil.",
                        "background": BG_CITY,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Heal the sick and injured",
                                "requirements": [ITEM_HEALING_POTION >= 1],
                                "consequences": {"items": [{"remove": ITEM_HEALING_POTION}], "relationship": {"villagers": 3}},
                                "next": "cleric_heal"
                            },
                            {
                                "text": "Investigate the nature of the affliction",
                                "requirements": [STAT_INTELLIGENCE >= 7],
                                "consequences": {"flags": [FLAG_COMPLETED_QUEST], "experience": 15},
                                "next": "cleric_investigate"
                            },
                            {
                                "text": "Gather testimonies from witnesses",
                                "requirements": [],
                                "consequences": {"relationship": {"witnesses": 2}, "flags": [FLAG_DEFEATED_BOSS]},
                                "next": "cleric_testimonies"
                            }
                        ]
                    },
                    
                    # Ranger story branches
                    "ranger_intro": {
                        "character": CHAR_RANGER,
                        "text": "You are the Ranger, a skilled hunter from the Forest of Whispers. Your journey begins at the edge of the forest, where you've noticed strange tracks that don't belong to any known creature.",
                        "background": BG_FOREST,
                        "music": MUSIC_PEACEFUL,
                        "location": LOC_FOREST,
                        "choices": [
                            {
                                "text": "Follow the tracks into the forest",
                                "requirements": [],
                                "consequences": {"experience": 10, "flags": [FLAG_FOUND_TREASURE]},
                                "next": "ranger_tracks"
                            },
                            {
                                "text": "Consult with the forest spirits",
                                "requirements": [STAT_INTELLIGENCE >= 5],
                                "consequences": {"relationship": {"spirits": 2}, "mana": 20},
                                "next": "ranger_spirits"
                            },
                            {
                                "text": "Gather information from nearby settlements",
                                "requirements": [],
                                "consequences": {"relationship": {"villagers": 1}, "flags": [FLAG_MET_CLERIC]},
                                "next": "ranger_villagers"
                            }
                        ]
                    },
                    "ranger_tracks": {
                        "character": CHAR_RANGER,
                        "text": "You follow the strange tracks into the forest. The path leads deeper into territory that even you find unfamiliar and unsettling.",
                        "background": BG_FOREST,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Track during the day",
                                "requirements": [],
                                "consequences": {"experience": 15, "items": [{"add": ITEM_HERBS_RARE}]},
                                "next": "ranger_day_tracking"
                            },
                            {
                                "text": "Track at night",
                                "requirements": [STAT_AGILITY >= 7],
                                "consequences": {"flags": [FLAG_DEFEATED_BOSS], "relationship": {"night_creatures": 1}},
                                "next": "ranger_night_tracking"
                            },
                            {
                                "text": "Set traps along the trail",
                                "requirements": [ITEM_HERBS >= 1],
                                "consequences": {"items": [{"remove": ITEM_HERBS}], "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "ranger_traps"
                            }
                        ]
                    },
                    "ranger_spirits": {
                        "character": CHAR_RANGER,
                        "text": "You consult with the forest spirits about the strange tracks. Their ancient wisdom provides insights into the nature of the creature that made them.",
                        "background": BG_FOREST,
                        "music": MUSIC_MYSTICAL,
                        "choices": [
                            {
                                "text": "Offer herbs to the nature spirits",
                                "requirements": [ITEM_HERBS >= 2],
                                "consequences": {"items": [{"remove": ITEM_HERBS, "quantity": 2}], "relationship": {"spirits": 3}},
                                "next": "ranger_nature_spirits"
                            },
                            {
                                "text": "Commune with the animal spirits",
                                "requirements": [STAT_CHARISMA >= 6],
                                "consequences": {"abilities": [{"upgrade": "Animal Companion"}], "experience": 20},
                                "next": "ranger_animal_spirits"
                            },
                            {
                                "text": "Meditate with the ancient tree spirits",
                                "requirements": [],
                                "consequences": {"flags": [FLAG_FOUND_TREASURE], "mana": 30},
                                "next": "ranger_tree_spirits"
                            }
                        ]
                    },
                    "ranger_villagers": {
                        "character": CHAR_RANGER,
                        "text": "You gather information from nearby settlements. The villagers' accounts confirm your suspicions and provide additional details about the strange occurrences.",
                        "background": BG_CITY,
                        "music": MUSIC_PEACEFUL,
                        "choices": [
                            {
                                "text": "Talk to the village elder",
                                "requirements": [],
                                "consequences": {"relationship": {"elder": 2}, "flags": [FLAG_COMPLETED_QUEST]},
                                "next": "ranger_elder"
                            },
                            {
                                "text": "Question the local hunters",
                                "requirements": [STAT_AGILITY >= 6],
                                "consequences": {"experience": 15, "relationship": {"hunters": 2}},
                                "next": "ranger_hunters"
                            },
                            {
                                "text": "Listen to the children's stories",
                                "requirements": [STAT_CHARISMA >= 5],
                                "consequences": {"flags": [FLAG_DEFEATED_BOSS], "items": [{"add": ITEM_CHILDREN_DOLL}]},
                                "next": "ranger_children"
                            }
                        ]
                    }
                },
                
                # Chapter 2: The Journey (placeholder structure)
                CHAPTER_2: {
                    # Additional story branches for Chapter 2 would go here
                    # This would continue the narrative with more complex choices
                    # and character interactions
                },
                
                # Chapter 3: The Confrontation (placeholder structure)
                CHAPTER_3: {
                    # Final chapter story branches would go here
                    # This would contain the climax and resolution of the story
                },
                
                # Epilogue
                CHAPTER_EPILOGUE: {
                    "ending": {
                        "text": "Your journey has reached its conclusion. The choices you made and the relationships you forged have shaped the fate of the realm.",
                        "background": BG_TEMPLE,
                        "music": MUSIC_VICTORY,
                        "next": "credits"
                    },
                    "credits": {
                        "text": "Thank you for playing Heroes of the Realm!",
                        "background": BG_BLACK,
                        "music": MUSIC_MAIN_THEME,
                        "next": "end"
                    }
                }
            }
        
        def _initialize_quest_data(self):
            """Initialize all quest data."""
            return {
                QUEST_MAIN: {
                    "name": "The Ancient Evil",
                    "description": "Investigate and defeat the ancient evil that threatens the realm.",
                    "type": "main",
                    "chapter": CHAPTER_1,
                    "requirements": [],
                    "rewards": {"experience": 100, "gold": 200, "achievements": [ACHIEVEMENT_COMPLETIONIST]},
                    "stages": [
                        {
                            "name": "Investigate the Disturbance",
                            "description": "Look into the strange occurrences happening around the realm.",
                            "completed": False
                        },
                        {
                            "name": "Gather Allies",
                            "description": "Find other heroes to join your cause.",
                            "completed": False
                        },
                        {
                            "name": "Confront the Evil",
                            "description": "Face the ancient evil in its lair.",
                            "completed": False
                        }
                    ]
                },
                QUEST_SIDE_1: {
                    "name": "The Missing Merchant",
                    "description": "Find the missing merchant and recover his valuable cargo.",
                    "type": "side",
                    "chapter": CHAPTER_1,
                    "requirements": [STAT_AGILITY >= 5],
                    "rewards": {"experience": 50, "gold": 100},
                    "stages": [
                        {
                            "name": "Find the Merchant",
                            "description": "Locate the missing merchant in the city.",
                            "completed": False
                        },
                        {
                            "name": "Recover the Cargo",
                            "description": "Retrieve the merchant's stolen goods.",
                            "completed": False
                        }
                    ]
                },
                QUEST_SIDE_2: {
                    "name": "The Cursed Artifact",
                    "description": "Destroy the cursed artifact that is plaguing the forest.",
                    "type": "side",
                    "chapter": CHAPTER_2,
                    "requirements": [STAT_INTELLIGENCE >= 6],
                    "rewards": {"experience": 75, "items": [ITEM_HOLY_SYMBOL]},
                    "stages": [
                        {
                            "name": "Research the Artifact",
                            "description": "Learn about the artifact's origins and powers.",
                            "completed": False
                        },
                        {
                            "name": "Find the Artifact",
                            "description": "Locate the cursed artifact in the forest.",
                            "completed": False
                        },
                        {
                            "name": "Destroy the Artifact",
                            "description": "Perform the ritual to destroy the artifact.",
                            "completed": False
                        }
                    ]
                },
                QUEST_HIDDEN: {
                    "name": "The Secret of the Ancients",
                    "description": "Uncover the secret knowledge of the ancient civilization.",
                    "type": "hidden",
                    "chapter": CHAPTER_3,
                    "requirements": [STAT_INTELLIGENCE >= 9, STAT_CHARISMA >= 7],
                    "rewards": {"experience": 150, "abilities": ["Ancient Knowledge"], "achievements": [ACHIEVEMENT_TREASURE_HUNTER]},
                    "stages": [
                        {
                            "name": "Find the Ancient Texts",
                            "description": "Discover the hidden texts of the ancient civilization.",
                            "completed": False
                        },
                        {
                            "name": "Decipher the Language",
                            "description": "Translate the ancient texts to understand their meaning.",
                            "completed": False
                        },
                        {
                            "name": "Master the Knowledge",
                            "description": "Learn and master the secret knowledge of the ancients.",
                            "completed": False
                        }
                    ]
                }
            }
        
        def _initialize_achievement_data(self):
            """Initialize all achievement data."""
            return {
                ACHIEVEMENT_FIRST_BLOOD: {
                    "name": "First Blood",
                    "description": "Defeat your first enemy in combat.",
                    "type": "combat",
                    "requirements": {"flags": [FLAG_DEFEATED_BOSS]},
                    "rewards": {"experience": 25, "gold": 50}
                },
                ACHIEVEMENT_TREASURE_HUNTER: {
                    "name": "Treasure Hunter",
                    "description": "Discover 5 hidden treasures throughout your journey.",
                    "type": "exploration",
                    "requirements": {"flags": [FLAG_FOUND_TREASURE], "count": 5},
                    "rewards": {"gold": 100, "items": [ITEM_MAP_TREASURE]}
                },
                ACHIEVEMENT_MASTER_TRADER: {
                    "name": "Master Trader",
                    "description": "Successfully trade items with 3 different characters.",
                    "type": "social",
                    "requirements": {"flags": [FLAG_TRADED_ITEMS], "count": 3},
                    "rewards": {"gold": 150, "relationship": {"merchants": 2}}
                },
                ACHIEVEMENT_FRIENDSHIP: {
                    "name": "Friendship",
                    "description": "Reach maximum relationship level with any character.",
                    "type": "social",
                    "requirements": {"relationship_level": RELATIONSHIP_COMPANION},
                    "rewards": {"experience": 100, "abilities": ["Inspire Allies"]}
                },
                ACHIEVEMENT_COMPLETIONIST: {
                    "name": "Completionist",
                    "description": "Complete all main and side quests.",
                    "type": "quest",
                    "requirements": {"quests_completed": "all"},
                    "rewards": {"experience": 200, "gold": 300, "items": [ITEM_LEGENDARY_WEAPON]}
                }
            }
        
        def get_story_node(self, chapter, node_id):
            """
            Get a story node by chapter and node ID.
            
            Args:
                chapter (str): The chapter identifier
                node_id (str): The node identifier
                
            Returns:
                dict: Story node data or None if not found
            """
            try:
                if chapter in self.story_data and node_id in self.story_data[chapter]:
                    return self.story_data[chapter][node_id]
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting story node {node_id} in chapter {chapter}: {e}")
                return None
        
        def get_current_chapter(self):
            """
            Get the current chapter.
            
            Returns:
                str: Current chapter identifier
            """
            return self.current_chapter
        
        def set_current_chapter(self, chapter):
            """
            Set the current chapter.
            
            Args:
                chapter (str): The chapter identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if chapter in self.story_data:
                    self.current_chapter = chapter
                    persistent.game_state["current_chapter"] = chapter
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting chapter {chapter}: {e}")
                return False
        
        def check_requirements(self, requirements):
            """
            Check if the player meets the given requirements.
            
            Args:
                requirements (list): List of requirements to check
                
            Returns:
                bool: True if all requirements are met, False otherwise
            """
            try:
                if not requirements:
                    return True
                
                selected_char = character_manager.get_selected_character()
                if not selected_char:
                    return False
                
                for req in requirements:
                    # Check stat requirements
                    if isinstance(req, str) and req in [STAT_STRENGTH, STAT_AGILITY, STAT_INTELLIGENCE, STAT_CHARISMA, STAT_ENDURANCE, STAT_LUCK]:
                        if selected_char["stats"][req] < 6:  # Default threshold
                            return False
                    
                    # Check item requirements
                    elif isinstance(req, str) and req.startswith("ITEM_"):
                        item_name = globals()[req]
                        if not inventory_manager.has_item(character_manager.selected_character, item_name):
                            return False
                    
                    # Check gold requirements
                    elif isinstance(req, str) and req.startswith("ITEM_GOLD"):
                        gold_amount = int(req.split("_")[-1])
                        if selected_char["gold"] < gold_amount:
                            return False
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error checking requirements: {e}")
                return False
        
        def apply_consequences(self, consequences):
            """
            Apply the consequences of a choice.
            
            Args:
                consequences (dict): Dictionary of consequences to apply
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not consequences:
                    return True
                
                selected_char = character_manager.get_selected_character()
                if not selected_char:
                    return False
                
                # Apply experience
                if "experience" in consequences:
                    character_manager.add_experience(character_manager.selected_character, consequences["experience"])
                
                # Apply gold changes
                if "gold" in consequences:
                    selected_char["gold"] += consequences["gold"]
                    selected_char["gold"] = max(0, selected_char["gold"])  # Prevent negative gold
                
                # Apply stat changes
                if "stats" in consequences:
                    for stat, change in consequences["stats"].items():
                        character_manager.update_character_stat(character_manager.selected_character, stat, 
                            selected_char["stats"][stat] + change)
                
                # Apply item changes
                if "items" in consequences:
                    for item_change in consequences["items"]:
                        if "add" in item_change:
                            quantity = item_change.get("quantity", 1)
                            inventory_manager.add_item(character_manager.selected_character, item_change["add"], quantity)
                        if "remove" in item_change:
                            quantity = item_change.get("quantity", 1)
                            inventory_manager.remove_item(character_manager.selected_character, item_change["remove"], quantity)
                
                # Apply ability changes
                if "abilities" in consequences:
                    for ability_change in consequences["abilities"]:
                        if "upgrade" in ability_change:
                            character_manager.upgrade_ability(character_manager.selected_character, ability_change["upgrade"])
                
                # Apply relationship changes
                if "relationship" in consequences:
                    for char_id, change in consequences["relationship"].items():
                        relationship_manager.modify_relationship(character_manager.selected_character, char_id, change)
                
                # Apply flags
                if "flags" in consequences:
                    for flag in consequences["flags"]:
                        self.story_flags[flag] = True
                
                # Apply health/mana changes
                if "health" in consequences:
                    selected_char["health"] += consequences["health"]
                    selected_char["health"] = max(0, min(selected_char["health"], selected_char["max_health"]))
                
                if "mana" in consequences:
                    selected_char["mana"] += consequences["mana"]
                    selected_char["mana"] = max(0, min(selected_char["mana"], selected_char["max_mana"]))
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error applying consequences: {e}")
                return False
        
        def get_quest(self, quest_id):
            """
            Get quest data by ID.
            
            Args:
                quest_id (str): The quest identifier
                
            Returns:
                dict: Quest data or None if not found
            """
            try:
                return self.quest_data.get(quest_id)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting quest {quest_id}: {e}")
                return None
        
        def start_quest(self, quest_id):
            """
            Start a quest for the player.
            
            Args:
                quest_id (str): The quest identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                quest = self.get_quest(quest_id)
                if not quest:
                    return False
                
                # Check if player already has this quest
                if quest_id in character_manager.get_selected_character()["quests"]:
                    return False
                
                # Check requirements
                if not self.check_requirements(quest["requirements"]):
                    return False
                
                # Add quest to character
                character_manager.get_selected_character()["quests"].append(quest_id)
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error starting quest {quest_id}: {e}")
                return False
        
        def complete_quest(self, quest_id):
            """
            Complete a quest and apply rewards.
            
            Args:
                quest_id (str): The quest identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                quest = self.get_quest(quest_id)
                if not quest:
                    return False
                
                # Check if player has this quest
                if quest_id not in character_manager.get_selected_character()["quests"]:
                    return False
                
                # Check if all stages are completed
                all_stages_completed = all(stage["completed"] for stage in quest["stages"])
                if not all_stages_completed:
                    return False
                
                # Remove quest from character
                character_manager.get_selected_character()["quests"].remove(quest_id)
                
                # Add to completed quests
                self.completed_quests.append(quest_id)
                
                # Apply rewards
                self.apply_consequences(quest["rewards"])
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error completing quest {quest_id}: {e}")
                return False
        
        def update_quest_stage(self, quest_id, stage_index):
            """
            Update a quest stage as completed.
            
            Args:
                quest_id (str): The quest identifier
                stage_index (int): The index of the stage to update
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                quest = self.get_quest(quest_id)
                if not quest:
                    return False
                
                if stage_index < 0 or stage_index >= len(quest["stages"]):
                    return False
                
                quest["stages"][stage_index]["completed"] = True
                
                # Check if quest is now complete
                if all(stage["completed"] for stage in quest["stages"]):
                    self.complete_quest(quest_id)
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error updating quest stage for {quest_id}: {e}")
                return False
        
        def get_achievement(self, achievement_id):
            """
            Get achievement data by ID.
            
            Args:
                achievement_id (str): The achievement identifier
                
            Returns:
                dict: Achievement data or None if not found
            """
            try:
                return self.achievement_data.get(achievement_id)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting achievement {achievement_id}: {e}")
                return None
        
        def unlock_achievement(self, achievement_id):
            """
            Unlock an achievement for the player.
            
            Args:
                achievement_id (str): The achievement identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                achievement = self.get_achievement(achievement_id)
                if not achievement:
                    return False
                
                # Check if already unlocked
                if achievement_id in self.achievements:
                    return False
                
                # Check requirements
                requirements = achievement.get("requirements", {})
                
                # Check flag requirements
                if "flags" in requirements:
                    for flag in requirements["flags"]:
                        if not self.story_flags.get(flag, False):
                            return False
                
                # Check relationship requirements
                if "relationship_level" in requirements:
                    has_required_relationship = False
                    for char_id in character_manager.characters:
                        if char_id != character_manager.selected_character:
                            relationship_level = relationship_manager.get_relationship(
                                character_manager.selected_character, char_id
                            )
                            if relationship_level >= requirements["relationship_level"]:
                                has_required_relationship = True
                                break
                    if not has_required_relationship:
                        return False
                
                # Check quest completion requirements
                if "quests_completed" in requirements:
                    if requirements["quests_completed"] == "all":
                        if len(self.completed_quests) != len(self.quest_data):
                            return False
                    elif isinstance(requirements["quests_completed"], int):
                        if len(self.completed_quests) < requirements["quests_completed"]:
                            return False
                
                # Unlock achievement
                self.achievements.append(achievement_id)
                
                # Apply rewards
                self.apply_consequences(achievement.get("rewards", {}))
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error unlocking achievement {achievement_id}: {e}")
                return False
        
        def check_achievements(self):
            """
            Check if any achievements should be unlocked based on current game state.
            """
            try:
                for achievement_id in self.achievement_data:
                    if achievement_id not in self.achievements:
                        self.unlock_achievement(achievement_id)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error checking achievements: {e}")
        
        def get_available_quests(self):
            """
            Get list of quests available to the player.
            
            Returns:
                list: List of available quest IDs
            """
            try:
                available_quests = []
                selected_char = character_manager.get_selected_character()
                
                for quest_id, quest in self.quest_data.items():
                    # Check if not already completed
                    if quest_id in self.completed_quests:
                        continue
                    
                    # Check if not already active
                    if quest_id in selected_char["quests"]:
                        continue
                    
                    # Check requirements
                    if self.check_requirements(quest["requirements"]):
                        available_quests.append(quest_id)
                
                return available_quests
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting available quests: {e}")
                return []
        
        def get_active_quests(self):
            """
            Get list of active quests for the player.
            
            Returns:
                list: List of active quest IDs
            """
            try:
                selected_char = character_manager.get_selected_character()
                return selected_char["quests"]
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting active quests: {e}")
                return []
        
        def get_completed_quests(self):
            """
            Get list of completed quests for the player.
            
            Returns:
                list: List of completed quest IDs
            """
            return self.completed_quests
        
        def advance_story(self, next_node):
            """
            Advance the story to the next node.
            
            Args:
                next_node (str): The next story node identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Check if the next node exists in the current chapter
                node = self.get_story_node(self.current_chapter, next_node)
                if not node:
                    # Check if it's a chapter transition
                    for chapter, chapter_data in self.story_data.items():
                        if next_node in chapter_data:
                            self.set_current_chapter(chapter)
                            node = chapter_data[next_node]
                            break
                
                if not node:
                    return False
                
                # Apply any immediate effects
                if "background" in node:
                    renpy.scene(node["background"])
                
                if "music" in node:
                    renpy.music.play(node["music"])
                
                if "location" in node:
                    persistent.game_state["current_location"] = node["location"]
                    character_manager.set_character_location(character_manager.selected_character, node["location"])
                
                # Update game time
                persistent.game_state["game_time"] += 1
                
                # Check for achievements
                self.check_achievements()
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error advancing story to {next_node}: {e}")
                return False
        
        def get_story_choices(self, node_id):
            """
            Get available choices for a story node.
            
            Args:
                node_id (str): The story node identifier
                
            Returns:
                list: List of available choices
            """
            try:
                node = self.get_story_node(self.current_chapter, node_id)
                if not node:
                    return []
                
                choices = node.get("choices", [])
                available_choices = []
                
                for choice in choices:
                    if self.check_requirements(choice.get("requirements", [])):
                        available_choices.append(choice)
                
                return available_choices
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting story choices for {node_id}: {e}")
                return []
        
        def make_choice(self, node_id, choice_index):
            """
            Make a choice in the story.
            
            Args:
                node_id (str): The story node identifier
                choice_index (int): The index of the choice to make
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                choices = self.get_story_choices(node_id)
                if choice_index < 0 or choice_index >= len(choices):
                    return False
                
                choice = choices[choice_index]
                
                # Apply consequences
                self.apply_consequences(choice.get("consequences", {}))
                
                # Advance story
                return self.advance_story(choice.get("next", ""))
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error making choice {choice_index} for node {node_id}: {e}")
                return False

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the story manager
    story_manager = StoryManager()