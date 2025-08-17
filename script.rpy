# game/script.rpy
# =============================================================================
# MAIN GAME SCRIPT - ENTRY POINT AND INITIALIZATION
# =============================================================================
init python:
    # =============================================================================
    # IMPORTS AND DEPENDENCIES
    # =============================================================================
    
    import time
    import json
    import os
    import sys
    import traceback
    from datetime import datetime
    
    try:
        import psutil
        PSUTIL_AVAILABLE = True
    except ImportError:
        PSUTIL_AVAILABLE = False
    
    # =============================================================================
    # GLOBAL MANAGER INSTANCES
    # =============================================================================
    
    # Initialize managers in dependency order
    try:
        # Configuration manager (no dependencies)
        from config import *
        
        # Utility managers (no dependencies)
        from utility import localization_manager, input_manager, accessibility_manager
        
        # Core managers (depend on config)
        from characters import character_manager, inventory_manager, relationship_manager
        from story import story_manager
        from save_load import save_load_manager
        from audio_visual import audio_visual_manager
        from main_menu import main_menu_manager
        from debug_tools import debug_manager
        
        # Set up logging
        def log_message(message, level="INFO"):
            """Log a message to console and debug manager if available."""
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {level}: {message}"
            print(log_entry)
            if 'debug_manager' in globals():
                debug_manager.log_message(message, level, "INIT")
        
        log_message("Starting game initialization...")
        
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to import managers: {e}")
        print(traceback.format_exc())
        sys.exit(1)
# =============================================================================
# INITIALIZATION FUNCTIONS
# =============================================================================
init python:
    def initialize_game():
        """
        Initialize all game systems in the correct order.
        Returns True if successful, False otherwise.
        """
        try:
            log_message("Initializing game systems...")
            
            # Step 1: Initialize configuration and settings
            log_message("Step 1: Loading configuration...")
            if not hasattr(persistent, 'game_state'):
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
            # Initialize relationships
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
            
            # Step 2: Initialize utility managers
            log_message("Step 2: Initializing utility managers...")
            
            # Load saved preferences
            if "preferred_language" in persistent.game_state:
                localization_manager.set_language(persistent.game_state["preferred_language"])
            
            if "key_bindings" in persistent.game_state["input_settings"]:
                input_manager.key_bindings = persistent.game_state["input_settings"]["key_bindings"]
            
            accessibility_manager.load_accessibility_settings()
            
            # Step 3: Initialize core managers
            log_message("Step 3: Initializing core managers...")
            
            # Validate character data
            all_characters_valid = True
            for char_id in character_manager.characters:
                if not character_manager.validate_character_data(char_id):
                    log_message(f"Warning: Invalid character data for {char_id}", "WARNING")
                    all_characters_valid = False
            
            if not all_characters_valid:
                log_message("Some character data is invalid", "WARNING")
            
            # Load saved character selection
            if persistent.game_state["selected_character"]:
                character_manager.select_character(persistent.game_state["selected_character"])
            
            # Set current chapter
            story_manager.set_current_chapter(persistent.game_state["current_chapter"])
            
            # Initialize save/load metadata
            save_load_manager.load_save_metadata()
            
            # Step 4: Initialize audio/visual systems
            log_message("Step 4: Initializing audio/visual systems...")
            
            # Apply audio settings
            audio_settings = persistent.game_state["audio_settings"]
            audio_visual_manager.set_music_volume(audio_settings["music_volume"])
            audio_visual_manager.set_sound_effects_volume(audio_settings["sound_volume"])
            audio_visual_manager.set_ambient_volume(audio_settings["ambient_volume"])
            audio_visual_manager.set_voice_volume(audio_settings["voice_volume"])
            
            # Apply visual settings
            visual_settings = persistent.game_state["visual_settings"]
            audio_visual_manager.visual_effects_enabled = visual_settings["effects_enabled"]
            audio_visual_manager.transitions_enabled = visual_settings["transitions_enabled"]
            
            # Step 5: Initialize debug systems
            log_message("Step 5: Initializing debug systems...")
            
            if DEBUG_MODE:
                debug_manager.enabled = True
                debug_manager.log_message("Debug mode enabled", "INFO")
                debug_manager.initialize_debug_system()
            
            # Step 6: Register overlay functions
            log_message("Step 6: Registering overlay functions...")
            
            # Clear existing overlay functions
            config.overlay_functions = []
            
            # Register necessary overlay functions
            config.overlay_functions.append(audio_visual_update)
            if DEBUG_MODE:
                config.overlay_functions.append(debug_overlay_update)
            
            # Step 7: Final validation
            log_message("Step 7: Final validation...")
            
            # Check critical systems
            critical_systems_ok = True
            
            if not character_manager.characters:
                log_message("CRITICAL: Character data not loaded", "ERROR")
                critical_systems_ok = False
            
            if not story_manager.story_data:
                log_message("CRITICAL: Story data not loaded", "ERROR")
                critical_systems_ok = False
            
            if critical_systems_ok:
                log_message("Game initialization completed successfully!")
                return True
            else:
                log_message("Game initialization failed - critical systems not loaded", "ERROR")
                return False
                
        except Exception as e:
            error_msg = f"CRITICAL ERROR during initialization: {e}"
            log_message(error_msg, "ERROR")
            log_message(traceback.format_exc(), "ERROR")
            return False
