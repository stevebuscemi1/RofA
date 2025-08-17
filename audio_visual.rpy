# game/audio_visual.rpy
    
init python:
    # =============================================================================
    # AUDIO AND VISUAL MANAGEMENT SYSTEM
    # =============================================================================
    
    class AudioVisualManager:
        """
        Manages all audio and visual aspects of the game including music,
        sound effects, transitions, and visual effects.
        """
        
        def __init__(self):
            """Initialize the audio/visual manager."""
            self.current_music = None
            self.current_ambient = None
            self.sound_effects_volume = 1.0
            self.music_volume = 1.0
            self.ambient_volume = 0.5
            self.voice_volume = 1.0
            self.audio_enabled = True
            self.visual_effects_enabled = True
            self.transitions_enabled = True
            self.current_background = None
            self.transition_cache = {}
            self.effect_queue = []
            self.audio_channels = {
                "music": 1,
                "ambient": 2,
                "sound": 3,
                "voice": 4
            }
            self.initialize_audio()
            self.load_visual_effects()
        
        def initialize_audio(self):
            """Initialize audio channels and settings."""
            try:
                # Import DEBUG_MODE if it exists
                global DEBUG_MODE
                if 'DEBUG_MODE' not in globals():
                    DEBUG_MODE = False
                
                # Configure audio channels
                for channel_name, channel_number in self.audio_channels.items():
                    renpy.music.register_channel(channel_name, channel_number)
                
                # Set default volumes
                self.set_music_volume(self.music_volume)
                self.set_sound_effects_volume(self.sound_effects_volume)
                self.set_ambient_volume(self.ambient_volume)
                self.set_voice_volume(self.voice_volume)
                
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error initializing audio system: {e}")
                self.audio_enabled = False
        
        def load_visual_effects(self):
            """Load and cache visual effects and transitions."""
            try:
                # Define transitions
                self.transition_cache = {
                    "fade": Fade(0.5, 0.0, 0.5),
                    "dissolve": Dissolve(0.5),
                    "pixellate": Pixellate(0.5),
                    "moveinright": MoveIn(0.5, "right"),
                    "moveinleft": MoveIn(0.5, "left"),
                    "moveintop": MoveIn(0.5, "top"),
                    "moveinbottom": MoveIn(0.5, "bottom"),
                    "zoomin": ZoomIn(0.5),
                    "zoomout": ZoomOut(0.5),
                    "irisout": IrisOut(0.5),
                    "vpunch": VPunch(0.5),
                    "hpunch": HPunch(0.5)
                }
                
                # Define visual effects
                self.visual_effects = {
                    "shake": self.create_shake_effect,
                    "flash": self.create_flash_effect,
                    "glow": self.create_glow_effect,
                    "blur": self.create_blur_effect,
                    "color_shift": self.create_color_shift_effect
                }
                
                if DEBUG_MODE:
                    print("Visual effects loaded successfully")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error loading visual effects: {e}")
                self.visual_effects_enabled = False
        
        def play_music(self, music_file, fadein=1.0, loop=True):
            """
            Play background music.
            
            Args:
                music_file (str): Path to the music file
                fadein (float): Fade in duration
                loop (bool): Whether to loop the music
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Stop current music if different
                if self.current_music != music_file:
                    self.stop_music(fadeout=0.5)
                
                # Play new music
                renpy.music.play(music_file, channel="music", fadein=fadein, loop=loop)
                self.current_music = music_file
                
                if DEBUG_MODE:
                    print(f"Playing music: {music_file}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing music {music_file}: {e}")
                return False
        
        def stop_music(self, fadeout=1.0):
            """
            Stop background music.
            
            Args:
                fadeout (float): Fade out duration
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                renpy.music.stop(channel="music", fadeout=fadeout)
                self.current_music = None
                
                if DEBUG_MODE:
                    print("Music stopped")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error stopping music: {e}")
                return False
        
        def play_ambient(self, ambient_file, fadein=2.0, loop=True):
            """
            Play ambient sound effects.
            
            Args:
                ambient_file (str): Path to the ambient sound file
                fadein (float): Fade in duration
                loop (bool): Whether to loop the ambient sound
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Stop current ambient if different
                if self.current_ambient != ambient_file:
                    self.stop_ambient(fadeout=1.0)
                
                # Play new ambient
                renpy.music.play(ambient_file, channel="ambient", fadein=fadein, loop=loop)
                self.current_ambient = ambient_file
                
                if DEBUG_MODE:
                    print(f"Playing ambient: {ambient_file}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing ambient {ambient_file}: {e}")
                return False
        
        def stop_ambient(self, fadeout=1.0):
            """
            Stop ambient sound effects.
            
            Args:
                fadeout (float): Fade out duration
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                renpy.music.stop(channel="ambient", fadeout=fadeout)
                self.current_ambient = None
                
                if DEBUG_MODE:
                    print("Ambient sound stopped")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error stopping ambient sound: {e}")
                return False
        
        def play_sound_effect(self, sound_file, volume=1.0, pan=0.0):
            """
            Play a sound effect.
            
            Args:
                sound_file (str): Path to the sound file
                volume (float): Volume multiplier (0.0 to 1.0)
                pan (float): Panning (-1.0 to 1.0)
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Apply volume multiplier
                actual_volume = volume * self.sound_effects_volume
                
                # Play sound effect
                renpy.sound.play(sound_file, channel="sound", volume=actual_volume, pan=pan)
                
                if DEBUG_MODE:
                    print(f"Playing sound effect: {sound_file}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing sound effect {sound_file}: {e}")
                return False
        
        def play_voice(self, voice_file, volume=1.0):
            """
            Play voice audio.
            
            Args:
                voice_file (str): Path to the voice file
                volume (float): Volume multiplier (0.0 to 1.0)
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Apply volume multiplier
                actual_volume = volume * self.voice_volume
                
                # Play voice
                renpy.sound.play(voice_file, channel="voice", volume=actual_volume)
                
                if DEBUG_MODE:
                    print(f"Playing voice: {voice_file}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing voice {voice_file}: {e}")
                return False
        
        def set_music_volume(self, volume):
            """
            Set the music volume.
            
            Args:
                volume (float): Volume level (0.0 to 1.0)
            """
            try:
                self.music_volume = max(0.0, min(1.0, volume))
                renpy.music.set_volume(self.music_volume, channel="music")
                
                if DEBUG_MODE:
                    print(f"Music volume set to: {self.music_volume}")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting music volume: {e}")
        
        def set_sound_effects_volume(self, volume):
            """
            Set the sound effects volume.
            
            Args:
                volume (float): Volume level (0.0 to 1.0)
            """
            try:
                self.sound_effects_volume = max(0.0, min(1.0, volume))
                renpy.sound.set_volume(self.sound_effects_volume, channel="sound")
                
                if DEBUG_MODE:
                    print(f"Sound effects volume set to: {self.sound_effects_volume}")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting sound effects volume: {e}")
        
        def set_ambient_volume(self, volume):
            """
            Set the ambient sound volume.
            
            Args:
                volume (float): Volume level (0.0 to 1.0)
            """
            try:
                self.ambient_volume = max(0.0, min(1.0, volume))
                renpy.music.set_volume(self.ambient_volume, channel="ambient")
                
                if DEBUG_MODE:
                    print(f"Ambient volume set to: {self.ambient_volume}")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting ambient volume: {e}")
        
        def set_voice_volume(self, volume):
            """
            Set the voice volume.
            
            Args:
                volume (float): Volume level (0.0 to 1.0)
            """
            try:
                self.voice_volume = max(0.0, min(1.0, volume))
                renpy.sound.set_volume(self.voice_volume, channel="voice")
                
                if DEBUG_MODE:
                    print(f"Voice volume set to: {self.voice_volume}")
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error setting voice volume: {e}")
        
        def toggle_audio(self):
            """
            Toggle audio on/off.
            
            Returns:
                bool: New audio state
            """
            try:
                self.audio_enabled = not self.audio_enabled
                
                if not self.audio_enabled:
                    # Stop all audio
                    self.stop_music(fadeout=0.0)
                    self.stop_ambient(fadeout=0.0)
                    renpy.sound.stop(channel="sound")
                    renpy.sound.stop(channel="voice")
                else:
                    # Restart current music if any
                    if self.current_music:
                        self.play_music(self.current_music, fadein=0.0)
                    if self.current_ambient:
                        self.play_ambient(self.current_ambient, fadein=0.0)
                
                if DEBUG_MODE:
                    print(f"Audio {'enabled' if self.audio_enabled else 'disabled'}")
                
                return self.audio_enabled
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling audio: {e}")
                return not self.audio_enabled
        
        def change_background(self, background_image, transition="fade"):
            """
            Change the background image with transition.
            
            Args:
                background_image (str): Path to the background image
                transition (str): Name of the transition to use
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    # Change background without transition
                    renpy.scene(background_image)
                    self.current_background = background_image
                    return True
                
                # Get transition
                trans = self.transition_cache.get(transition, self.transition_cache["fade"])
                
                # Apply transition
                renpy.scene(background_image, with_=trans)
                self.current_background = background_image
                
                if DEBUG_MODE:
                    print(f"Background changed to: {background_image} with {transition} transition")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error changing background to {background_image}: {e}")
                return False
        
        def apply_transition(self, transition_name="fade"):
            """
            Apply a transition effect.
            
            Args:
                transition_name (str): Name of the transition to apply
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled or not self.transitions_enabled:
                    return False
                
                # Get transition
                trans = self.transition_cache.get(transition_name, self.transition_cache["fade"])
                
                # Apply transition
                renpy.with_statement(trans)
                
                if DEBUG_MODE:
                    print(f"Applied transition: {transition_name}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error applying transition {transition_name}: {e}")
                return False
        
        def create_shake_effect(self, intensity=5, duration=0.5):
            """
            Create a screen shake effect.
            
            Args:
                intensity (int): Intensity of the shake
                duration (float): Duration of the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    return False
                
                # Create shake effect
                shake = Shake((0, intensity, 0), duration)
                renpy.with_statement(shake)
                
                if DEBUG_MODE:
                    print(f"Applied shake effect: intensity={intensity}, duration={duration}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error creating shake effect: {e}")
                return False
        
        def create_flash_effect(self, color="#FFFFFF", duration=0.3):
            """
            Create a flash effect.
            
            Args:
                color (str): Color of the flash
                duration (float): Duration of the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    return False
                
                # Create flash effect
                flash = Flash(color, duration)
                renpy.with_statement(flash)
                
                if DEBUG_MODE:
                    print(f"Applied flash effect: color={color}, duration={duration}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error creating flash effect: {e}")
                return False
        
        def create_glow_effect(self, duration=1.0):
            """
            Create a glow effect.
            
            Args:
                duration (float): Duration of the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    return False
                
                # Create glow effect
                glow = AlphaBlend(0.5, 1.0, duration)
                renpy.with_statement(glow)
                
                if DEBUG_MODE:
                    print(f"Applied glow effect: duration={duration}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error creating glow effect: {e}")
                return False
        
        def create_blur_effect(self, duration=0.5):
            """
            Create a blur effect.
            
            Args:
                duration (float): Duration of the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    return False
                
                # Create blur effect
                blur = Blur(1.0, duration)
                renpy.with_statement(blur)
                
                if DEBUG_MODE:
                    print(f"Applied blur effect: duration={duration}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error creating blur effect: {e}")
                return False
        
        def create_color_shift_effect(self, color_shift, duration=0.5):
            """
            Create a color shift effect.
            
            Args:
                color_shift (tuple): RGB color shift values
                duration (float): Duration of the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.visual_effects_enabled:
                    return False
                
                # Create color shift effect
                color_shift_effect = ColorMatrix(color_shift, duration)
                renpy.with_statement(color_shift_effect)
                
                if DEBUG_MODE:
                    print(f"Applied color shift effect: color_shift={color_shift}, duration={duration}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error creating color shift effect: {e}")
                return False
        
        def queue_visual_effect(self, effect_name, *args, **kwargs):
            """
            Queue a visual effect to be played later.
            
            Args:
                effect_name (str): Name of the effect
                *args: Arguments for the effect
                **kwargs: Keyword arguments for the effect
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                self.effect_queue.append((effect_name, args, kwargs))
                
                if DEBUG_MODE:
                    print(f"Queued visual effect: {effect_name}")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error queuing visual effect {effect_name}: {e}")
                return False
        
        def process_effect_queue(self):
            """
            Process all queued visual effects.
            
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                while self.effect_queue:
                    effect_name, args, kwargs = self.effect_queue.pop(0)
                    
                    if effect_name in self.visual_effects:
                        self.visual_effects[effect_name](*args, **kwargs)
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error processing effect queue: {e}")
                return False
        
        def play_location_audio(self, location):
            """
            Play appropriate audio for a location.
            
            Args:
                location (str): Location identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Location-specific audio mapping
                location_audio = {
                    LOC_CITY: {
                        "music": MUSIC_PEACEFUL,
                        "ambient": "sounds/ambient/city.ogg"
                    },
                    LOC_FOREST: {
                        "music": MUSIC_MYSTICAL,
                        "ambient": "sounds/ambient/forest.ogg"
                    },
                    LOC_TEMPLE: {
                        "music": MUSIC_PEACEFUL,
                        "ambient": "sounds/ambient/temple.ogg"
                    },
                    LOC_DUNGEON: {
                        "music": MUSIC_BATTLE,
                        "ambient": "sounds/ambient/dungeon.ogg"
                    },
                    LOC_CASTLE: {
                        "music": MUSIC_PEACEFUL,
                        "ambient": "sounds/ambient/castle.ogg"
                    },
                    LOC_MARKET: {
                        "music": MUSIC_PEACEFUL,
                        "ambient": "sounds/ambient/market.ogg"
                    },
                    LOC_TAVERN: {
                        "music": MUSIC_PEACEFUL,
                        "ambient": "sounds/ambient/tavern.ogg"
                    }
                }
                
                if location in location_audio:
                    audio_config = location_audio[location]
                    
                    # Play music
                    if "music" in audio_config:
                        self.play_music(audio_config["music"], fadein=2.0)
                    
                    # Play ambient
                    if "ambient" in audio_config:
                        self.play_ambient(audio_config["ambient"], fadein=2.0)
                    
                    if DEBUG_MODE:
                        print(f"Playing location audio for: {location}")
                    
                    return True
                
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing location audio for {location}: {e}")
                return False
        
        def play_character_theme(self, character_id):
            """
            Play a character-specific theme.
            
            Args:
                character_id (str): Character identifier
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Character theme mapping
                character_themes = {
                    CHAR_WARRIOR: "music/themes/warrior.ogg",
                    CHAR_MAGE: "music/themes/mage.ogg",
                    CHAR_ROGUE: "music/themes/rogue.ogg",
                    CHAR_CLERIC: "music/themes/cleric.ogg",
                    CHAR_RANGER: "music/themes/ranger.ogg"
                }
                
                if character_id in character_themes:
                    theme_file = character_themes[character_id]
                    self.play_music(theme_file, fadein=1.0)
                    
                    if DEBUG_MODE:
                        print(f"Playing character theme for: {character_id}")
                    
                    return True
                
                return False
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing character theme for {character_id}: {e}")
                return False
        
        def play_story_audio(self, story_node):
            """
            Play appropriate audio for a story node.
            
            Args:
                story_node (dict): Story node data
                
            Returns:
                bool: True if successful, False otherwise
            """
            try:
                if not self.audio_enabled:
                    return False
                
                # Play background music if specified
                if "music" in story_node:
                    self.play_music(story_node["music"], fadein=1.0)
                
                # Play location audio if location is specified
                if "location" in story_node:
                    self.play_location_audio(story_node["location"])
                
                # Play character theme if character is specified
                if "character" in story_node:
                    self.play_character_theme(story_node["character"])
                
                # Play sound effects based on story content
                if "text" in story_node:
                    text = story_node["text"].lower()
                    if any(word in text for word in ["battle", "fight", "combat"]):
                        self.play_sound_effect(SFX_BATTLE, volume=0.8)
                    elif any(word in text for word in ["treasure", "gold", "reward"]):
                        self.play_sound_effect(SFX_SUCCESS, volume=0.8)
                    elif any(word in text for word in ["danger", "warning", "alert"]):
                        self.play_sound_effect(SFX_FAILURE, volume=0.8)
                
                if DEBUG_MODE:
                    print("Played story audio for current node")
                
                return True
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error playing story audio: {e}")
                return False
        
        def toggle_visual_effects(self):
            """
            Toggle visual effects on/off.
            
            Returns:
                bool: New visual effects state
            """
            try:
                self.visual_effects_enabled = not self.visual_effects_enabled
                
                if DEBUG_MODE:
                    print(f"Visual effects {'enabled' if self.visual_effects_enabled else 'disabled'}")
                
                return self.visual_effects_enabled
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling visual effects: {e}")
                return not self.visual_effects_enabled
        
        def toggle_transitions(self):
            """
            Toggle transitions on/off.
            
            Returns:
                bool: New transitions state
            """
            try:
                self.transitions_enabled = not self.transitions_enabled
                
                if DEBUG_MODE:
                    print(f"Transitions {'enabled' if self.transitions_enabled else 'disabled'}")
                
                return self.transitions_enabled
                
            except Exception as e:
                if DEBUG_MODE:
                    print(f"Error toggling transitions: {e}")
                return not self.transitions_enabled
        
        def get_audio_status(self):
            """
            Get current audio status.
            
            Returns:
                dict: Audio status information
            """
            return {
                "enabled": self.audio_enabled,
                "music_volume": self.music_volume,
                "sound_effects_volume": self.sound_effects_volume,
                "ambient_volume": self.ambient_volume,
                "voice_volume": self.voice_volume,
                "current_music": self.current_music,
                "current_ambient": self.current_ambient
            }
        
        def get_visual_status(self):
            """
            Get current visual effects status.
            
            Returns:
                dict: Visual effects status information
            """
            return {
                "enabled": self.visual_effects_enabled,
                "transitions_enabled": self.transitions_enabled,
                "current_background": self.current_background,
                "effect_queue_length": len(self.effect_queue)
            }

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the audio/visual manager
    audio_visual_manager = AudioVisualManager()

# =============================================================================
# AUDIO/VISUAL SETTINGS SCREEN
# =============================================================================

screen audio_visual_settings():
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
            text "Audio & Visual Settings" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Audio settings
            frame:
                xsize 700
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Audio Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    # Audio toggle
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Audio Enabled:" size TEXT_SIZE_SMALL
                        textbutton ("On" if audio_visual_manager.transitions_enabled else "Off") action [
                            Function(audio_visual_manager.toggle_audio),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    # Music volume
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Music Volume:" size TEXT_SIZE_SMALL
                        bar value audio_visual_manager.music_volume range 1.0 xsize 200
                        text "{:.0f}%".format(audio_visual_manager.music_volume * 100) size TEXT_SIZE_SMALL
                    
                    # Sound effects volume
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Sound Effects Volume:" size TEXT_SIZE_SMALL
                        bar value audio_visual_manager.sound_effects_volume range 1.0 xsize 200
                        text "{:.0f}%".format(audio_visual_manager.sound_effects_volume * 100) size TEXT_SIZE_SMALL
                    
                    # Ambient volume
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Ambient Volume:" size TEXT_SIZE_SMALL
                        bar value audio_visual_manager.ambient_volume range 1.0 xsize 200
                        text "{:.0f}%".format(audio_visual_manager.ambient_volume * 100) size TEXT_SIZE_SMALL
                    
                    # Voice volume
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Voice Volume:" size TEXT_SIZE_SMALL
                        bar value audio_visual_manager.voice_volume range 1.0 xsize 200
                        text "{:.0f}%".format(audio_visual_manager.voice_volume * 100) size TEXT_SIZE_SMALL
            
            # Visual settings
            frame:
                xsize 700
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Visual Settings" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    # Visual effects toggle
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                    
                        text "Visual Effects:" size TEXT_SIZE_SMALL
                        textbutton ("On" if audio_visual_manager.transitions_enabled else "Off") action [
                            Function(audio_visual_manager.toggle_visual_effects),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
                    
                    # Transitions toggle
                    hbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Transitions:" size TEXT_SIZE_SMALL
                        textbutton ("On" if audio_visual_manager.transitions_enabled else "Off") action [
                            Function(audio_visual_manager.toggle_transitions),
                            Function(renpy.play, SFX_CLICK)
                        ] xsize 80
            
            # Test buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Test Sound" action [
                    Function(audio_visual_manager.play_sound_effect, SFX_CLICK),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
                textbutton "Test Music" action [
                    Function(audio_visual_manager.play_music, MUSIC_MAIN_THEME, 0.5),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
                textbutton "Test Effect" action [
                    Function(audio_visual_manager.create_flash_effect),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
            
            # Close button
            textbutton "Close" action Hide("audio_visual_settings") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# AUDIO/VISUAL HOOKS
# =============================================================================

init python:
    def audio_visual_update():
        """Update audio/visual systems each frame."""
        try:
            # Process effect queue
            audio_visual_manager.process_effect_queue()
            
            # Update volumes based on settings
            audio_visual_manager.set_music_volume(audio_visual_manager.music_volume)
            audio_visual_manager.set_sound_effects_volume(audio_visual_manager.sound_effects_volume)
            audio_visual_manager.set_ambient_volume(audio_visual_manager.ambient_volume)
            audio_visual_manager.set_voice_volume(audio_visual_manager.voice_volume)
            
            return 0.016  # ~60 FPS
            
        except Exception as e:
            if DEBUG_MODE:
                print(f"Error in audio/visual update: {e}")
            return 0.1
    
    # Register audio/visual update function
    config.overlay_functions.append(audio_visual_update)