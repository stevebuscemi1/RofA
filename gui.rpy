# game/gui.rpy

init python:
    try:
        from config import *
        from utility import localization_manager
    except ImportError as e:
        print(f"Error importing modules: {e}")
    
    # Initialize accessibility_manager if it doesn't exist
    try:
        accessibility_manager
    except NameError:
        class AccessibilityManager:
            def __init__(self):
                self.text_size_multiplier = 1.0
                self.high_contrast_mode = False
                self.color_blind_mode = "none"
                self.screen_reader_enabled = False
                self.subtitles_enabled = True
                self.reduced_motion = False
                
            def toggle_high_contrast(self):
                self.high_contrast_mode = not self.high_contrast_mode
                
            def set_color_blind_mode(self, mode):
                self.color_blind_mode = mode
                
            def toggle_screen_reader(self):
                self.screen_reader_enabled = not self.screen_reader_enabled
                
            def toggle_subtitles(self):
                self.subtitles_enabled = not self.subtitles_enabled
                
            def toggle_reduced_motion(self):
                self.reduced_motion = not self.reduced_motion
        
        accessibility_manager = AccessibilityManager()
    
    # Initialize mouse sensitivity if not already set
    if not hasattr(persistent, "mouse_sensitivity"):
        persistent.mouse_sensitivity = 1.0
    
    # Initialize controller preference if not already set
    if not hasattr(persistent, "controller_enabled"):
        persistent.controller_enabled = False
    
    # =============================================================================
    # STYLE DEFINITIONS
    # =============================================================================
    
    # Define custom styles with appropriate parent styles
    style.gm_root = Style(style.default)
    style.gm_frame = Style(style.frame)
    style.gm_button = Style(style.button)
    style.gm_button_text = Style(style.button_text)
    style.gm_label = Style(style.label)
    style.gm_input = Style(style.input)
    style.gm_bar = Style(style.bar)
    style.gm_vbar = Style(style.vbar)
    style.gm_scrollbar = Style(style.scrollbar)
    style.gm_slider = Style(style.slider)
    style.gm_viewport = Style(style.viewport)
    style.gm_tooltip = Style(style.default)
    style.gm_tooltip_text = Style(style.default)
    
    # Screen styles
    style.screen_frame = Style(style.frame)
    style.screen_title = Style(style.label)
    style.screen_text = Style(style.default)
    style.screen_button = Style(style.button)
    style.screen_button_text = Style(style.button_text)
    
    # Character selection styles
    style.char_select_frame = Style(style.frame)
    style.char_select_name = Style(style.label)
    style.char_select_class = Style(style.label)
    
    # Character info styles
    style.char_info_frame = Style(style.frame)
    style.char_info_name = Style(style.label)
    style.char_info_value = Style(style.label)
    
    # Inventory styles
    style.inventory_slot = Style(style.frame)
    style.inventory_item = Style(style.label)
    style.inventory_count = Style(style.label)
    
    # Dialogue styles
    style.dialogue_window = Style(style.window)
    style.dialogue_text = Style(style.say_dialogue)
    style.dialogue_name = Style(style.say_label)
    
    # Choice styles
    style.choice_frame = Style(style.frame)
    style.choice_text = Style(style.button_text)
    
    # Menu styles
    style.menu_frame = Style(style.frame)
    style.menu_title = Style(style.label)
    style.menu_item_frame = Style(style.frame)
    style.menu_item_text = Style(style.button_text)
    
    # Quick menu styles
    style.quick_menu_frame = Style(style.frame)
    style.quick_button = Style(style.button)
    style.quick_button_text = Style(style.button_text)
    
    # Tooltip styles
    style.tooltip_frame = Style(style.frame)
    style.tooltip_text = Style(style.label)
    
    # Notification styles
    style.notification_frame = Style(style.frame)
    style.notification_text = Style(style.label)
    
    # Loading screen styles
    style.loading_frame = Style(style.frame)
    style.loading_text = Style(style.label)
    style.loading_bar = Style(style.bar)
    
    # Message styles
    style.error_frame = Style(style.frame)
    style.error_text = Style(style.label)
    style.success_frame = Style(style.frame)
    style.success_text = Style(style.label)
    style.warning_frame = Style(style.frame)
    style.warning_text = Style(style.label)
    style.info_frame = Style(style.frame)
    style.info_text = Style(style.label)