# =============================================================================
# OVERLAY UPDATE FUNCTIONS
# =============================================================================
init python:
    def audio_visual_update():
        """Update audio/visual systems."""
        try:
            # Update performance stats
            if hasattr(audio_visual_manager, 'update_performance_stats'):
                audio_visual_manager.update_performance_stats()
            
            # Process effect queue
            if hasattr(audio_visual_manager, 'process_effect_queue'):
                audio_visual_manager.process_effect_queue()
            
            return 0.016  # ~60 FPS
        except Exception as e:
            log_message(f"Error in audio_visual_update: {e}", "ERROR")
            return 0.1
    
    def debug_overlay_update():
        """Update debug overlays."""
        try:
            if not debug_manager.enabled:
                return 0.1
            
            # Update performance stats
            if hasattr(debug_manager, 'update_performance_stats'):
                debug_manager.update_performance_stats()
            
            # Check watch variables
            if hasattr(debug_manager, 'check_watch_variables'):
                debug_manager.check_watch_variables()
            
            # Show debug overlays
            for overlay in debug_manager.debug_overlays:
                try:
                    overlay["function"]()
                except Exception as e:
                    debug_manager.log_message(f"Error in debug overlay {overlay['name']}: {e}", "ERROR")
            
            return 0.016  # ~60 FPS
        except Exception as e:
            log_message(f"Error in debug_overlay_update: {e}", "ERROR")
            return 0.1
# =============================================================================
# ERROR HANDLING AND RECOVERY
# =============================================================================
init python:
    def show_error_screen(title, message, can_continue=True):
        """Show an error screen to the user."""
        try:
            renpy.show_screen("error_screen", title, message, can_continue)
        except Exception as e:
            log_message(f"Error showing error screen: {e}", "ERROR")
            # Fallback to simple text display
            renpy.say(f"ERROR: {title}\n{message}")
    
    def handle_critical_error(context, error):
        """Handle critical errors that prevent game continuation."""
        error_msg = f"CRITICAL ERROR in {context}: {error}"
        log_message(error_msg, "ERROR")
        log_message(traceback.format_exc(), "ERROR")
        
        # Try to show error screen
        show_error_screen("Critical Error", 
                         f"A critical error occurred in {context}.\n\n{error}\n\nThe game cannot continue.", 
                         can_continue=False)
        
        # Attempt to save debug report
        try:
            if hasattr(debug_manager, 'export_debug_report'):
                report_file = debug_manager.export_debug_report()
                if report_file:
                    renpy.say(f"Debug report saved to: {report_file}")
        except:
            pass
        
        return False

# =============================================================================
# STORY HANDLER FUNCTIONS (moved outside init python block)
# =============================================================================
python early:
    def handle_story_node_setup(node_id):
        """
        Set up a story node and return the necessary data.
        
        Args:
            node_id (str): The ID of the story node to handle
            
        Returns:
            tuple: (node, choices) or (None, None) if error
        """
        try:
            # Get the story node
            node = story_manager.get_story_node(story_manager.current_chapter, node_id)
            if not node:
                show_error_screen("Story Error", f"Story node '{node_id}' not found.")
                return None, None
            
            # Apply background and music if specified
            if "background" in node:
                renpy.scene(node["background"])
            if "music" in node:
                audio_visual_manager.play_music(node["music"], fadein=1.0)
            
            # Update location if specified
            if "location" in node:
                persistent.game_state["current_location"] = node["location"]
                character_manager.set_character_location(character_manager.selected_character, node["location"])
                # Play location audio
                audio_visual_manager.play_location_audio(node["location"])
            
            # Get available choices
            choices = story_manager.get_story_choices(node_id)
            
            # Return the node and choices for processing in Ren'Py script
            return node, choices
            
        except Exception as e:
            error_msg = f"Error handling story node {node_id}: {e}"
            log_message(error_msg, "ERROR")
            log_message(traceback.format_exc(), "ERROR")
            show_error_screen("Story Error", f"An error occurred while processing the story: {error_msg}")
            return None, None

