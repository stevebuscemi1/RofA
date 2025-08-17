# game/save_load.rpy

init python:
    # =============================================================================
    # SAVE AND LOAD MANAGEMENT SYSTEM
    # =============================================================================
    
    class SaveLoadManager:
        """
        Manages game save and load operations with comprehensive state tracking,
        error handling, and validation.
        """
        
        def __init__(self):
            """Initialize the save/load manager."""
            self.save_slots = SAVE_SLOTS
            self.auto_save_enabled = True
            self.auto_save_interval = 300  # 5 minutes in seconds
            self.last_auto_save = 0
            self.save_directory = "saves"
            self.save_metadata = {}
            self.load_save_metadata()
        
        def load_save_metadata(self):
            """Load metadata for all save files."""
            try:
                self.save_metadata = {}
                save_files = renpy.list_savefiles()
                
                for save_file in save_files:
                    try:
                        # Extract slot number from filename
                        slot_match = re.search(r'slot-(\d+)', save_file)
                        if slot_match:
                            slot_number = int(slot_match.group(1))
                            
                            # Load save info
                            save_info = renpy.load_save_info(save_file)
                            if save_info:
                                self.save_metadata[slot_number] = {
                                    "filename": save_file,
                                    "name": save_info.get("name", "Unknown"),
                                    "date": save_info.get("date", "Unknown"),
                                    "time": save_info.get("time", "Unknown"),
                                    "character": save_info.get("extra_info", {}).get("character", "Unknown"),
                                    "chapter": save_info.get("extra_info", {}).get("chapter", "Unknown"),
                                    "game_time": save_info.get("extra_info", {}).get("game_time", 0),
                                    "screenshot": save_info.get("screenshot", None)
                                }
                    except Exception as e:
                        if DEBUG_MODE:
                            print(f"Error loading metadata for {save_file}: {e}")
                
                if DEBUG_MODE:
                    print(f"Loaded metadata for {len(self.save_metadata)} save files")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error loading save metadata: {e}")
                self.save_metadata = {}
        
        def get_save_slots(self):
            """
            Get information about all save slots.
            
            Returns:
                dict: Dictionary containing save slot information
            """
            try:
                slots = {}
                
                for i in range(1, self.save_slots + 1):
                    if i in self.save_metadata:
                        slots[i] = self.save_metadata[i]
                    else:
                        slots[i] = {
                            "empty": True,
                            "slot_number": i
                        }
                
                return slots
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting save slots: {e}")
                return {}
        
        def validate_game_state(self):
            """
            Validate the current game state before saving.
            
            Returns:
                bool: True if state is valid, False otherwise
            """
            try:
                # Check if character is selected
                if not character_manager.selected_character:
                    return False
                
                # Validate character data
                if not character_manager.validate_character_data(character_manager.selected_character):
                    return False
                
                # Check story manager state
                if not story_manager.current_chapter:
                    return False
                
                # Validate persistent data structure
                required_keys = ["selected_character", "relationships", "flags", "achievements", 
                                "current_chapter", "completed_quests", "current_location", "game_time"]
                for key in required_keys:
                    if key not in persistent.game_state:
                        return False
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error validating game state: {e}")
                return False
        
        def prepare_save_data(self):
            """
            Prepare all data for saving.
            
            Returns:
                dict: Complete save data
            """
            try:
                save_data = {
                    "game_state": persistent.game_state,
                    "characters": character_manager.characters,
                    "story_flags": story_manager.story_flags,
                    "completed_quests": story_manager.completed_quests,
                    "achievements": story_manager.achievements,
                    "current_chapter": story_manager.current_chapter,
                    "relationships": persistent.game_state["relationships"],
                    "timestamp": time.time(),
                    "version": "1.0"
                }
                
                return save_data
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error preparing save data: {e}")
                return None
        
        def restore_save_data(self, save_data):
            """
            Restore game state from save data.
            
            Args:
                save_data (dict): The save data to restore
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Restore game state
                if "game_state" in save_data:
                    persistent.game_state = save_data["game_state"]
                
                # Restore characters
                if "characters" in save_data:
                    character_manager.characters = save_data["characters"]
                
                # Restore story data
                if "story_flags" in save_data:
                    story_manager.story_flags = save_data["story_flags"]
                
                if "completed_quests" in save_data:
                    story_manager.completed_quests = save_data["completed_quests"]
                
                if "achievements" in save_data:
                    story_manager.achievements = save_data["achievements"]
                
                if "current_chapter" in save_data:
                    story_manager.current_chapter = save_data["current_chapter"]
                
                if "relationships" in save_data:
                    persistent.game_state["relationships"] = save_data["relationships"]
                
                # Restore character selection
                if persistent.game_state["selected_character"]:
                    character_manager.select_character(persistent.game_state["selected_character"])
                
                # Restore current location
                if persistent.game_state["current_location"]:
                    persistent.game_state["current_location"] = save_data["game_state"]["current_location"]
                
                # Apply restored state
                renpy.scene(persistent.game_state["current_location"])
                
                if DEBUG_MODE:
                    print("Save data restored successfully")
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error restoring save data: {e}")
                return False
        
        def save_game(self, slot_number, save_name=None):
            """
            Save the game to a specific slot.
            
            Args:
                slot_number (int): The slot number to save to
                save_name (str): Optional custom save name
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Validate slot number
                if slot_number < 1 or slot_number > self.save_slots:
                    return False
                
                # Validate game state
                if not self.validate_game_state():
                    if DEBUG_MODE:
                        print("Cannot save: Invalid game state")
                    return False
                
                # Generate save name if not provided
                if not save_name:
                    selected_char = character_manager.get_selected_character()
                    char_name = selected_char["name"] if selected_char else "No Character"
                    save_name = "Slot {0} - {1} - Day {2}".format(
                        slot_number,
                        char_name,
                        persistent.game_state["game_time"] // 24
                    )
                
                # Prepare save data
                save_data = self.prepare_save_data()
                if not save_data:
                    return False
                
                # Create save filename
                filename = f"slot-{slot_number:02d}-save"
                
                # Prepare extra info for save
                extra_info = {
                    "character": character_manager.selected_character,
                    "chapter": story_manager.current_chapter,
                    "game_time": persistent.game_state["game_time"],
                    "save_data": save_data
                }
                
                # Perform the save
                result = renpy.save(filename, extra_info=extra_info)
                
                if result:
                    # Update metadata
                    self.save_metadata[slot_number] = {
                        "filename": filename,
                        "name": save_name,
                        "date": time.strftime("%Y-%m-%d"),
                        "time": time.strftime("%H:%M:%S"),
                        "character": character_manager.selected_character,
                        "chapter": story_manager.current_chapter,
                        "game_time": persistent.game_state["game_time"],
                        "screenshot": renpy.take_screenshot()
                    }
                    
                    # Play success sound
                    renpy.play(SFX_SUCCESS)
                    
                    if DEBUG_MODE:
                        print(f"Game saved to slot {slot_number}")
                    
                    return True
                else:
                    if DEBUG_MODE:
                        print(f"Failed to save to slot {slot_number}")
                    return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error saving game to slot {slot_number}: {e}")
                return False
        
        def load_game(self, slot_number):
            """
            Load a game from a specific slot.
            
            Args:
                slot_number (int): The slot number to load from
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Validate slot number
                if slot_number < 1 or slot_number > self.save_slots:
                    return False
                
                # Check if slot has save data
                if slot_number not in self.save_metadata:
                    return False
                
                filename = self.save_metadata[slot_number]["filename"]
                
                # Load the save file
                load_result = renpy.load(filename)
                
                if load_result:
                    # Get extra info from load
                    extra_info = renpy.get_load_info(filename)
                    if extra_info and "extra_info" in extra_info:
                        save_data = extra_info["extra_info"].get("save_data")
                        if save_data:
                            # Restore save data
                            if self.restore_save_data(save_data):
                                # Play success sound
                                renpy.play(SFX_SUCCESS)
                                
                                if DEBUG_MODE:
                                    print(f"Game loaded from slot {slot_number}")
                                
                                return True
                
                if DEBUG_MODE:
                    print(f"Failed to load from slot {slot_number}")
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error loading game from slot {slot_number}: {e}")
                return False
        
        def delete_save(self, slot_number):
            """
            Delete a save file from a specific slot.
            
            Args:
                slot_number (int): The slot number to delete
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Validate slot number
                if slot_number < 1 or slot_number > self.save_slots:
                    return False
                
                # Check if slot has save data
                if slot_number not in self.save_metadata:
                    return False
                
                filename = self.save_metadata[slot_number]["filename"]
                
                # Delete the save file
                if renpy.unlink_save(filename):
                    # Remove from metadata
                    del self.save_metadata[slot_number]
                    
                    # Play success sound
                    renpy.play(SFX_SUCCESS)
                    
                    if DEBUG_MODE:
                        print(f"Save file deleted from slot {slot_number}")
                    
                    return True
                else:
                    if DEBUG_MODE:
                        print(f"Failed to delete save file from slot {slot_number}")
                    return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error deleting save from slot {slot_number}: {e}")
                return False
        
        def auto_save(self):
            """
            Perform auto-save if enabled and enough time has passed.
            
            Returns:
                bool: True if auto-save was performed, False otherwise
            """
            try:
                if not self.auto_save_enabled:
                    return False
                
                current_time = time.time()
                if current_time - self.last_auto_save < self.auto_save_interval:
                    return False
                
                # Find an empty auto-save slot or overwrite oldest
                auto_save_slot = None
                for i in range(1, 4):  # Use slots 1-3 for auto-save
                    if i not in self.save_metadata or "auto" in self.save_metadata[i].get("name", "").lower():
                        auto_save_slot = i
                        break
                
                if not auto_save_slot:
                    auto_save_slot = 1  # Default to slot 1
                
                # Perform auto-save
                save_name = f"AUTO-SAVE - {time.strftime('%Y-%m-%d %H:%M:%S')}"
                if self.save_game(auto_save_slot, save_name):
                    self.last_auto_save = current_time
                    
                    if DEBUG_MODE:
                        print(f"Auto-save completed in slot {auto_save_slot}")
                    
                    return True
                
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error performing auto-save: {e}")
                return False
        
        def get_save_info(self, slot_number):
            """
            Get detailed information about a save file.
            
            Args:
                slot_number (int): The slot number to get info for
                
            Returns:
                dict: Save file information or None if not found
            """
            try:
                if slot_number in self.save_metadata:
                    return self.save_metadata[slot_number]
                return None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting save info for slot {slot_number}: {e}")
                return None
        
        def export_save(self, slot_number, export_path):
            """
            Export a save file to an external location.
            
            Args:
                slot_number (int): The slot number to export
                export_path (str): The path to export to
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if slot_number not in self.save_metadata:
                    return False
                
                filename = self.save_metadata[slot_number]["filename"]
                
                # Get save file data
                save_data = renpy.load_save_info(filename)
                if not save_data:
                    return False
                
                # Export to file
                with open(export_path, 'w') as f:
                    json.dump(save_data, f, indent=2)
                
                if DEBUG_MODE:
                    print(f"Save exported from slot {slot_number} to {export_path}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error exporting save from slot {slot_number}: {e}")
                return False
        
        def import_save(self, import_path, slot_number):
            """
            Import a save file from an external location.
            
            Args:
                import_path (str): The path to import from
                slot_number (int): The slot number to import to
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                # Load import data
                with open(import_path, 'r') as f:
                    import_data = json.load(f)
                
                # Validate import data
                if not isinstance(import_data, dict):
                    return False
                
                # Create save filename
                filename = f"slot-{slot_number:02d}-save"
                
                # Prepare extra info
                extra_info = {
                    "character": import_data.get("character", "Unknown"),
                    "chapter": import_data.get("chapter", "Unknown"),
                    "game_time": import_data.get("game_time", 0),
                    "imported": True
                }
                
                # Perform the save
                result = renpy.save(filename, extra_info=extra_info)
                
                if result:
                    # Update metadata
                    self.save_metadata[slot_number] = {
                        "filename": filename,
                        "name": f"IMPORTED - {time.strftime('%Y-%m-%d %H:%M:%S')}",
                        "date": time.strftime("%Y-%m-%d"),
                        "time": time.strftime("%H:%M:%S"),
                        "character": import_data.get("character", "Unknown"),
                        "chapter": import_data.get("chapter", "Unknown"),
                        "game_time": import_data.get("game_time", 0),
                        "imported": True
                    }
                    
                    # Reload metadata
                    self.load_save_metadata()
                    
                    if DEBUG_MODE:
                        print(f"Save imported to slot {slot_number}")
                    
                    return True
                
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error importing save to slot {slot_number}: {e}")
                return False
        
        def get_save_statistics(self):
            """
            Get statistics about save files.
            
            Returns:
                dict: Save statistics
            """
            try:
                stats = {
                    "total_saves": len(self.save_metadata),
                    "characters": {},
                    "chapters": {},
                    "total_play_time": 0
                }
                
                for slot_data in self.save_metadata.values():
                    # Count characters
                    char = slot_data.get("character", "Unknown")
                    stats["characters"][char] = stats["characters"].get(char, 0) + 1
                    
                    # Count chapters
                    chapter = slot_data.get("chapter", "Unknown")
                    stats["chapters"][chapter] = stats["chapters"].get(chapter, 0) + 1
                    
                    # Sum play time
                    stats["total_play_time"] += slot_data.get("game_time", 0)
                
                return stats
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error getting save statistics: {e}")
                return {}

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the save/load manager
    save_load_manager = SaveLoadManager()