# Update the style definitions to use accessibility settings
init python:
    # Apply text size multiplier from accessibility settings
    if hasattr(accessibility_manager, 'text_size_multiplier'):
        text_size_multiplier = accessibility_manager.text_size_multiplier
        style.default.size = int(TEXT_SIZE_NORMAL * text_size_multiplier)
    
    # Apply high contrast mode if enabled
    if hasattr(accessibility_manager, 'high_contrast_mode') and accessibility_manager.high_contrast_mode:
        style.default.color = "#FFFFFF"
        style.window.background = "#000000"
        style.frame.background = "#000000"
        style.button.background = "#FFFFFF"
        style.button.text_color = "#000000"
        style.button.hover_color = "#000000"
        style.button.text_hover_color = "#FFFFFF"
        style.button.disabled_background = "#808080"
        style.button.disabled_text_color = "#FFFFFF"
    
    # Custom GUI elements
    style.gm_root.background = "#000000"
    style.gm_root.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    style.gm_frame.background = Frame(UI_FRAME, 20, 20)
    style.gm_frame.padding = UI_PADDING
    style.gm_frame.margin = UI_PADDING
    style.gm_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.gm_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.gm_button.insensitive_background = Frame(UI_BUTTON_DISABLED, 10, 10)
    style.gm_button.size_group = "gm_button"
    style.gm_button.xsize = UI_BUTTON_WIDTH
    style.gm_button.ysize = UI_BUTTON_HEIGHT
    style.gm_button_text.font = "fonts/DejaVuSans.ttf"
    style.gm_button_text.size = TEXT_SIZE_NORMAL
    style.gm_button_text.color = TEXT_COLOR_NORMAL
    style.gm_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.gm_button_text.insensitive_color = TEXT_COLOR_DISABLED
    style.gm_label.font = "fonts/DejaVuSans.ttf"
    style.gm_label.size = TEXT_SIZE_NORMAL
    style.gm_label.color = TEXT_COLOR_NORMAL
    style.gm_label.outlines = [(1, "#000000", 0, 0)]
    style.gm_label.xalign = 0.5
    style.gm_label.yalign = 0.5
    style.gm_input.background = Frame(UI_FRAME, 10, 10)
    style.gm_input.padding = 5
    style.gm_input.margin = 5
    style.gm_input.xsize = 400
    style.gm_input.ysize = 30
    style.gm_input.color = TEXT_COLOR_NORMAL
    style.gm_input.caret = TEXT_COLOR_HIGHLIGHT
    style.gm_input.selected_color = TEXT_COLOR_HIGHLIGHT
    style.gm_input.insensitive_color = TEXT_COLOR_DISABLED
    style.gm_bar.xmaximum = 200
    style.gm_bar.ymaximum = 20
    style.gm_bar.left_bar = Frame("images/ui/bar_left.png", 10, 10)
    style.gm_bar.right_bar = Frame("images/ui/bar_right.png", 10, 10)
    style.gm_bar.thumb = Frame("images/ui/bar_thumb.png", 10, 10)
    style.gm_bar.thumb_offset = 5
    style.gm_bar.thumb_shadow = None
    style.gm_vbar.xmaximum = 20
    style.gm_vbar.ymaximum = 200
    style.gm_vbar.top_bar = Frame("images/ui/bar_top.png", 10, 10)
    style.gm_vbar.bottom_bar = Frame("images/ui/bar_bottom.png", 10, 10)
    style.gm_vbar.thumb = Frame("images/ui/bar_thumb.png", 10, 10)
    style.gm_vbar.thumb_offset = 5
    style.gm_vbar.thumb_shadow = None
    style.gm_scrollbar.xmaximum = 20
    style.gm_scrollbar.ymaximum = 200
    style.gm_scrollbar.base_bar = Frame("images/ui/scrollbar_base.png", 10, 10)
    style.gm_scrollbar.thumb = Frame("images/ui/scrollbar_thumb.png", 10, 10)
    style.gm_scrollbar.thumb_offset = 5
    style.gm_scrollbar.thumb_shadow = None
    style.gm_slider.xmaximum = 200
    style.gm_slider.ymaximum = 30
    style.gm_slider.base_bar = Frame("images/ui/slider_base.png", 10, 10)
    style.gm_slider.thumb = Frame("images/ui/slider_thumb.png", 10, 10)
    style.gm_slider.thumb_offset = 5
    style.gm_slider.thumb_shadow = None
    style.gm_viewport.background = "#000000"
    style.gm_viewport.xsize = 800
    style.gm_viewport.ysize = 600
    style.gm_viewport.clipping = True
    
    # Tooltip styles
    style.gm_tooltip.background = Frame(UI_FRAME, 10, 10)
    style.gm_tooltip.padding = 5
    style.gm_tooltip.margin = 5
    style.gm_tooltip.xalign = 0.5
    style.gm_tooltip.yalign = 0.0
    style.gm_tooltip_text.font = "fonts/DejaVuSans.ttf"
    style.gm_tooltip_text.size = TEXT_SIZE_SMALL
    style.gm_tooltip_text.color = TEXT_COLOR_NORMAL
    style.gm_tooltip_text.outlines = [(1, "#000000", 0, 0)]
    
    # Custom screen styles
    style.screen_frame.background = Frame(UI_FRAME, 20, 20)
    style.screen_frame.padding = UI_PADDING
    style.screen_frame.margin = UI_PADDING
    style.screen_frame.xalign = 0.5
    style.screen_frame.yalign = 0.5
    style.screen_title.font = "fonts/DejaVuSans.ttf"
    style.screen_title.size = TEXT_SIZE_LARGE
    style.screen_title.color = TEXT_COLOR_HIGHLIGHT
    style.screen_title.outlines = [(2, "#000000", 0, 0)]
    style.screen_title.xalign = 0.5
    style.screen_title.yalign = 0.0
    style.screen_text.font = "fonts/DejaVuSans.ttf"
    style.screen_text.size = TEXT_SIZE_NORMAL
    style.screen_text.color = TEXT_COLOR_NORMAL
    style.screen_text.outlines = [(1, "#000000", 0, 0)]
    style.screen_text.line_leading = 1.2
    style.screen_text.line_spacing = 0
    style.screen_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.screen_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.screen_button.insensitive_background = Frame(UI_BUTTON_DISABLED, 10, 10)
    style.screen_button.size_group = "screen_button"
    style.screen_button.xsize = UI_BUTTON_WIDTH
    style.screen_button.ysize = UI_BUTTON_HEIGHT
    style.screen_button_text.font = "fonts/DejaVuSans.ttf"
    style.screen_button_text.size = TEXT_SIZE_NORMAL
    style.screen_button_text.color = TEXT_COLOR_NORMAL
    style.screen_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.screen_button_text.insensitive_color = TEXT_COLOR_DISABLED
    
    # Character selection styles
    style.char_select_frame.background = Frame(UI_FRAME, 20, 20)
    style.char_select_frame.padding = UI_PADDING
    style.char_select_frame.margin = UI_SPACING
    style.char_select_frame.xsize = 300
    style.char_select_frame.ysize = 200
    style.char_select_frame.hover_background = Frame(UI_BUTTON_HOVER, 20, 20)
    style.char_select_name.font = "fonts/DejaVuSans.ttf"
    style.char_select_name.size = TEXT_SIZE_NORMAL
    style.char_select_name.color = TEXT_COLOR_NORMAL
    style.char_select_name.outlines = [(1, "#000000", 0, 0)]
    style.char_select_name.xalign = 0.5
    style.char_select_name.yalign = 0.0
    style.char_select_class.font = "fonts/DejaVuSans.ttf"
    style.char_select_class.size = TEXT_SIZE_SMALL
    style.char_select_class.color = TEXT_COLOR_DISABLED
    style.char_select_class.outlines = [(1, "#000000", 0, 0)]
    style.char_select_class.xalign = 0.5
    style.char_select_class.yalign = 1.0
    
    # Character info styles
    style.char_info_frame.background = Frame(UI_FRAME, 20, 20)
    style.char_info_frame.padding = UI_PADDING
    style.char_info_frame.margin = UI_SPACING
    style.char_info_frame.xsize = 200
    style.char_info_frame.ysize = 200
    style.char_info_name.font = "fonts/DejaVuSans.ttf"
    style.char_info_name.size = TEXT_SIZE_NORMAL
    style.char_info_name.color = TEXT_COLOR_HIGHLIGHT
    style.char_info_name.outlines = [(1, "#000000", 0, 0)]
    style.char_info_name.xalign = 0.5
    style.char_info_name.yalign = 0.0
    style.char_info_value.font = "fonts/DejaVuSans.ttf"
    style.char_info_value.size = TEXT_SIZE_SMALL
    style.char_info_value.color = TEXT_COLOR_NORMAL
    style.char_info_value.outlines = [(1, "#000000", 0, 0)]
    style.char_info_value.xalign = 0.5
    style.char_info_value.yalign = 0.5
    
    # Inventory styles
    style.inventory_slot.background = Frame(UI_FRAME, 10, 10)
    style.inventory_slot.padding = 5
    style.inventory_slot.margin = 2
    style.inventory_slot.xsize = 80
    style.inventory_slot.ysize = 80
    style.inventory_slot.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.inventory_item.font = "fonts/DejaVuSans.ttf"
    style.inventory_item.size = TEXT_SIZE_SMALL
    style.inventory_item.color = TEXT_COLOR_NORMAL
    style.inventory_item.outlines = [(1, "#000000", 0, 0)]
    style.inventory_item.xalign = 0.5
    style.inventory_item.yalign = 0.5
    style.inventory_count.font = "fonts/DejaVuSans.ttf"
    style.inventory_count.size = TEXT_SIZE_SMALL
    style.inventory_count.color = TEXT_COLOR_HIGHLIGHT
    style.inventory_count.outlines = [(1, "#000000", 0, 0)]
    style.inventory_count.xalign = 1.0
    style.inventory_count.yalign = 1.0
    
    # Dialogue styles
    style.dialogue_window.background = Frame(UI_FRAME, 20, 20)
    style.dialogue_window.padding = UI_PADDING
    style.dialogue_window.margin = UI_PADDING
    style.dialogue_window.xalign = 0.5
    style.dialogue_window.yalign = 0.9
    style.dialogue_window.xminimum = 800
    style.dialogue_window.ymaximum = 200
    style.dialogue_text.font = "fonts/DejaVuSans.ttf"
    style.dialogue_text.size = TEXT_SIZE_NORMAL
    style.dialogue_text.color = TEXT_COLOR_NORMAL
    style.dialogue_text.outlines = [(1, "#000000", 0, 0)]
    style.dialogue_text.line_leading = 1.2
    style.dialogue_text.line_spacing = 0
    style.dialogue_name.font = "fonts/DejaVuSans.ttf"
    style.dialogue_name.size = TEXT_SIZE_NORMAL
    style.dialogue_name.color = TEXT_COLOR_HIGHLIGHT
    style.dialogue_name.outlines = [(2, "#000000", 0, 0)]
    style.dialogue_name.xalign = 0.0
    style.dialogue_name.yalign = 0.5
    
    # Choice styles
    style.choice_frame.background = Frame(UI_FRAME, 10, 10)
    style.choice_frame.padding = UI_SPACING
    style.choice_frame.margin = UI_SPACING
    style.choice_frame.xalign = 0.5
    style.choice_frame.xminimum = 600
    style.choice_frame.ymaximum = 50
    style.choice_frame.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.choice_text.font = "fonts/DejaVuSans.ttf"
    style.choice_text.size = TEXT_SIZE_NORMAL
    style.choice_text.color = TEXT_COLOR_NORMAL
    style.choice_text.outlines = [(1, "#000000", 0, 0)]
    style.choice_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.choice_text.xalign = 0.5
    style.choice_text.yalign = 0.5
    
    # Menu styles
    style.menu_frame.background = Frame(UI_FRAME, 20, 20)
    style.menu_frame.padding = UI_PADDING
    style.menu_frame.margin = UI_PADDING
    style.menu_frame.xalign = 0.5
    style.menu_frame.yalign = 0.5
    style.menu_title.font = "fonts/DejaVuSans.ttf"
    style.menu_title.size = TEXT_SIZE_LARGE + 10
    style.menu_title.color = TEXT_COLOR_HIGHLIGHT
    style.menu_title.outlines = [(2, "#000000", 0, 0)]
    style.menu_title.xalign = 0.5
    style.menu_title.yalign = 0.0
    style.menu_item_frame.background = Frame(UI_FRAME, 10, 10)
    style.menu_item_frame.padding = UI_SPACING
    style.menu_item_frame.margin = UI_SPACING
    style.menu_item_frame.xalign = 0.5
    style.menu_item_frame.xminimum = 600
    style.menu_item_frame.ymaximum = 60
    style.menu_item_frame.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.menu_item_text.font = "fonts/DejaVuSans.ttf"
    style.menu_item_text.size = TEXT_SIZE_NORMAL
    style.menu_item_text.color = TEXT_COLOR_NORMAL
    style.menu_item_text.outlines = [(1, "#000000", 0, 0)]
    style.menu_item_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.menu_item_text.xalign = 0.5
    style.menu_item_text.yalign = 0.5
    
    # Quick menu styles
    style.quick_menu_frame.background = None
    style.quick_menu_frame.padding = 0
    style.quick_menu_frame.margin = 0
    style.quick_menu_frame.xalign = 0.5
    style.quick_menu_frame.yalign = 1.0
    style.quick_button.background = Frame(UI_BUTTON_NORMAL, 10, 10)
    style.quick_button.hover_background = Frame(UI_BUTTON_HOVER, 10, 10)
    style.quick_button.insensitive_background = Frame(UI_BUTTON_DISABLED, 10, 10)
    style.quick_button.size_group = "quick_button"
    style.quick_button.xsize = 100
    style.quick_button.ysize = 30
    style.quick_button.yoffset = 0
    style.quick_button_text.font = "fonts/DejaVuSans.ttf"
    style.quick_button_text.size = TEXT_SIZE_SMALL
    style.quick_button_text.color = TEXT_COLOR_NORMAL
    style.quick_button_text.hover_color = TEXT_COLOR_HIGHLIGHT
    style.quick_button_text.insensitive_color = TEXT_COLOR_DISABLED
    style.quick_button_text.xalign = 0.5
    style.quick_button_text.yalign = 0.5
    
    # Tooltip styles
    style.tooltip_frame.background = Frame(UI_FRAME, 10, 10)
    style.tooltip_frame.padding = 5
    style.tooltip_frame.margin = 5
    style.tooltip_frame.xalign = 0.5
    style.tooltip_frame.yalign = 0.0
    style.tooltip_text.font = "fonts/DejaVuSans.ttf"
    style.tooltip_text.size = TEXT_SIZE_SMALL
    style.tooltip_text.color = TEXT_COLOR_NORMAL
    style.tooltip_text.outlines = [(1, "#000000", 0, 0)]
    style.tooltip_text.xalign = 0.5
    style.tooltip_text.yalign = 0.5
    
    # Notification styles
    style.notification_frame.background = Frame(UI_FRAME, 10, 10)
    style.notification_frame.padding = 5
    style.notification_frame.margin = 5
    style.notification_frame.xalign = 0.5
    style.notification_frame.yalign = 0.1
    style.notification_text.font = "fonts/DejaVuSans.ttf"
    style.notification_text.size = TEXT_SIZE_SMALL
    style.notification_text.color = TEXT_COLOR_NORMAL
    style.notification_text.outlines = [(1, "#000000", 0, 0)]
    style.notification_text.xalign = 0.5
    style.notification_text.yalign = 0.5
    
    # Loading screen styles
    style.loading_frame.background = Frame(UI_FRAME, 20, 20)
    style.loading_frame.padding = UI_PADDING
    style.loading_frame.margin = UI_PADDING
    style.loading_frame.xalign = 0.5
    style.loading_frame.yalign = 0.5
    style.loading_frame.xsize = 400
    style.loading_frame.ysize = 100
    style.loading_text.font = "fonts/DejaVuSans.ttf"
    style.loading_text.size = TEXT_SIZE_NORMAL
    style.loading_text.color = TEXT_COLOR_NORMAL
    style.loading_text.outlines = [(1, "#000000", 0, 0)]
    style.loading_text.xalign = 0.5
    style.loading_text.yalign = 0.5
    style.loading_bar.xmaximum = 300
    style.loading_bar.ymaximum = 20
    style.loading_bar.left_bar = Frame("images/ui/bar_left.png", 10, 10)
    style.loading_bar.right_bar = Frame("images/ui/bar_right.png", 10, 10)
    style.loading_bar.thumb = Frame("images/ui/bar_thumb.png", 10, 10)
    style.loading_bar.thumb_offset = 5
    style.loading_bar.thumb_shadow = None
    
    # Error message styles
    style.error_frame.background = Frame(UI_FRAME, 20, 20)
    style.error_frame.padding = UI_PADDING
    style.error_frame.margin = UI_PADDING
    style.error_frame.xalign = 0.5
    style.error_frame.yalign = 0.5
    style.error_frame.xsize = 600
    style.error_frame.ysize = 200
    style.error_text.font = "fonts/DejaVuSans.ttf"
    style.error_text.size = TEXT_SIZE_NORMAL
    style.error_text.color = "#FF6666"
    style.error_text.outlines = [(1, "#000000", 0, 0)]
    style.error_text.xalign = 0.5
    style.error_text.yalign = 0.5
    
    # Success message styles
    style.success_frame.background = Frame(UI_FRAME, 20, 20)
    style.success_frame.padding = UI_PADDING
    style.success_frame.margin = UI_PADDING
    style.success_frame.xalign = 0.5
    style.success_frame.yalign = 0.5
    style.success_frame.xsize = 600
    style.success_frame.ysize = 100
    style.success_text.font = "fonts/DejaVuSans.ttf"
    style.success_text.size = TEXT_SIZE_NORMAL
    style.success_text.color = "#66FF66"
    style.success_text.outlines = [(1, "#000000", 0, 0)]
    style.success_text.xalign = 0.5
    style.success_text.yalign = 0.5
    
    # Warning message styles
    style.warning_frame.background = Frame(UI_FRAME, 20, 20)
    style.warning_frame.padding = UI_PADDING
    style.warning_frame.margin = UI_PADDING
    style.warning_frame.xalign = 0.5
    style.warning_frame.yalign = 0.5
    style.warning_frame.xsize = 600
    style.warning_frame.ysize = 100
    style.warning_text.font = "fonts/DejaVuSans.ttf"
    style.warning_text.size = TEXT_SIZE_NORMAL
    style.warning_text.color = "#FFFF66"
    style.warning_text.outlines = [(1, "#000000", 0, 0)]
    style.warning_text.xalign = 0.5
    style.warning_text.yalign = 0.5
    
    # Info message styles
    style.info_frame.background = Frame(UI_FRAME, 20, 20)
    style.info_frame.padding = UI_PADDING
    style.info_frame.margin = UI_PADDING
    style.info_frame.xalign = 0.5
    style.info_frame.yalign = 0.5
    style.info_frame.xsize = 600
    style.info_frame.ysize = 100
    style.info_text.font = "fonts/DejaVuSans.ttf"
    style.info_text.size = TEXT_SIZE_NORMAL
    style.info_text.color = "#66FFFF"
    style.info_text.outlines = [(1, "#000000", 0, 0)]
    style.info_text.xalign = 0.5
    style.info_text.yalign = 0.5