# =============================================================================
# GAME ENTRY POINT
# =============================================================================
label start:
    # Initialize game
    $ initialization_success = initialize_game()
    
    if not initialization_success:
        # Show initialization error
        $ show_error_screen("Initialization Failed",
                        "The game failed to initialize properly.\n\nPlease check the debug log for details.",
                         can_continue=False)
        return
    
    # Play main theme music
    $ audio_visual_manager.play_music(MUSIC_MAIN_THEME, fadein=1.0, loop=True)
    
    # Show splash screen
    scene BG_BLACK
    with None
    
    # Wait for click to show context text
    " "
    
    # Show prologue intro
    $ intro_node = story_manager.get_story_node(CHAPTER_PROLOGUE, "intro")
    if intro_node:
        "[intro_node['text']]"
    else:
        $ show_error_screen("Story Error", "Failed to load story introduction.")
        return
    
    # Wait for click to show character selection
    " "
    
    # Show character selection screen
    call screen character_selection
# =============================================================================
# CHARACTER SELECTION AND DETAIL HANDLERS
# =============================================================================
label character_detail_warrior:
    call screen character_detail(CHAR_WARRIOR)
label character_detail_mage:
    call screen character_detail(CHAR_MAGE)
label character_detail_rogue:
    call screen character_detail(CHAR_ROGUE)
label character_detail_cleric:
    call screen character_detail(CHAR_CLERIC)
label character_detail_ranger:
    call screen character_detail(CHAR_RANGER)
# =============================================================================
# CHARACTER ADVENTURE STARTERS
# =============================================================================
label start_adventure_warrior:
    $ character_manager.select_character(CHAR_WARRIOR)
    $ story_manager.set_current_chapter(CHAPTER_1)
    jump start_adventure
label start_adventure_mage:
    $ character_manager.select_character(CHAR_MAGE)
    $ story_manager.set_current_chapter(CHAPTER_1)
    jump start_adventure
label start_adventure_rogue:
    $ character_manager.select_character(CHAR_ROGUE)
    $ story_manager.set_current_chapter(CHAPTER_1)
    jump start_adventure
label start_adventure_cleric:
    $ character_manager.select_character(CHAR_CLERIC)
    $ story_manager.set_current_chapter(CHAPTER_1)
    jump start_adventure
label start_adventure_ranger:
    $ character_manager.select_character(CHAR_RANGER)
    $ story_manager.set_current_chapter(CHAPTER_1)
    jump start_adventure
# =============================================================================
# MAIN ADVENTURE LABEL
# =============================================================================
label start_adventure:
    # Get character-specific intro
    $ selected_char = character_manager.get_selected_character()
    if not selected_char:
        $ show_error_screen("Character Error", "No character selected. Please return to character selection.")
        jump character_selection
    
    # Show character-specific intro
    if selected_char["id"] == CHAR_WARRIOR:
        $ intro_node = story_manager.get_story_node(CHAPTER_1, "warrior_intro")
    elif selected_char["id"] == CHAR_MAGE:
        $ intro_node = story_manager.get_story_node(CHAPTER_1, "mage_intro")
    elif selected_char["id"] == CHAR_ROGUE:
        $ intro_node = story_manager.get_story_node(CHAPTER_1, "rogue_intro")
    elif selected_char["id"] == CHAR_CLERIC:
        $ intro_node = story_manager.get_story_node(CHAPTER_1, "cleric_intro")
    elif selected_char["id"] == CHAR_RANGER:
        $ intro_node = story_manager.get_story_node(CHAPTER_1, "ranger_intro")
    
    if not intro_node:
        $ show_error_screen("Story Error", f"Failed to load story intro for {selected_char['name']}.")
        return
    
    # Apply background and music
    if "background" in intro_node:
        scene intro_node["background"]
    if "music" in intro_node:
        $ audio_visual_manager.play_music(intro_node["music"], fadein=1.0)
    
    # Show intro text
    "[intro_node['text']]"
    
    # Start the story node
    if selected_char["id"] == CHAR_WARRIOR:
        jump story_node_warrior_intro
    elif selected_char["id"] == CHAR_MAGE:
        jump story_node_mage_intro
    elif selected_char["id"] == CHAR_ROGUE:
        jump story_node_rogue_intro
    elif selected_char["id"] == CHAR_CLERIC:
        jump story_node_cleric_intro
    elif selected_char["id"] == CHAR_RANGER:
        jump story_node_ranger_intro