# =============================================================================
# SAVE AND LOAD SCREENS
# =============================================================================

screen save_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 1000
        ysize 700
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Save Game" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Save slots grid
            grid 3 4:
                spacing UI_SPACING
                xalign 0.5
                
                $ save_slots = save_load_manager.get_save_slots()
                
                for i in range(1, save_load_manager.save_slots + 1):
                    frame:
                        xsize 300
                        ysize 120
                        background Frame(UI_FRAME, 10, 10)
                        
                        if i in save_slots and not save_slots[i].get("empty", True):
                            # Occupied slot
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                yalign 0.5
                                
                                text "Slot {slot}".format(slot=i) size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                text save_slots[i]["name"] size TEXT_SIZE_SMALL
                                text "{date} {time}".format(
                                    date=save_slots[i]["date"],
                                    time=save_slots[i]["time"]
                                ) size TEXT_SIZE_SMALL
                                text "Character: {char}".format(
                                    char=save_slots[i]["character"]
                                ) size TEXT_SIZE_SMALL
                                
                                hbox:
                                    spacing UI_SPACING
                                    xalign 0.5
                                    
                                    textbutton "Overwrite" action [
                                        Function(save_load_manager.save_game, i),
                                        Function(renpy.play, SFX_CLICK)
                                    ] xsize 100
                                    textbutton "Delete" action [
                                        Function(save_load_manager.delete_save, i),
                                        Function(renpy.play, SFX_CLICK)
                                    ] xsize 80
                        else:
                            # Empty slot
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                yalign 0.5
                                
                                text "Slot {slot}".format(slot=i) size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                text "Empty" size TEXT_SIZE_SMALL
                                
                                textbutton "Save" action [
                                    Function(save_load_manager.save_game, i),
                                    Function(renpy.play, SFX_CLICK)
                                ] xsize 100 xalign 0.5
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Auto-Save Now" action [
                    Function(save_load_manager.auto_save),
                    Function(renpy.play, SFX_CLICK)
                ] xsize UI_BUTTON_WIDTH
                textbutton "Back" action Hide("save_screen") xsize UI_BUTTON_WIDTH