# Custom screen definitions
screen loading_screen():
    tag menu
    zorder 100
    
    frame:
        style "loading_frame"
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Loading..." style "loading_text"
            
            bar:
                style "loading_bar"
                value 0
                range 100

screen error_screen(title, message, can_continue=True):
    tag menu
    zorder 100
    modal True

    frame:
        style "error_frame"
        xsize 600
        ysize 300

    vbox:
        spacing UI_SPACING
        xalign 0.5
        yalign 0.5
    
        text title style "error_text"
        text message style "error_text"
    
    if can_continue:
        textbutton "Continue" action Hide("error_screen") style "screen_button"
    else:
        textbutton "Quit" action Quit() style "screen_button"

screen success_screen(message):
    tag menu
    zorder 100
    modal True
    
    frame:
        style "success_frame"
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Success" style "success_text"
            text message style "success_text"
            
            textbutton "OK" action Hide("success_screen") style "screen_button"

screen warning_screen(message):
    tag menu
    zorder 100
    modal True
    
    frame:
        style "warning_frame"
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Warning" style "warning_text"
            text message style "warning_text"
            
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "OK" action Hide("warning_screen") style "screen_button"
                textbutton "Cancel" action Hide("warning_screen") style "screen_button"

screen info_screen(message):
    tag menu
    zorder 100
    modal True
    
    frame:
        style "info_frame"
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Information" style "info_text"
            text message style "info_text"
            
            textbutton "OK" action Hide("info_screen") style "screen_button"