# =============================================================================
# STORY NODE HANDLERS
# =============================================================================
# Warrior story nodes
label story_node_warrior_intro:
    call handle_story_node("warrior_intro")
label story_node_warrior_city_investigation:
    call handle_story_node("warrior_city_investigation")
label story_node_warrior_outskirts:
    call handle_story_node("warrior_outskirts")
label story_node_warrior_blacksmith:
    call handle_story_node("warrior_blacksmith")
label story_node_warrior_tavern:
    call handle_story_node("warrior_tavern")
label story_node_warrior_archives:
    call handle_story_node("warrior_archives")
label story_node_warrior_guard_captain:
    call handle_story_node("warrior_guard_captain")
label story_node_warrior_camp:
    call handle_story_node("warrior_camp")
label story_node_warrior_forest:
    call handle_story_node("warrior_forest")
label story_node_warrior_tracks:
    call handle_story_node("warrior_tracks")
label story_node_warrior_sword_upgrade:
    call handle_story_node("warrior_sword_upgrade")
label story_node_warrior_shield_upgrade:
    call handle_story_node("warrior_shield_upgrade")
label story_node_warrior_blacksmith_info:
    call handle_story_node("warrior_blacksmith_info")
# Mage story nodes
label story_node_mage_intro:
    call handle_story_node("mage_intro")
label story_node_mage_library:
    call handle_story_node("mage_library")
label story_node_mage_observatory:
    call handle_story_node("mage_observatory")
label story_node_mage_colleagues:
    call handle_story_node("mage_colleagues")
label story_node_mage_elemental:
    call handle_story_node("mage_elemental")
label story_node_mage_prophecies:
    call handle_story_node("mage_prophecies")
label story_node_mage_creatures:
    call handle_story_node("mage_creatures")
label story_node_mage_patterns:
    call handle_story_node("mage_patterns")
label story_node_mage_source:
    call handle_story_node("mage_source")
label story_node_mage_scrying:
    call handle_story_node("mage_scrying")
label story_node_mage_elementalist:
    call handle_story_node("mage_elementalist")
label story_node_mage_diviner:
    call handle_story_node("mage_diviner")
label story_node_mage_enchanter:
    call handle_story_node("mage_enchanter")
# Rogue story nodes
label story_node_rogue_intro:
    call handle_story_node("rogue_intro")
label story_node_rogue_rumors:
    call handle_story_node("rogue_rumors")
label story_node_rogue_locations:
    call handle_story_node("rogue_locations")
label story_node_rogue_underworld:
    call handle_story_node("rogue_underworld")
label story_node_rogue_nobleman:
    call handle_story_node("rogue_nobleman")
label story_node_rogue_tavern_keeper:
    call handle_story_node("rogue_tavern_keeper")
label story_node_rogue_merchant:
    call handle_story_node("rogue_merchant")
label story_node_rogue_mansion:
    call handle_story_node("rogue_mansion")
label story_node_rogue_catacombs:
    call handle_story_node("rogue_catacombs")
label story_node_rogue_temple:
    call handle_story_node("rogue_temple")
label story_node_rogue_thieves_guild:
    call handle_story_node("rogue_thieves_guild")
label story_node_rogue_fence:
    call handle_story_node("rogue_fence")
label story_node_rogue_broker:
    call handle_story_node("rogue_broker")
# Cleric story nodes
label story_node_cleric_intro:
    call handle_story_node("cleric_intro")
label story_node_cleric_high_priest:
    call handle_story_node("cleric_high_priest")
label story_node_cleric_divination:
    call handle_story_node("cleric_divination")
