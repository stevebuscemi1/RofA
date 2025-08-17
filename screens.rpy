# game/screens.rpy

init python:
    # =============================================================================
    # SCREEN MANAGEMENT SYSTEM
    # =============================================================================
    
    class ScreenManager:
        """
        Manages all game screens and UI elements with proper organization and styling.
        """
        
        def __init__(self):
            """Initialize the screen manager."""
            self.current_screen = None
            self.screen_history = []
            self.ui_theme = self._initialize_ui_theme()
        
        def _initialize_ui_theme(self):
            """Initialize the UI theme with colors, fonts, and styles."""
            return {
                "background_color": "#000000",
                "text_color": "#FFFFFF",
                "button_color": "#4A4A4A",
                "button_hover_color": "#6A6A6A",
                "button_text_color": "#FFFFFF",
                "frame_color": "#2A2A2A",
                "frame_border_color": "#4A4A4A",
                "highlight_color": "#FFFF00",
                "error_color": "#FF0000",
                "success_color": "#00FF00",
                "font": "fonts/DejaVuSans.ttf",
                "font_size": TEXT_SIZE_NORMAL,
                "font_size_large": TEXT_SIZE_LARGE,
                "font_size_small": TEXT_SIZE_SMALL
            }
        
        def show_screen(self, screen_name, *args, **kwargs):
            """
            Show a screen and add it to history.
            
            Args:
                screen_name (str): The name of the screen to show
                *args: Arguments to pass to the screen
                **kwargs: Keyword arguments to pass to the screen
            """
            try:
                self.current_screen = screen_name
                self.screen_history.append(screen_name)
                renpy.show_screen(screen_name, *args, **kwargs)
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error showing screen {screen_name}: {e}")
        
        def hide_screen(self, screen_name):
            """
            Hide a screen.
            
            Args:
                screen_name (str): The name of the screen to hide
            """
            try:
                renpy.hide_screen(screen_name)
                if self.current_screen == screen_name:
                    self.current_screen = None
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error hiding screen {screen_name}: {e}")
        
        def go_back(self):
            """Go back to the previous screen."""
            try:
                if len(self.screen_history) > 1:
                    self.screen_history.pop()  # Remove current screen
                    previous_screen = self.screen_history[-1]
                    self.show_screen(previous_screen)
                    return True
                return False
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error going back: {e}")
                return False
        
        def apply_theme(self):
            """Apply the UI theme to all screens."""
            try:
                # Define styles based on theme
                theme = self.ui_theme
                
                # Text styles
                style.default.font = theme["font"]
                style.default.size = theme["font_size"]
                style.default.color = theme["text_color"]
                
                # Button styles
                style.button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
                style.button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
                style.button.disabled_background = Frame(UI_BUTTON_DISABLED, 10, 10)
                style.button.xsize = UI_BUTTON_WIDTH
                style.button.ysize = UI_BUTTON_HEIGHT
                style.button.text_color = theme["button_text_color"]
                style.button.text_size = theme["font_size"]
                style.button.text_outlines = [(1, "#000000", 0, 0)]
                
                # Frame styles
                style.frame.background = Frame(UI_FRAME, 20, 20)
                style.frame.xmargin = UI_PADDING
                style.frame.ymargin = UI_PADDING
                style.frame.padding = UI_PADDING
                
                # Window styles
                style.window.background = Frame(UI_FRAME, 20, 20)
                style.window.xmargin = UI_PADDING
                style.window.ymargin = UI_PADDING
                style.window.padding = UI_PADDING
                
                return True
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error applying theme: {e}")
                return False

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the screen manager
    screen_manager = ScreenManager()

# =============================================================================
# CHARACTER SELECTION SCREEN
# =============================================================================

