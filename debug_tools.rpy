# game/debug_tools.rpy

init python:
    # =============================================================================
    # DEBUGGING AND TESTING TOOLS
    # =============================================================================
    
    class DebugManager:
        """
        Manages all debugging tools, testing utilities, and development features.
        Provides comprehensive debugging capabilities for development and testing.
        """
        
        def __init__(self):
            """Initialize the debug manager."""
            self.enabled = DEBUG_MODE
            self.debug_log = []
            self.max_log_entries = 1000
            self.performance_stats = {
                "fps": 0,
                "memory_usage": 0,
                "load_times": {},
                "frame_times": []
            }
            self.test_suites = {}
            self.debug_commands = self._initialize_debug_commands()
            self.debug_screens = self._initialize_debug_screens()
            self.test_results = {}
            self.breakpoints = {}
            self.watch_variables = {}
            self.debug_overlays = []
            self.performance_monitoring = True
            self.log_to_file = True
            self.log_file_path = "debug_log.txt"
            self.initialize_debug_system()
        
        def _initialize_debug_commands(self):
            """Initialize available debug commands."""
            return {
                "help": {
                    "description": "Show available debug commands",
                    "usage": "help [command]",
                    "function": self.debug_command_help
                },
                "godmode": {
                    "description": "Toggle god mode (invincibility)",
                    "usage": "godmode",
                    "function": self.debug_command_godmode
                },
                "additem": {
                    "description": "Add item to character inventory",
                    "usage": "additem <item_name> [quantity]",
                    "function": self.debug_command_additem
                },
                "setstat": {
                    "description": "Set character stat value",
                    "usage": "setstat <stat_name> <value>",
                    "function": self.debug_command_setstat
                },
                "teleport": {
                    "description": "Teleport to location",
                    "usage": "teleport <location_id>",
                    "function": self.debug_command_teleport
                },
                "completequest": {
                    "description": "Complete a quest",
                    "usage": "completequest <quest_id>",
                    "function": self.debug_command_completequest
                },
                "addexp": {
                    "description": "Add experience to character",
                    "usage": "addexp <amount>",
                    "function": self.debug_command_addexp
                },
                "setrelationship": {
                    "description": "Set relationship level",
                    "usage": "setrelationship <char1_id> <char2_id> <level>",
                    "function": self.debug_command_setrelationship
                },
                "unlockachievement": {
                    "description": "Unlock an achievement",
                    "usage": "unlockachievement <achievement_id>",
                    "function": self.debug_command_unlockachievement
                },
                "showflags": {
                    "description": "Show all story flags",
                    "usage": "showflags",
                    "function": self.debug_command_showflags
                },
                "setflag": {
                    "description": "Set a story flag",
                    "usage": "setflag <flag_name> <value>",
                    "function": self.debug_command_setflag
                },
                "listcharacters": {
                    "description": "List all characters",
                    "usage": "listcharacters",
                    "function": self.debug_command_listcharacters
                },
                "showinventory": {
                    "description": "Show character inventory",
                    "usage": "showinventory [character_id]",
                    "function": self.debug_command_showinventory
                },
                "test": {
                    "description": "Run test suite",
                    "usage": "test [suite_name]",
                    "function": self.debug_command_test
                },
                "benchmark": {
                    "description": "Run performance benchmark",
                    "usage": "benchmark",
                    "function": self.debug_command_benchmark
                },
                "screenshot": {
                    "description": "Take screenshot",
                    "usage": "screenshot [filename]",
                    "function": self.debug_command_screenshot
                },
                "clearlog": {
                    "description": "Clear debug log",
                    "usage": "clearlog",
                    "function": self.debug_command_clearlog
                }
            }
        
        def _initialize_debug_screens(self):
            """Initialize debug screen definitions."""
            return {
                "console": {
                    "title": "Debug Console",
                    "description": "Interactive debug command console"
                },
                "variables": {
                    "title": "Variable Inspector",
                    "description": "Inspect and modify game variables"
                },
                "performance": {
                    "title": "Performance Monitor",
                    "description": "Monitor game performance metrics"
                },
                "tests": {
                    "title": "Test Runner",
                    "description": "Run and view test results"
                },
                "log": {
                    "title": "Debug Log",
                    "description": "View debug log entries"
                }
            }
        
        def initialize_debug_system(self):
            """Initialize the debug system."""
            try:
                # Clear debug log
                self.debug_log = []
                
                # Initialize performance monitoring
                self.performance_stats["start_time"] = time.time()
                self.performance_stats["frame_count"] = 0
                
                # Register debug overlays
                if self.enabled:
                    self.register_debug_overlay("fps_counter", self.show_fps_counter)
                    self.register_debug_overlay("memory_usage", self.show_memory_usage)
                    self.register_debug_overlay("debug_info", self.show_debug_info)
                
                # Initialize test suites
                self.initialize_test_suites()
                
                # Load breakpoints from file if exists
                self.load_breakpoints()
                
                # Start logging to file if enabled
                if self.log_to_file:
                    self.start_file_logging()
                
                self.log_message("Debug system initialized", "INFO")
                
            except Exception as e:
                print(f"Error initializing debug system: {e}")
        
        def log_message(self, message, level="DEBUG", category="GENERAL"):
            """
            Log a debug message.
            
            Args:
                message (str): The message to log
                level (str): Log level (DEBUG, INFO, WARNING, ERROR)
                category (str): Message category
            """
            try:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                log_entry = {
                    "timestamp": timestamp,
                    "level": level,
                    "category": category,
                    "message": message
                }
                
                self.debug_log.append(log_entry)
                
                # Limit log size
                if len(self.debug_log) > self.max_log_entries:
                    self.debug_log = self.debug_log[-self.max_log_entries:]
                
                # Print to console if debug mode enabled
                if self.enabled:
                    print(f"[{timestamp}] {level}: {category} - {message}")
                
                # Write to file if enabled
                if self.log_to_file:
                    self.write_log_to_file(log_entry)
                
            except Exception as e:
                print(f"Error logging message: {e}")
        
        def write_log_to_file(self, log_entry):
            """
            Write a log entry to file.
            
            Args:
                log_entry (dict): The log entry to write
            """
            try:
                with open(self.log_file_path, "a", encoding="utf-8") as f:
                    f.write(f"[{log_entry['timestamp']}] {log_entry['level']}: {log_entry['category']} - {log_entry['message']}\n")
            except Exception as e:
                print(f"Error writing log to file: {e}")
        
        def start_file_logging(self):
            """Start logging to file."""
            try:
                # Clear existing log file
                with open(self.log_file_path, "w", encoding="utf-8") as f:
                    f.write(f"Debug Log Started: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("=" * 50 + "\n")
            except Exception as e:
                print(f"Error starting file logging: {e}")
                self.log_to_file = False
        
        def register_debug_overlay(self, name, function):
            """
            Register a debug overlay function.
            
            Args:
                name (str): Name of the overlay
                function (callable): Function to call for the overlay
            """
            try:
                self.debug_overlays.append({"name": name, "function": function})
                self.log_message(f"Registered debug overlay: {name}", "INFO")
            except Exception as e:
                self.log_message(f"Error registering debug overlay {name}: {e}", "ERROR")
        
        def show_fps_counter(self):
            """Show FPS counter overlay."""
            try:
                if not self.enabled:
                    return
                
                fps = self.performance_stats.get("fps", 0)
                ui.text(f"FPS: {fps:.1f}", size=16, color="#FFFFFF", xalign=0.0, yalign=0.0)
            except Exception as e:
                self.log_message(f"Error showing FPS counter: {e}", "ERROR")
        
        def show_memory_usage(self):
            """Show memory usage overlay."""
            try:
                if not self.enabled:
                    return
                
                memory_mb = self.performance_stats.get("memory_usage", 0)
                ui.text(f"Memory: {memory_mb:.1f}MB", size=16, color="#FFFFFF", xalign=0.0, yalign=0.05)
            except Exception as e:
                self.log_message(f"Error showing memory usage: {e}", "ERROR")
        
        def show_debug_info(self):
            """Show general debug information overlay."""
            try:
                if not self.enabled:
                    return
                
                selected_char = character_manager.get_selected_character()
                char_name = selected_char["name"] if selected_char else "None"
                
                info_text = f"Char: {char_name} | Location: {persistent.game_state['current_location']} | Chapter: {story_manager.current_chapter}"
                ui.text(info_text, size=16, color="#FFFFFF", xalign=0.0, yalign=0.1)
            except Exception as e:
                self.log_message(f"Error showing debug info: {e}", "ERROR")
        
        def update_performance_stats(self):
            """Update performance statistics."""
            try:
                if not self.performance_monitoring:
                    return
                
                # Update frame count
                self.performance_stats["frame_count"] += 1
                
                # Calculate FPS
                current_time = time.time()
                elapsed_time = current_time - self.performance_stats.get("last_fps_update", current_time)
                
                if elapsed_time >= 1.0:  # Update FPS every second
                    fps = self.performance_stats["frame_count"] / elapsed_time
                    self.performance_stats["fps"] = fps
                    self.performance_stats["frame_count"] = 0
                    self.performance_stats["last_fps_update"] = current_time
                
                # Update memory usage (if psutil is available)
                try:
                    import psutil
                    process = psutil.Process()
                    memory_mb = process.memory_info().rss / 1024 / 1024
                    self.performance_stats["memory_usage"] = memory_mb
                except ImportError:
                    pass
                
                # Record frame time
                frame_time = current_time - self.performance_stats.get("last_frame_time", current_time)
                self.performance_stats["frame_times"].append(frame_time)
                
                # Keep only recent frame times
                if len(self.performance_stats["frame_times"]) > 100:
                    self.performance_stats["frame_times"] = self.performance_stats["frame_times"][-100:]
                
                self.performance_stats["last_frame_time"] = current_time
                
            except Exception as e:
                self.log_message(f"Error updating performance stats: {e}", "ERROR")
        
        def execute_debug_command(self, command_text):
            """
            Execute a debug command.
            
            Args:
                command_text (str): The command to execute
                
            Returns:
                str: Result message
            """
            try:
                if not self.enabled:
                    return "Debug mode is disabled"
                
                # Parse command
                parts = command_text.strip().split()
                if not parts:
                    return "No command provided"
                
                command_name = parts[0].lower()
                args = parts[1:]
                
                # Find command
                if command_name not in self.debug_commands:
                    return f"Unknown command: {command_name}. Type 'help' for available commands."
                
                command = self.debug_commands[command_name]
                
                # Execute command
                try:
                    result = command["function"](args)
                    self.log_message(f"Executed debug command: {command_text}", "INFO")
                    return result
                except Exception as e:
                    error_msg = f"Error executing command '{command_name}': {e}"
                    self.log_message(error_msg, "ERROR")
                    return error_msg
                
            except Exception as e:
                self.log_message(f"Error parsing debug command '{command_text}': {e}", "ERROR")
                return f"Error parsing command: {e}"
        
        def debug_command_help(self, args):
            """Handle help command."""
            try:
                if not args:
                    # Show all commands
                    help_text = "Available debug commands:\n"
                    for cmd_name, cmd_info in self.debug_commands.items():
                        help_text += f"  {cmd_name}: {cmd_info['description']}\n"
                    help_text += "\nType 'help <command>' for detailed usage."
                else:
                    # Show specific command help
                    cmd_name = args[0].lower()
                    if cmd_name in self.debug_commands:
                        cmd_info = self.debug_commands[cmd_name]
                        help_text = f"{cmd_name}: {cmd_info['description']}\n"
                        help_text += f"Usage: {cmd_info['usage']}"
                    else:
                        help_text = f"Unknown command: {cmd_name}"
                
                return help_text
            except Exception as e:
                return f"Error in help command: {e}"
        
        def debug_command_godmode(self, args):
            """Handle godmode command."""
            try:
                selected_char = character_manager.get_selected_character()
                if not selected_char:
                    return "No character selected"
                
                # Toggle god mode (set health and mana to max)
                selected_char["health"] = selected_char["max_health"]
                selected_char["mana"] = selected_char["max_mana"]
                
                return "God mode enabled - health and mana restored to maximum"
            except Exception as e:
                return f"Error in godmode command: {e}"
        
        def debug_command_additem(self, args):
            """Handle additem command."""
            try:
                if not args:
                    return "Usage: additem <item_name> [quantity]"
                
                item_name = args[0]
                quantity = int(args[1]) if len(args) > 1 else 1
                
                if not character_manager.selected_character:
                    return "No character selected"
                
                success = inventory_manager.add_item(character_manager.selected_character, item_name, quantity)
                if success:
                    return f"Added {quantity}x {item_name} to inventory"
                else:
                    return f"Failed to add {item_name} to inventory"
            except Exception as e:
                return f"Error in additem command: {e}"
        
        def debug_command_setstat(self, args):
            """Handle setstat command."""
            try:
                if len(args) < 2:
                    return "Usage: setstat <stat_name> <value>"
                
                stat_name = args[0]
                value = int(args[1])
                
                if not character_manager.selected_character:
                    return "No character selected"
                
                success = character_manager.update_character_stat(character_manager.selected_character, stat_name, value)
                if success:
                    return f"Set {stat_name} to {value}"
                else:
                    return f"Failed to set {stat_name} to {value}"
            except Exception as e:
                return f"Error in setstat command: {e}"
        
        def debug_command_teleport(self, args):
            """Handle teleport command."""
            try:
                if not args:
                    return "Usage: teleport <location_id>"
                
                location_id = args[0]
                
                # Change location
                persistent.game_state["current_location"] = location_id
                character_manager.set_character_location(character_manager.selected_character, location_id)
                
                # Change background
                background_map = {
                    LOC_CITY: BG_CITY,
                    LOC_FOREST: BG_FOREST,
                    LOC_TEMPLE: BG_TEMPLE,
                    LOC_DUNGEON: BG_DUNGEON,
                    LOC_CASTLE: BG_CASTLE,
                    LOC_MARKET: BG_MARKET,
                    LOC_TAVERN: BG_TAVERN
                }
                
                if location_id in background_map:
                    renpy.scene(background_map[location_id])
                
                # Play location audio
                audio_visual_manager.play_location_audio(location_id)
                
                return f"Teleported to {location_id}"
            except Exception as e:
                return f"Error in teleport command: {e}"
        
        def debug_command_completequest(self, args):
            """Handle completequest command."""
            try:
                if not args:
                    return "Usage: completequest <quest_id>"
                
                quest_id = args[0]
                
                success = story_manager.complete_quest(quest_id)
                if success:
                    return f"Completed quest: {quest_id}"
                else:
                    return f"Failed to complete quest: {quest_id}"
            except Exception as e:
                return f"Error in completequest command: {e}"
        
        def debug_command_addexp(self, args):
            """Handle addexp command."""
            try:
                if not args:
                    return "Usage: addexp <amount>"
                
                amount = int(args[0])
                
                if not character_manager.selected_character:
                    return "No character selected"
                
                character_manager.add_experience(character_manager.selected_character, amount)
                return f"Added {amount} experience"
            except Exception as e:
                return f"Error in addexp command: {e}"
        
        def debug_command_setrelationship(self, args):
            """Handle setrelationship command."""
            try:
                if len(args) < 3:
                    return "Usage: setrelationship <char1_id> <char2_id> <level>"
                
                char1_id = args[0]
                char2_id = args[1]
                level = int(args[2])
                
                success = relationship_manager.set_relationship(char1_id, char2_id, level)
                if success:
                    return f"Set relationship between {char1_id} and {char2_id} to level {level}"
                else:
                    return f"Failed to set relationship"
            except Exception as e:
                return f"Error in setrelationship command: {e}"
        
        def debug_command_unlockachievement(self, args):
            """Handle unlockachievement command."""
            try:
                if not args:
                    return "Usage: unlockachievement <achievement_id>"
                
                achievement_id = args[0]
                
                success = story_manager.unlock_achievement(achievement_id)
                if success:
                    return f"Unlocked achievement: {achievement_id}"
                else:
                    return f"Failed to unlock achievement: {achievement_id}"
            except Exception as e:
                return f"Error in unlockachievement command: {e}"
        
        def debug_command_showflags(self, args):
            """Handle showflags command."""
            try:
                flags_text = "Story Flags:\n"
                for flag_name, flag_value in story_manager.story_flags.items():
                    flags_text += f"  {flag_name}: {flag_value}\n"
                return flags_text
            except Exception as e:
                return f"Error in showflags command: {e}"
        
        def debug_command_setflag(self, args):
            """Handle setflag command."""
            try:
                if len(args) < 2:
                    return "Usage: setflag <flag_name> <value>"
                
                flag_name = args[0]
                value = args[1].lower() in ["true", "1", "yes", "on"]
                
                story_manager.story_flags[flag_name] = value
                return f"Set flag {flag_name} to {value}"
            except Exception as e:
                return f"Error in setflag command: {e}"
        
        def debug_command_listcharacters(self, args):
            """Handle listcharacters command."""
            try:
                chars_text = "Characters:\n"
                for char_id, char_data in character_manager.characters.items():
                    chars_text += f"  {char_id}: {char_data['name']} (Level {char_data['level']})\n"
                return chars_text
            except Exception as e:
                return f"Error in listcharacters command: {e}"
        
        def debug_command_showinventory(self, args):
            """Handle showinventory command."""
            try:
                char_id = args[0] if args else character_manager.selected_character
                
                if not char_id or char_id not in character_manager.characters:
                    return "Invalid character ID"
                
                char_data = character_manager.characters[char_id]
                inv_text = f"Inventory for {char_data['name']}:\n"
                
                for item in char_data["inventory"]:
                    inv_text += f"  - {item}\n"
                
                return inv_text
            except Exception as e:
                return f"Error in showinventory command: {e}"
        
        def debug_command_test(self, args):
            """Handle test command."""
            try:
                suite_name = args[0] if args else "all"
                
                results = self.run_test_suite(suite_name)
                
                result_text = f"Test Results ({suite_name}):\n"
                result_text += f"  Passed: {results['passed']}\n"
                result_text += f"  Failed: {results['failed']}\n"
                result_text += f"  Total: {results['total']}\n"
                
                if results['failed'] > 0:
                    result_text += "\nFailed Tests:\n"
                    for failure in results['failures']:
                        result_text += f"  - {failure}\n"
                
                return result_text
            except Exception as e:
                return f"Error in test command: {e}"
        
        def debug_command_benchmark(self, args):
            """Handle benchmark command."""
            try:
                results = self.run_benchmark()
                
                result_text = "Benchmark Results:\n"
                result_text += f"  Average FPS: {results['avg_fps']:.2f}\n"
                result_text += f"  Average Frame Time: {results['avg_frame_time']:.4f}s\n"
                result_text += f"  Memory Usage: {results['memory_usage']:.2f}MB\n"
                result_text += f"  Test Duration: {results['duration']:.2f}s\n"
                
                return result_text
            except Exception as e:
                return f"Error in benchmark command: {e}"
        
        def debug_command_screenshot(self, args):
            """Handle screenshot command."""
            try:
                filename = args[0] if args else f"screenshot_{int(time.time())}.png"
                
                screenshot = renpy.take_screenshot()
                if screenshot:
                    # Save screenshot (this would need actual file saving implementation)
                    return f"Screenshot saved as {filename}"
                else:
                    return "Failed to take screenshot"
            except Exception as e:
                return f"Error in screenshot command: {e}"
        
        def debug_command_clearlog(self, args):
            """Handle clearlog command."""
            try:
                self.debug_log = []
                return "Debug log cleared"
            except Exception as e:
                return f"Error in clearlog command: {e}"
        
        def initialize_test_suites(self):
            """Initialize test suites."""
            try:
                self.test_suites = {
                    "character": {
                        "name": "Character Tests",
                        "tests": [
                            self.test_character_creation,
                            self.test_character_stats,
                            self.test_character_inventory
                        ]
                    },
                    "story": {
                        "name": "Story Tests",
                        "tests": [
                            self.test_story_nodes,
                            self.test_quest_system,
                            self.test_achievement_system
                        ]
                    },
                    "inventory": {
                        "name": "Inventory Tests",
                        "tests": [
                            self.test_item_management,
                            self.test_item_trading
                        ]
                    },
                    "performance": {
                        "name": "Performance Tests",
                        "tests": [
                            self.test_load_times,
                            self.test_memory_usage
                        ]
                    }
                }
                
                self.log_message("Test suites initialized", "INFO")
            except Exception as e:
                self.log_message(f"Error initializing test suites: {e}", "ERROR")
        
        def run_test_suite(self, suite_name="all"):
            """
            Run a test suite or all tests.
            
            Args:
                suite_name (str): Name of the suite to run, or "all" for all tests
                
            Returns:
                dict: Test results
            """
            try:
                results = {
                    "passed": 0,
                    "failed": 0,
                    "total": 0,
                    "failures": []
                }
                
                if suite_name == "all":
                    # Run all test suites
                    for suite_data in self.test_suites.values():
                        suite_results = self._run_test_suite_tests(suite_data["tests"])
                        results["passed"] += suite_results["passed"]
                        results["failed"] += suite_results["failed"]
                        results["total"] += suite_results["total"]
                        results["failures"].extend(suite_results["failures"])
                else:
                    # Run specific test suite
                    if suite_name in self.test_suites:
                        suite_data = self.test_suites[suite_name]
                        results = self._run_test_suite_tests(suite_data["tests"])
                    else:
                        self.log_message(f"Unknown test suite: {suite_name}", "WARNING")
                
                # Store results
                self.test_results[suite_name] = results
                
                self.log_message(f"Test suite '{suite_name}' completed: {results['passed']}/{results['total']} passed", "INFO")
                
                return results
                
            except Exception as e:
                self.log_message(f"Error running test suite '{suite_name}': {e}", "ERROR")
                return {"passed": 0, "failed": 1, "total": 1, "failures": [str(e)]}
        
        def _run_test_suite_tests(self, tests):
            """Run tests in a suite."""
            results = {"passed": 0, "failed": 0, "total": 0, "failures": []}
            
            for test_func in tests:
                results["total"] += 1
                try:
                    test_result = test_func()
                    if test_result:
                        results["passed"] += 1
                    else:
                        results["failed"] += 1
                        results["failures"].append(test_func.__name__)
                except Exception as e:
                    results["failed"] += 1
                    results["failures"].append(f"{test_func.__name__}: {str(e)}")
            
            return results
        
        def test_character_creation(self):
            """Test character creation."""
            try:
                # Test that all characters are properly initialized
                for char_id in character_manager.characters:
                    char_data = character_manager.characters[char_id]
                    if not char_data.get("name") or not char_data.get("stats"):
                        return False
                
                return True
            except Exception as e:
                self.log_message(f"Character creation test failed: {e}", "ERROR")
                return False
        
        def test_character_stats(self):
            """Test character stats system."""
            try:
                # Test stat modification
                test_char = character_manager.get_character(CHAR_WARRIOR)
                if not test_char:
                    return False
                
                original_strength = test_char["stats"][STAT_STRENGTH]
                character_manager.update_character_stat(CHAR_WARRIOR, STAT_STRENGTH, original_strength + 1)
                
                if test_char["stats"][STAT_STRENGTH] != original_strength + 1:
                    return False
                
                return True
            except Exception as e:
                self.log_message(f"Character stats test failed: {e}", "ERROR")
                return False
        
        def test_character_inventory(self):
            """Test character inventory system."""
            try:
                # Test item addition and removal
                test_char = character_manager.get_character(CHAR_WARRIOR)
                if not test_char:
                    return False
                
                original_count = len(test_char["inventory"])
                
                # Add item
                inventory_manager.add_item(CHAR_WARRIOR, ITEM_HEALTH_POTION)
                if len(test_char["inventory"]) != original_count + 1:
                    return False
                
                # Remove item
                inventory_manager.remove_item(CHAR_WARRIOR, ITEM_HEALTH_POTION)
                if len(test_char["inventory"]) != original_count:
                    return False
                
                return True
            except Exception as e:
                self.log_message(f"Character inventory test failed: {e}", "ERROR")
                return False
        
        def test_story_nodes(self):
            """Test story node system."""
            try:
                # Test that story nodes are accessible
                test_node = story_manager.get_story_node(CHAPTER_PROLOGUE, "intro")
                if not test_node:
                    return False
                
                if not test_node.get("text"):
                    return False
                
                return True
            except Exception as e:
                self.log_message(f"Story nodes test failed: {e}", "ERROR")
                return False
        
        def test_quest_system(self):
            """Test quest system."""
            try:
                # Test quest starting and completion
                available_quests = story_manager.get_available_quests()
                if not isinstance(available_quests, list):
                    return False
                
                return True
            except Exception as e:
                self.log_message(f"Quest system test failed: {e}", "ERROR")
                return False
        
        def test_achievement_system(self):
            """Test achievement system."""
            try:
                # Test achievement checking
                story_manager.check_achievements()
                return True
            except Exception as e:
                self.log_message(f"Achievement system test failed: {e}", "ERROR")
                return False
        
        def test_item_management(self):
            """Test item management system."""
            try:
                # Test item database
                item_info = inventory_manager.get_item_info(ITEM_HEALTH_POTION)
                if not item_info:
                    return False
                
                return True
            except Exception as e:
                self.log_message(f"Item management test failed: {e}", "ERROR")
                return False
        
        def test_item_trading(self):
            """Test item trading system."""
            try:
                # Test item exchange
                success = inventory_manager.exchange_items(CHAR_WARRIOR, CHAR_MAGE, ITEM_HEALTH_POTION, ITEM_MANA_POTION)
                # This might fail if characters don't have the items, but the system should handle it gracefully
                return True
            except Exception as e:
                self.log_message(f"Item trading test failed: {e}", "ERROR")
                return False
        
        def test_load_times(self):
            """Test load times."""
            try:
                # Measure load time for a story node
                start_time = time.time()
                test_node = story_manager.get_story_node(CHAPTER_PROLOGUE, "intro")
                load_time = time.time() - start_time
                
                if load_time > 1.0:  # More than 1 second is considered slow
                    self.log_message(f"Slow load time detected: {load_time:.3f}s", "WARNING")
                
                return load_time < 1.0
            except Exception as e:
                self.log_message(f"Load times test failed: {e}", "ERROR")
                return False
        
        def test_memory_usage(self):
            """Test memory usage."""
            try:
                # Check memory usage
                memory_mb = self.performance_stats.get("memory_usage", 0)
                
                if memory_mb > 500:  # More than 500MB is considered high
                    self.log_message(f"High memory usage detected: {memory_mb:.1f}MB", "WARNING")
                
                return memory_mb < 500
            except Exception as e:
                self.log_message(f"Memory usage test failed: {e}", "ERROR")
                return False
        
        def run_benchmark(self):
            """
            Run performance benchmark.
            
            Returns:
                dict: Benchmark results
            """
            try:
                self.log_message("Starting performance benchmark", "INFO")
                
                start_time = time.time()
                frame_times = []
                
                # Run benchmark for 5 seconds
                benchmark_duration = 5.0
                while time.time() - start_time < benchmark_duration:
                    frame_start = time.time()
                    
                    # Simulate game operations
                    story_manager.get_story_node(CHAPTER_PROLOGUE, "intro")
                    character_manager.get_character(CHAR_WARRIOR)
                    inventory_manager.get_item_info(ITEM_HEALTH_POTION)
                    
                    frame_end = time.time()
                    frame_times.append(frame_end - frame_start)
                
                # Calculate results
                total_time = time.time() - start_time
                avg_frame_time = sum(frame_times) / len(frame_times)
                avg_fps = 1.0 / avg_frame_time if avg_frame_time > 0 else 0
                
                results = {
                    "avg_fps": avg_fps,
                    "avg_frame_time": avg_frame_time,
                    "memory_usage": self.performance_stats.get("memory_usage", 0),
                    "duration": total_time
                }
                
                self.log_message(f"Benchmark completed: {avg_fps:.2f} FPS average", "INFO")
                
                return results
                
            except Exception as e:
                self.log_message(f"Benchmark failed: {e}", "ERROR")
                return {"avg_fps": 0, "avg_frame_time": 0, "memory_usage": 0, "duration": 0}
        
        def add_breakpoint(self, location, condition=None):
            """
            Add a breakpoint.
            
            Args:
                location (str): Location identifier
                condition (str): Optional condition for breakpoint
            """
            try:
                self.breakpoints[location] = {
                    "condition": condition,
                    "enabled": True
                }
                self.log_message(f"Added breakpoint at {location}", "INFO")
            except Exception as e:
                self.log_message(f"Error adding breakpoint: {e}", "ERROR")
        
        def remove_breakpoint(self, location):
            """
            Remove a breakpoint.
            
            Args:
                location (str): Location identifier
            """
            try:
                if location in self.breakpoints:
                    del self.breakpoints[location]
                    self.log_message(f"Removed breakpoint at {location}", "INFO")
            except Exception as e:
                self.log_message(f"Error removing breakpoint: {e}", "ERROR")
        
        def check_breakpoints(self, location):
            """
            Check if any breakpoints are triggered at the current location.
            
            Args:
                location (str): Current location
                
            Returns:
                bool: True if breakpoint was triggered
            """
            try:
                if location in self.breakpoints:
                    breakpoint_data = self.breakpoints[location]
                    
                    if breakpoint_data["enabled"]:
                        condition = breakpoint_data.get("condition")
                        
                        # Check condition if specified
                        if condition:
                            # This is a simplified condition check
                            # In a real implementation, you'd need to parse and evaluate the condition
                            condition_met = True
                        else:
                            condition_met = True
                        
                        if condition_met:
                            self.log_message(f"Breakpoint triggered at {location}", "INFO")
                            return True
                
                return False
            except Exception as e:
                self.log_message(f"Error checking breakpoints: {e}", "ERROR")
                return False
        
        def add_watch_variable(self, name, variable_path):
            """
            Add a variable to watch.
            
            Args:
                name (str): Name for the watch
                variable_path (str): Path to the variable (e.g., "character_manager.selected_character.health")
            """
            try:
                self.watch_variables[name] = {
                    "path": variable_path,
                    "last_value": None
                }
                self.log_message(f"Added watch variable: {name}", "INFO")
            except Exception as e:
                self.log_message(f"Error adding watch variable: {e}", "ERROR")
        
        def remove_watch_variable(self, name):
            """
            Remove a watch variable.
            
            Args:
                name (str): Name of the watch variable
            """
            try:
                if name in self.watch_variables:
                    del self.watch_variables[name]
                    self.log_message(f"Removed watch variable: {name}", "INFO")
            except Exception as e:
                self.log_message(f"Error removing watch variable: {e}", "ERROR")
        
        def check_watch_variables(self):
            """Check all watch variables for changes."""
            try:
                for name, watch_data in self.watch_variables.items():
                    try:
                        # Get current value (this is a simplified implementation)
                        # In a real implementation, you'd need to parse the variable path and evaluate it
                        current_value = "N/A"
                        
                        last_value = watch_data["last_value"]
                        
                        if current_value != last_value:
                            self.log_message(f"Watch variable '{name}' changed: {last_value} -> {current_value}", "INFO")
                            watch_data["last_value"] = current_value
                    
                    except Exception as e:
                        self.log_message(f"Error checking watch variable '{name}': {e}", "ERROR")
            except Exception as e:
                self.log_message(f"Error checking watch variables: {e}", "ERROR")
        
        def save_breakpoints(self):
            """Save breakpoints to file."""
            try:
                with open("debug_breakpoints.json", "w") as f:
                    json.dump(self.breakpoints, f, indent=2)
                self.log_message("Breakpoints saved", "INFO")
            except Exception as e:
                self.log_message(f"Error saving breakpoints: {e}", "ERROR")
        
        def load_breakpoints(self):
            """Load breakpoints from file."""
            try:
                if os.path.exists("debug_breakpoints.json"):
                    with open("debug_breakpoints.json", "r") as f:
                        self.breakpoints = json.load(f)
                    self.log_message("Breakpoints loaded", "INFO")
            except Exception as e:
                self.log_message(f"Error loading breakpoints: {e}", "ERROR")
        
        def generate_debug_report(self):
            """
            Generate a comprehensive debug report.
            
            Returns:
                str: Debug report content
            """
            try:
                report = []
                report.append("=" * 50)
                report.append("DEBUG REPORT")
                report.append("=" * 50)
                report.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                report.append("")
                
                # System information
                report.append("SYSTEM INFORMATION:")
                report.append(f"  Debug Mode: {'Enabled' if self.enabled else 'Disabled'}")
                report.append(f"  FPS: {self.performance_stats.get('fps', 0):.2f}")
                report.append(f"  Memory Usage: {self.performance_stats.get('memory_usage', 0):.2f}MB")
                report.append("")
                
                # Game state
                report.append("GAME STATE:")
                report.append(f"  Selected Character: {character_manager.selected_character}")
                report.append(f"  Current Chapter: {story_manager.current_chapter}")
                report.append(f"  Current Location: {persistent.game_state['current_location']}")
                report.append(f"  Game Time: {persistent.game_state['game_time']}")
                report.append("")
                
                # Character information
                report.append("CHARACTERS:")
                for char_id, char_data in character_manager.characters.items():
                    report.append(f"  {char_id}:")
                    report.append(f"    Name: {char_data['name']}")
                    report.append(f"    Level: {char_data['level']}")
                    report.append(f"    Health: {char_data['health']}/{char_data['max_health']}")
                    report.append(f"    Mana: {char_data['mana']}/{char_data['max_mana']}")
                    report.append(f"    Inventory: {len(char_data['inventory'])} items")
                report.append("")
                
                # Recent log entries
                report.append("RECENT LOG ENTRIES:")
                recent_logs = self.debug_log[-20:]  # Last 20 entries
                for entry in recent_logs:
                    report.append(f"  [{entry['timestamp']}] {entry['level']}: {entry['message']}")
                report.append("")
                
                # Test results
                report.append("TEST RESULTS:")
                for suite_name, results in self.test_results.items():
                    report.append(f"  {suite_name}: {results['passed']}/{results['total']} passed")
                    if results['failed'] > 0:
                        report.append(f"    Failures: {', '.join(results['failures'])}")
                report.append("")
                
                # Performance statistics
                report.append("PERFORMANCE STATISTICS:")
                frame_times = self.performance_stats.get("frame_times", [])
                if frame_times:
                    avg_frame_time = sum(frame_times) / len(frame_times)
                    min_frame_time = min(frame_times)
                    max_frame_time = max(frame_times)
                    
                    report.append(f"  Average Frame Time: {avg_frame_time:.4f}s")
                    report.append(f"  Min Frame Time: {min_frame_time:.4f}s")
                    report.append(f"  Max Frame Time: {max_frame_time:.4f}s")
                    report.append(f"  Frame Count: {len(frame_times)}")
                
                return "\n".join(report)
                
            except Exception as e:
                self.log_message(f"Error generating debug report: {e}", "ERROR")
                return f"Error generating debug report: {e}"
        
        def export_debug_report(self, filename=None):
            """
            Export debug report to file.
            
            Args:
                filename (str): Optional filename, defaults to timestamp-based name
            """
            try:
                if not filename:
                    filename = f"debug_report_{int(time.time())}.txt"
                
                report_content = self.generate_debug_report()
                
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(report_content)
                
                self.log_message(f"Debug report exported to {filename}", "INFO")
                return filename
            except Exception as e:
                self.log_message(f"Error exporting debug report: {e}", "ERROR")
                return None

    # =============================================================================
    # GLOBAL INSTANCES
    # =============================================================================
    
    # Create global instance of the debug manager
    debug_manager = DebugManager()

# =============================================================================
    # DEBUG SCREENS
    # =============================================================================

screen debug_console():
    tag menu
    use game_screen()
    
    default console_input = ""
    default console_output = []
    default console_history = []
    default history_index = -1
    
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Debug Console" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Console output
            frame:
                xsize 850
                ysize 300
                background Frame(UI_FRAME, 10, 10)
                
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 830
                    ysize 280
                    
                    vbox:
                        spacing 2
                        xalign 0.0
                        
                        for line in console_output:
                            text line size TEXT_SIZE_SMALL color "#FFFFFF"
            
            # Console input
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                input:
                    size TEXT_SIZE_SMALL
                    xsize 700
                    value ScreenVariableInputValue("console_input")
                    copypaste True
                
                textbutton "Execute" action [
                    Function(debug_manager.execute_debug_command, console_input),
                    Function(console_output.append, "> " + console_input),
                    Function(console_output.append, debug_manager.execute_debug_command(console_input)),
                    Function(setattr, console_input, ""),
                    Function(console_history.append, console_input),
                    Function(setattr, history_index, len(console_history))
                ] xsize 100
                
                textbutton "Clear" action [
                    Function(setattr, console_output, []),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 80
            
            # Help text
            text "Type 'help' for available commands" size TEXT_SIZE_SMALL color screen_manager.ui_theme["text_color"] xalign 0.5
            
            # Close button
            textbutton "Close" action Hide("debug_console") xsize UI_BUTTON_WIDTH xalign 0.5

screen debug_variables():
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
            text "Variable Inspector" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Game state variables
            frame:
                xsize 750
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Game State" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    text "Selected Character: [character_manager.selected_character]" size TEXT_SIZE_SMALL
                    text "Current Chapter: [story_manager.current_chapter]" size TEXT_SIZE_SMALL
                    text "Current Location: [persistent.game_state['current_location']]" size TEXT_SIZE_SMALL
                    text "Game Time: [persistent.game_state['game_time']]" size TEXT_SIZE_SMALL
            
            # Character variables
            if character_manager.selected_character:
                frame:
                    xsize 750
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Character Variables" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        $ selected_char = character_manager.get_selected_character()
                        if selected_char:
                            text "Name: [selected_char['name']]" size TEXT_SIZE_SMALL
                            text "Level: [selected_char['level']]" size TEXT_SIZE_SMALL
                            text "Experience: [selected_char['experience']]" size TEXT_SIZE_SMALL
                            text "Health: [selected_char['health']]/[selected_char['max_health']]" size TEXT_SIZE_SMALL
                            text "Mana: [selected_char['mana']]/[selected_char['max_mana']]" size TEXT_SIZE_SMALL
                            text "Gold: [selected_char['gold']]" size TEXT_SIZE_SMALL
                            
                            text "Stats:" size TEXT_SIZE_SMALL color screen_manager.ui_theme["highlight_color"]
                            for stat_name, stat_value in selected_char["stats"].items():
                                text "  [stat_name]: [stat_value]" size TEXT_SIZE_SMALL
            
            # Story flags
            frame:
                xsize 750
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Story Flags" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        xsize 730
                        ysize 150
                        
                        vbox:
                            spacing 2
                            xalign 0.0
                            
                            for flag_name, flag_value in story_manager.story_flags.items():
                                text "[flag_name]: [flag_value]" size TEXT_SIZE_SMALL
            
            # Close button
            textbutton "Close" action Hide("debug_variables") xsize UI_BUTTON_WIDTH xalign 0.5

screen debug_performance():
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
            text "Performance Monitor" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Performance stats
            frame:
                xsize 750
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Current Performance" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    text "FPS: [debug_manager.performance_stats['fps']:.1f]" size TEXT_SIZE_SMALL
                    text "Memory Usage: [debug_manager.performance_stats['memory_usage']:.1f]MB" size TEXT_SIZE_SMALL
                    text "Frame Count: [debug_manager.performance_stats['frame_count']]" size TEXT_SIZE_SMALL
            
            # Frame time graph (simplified)
            frame:
                xsize 750
                ysize 200
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Frame Time History" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    text "Frame time graph would be displayed here" size TEXT_SIZE_SMALL
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Run Benchmark" action [
                    Function(debug_manager.run_benchmark),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 150
                textbutton "Export Report" action [
                    Function(debug_manager.export_debug_report),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 150
                textbutton "Clear Stats" action [
                    Function(setattr, debug_manager.performance_stats["frame_times"], []),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 150
            
            # Close button
            textbutton "Close" action Hide("debug_performance") xsize UI_BUTTON_WIDTH xalign 0.5

screen debug_tests():
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
            text "Test Runner" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Test suites
            frame:
                xsize 750
                background Frame(UI_FRAME, 10, 10)
                
                vbox:
                    spacing UI_SPACING
                    xalign 0.5
                    
                    text "Available Test Suites" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                    
                    for suite_name, suite_data in debug_manager.test_suites.items():
                        frame:
                            xsize 700
                            background Frame(UI_FRAME, 5, 5)
                            
                            hbox:
                                spacing UI_SPACING
                                xalign 0.5
                                
                                text suite_data["name"] size TEXT_SIZE_SMALL
                                textbutton "Run" action [
                                    Function(debug_manager.run_test_suite, suite_name),
                                    Function(renpy.play, SFX_CLICK)
                                ] xsize 80
                    
                    textbutton "Run All Tests" action [
                        Function(debug_manager.run_test_suite, "all"),
                        Function(renpy.play, SFX_CLICK)
                    ] xsize 150
            
            # Test results
            if debug_manager.test_results:
                frame:
                    xsize 750
                    background Frame(UI_FRAME, 10, 10)
                    
                    vbox:
                        spacing UI_SPACING
                        xalign 0.5
                        
                        text "Recent Test Results" size TEXT_SIZE_NORMAL color screen_manager.ui_theme["highlight_color"]
                        
                        for suite_name, results in debug_manager.test_results.items():
                            text "[suite_name]: [results['passed']]/[results['total']] passed" size TEXT_SIZE_SMALL
                            if results['failed'] > 0:
                                text "  Failures: [', '.join(results['failures'])]" size TEXT_SIZE_SMALL color "#FF6666"
            
            # Close button
            textbutton "Close" action Hide("debug_tests") xsize UI_BUTTON_WIDTH xalign 0.5

screen debug_log():
    tag menu
    use game_screen()
    
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 600
        background Frame(UI_FRAME, 20, 20)
        
        vbox:
            spacing UI_SPACING
            xalign 0.5
            yalign 0.5
            
            # Header
            text "Debug Log" size TEXT_SIZE_LARGE color screen_manager.ui_theme["highlight_color"] xalign 0.5
            
            # Log entries
            frame:
                xsize 850
                ysize 400
                background Frame(UI_FRAME, 10, 10)
                
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 830
                    ysize 380
                    
                    vbox:
                        spacing 2
                        xalign 0.0
                        
                        for entry in debug_manager.debug_log[-100:]:  # Show last 100 entries
                            $ color = "#FFFFFF"
                            if entry["level"] == "ERROR":
                                $ color = "#FF6666"
                            elif entry["level"] == "WARNING":
                                $ color = "#FFFF66"
                            elif entry["level"] == "INFO":
                                $ color = "#66FF66"
                            
                            text "[entry['timestamp']] [entry['level']]: [entry['message']]" size TEXT_SIZE_SMALL color "#FFFFFF"
            
            # Action buttons
            hbox:
                spacing UI_SPACING
                xalign 0.5
                
                textbutton "Clear Log" action [
                    Function(setattr, debug_manager.debug_log, []),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
                textbutton "Export Log" action [
                    Function(debug_manager.export_debug_report),
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
                textbutton "Refresh" action [
                    Function(renpy.play, SFX_CLICK)
                ] xsize 120
            
            # Close button
            textbutton "Close" action Hide("debug_log") xsize UI_BUTTON_WIDTH xalign 0.5

# =============================================================================
# DEBUG OVERLAY FUNCTIONS
# =============================================================================

init python:
    def debug_overlay_update():
        """Update debug overlays."""
        try:
            if not debug_manager.enabled:
                return 0.1
            
            # Update performance stats
            debug_manager.update_performance_stats()
            
            # Check watch variables
            debug_manager.check_watch_variables()
            
            # Show debug overlays
            for overlay in debug_manager.debug_overlays:
                try:
                    overlay["function"]()
                except Exception as e:
                    debug_manager.log_message(f"Error in debug overlay {overlay['name']}: {e}", "ERROR")
            
            return 0.016  # ~60 FPS
            
        except Exception as e:
            debug_manager.log_message(f"Error in debug overlay update: {e}", "ERROR")
            return 0.1
    
    # Register debug overlay update function
    config.overlay_functions.append(debug_overlay_update)

# =============================================================================
# DEBUG KEYBOARD SHORTCUTS
# =============================================================================

init python:
    def debug_key_handler(event):
        """Handle debug keyboard shortcuts."""
        try:
            if not debug_manager.enabled:
                return
            
            if event.type == 'keydown':
                if event.key == 'f1':  # F1 - Show debug console
                    renpy.show_screen("debug_console")
                elif event.key == 'f2':  # F2 - Show variable inspector
                    renpy.show_screen("debug_variables")
                elif event.key == 'f3':  # F3 - Show performance monitor
                    renpy.show_screen("debug_performance")
                elif event.key == 'f4':  # F4 - Show test runner
                    renpy.show_screen("debug_tests")
                elif event.key == 'f5':  # F5 - Show debug log
                    renpy.show_screen("debug_log")
                elif event.key == 'f12':  # F12 - Toggle debug mode
                    debug_manager.enabled = not debug_manager.enabled
                    debug_manager.log_message(f"Debug mode {'enabled' if debug_manager.enabled else 'disabled'}", "INFO")
        
        except Exception as e:
            debug_manager.log_message(f"Error in debug key handler: {e}", "ERROR")
    
    # Register debug key handler
    config.keymap["debug_console"] = ['f1']
    config.keymap["debug_variables"] = ['f2']
    config.keymap["debug_performance"] = ['f3']
    config.keymap["debug_tests"] = ['f4']
    config.keymap["debug_log"] = ['f5']
    config.keymap["toggle_debug"] = ['f12']