screen load_screen():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 1000
        ysize 700
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Load Game" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Save slots grid
            grid 3 4:
                spacing UI_SPACING
                xalign 0.5
                
                $ save_slots = save_load_manager.get_save_slots()
                
                for i in range(1, save_load_manager.save_slots + 1):
                    frame:
                        xsize 300
                        ysize 120
                        background Frame(UI_FRAME, 10, 10)
                        
                        if i in save_slots and not save_slots[i].get("empty", True):
                            # Occupied slot
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                yalign 0.5
                                
                                text "Slot {slot}".format(slot=i) size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                text save_slots[i]["name"] size TEXT_SIZE_SMALL
                                text "{date} {time}".format(
                                    date=save_slots[i]["date"],
                                    time=save_slots[i]["time"]
                                ) size TEXT_SIZE_SMALL
                                text "Character: {char}".format(
                                    char=save_slots[i]["character"]
                                ) size TEXT_SIZE_SMALL
                                
                                hbox:
                                    spacing UI_SPACING
                                    xalign 0.5
                                    
                                    textbutton "Load" action [
                                        Function(save_load_manager.load_game, i),
                                        Function(renpy.play, SFX_CLICK),
                                        Hide("load_screen"),
                                        Jump("start")
                                    ] xsize 100
                                    textbutton "Delete" action [
                                        Function(save_load_manager.delete_save, i),
                                        Function(renpy.play, SFX_CLICK)
                                    ] xsize 80
                        else:
                            # Empty slot
                            vbox:
                                spacing UI_SPACING
                                xalign 0.5
                                yalign 0.5
                                
                                text "Slot {slot}".format(slot=i) size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                text "Empty" size TEXT_SIZE_SMALL
                                text "No save data" size TEXT_SIZE_SMALL
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Refresh" action [
                    Function(save_load_manager.load_save_metadata),
                    Function(renpy.play, SFX_CLICK)
                ] xsize UI_BUTTON_WIDTH
                textbutton "Back" action Hide("load_screen") xsize UI_BUTTON_WIDTH

screen save_statistics():
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
            text "Save Statistics" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Statistics
            $ stats = save_load_manager.get_save_statistics()
            
            frame:
                xsize 700
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Total Saves: {total}".format(total=stats["total_saves"]) size TEXT_SIZE_NORMAL
                    
                    text "Characters:" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    for char, count in stats["characters"].items():
                        text "  {char}: {count} saves".format(char=char, count=count) size TEXT_SIZE_SMALL
                    
                    text "Chapters:" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    for chapter, count in stats["chapters"].items():
                        text "  {chapter}: {count} saves".format(chapter=chapter, count=count) size TEXT_SIZE_SMALL
                    
                    text "Total Play Time: {days} days".format(
                        days=stats["total_play_time"] // 24
                    ) size TEXT_SIZE_NORMAL
            
            # Close button
            textbutton "Close" action Hide("save_statistics") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# AUTO-SAVE HOOKS
# =============================================================================

init python:
    def auto_save_check():
        """Check and perform auto-save at regular intervals."""
        save_load_manager.auto_save()
        return 0.1  # Check every 0.1 seconds
    
    # Register auto-save check
    config.overlay_functions.append(auto_save_check)