label story_node_cleric_afflicted:
    call handle_story_node("cleric_afflicted")
label story_node_cleric_prophecies:
    call handle_story_node("cleric_prophecies")
label story_node_cleric_guidance:
    call handle_story_node("cleric_guidance")
label story_node_cleric_mission:
    call handle_story_node("cleric_mission")
label story_node_cleric_source:
    call handle_story_node("cleric_source")
label story_node_cleric_solution:
    call handle_story_node("cleric_solution")
label story_node_cleric_allies:
    call handle_story_node("cleric_allies")
label story_node_cleric_heal:
    call handle_story_node("cleric_heal")
label story_node_cleric_investigate:
    call handle_story_node("cleric_investigate")
label story_node_cleric_testimonies:
    call handle_story_node("cleric_testimonies")
# Ranger story nodes
label story_node_ranger_intro:
    call handle_story_node("ranger_intro")
label story_node_ranger_tracks:
    call handle_story_node("ranger_tracks")
label story_node_ranger_spirits:
    call handle_story_node("ranger_spirits")
label story_node_ranger_villagers:
    call handle_story_node("ranger_villagers")
label story_node_ranger_day_tracking:
    call handle_story_node("ranger_day_tracking")
label story_node_ranger_night_tracking:
    call handle_story_node("ranger_night_tracking")
label story_node_ranger_traps:
    call handle_story_node("ranger_traps")
label story_node_ranger_nature_spirits:
    call handle_story_node("ranger_nature_spirits")
label story_node_ranger_animal_spirits:
    call handle_story_node("ranger_animal_spirits")
label story_node_ranger_tree_spirits:
    call handle_story_node("ranger_tree_spirits")
label story_node_ranger_elder:
    call handle_story_node("ranger_elder")
label story_node_ranger_hunters:
    call handle_story_node("ranger_hunters")
label story_node_ranger_children:
    call handle_story_node("ranger_children")
# =============================================================================
# STORY HANDLER LABEL (moved outside init python block)
# =============================================================================
label handle_story_node(node_id):
    $ node, choices = handle_story_node_setup(node_id)
    if node is None:
        return
    
    # Show the node text
    "[node['text']]"
    
    if choices:
        # Build menu choices dynamically
        $ menu_choices = []
        $ i = 0
        while i < len(choices):
            $ menu_choices.append((choices[i]["text"], i))
            $ i += 1
        
        # Show choices menu
        if len(menu_choices) == 1:
            $ choice_text, choice_value = menu_choices[0]
            menu:
                "[choice_text]":
                    $ result = choices[choice_value]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
        elif len(menu_choices) == 2:
            $ choice_text_1, choice_value_1 = menu_choices[0]
            $ choice_text_2, choice_value_2 = menu_choices[1]
            menu:
                "[choice_text_1]":
                    $ result = choices[choice_value_1]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value_1].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
                "[choice_text_2]":
                    $ result = choices[choice_value_2]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value_2].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
        elif len(menu_choices) == 3:
            $ choice_text_1, choice_value_1 = menu_choices[0]
            $ choice_text_2, choice_value_2 = menu_choices[1]
            $ choice_text_3, choice_value_3 = menu_choices[2]
            menu:
                "[choice_text_1]":
                    $ result = choices[choice_value_1]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value_1].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
                "[choice_text_2]":
                    $ result = choices[choice_value_2]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value_2].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
                "[choice_text_3]":
                    $ result = choices[choice_value_3]["id"]
                    $ success = story_manager.make_choice(node_id, result)
                    if not success:
                        $ show_error_screen("Story Error", "Failed to process story choice.")
                    $ next_node = choices[choice_value_3].get("next", "")
                    if next_node:
                        jump expression "story_node_" + next_node
                    else:
                        jump end
        else:
            # Handle more than 3 choices
            $ current_node_id = node_id
            jump handle_many_choices
        
    else:
        # No choices, advance to next node if specified
        $ next_node = node.get("next", "")
        if next_node:
            $ story_manager.advance_story(next_node)
            if next_node == "end":
                jump end
            else:
                jump expression "story_node_" + next_node
        else:
            # End of story branch
            jump end