screen character_selection():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 1000
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Choose Your Character" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            grid 3 2:
                spacing UI_SPACING
                xalign 0.5
                
                for char_id, char in character_manager.characters.items():
                    frame:
                        xsize 300
                        ysize 200
                        background Frame(UI_FRAME, 10, 10)
                        
                        vbox:
                            spacing UI_SPACING
                            xalign 0.5
                            yalign 0.5
                            
                            # Character image
                            add char["image_small"] size (100, 100) xalign 0.5
                            
                            # Character name
                            text char["name"] size TEXT_SIZE_NORMAL xalign 0.5
                            
                            # Character class preview
                            text "Level {level} {class_name}".format(
                                level=char["level"],
                                class_name=char["name"]
                            ) size TEXT_SIZE_SMALL xalign 0.5
                            
                            # Select button
                            textbutton "Select" action Jump("character_detail_{}".format(char_id)) xalign 0.5

# =============================================================================
# CHARACTER DETAIL SCREEN
# =============================================================================

screen character_detail(char_id):
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 1200
        ysize 700
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Character header
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                # Character image
                add character_manager.characters[char_id]["image_large"] size (200, 200)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    # Character name and level
                    text "{name} - Level {level}".format(
                        name=character_manager.characters[char_id]["name"],
                        level=character_manager.characters[char_id]["level"]
                    ) size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"]
                    
                    # Character bio
                    frame:
                        xsize 600
                        background Frame(UI_FRAME, 10, 10)
                        text character_manager.characters[char_id]["bio"] size TEXT_SIZE_SMALL
            
            # Stats and abilities
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                # Stats section
                frame:
                    xsize 350
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Stats" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for stat_name, stat_value in character_manager.characters[char_id]["stats"].items():
                            hbox:
                                spacing UI_SPACING
                                xsize 300
                                
                                text "{stat}:".format(stat=stat_name.capitalize()) size TEXT_SIZE_SMALL
                                bar value stat_value range MAX_STAT_VALUE xsize 150
                                text "{value}/{max}".format(value=stat_value, max=MAX_STAT_VALUE) size TEXT_SIZE_SMALL
                
                # Abilities section
                frame:
                    xsize 350
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Abilities" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for ability in character_manager.characters[char_id]["abilities"]:
                            frame:
                                xsize 320
                                background Frame(UI_FRAME, 5, 5)
                                
                                vbox:
                                    spacing UI_SPACING
                                    
                                    hbox:
                                        spacing UI_SPACING
                                        
                                        text ability["name"] size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                        text "Level {level}/{max_level}".format(
                                            level=ability["level"],
                                            max_level=ability["max_level"]
                                        ) size TEXT_SIZE_SMALL
                                    
                                    text ability["description"] size TEXT_SIZE_SMALL
                                    
                                    text "Type: {ability_type}".format(
                                        ability_type=ability["type"].capitalize()
                                    ) size TEXT_SIZE_SMALL
            
            # Inventory section
            frame:
                xsize 900
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Inventory" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    grid 5 4:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        for i, item_name in enumerate(character_manager.characters[char_id]["inventory"]):
                            if i < MAX_INVENTORY_SLOTS:
                                frame:
                                    xsize 150
                                    ysize 80
                                    background Frame(UI_FRAME, 5, 5)
                                    
                                    vbox:
                                        spacing UI_SPACING
                                        xalign 0.5
                                        yalign 0.5
                                        
                                        text item_name size TEXT_SIZE_SMALL xalign 0.5
                                        
                                        $ item_info = inventory_manager.get_item_info(item_name)
                                        if item_info:
                                            text "{item_type} - {rarity}".format(
                                                item_type=item_info["type"].capitalize(),
                                                rarity=item_info["rarity"].capitalize()
                                            ) size TEXT_SIZE_SMALL xalign 0.5
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Return to Selection" action Jump("character_selection") xsize UI_BUTTON_WIDTH
                textbutton "Confirm Selection" action Jump("start_adventure_{}".format(char_id)) xsize UI_BUTTON_WIDTH

# =============================================================================
# CHARACTER INFO SCREEN (ACCESSIBLE FROM TOP-LEFT)
# =============================================================================