screen notification_screen(message, duration=3.0):
    tag menu
    zorder 100
    modal False
    
    timer duration action Hide("notification_screen")
    
    frame:
        style "notification_frame"
        
        text message style "notification_text"

# Quick menu screen
screen quick_menu():
    tag menu
    zorder 100
    
    if QUICK_MENU_ENABLED:
        use game_screen()
        
        frame:
            style "quick_menu_frame"
            
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Save" action Show("save_screen") style "quick_button"
                textbutton "Load" action Show("load_screen") style "quick_button"
                textbutton "Q.Save" action [
                    Function(save_load_manager.save_game, 1, "Quick Save"),
                    Function(renpy.play, SFX_SUCCESS)
                ] style "quick_button"
                textbutton "Q.Load" action [
                    Function(save_load_manager.load_game, 1),
                    Function(renpy.play, SFX_SUCCESS)
                ] style "quick_button"
                textbutton "Prefs" action Show("preferences") style "quick_button"
                textbutton "Help" action Show("help_screen") style "quick_button"
                textbutton "Quit" action Show("confirm_quit") style "quick_button"

# Confirm quit screen
screen confirm_quit():
    tag menu
    zorder 100
    modal True
    
    frame:
        style "screen_frame"
        xsize 400
        ysize 200
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Are you sure you want to quit?" style "screen_text"
            
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Yes" action [
                    Function(renpy.quit),
                    Function(renpy.play, SFX_CLICK)
                ] style "screen_button"
                textbutton "No" action [
                    Hide("confirm_quit"),
                    Function(renpy.play, SFX_CLICK)
                ] style "screen_button"