# =============================================================================
# CHARACTER MEETING AND INTERACTION HANDLERS
# =============================================================================
label character_meeting_example:
    "During your journey, you meet another traveler."
    
    $ selected_char = character_manager.get_selected_character()
    
    if selected_char["id"] == CHAR_WARRIOR:
        "You meet a Mage who is also investigating the strange occurrences."
        
        menu:
            "Offer to trade your Health Potion for a Mana Potion":
                "The Mage agrees to the trade."
                $ success = inventory_manager.exchange_items(CHAR_WARRIOR, CHAR_MAGE, ITEM_HEALTH_POTION, ITEM_MANA_POTION)
                if success:
                    "You now have a Mana Potion, and the Mage has a Health Potion."
                    $ relationship_manager.modify_relationship(CHAR_WARRIOR, CHAR_MAGE, 1)
                    $ story_manager.story_flags[FLAG_TRADED_ITEMS] = True
                    $ story_manager.check_achievements()
                else:
                    $ show_error_screen("Trade Error", "Failed to complete the trade.")
            "Ask to travel together":
                "The Mage agrees to join you on your journey."
                $ relationship_manager.modify_relationship(CHAR_WARRIOR, CHAR_MAGE, 2)
                $ story_manager.story_flags[FLAG_MET_MAGE] = True
            "Part ways":
                "You decide to continue your journey alone."
    
    elif selected_char["id"] == CHAR_MAGE:
        "You meet a Warrior who is also investigating the strange occurrences."
        
        menu:
            "Offer to trade your Mana Potion for a Health Potion":
                "The Warrior agrees to the trade."
                $ success = inventory_manager.exchange_items(CHAR_MAGE, CHAR_WARRIOR, ITEM_MANA_POTION, ITEM_HEALTH_POTION)
                if success:
                    "You now have a Health Potion, and the Warrior has a Mana Potion."
                    $ relationship_manager.modify_relationship(CHAR_MAGE, CHAR_WARRIOR, 1)
                    $ story_manager.story_flags[FLAG_TRADED_ITEMS] = True
                    $ story_manager.check_achievements()
                else:
                    $ show_error_screen("Trade Error", "Failed to complete the trade.")
            "Ask to travel together":
                "The Warrior agrees to join you on your journey."
                $ relationship_manager.modify_relationship(CHAR_MAGE, CHAR_WARRIOR, 2)
                $ story_manager.story_flags[FLAG_MET_WARRIOR] = True
            "Part ways":
                "You decide to continue your journey alone."
# =============================================================================
    # SAVE AND LOAD HANDLERS
# =============================================================================
# =============================================================================
    # END GAME
# =============================================================================
label end:
    $ epilogue_node = None
    $ selected_char = None
    $ credits_node = None
    $ completion_achievement = False
    
    python:
        try:
            # Get epilogue node
            epilogue_node = story_manager.get_story_node(CHAPTER_EPILOGUE, "ending")
            
            # Get selected character
            selected_char = character_manager.get_selected_character()
            
            # Get credits node
            credits_node = story_manager.get_story_node(CHAPTER_EPILOGUE, "credits")
            
            # Check for completion achievement
            if selected_char and len(story_manager.completed_quests) == len(story_manager.quest_data):
                completion_achievement = True
                story_manager.unlock_achievement(ACHIEVEMENT_COMPLETIONIST)
                
        except Exception as e:
            show_error_screen("End Game Error", f"An error occurred during the end game sequence: {e}")
            renpy.jump("start")
    
    # Show epilogue
    if epilogue_node:
        if "background" in epilogue_node:
            scene epilogue_node["background"]
        if "music" in epilogue_node:
            $ audio_visual_manager.play_music(epilogue_node["music"])
        "[epilogue_node['text']]"
    
    # Show final statistics
    if selected_char:
        "Final Statistics:"
        "Character: [selected_char['name']]"
        "Level: [selected_char['level']]"
        "Experience: [selected_char['experience']]"
        "Completed Quests: [len(story_manager.completed_quests)]"
        "Achievements Unlocked: [len(story_manager.achievements)]"
        "Game Time: [persistent.game_state['game_time'] // 24] days"
    
    # Show credits
    if credits_node:
        "[credits_node['text']]"
    
    # Return to main menu
    return
# =============================================================================
    # QUIT HANDLER
# =============================================================================
label quit_game:
    python:
        try:
            # Show confirmation dialog
            renpy.call_screen("confirm_quit")
        except Exception as e:
            show_error_screen("Quit Error", f"An error occurred while quitting: {e}")
            renpy.jump("start")
    return