screen character_info():
    modal True
    zorder 100
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
            text "Character Information" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Character overview
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                # Character image and basic info
                frame:
                    xsize 300
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        add character_manager.get_selected_character()["image_large"] size (200, 200) xalign 0.5
                        
                        text character_manager.get_selected_character()["name"] size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"] xalign 0.5
                        
                        text "Level {level}".format(
                            level=character_manager.get_selected_character()["level"]
                        ) size TEXT_SIZE_SMALL xalign 0.5
                        
                        text "Location: {location}".format(
                            location=character_manager.get_selected_character()["location"].capitalize()
                        ) size TEXT_SIZE_SMALL xalign 0.5
                
                # Detailed info tabs
                frame:
                    xsize 650
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        # Tab buttons
                        hbox:
                            spacing UI_SPACING
                            xalign 0.5
                            
                            textbutton "Stats" action SetScreenVariable("current_tab", "stats") xsize 100
                            textbutton "Abilities" action SetScreenVariable("current_tab", "abilities") xsize 100
                            textbutton "Inventory" action SetScreenVariable("current_tab", "inventory") xsize 100
                            textbutton "Relations" action SetScreenVariable("current_tab", "relations") xsize 100
                        
                        # Tab content
                        if current_tab == "stats":
                            use character_stats_tab()
                        elif current_tab == "abilities":
                            use character_abilities_tab()
                        elif current_tab == "inventory":
                            use character_inventory_tab()
                        elif current_tab == "relations":
                            use character_relations_tab()
            
            # Close button
            textbutton "Close" action Hide("character_info") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# CHARACTER INFO TABS
# =============================================================================

screen character_stats_tab():
    frame:
        xsize 620
        ysize 400
        background Frame(UI_FRAME, 10, 10)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Character Stats" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
            
            for stat_name, stat_value in character_manager.get_selected_character()["stats"].items():
                hbox:
                    spacing UI_SPACING
                    xsize 600
                    
                    text "{stat}:".format(stat=stat_name.capitalize()) size TEXT_SIZE_SMALL
                    bar value stat_value range MAX_STAT_VALUE xsize 300
                    text "{value}/{max}".format(value=stat_value, max=MAX_STAT_VALUE) size TEXT_SIZE_SMALL
            
            # Health and mana bars
            text "Health" size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
            hbox:
                spacing UI_SPACING
                xsize 600
                
                bar value character_manager.get_selected_character()["health"] range character_manager.get_selected_character()["max_health"] xsize 300
                text "{health}/{max_health}".format(
                    health=character_manager.get_selected_character()["health"],
                    max_health=character_manager.get_selected_character()["max_health"]
                ) size TEXT_SIZE_SMALL
            
            text "Mana" size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
            hbox:
                spacing UI_SPACING
                xsize 600
                
                bar value character_manager.get_selected_character()["mana"] range character_manager.get_selected_character()["max_mana"] xsize 300
                text "{mana}/{max_mana}".format(
                    mana=character_manager.get_selected_character()["mana"],
                    max_mana=character_manager.get_selected_character()["max_mana"]
                ) size TEXT_SIZE_SMALL
            
            # Experience
            text "Experience" size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
            hbox:
                spacing UI_SPACING
                xsize 600
                
                bar value character_manager.get_selected_character()["experience"] range (character_manager.get_selected_character()["level"] * 100) xsize 300
                text "{exp}/{needed}".format(
                    exp=character_manager.get_selected_character()["experience"],
                    needed=(character_manager.get_selected_character()["level"] * 100)
                ) size TEXT_SIZE_SMALL