# Confirm overwrite screen
screen confirm_overwrite(slot_number):
    tag menu
    zorder 100
    modal True
    
    frame:
        style "screen_frame"
        xsize 400
        ysize 200
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Are you sure you want to overwrite this save slot?" style "screen_text"
            
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Yes" action [
                    Function(save_load_manager.save_game, slot_number),
                    Function(renpy.play, SFX_SUCCESS),
                    Hide("confirm_overwrite")
                ] style "screen_button"
                textbutton "No" action [
                    Hide("confirm_overwrite"),
                    Function(renpy.play, SFX_CLICK)
                ] style "screen_button"

# Confirm delete screen
screen confirm_delete(slot_number):
    tag menu
    zorder 100
    modal True
    
    frame:
        style "screen_frame"
        xsize 400
        ysize 200
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Are you sure you want to delete this save?" style "screen_text"
            
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Yes" action [
                    Function(save_load_manager.delete_save, slot_number),
                    Function(renpy.play, SFX_SUCCESS),
                    Hide("confirm_delete")
                ] style "screen_button"
                textbutton "No" action [
                    Hide("confirm_delete"),
                    Function(renpy.play, SFX_CLICK)
                ] style "screen_button"

# Custom preferences screen
screen preferences():
    tag menu
    use game_screen()
    
    frame:
        style "screen_frame"
        xsize 900
        ysize 700
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Preferences" style "screen_title"
            
            # Add tabs for different preference categories
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Audio" action SetScreenVariable("current_tab", "audio") style "screen_button"
                textbutton "Visual" action SetScreenVariable("current_tab", "visual") style "screen_button"
                textbutton "Gameplay" action SetScreenVariable("current_tab", "gameplay") style "screen_button"
                textbutton "Controls" action SetScreenVariable("current_tab", "controls") style "screen_button"
                textbutton "Accessibility" action SetScreenVariable("current_tab", "accessibility") style "screen_button"
                        
            # Add tab content based on current selection
            if current_tab == "audio":
                use audio_preferences_tab()
            elif current_tab == "visual":
                use visual_preferences_tab()
            elif current_tab == "gameplay":
                use gameplay_preferences_tab()
            elif current_tab == "controls":
                use controls_preferences_tab()
            elif current_tab == "accessibility":
                use accessibility_preferences_tab()
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Apply" action [
                    Function(renpy.play, SFX_SUCCESS),
                    Hide("preferences")
                ] style "screen_button"
                textbutton "Reset" action [
                    Function(renpy.play, SFX_CLICK),
                    Function(renpy.preference.reset),
                    Hide("preferences")
                ] style "screen_button"
                textbutton "Cancel" action [
                    Function(renpy.play, SFX_CLICK),
                    Hide("preferences")
                ] style "screen_button"

# Add new screen for audio preferences tab
screen audio_preferences_tab():
    frame:
        style "screen_frame"
        xsize 850
        ysize 500
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            
            text "Audio Settings" style "screen_text"
            
            grid 2 1:
                spacing UI_SPACING
                xalign 0.5
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Master Volume:" style "screen_text"
                    text "Music Volume:" style "screen_text"
                    text "Sound Volume:" style "screen_text"
                    text "Voice Volume:" style "screen_text"
                    text "Ambient Volume:" style "screen_text"
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    bar:
                        style "gm_bar"
                        value Preference("music volume")
                        range 1.0
                    
                    bar:
                        style "gm_bar"
                        value Preference("music volume")
                        range 1.0
                    
                    bar:
                        style "gm_bar"
                        value Preference("sound volume")
                        range 1.0
                    
                    bar:
                        style "gm_bar"
                        value Preference("voice volume")
                        range 1.0
                    
                    bar:
                        style "gm_bar"
                        value Preference("voice volume")
                        range 1.0

# Add new screen for visual preferences tab
screen visual_preferences_tab():
    frame:
        style "screen_frame"
        xsize 850
        ysize 500
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            
            text "Visual Settings" style "screen_text"
            
            grid 2 1:
                spacing UI_SPACING
                xalign 0.5
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Transitions:" style "screen_text"
                    text "Visual Effects:" style "screen_text"
                    text "Particles:" style "screen_text"
                    text "Animations:" style "screen_text"
                    text "Text Speed:" style "screen_text"
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    textbutton ("On" if preferences.transitions else "Off") action [
                        Preference("transitions", not preferences.transitions),
                        TogglePreference("transitions"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if preferences.effects_enabled else "Off") action [
                        Preference("effects_enabled", not preferences.transitions),
                        TogglePreference("effects_enabled"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if preferences.particles_enabled else "Off") action [
                        Preference("particles_enabled", not preferences.transitions),
                        TogglePreference("particles_enabled"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if preferences.animations_enabled else "Off") action [
                        Preference("animations_enabled", not preferences.transitions),
                        TogglePreference("animations_enabled"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    bar:
                        style "gm_bar"
                        value Preference("text speed")
                        range 200

# Add new screen for gameplay preferences tab
screen gameplay_preferences_tab():
    frame:
        style "screen_frame"
        xsize 850
        ysize 500
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            
            text "Gameplay Settings" style "screen_text"
            
            grid 2 1:
                spacing UI_SPACING
                xalign 0.5
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Difficulty:" style "screen_text"
                    text "Auto-Forward:" style "screen_text"
                    text "Auto-Forward Time:" style "screen_text"
                    text "Skip Unread Text:" style "screen_text"
                    text "Show Empty Window:" style "screen_text"
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    textbutton ("Easy" if persistent.difficulty == "Easy" else "Normal" if persistent.difficulty == "Normal" else "Hard" if persistent.difficulty == "Hard" else "Expert") action [
                        SetVariable("difficulty", "Easy" if persistent.difficulty != "Easy" else "Normal" if persistent.difficulty != "Normal" else "Hard" if persistent.difficulty != "Hard" else "Expert"),
                        CyclePreference("difficulty", ["easy", "normal", "hard", "expert"]),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if preferences.afm_enable else "Off") action [
                        Preference("afm_enable", not preferences.afm_enable),
                        TogglePreference("afm_enable"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    bar:
                        style "gm_bar"
                        value Preference("auto-forward time")
                        range 20
                    
                    textbutton ("On" if config.skip_unseen else "Off") action [
                        SetVariable("skip_unseen", not config.skip_unseen),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton Preference("show empty window") action [
                        TogglePreference("show empty window"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"

# Add new screen for controls preferences tab
screen controls_preferences_tab():
    frame:
        style "screen_frame"
        xsize 850
        ysize 500
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            
            text "Control Settings" style "screen_text"
            
            grid 2 1:
                spacing UI_SPACING
                xalign 0.5
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Joystick:" style "screen_text"
                    text "Mouse Sensitivity:" style "screen_text"
                    text "Controller:" style "screen_text"
                    text "Quick Menu:" style "screen_text"
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    textbutton Preference("joystick") action [
                        TogglePreference("joystick"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    bar:
                        style "gm_bar"
                        value FieldValue(persistent, "mouse_sensitivity", range=2.0, default=1.0)
                        range 2.0
                    
                    textbutton ("On" if persistent.controller_enabled else "Off") action [
                        ToggleVariable(persistent, "controller_enabled"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton Preference("quick_menu") action [
                        TogglePreference("quick_menu"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"

# Add new screen for accessibility preferences tab
screen accessibility_preferences_tab():
    frame:
        style "screen_frame"
        xsize 850
        ysize 600
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            
            text "Accessibility Settings" style "screen_text"
            
            grid 2 1:
                spacing UI_SPACING
                xalign 0.5
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Text Size:" style "screen_text"
                    text "High Contrast:" style "screen_text"
                    text "Color Blind Mode:" style "screen_text"
                    text "Screen Reader:" style "screen_text"
                    text "Subtitles:" style "screen_text"
                    text "Reduced Motion:" style "screen_text"
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    bar:
                        style "gm_bar"
                        value accessibility_manager.text_size_multiplier
                        range 2.0
                        
                    textbutton ("On" if accessibility_manager.high_contrast_mode else "Off") action [
                        Function(accessibility_manager.toggle_high_contrast),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton accessibility_manager.color_blind_mode.capitalize() action [
                        Function(accessibility_manager.set_color_blind_mode, 
                            "protanopia" if accessibility_manager.color_blind_mode == "none" else "none"),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if accessibility_manager.screen_reader_enabled else "Off") action [
                        Function(accessibility_manager.toggle_screen_reader),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if accessibility_manager.subtitles_enabled else "Off") action [
                        Function(accessibility_manager.toggle_subtitles),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"
                    
                    textbutton ("On" if accessibility_manager.reduced_motion else "Off") action [
                        Function(accessibility_manager.toggle_reduced_motion),
                        Function(renpy.play, SFX_CLICK)
                    ] style "screen_button"

# Initialize current tab for preferences screen
init python:
    current_tab = "audio"

# Help screen
screen help_screen():
    tag menu
    use game_screen()
    
    frame:
        style "screen_frame"
        xsize 800
        ysize 600
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "Help" style "screen_title"
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                xsize 750
                ysize 450
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Controls" style "screen_text"
                    text "Left Click - Advance text/Select option" style "screen_text"
                    text "Right Click - Open menu/Go back" style "screen_text"
                    text "Spacebar - Advance text" style "screen_text"
                    text "Escape - Open menu" style "screen_text"
                    text "F1 - Take screenshot" style "screen_text"
                    text "F5 - Quick save" style "screen_text"
                    text "F9 - Quick load" style "screen_text"
                    
                    text "Tips" style "screen_text"
                    text "• Different characters have unique stories" style "screen_text"
                    text "• Your choices affect the outcome" style "screen_text"
                    text "• Build relationships with other characters" style "screen_text"
                    text "• Manage your inventory wisely" style "screen_text"
                    text "• Explore all paths for the full experience" style "screen_text"
    
            textbutton "Close" action Hide("help_screen") style "screen_button"

# About screen
screen about_screen():
    tag menu
    use game_screen()
    
    frame:
        style "screen_frame"
        xsize 600
        ysize 400
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            text "About" style "screen_title"
            
            text SCREEN_TITLE style "screen_text"
            text "Version 1.0" style "screen_text"
            text "Created with Ren'Py" style "screen_text"
            
            textbutton "Close" action Hide("about_screen") style "screen_button"

# Splash screen
screen splash_screen():
    tag menu
    zorder 100
    
    add BG_BLACK
    
    timer 2.0 action Jump("start")

# Custom init block
init python:
    # Register custom screens
    config.overlay_screens.append("quick_menu")
    
    # Set up default preferences
    if not hasattr(persistent, '_preferences'):
        persistent._preferences = config.default_preferences