screen character_abilities_tab():
    frame:
        xsize 620
        ysize 400
        background Frame(UI_FRAME, 10, 10)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Character Abilities" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 600
                ysize 350
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for ability in character_manager.get_selected_character()["abilities"]:
                        frame:
                            xsize 580
                            background Frame(UI_FRAME, 5, 5)
                            
                            vbox:
                                spacing UI_SPACING
                                
                                hbox:
                                    spacing UI_SPACING
                                    
                                    text ability["name"] size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                    text "Level {level}/{max_level}".format(
                                        level=ability["level"],
                                        max_level=ability["max_level"]
                                    ) size TEXT_SIZE_SMALL
                                
                                text ability["description"] size TEXT_SIZE_SMALL
                                
                                hbox:
                                    spacing UI_SPACING
                                    
                                    text "Type: {ability_type}".format(
                                        ability_type=ability["type"].capitalize()
                                    ) size TEXT_SIZE_SMALL
                                    
                                    if ability["level"] < ability["max_level"]:
                                        textbutton "Upgrade" action [
                                            Function(character_manager.upgrade_ability, character_manager.selected_character, ability["name"]),
                                            Function(renpy.play, SFX_SUCCESS)
                                        ] xsize 100

screen character_inventory_tab():
    frame:
        xsize 620
        ysize 400
        background Frame(UI_FRAME, 10, 10)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Character Inventory" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
            
            text "Items: {current}/{max}".format(
                current=len(character_manager.get_selected_character()["inventory"]),
                max=MAX_INVENTORY_SLOTS
            ) size TEXT_SIZE_SMALL
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 600
                ysize 320
                
                grid 5 4:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for i, item_name in enumerate(character_manager.get_selected_character()["inventory"]):
                        if i < MAX_INVENTORY_SLOTS:
                            frame:
                                xsize 100
                                ysize 100
                                background Frame(UI_FRAME, 5, 5)
                                
                                vbox:
                                    spacing UI_SPACING
                                    xalign 0.5
                                    yalign 0.5
                                    
                                    text item_name size TEXT_SIZE_SMALL xalign 0.5
                                    
                                    $ item_info = inventory_manager.get_item_info(item_name)
                                    if item_info:
                                        text "{item_type}".format(
                                            item_type=item_info["type"].capitalize()
                                        ) size TEXT_SIZE_SMALL xalign 0.5
                                        
                                        if item_info["type"] == ITEM_TYPE_CONSUMABLE:
                                            textbutton "Use" action [
                                                Function(inventory_manager.use_item, character_manager.selected_character, item_name),
                                                Function(renpy.play, SFX_SUCCESS)
                                            ] xsize 80

screen character_relations_tab():
    frame:
        xsize 620
        ysize 400
        background Frame(UI_FRAME, 10, 10)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Character Relationships" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 600
                ysize 350
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    for char_id, char in character_manager.characters.items():
                        if char_id != character_manager.selected_character:
                            frame:
                                xsize 580
                                background Frame(UI_FRAME, 5, 5)
                                
                                hbox:
                                    spacing UI_SPACING
                                    
                                    add char["image_small"] size (50, 50)
                                    
                                    vbox:
                                        spacing UI_SPACING
                                        
                                        text char["name"] size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                                        
                                        $ relationship_level = relationship_manager.get_relationship(
                                            character_manager.selected_character,
                                            char_id
                                        )
                                        
                                        text relationship_manager.get_relationship_description(relationship_level) size TEXT_SIZE_SMALL
                                        
                                        bar value relationship_level range RELATIONSHIP_COMPANION xsize 200

# =============================================================================
# MAIN GAME SCREEN
# =============================================================================

screen game_screen():
    # Character info button in top-left corner
    frame:
        xalign 0.0
        yalign 0.0
        background None
        
        textbutton "Character Info" action Show("character_info") xsize 150 ysize 40
    
    # Game time display
    frame:
        xalign 1.0
        yalign 0.0
        background None
        
        text "Day {day} - Time: {time}".format(
            day=persistent.game_state["game_time"] // 24,
            time=persistent.game_state["game_time"] % 24
        ) size TEXT_SIZE_SMALL
    
    # Current location display
    frame:
        xalign 0.5
        yalign 0.0
        background None
        
        text "Location: {location}".format(
            location=persistent.game_state["current_location"].capitalize()
        ) size TEXT_SIZE_SMALL

# =============================================================================
# INITIALIZATION
# =============================================================================

init python:
    # Apply UI theme when game starts
    screen_manager.apply_theme()
    
    # Initialize current tab for character info screen
    current_tab = "stats"