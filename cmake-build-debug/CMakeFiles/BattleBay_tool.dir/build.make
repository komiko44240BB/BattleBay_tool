# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2024.1.4\bin\cmake\win\x64\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2024.1.4\bin\cmake\win\x64\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Pierre-Luc\BattleBay_tool

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/BattleBay_tool.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/BattleBay_tool.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/BattleBay_tool.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/BattleBay_tool.dir/flags.make

CMakeFiles/BattleBay_tool.dir/main.c.obj: CMakeFiles/BattleBay_tool.dir/flags.make
CMakeFiles/BattleBay_tool.dir/main.c.obj: C:/Users/Pierre-Luc/BattleBay_tool/main.c
CMakeFiles/BattleBay_tool.dir/main.c.obj: CMakeFiles/BattleBay_tool.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/BattleBay_tool.dir/main.c.obj"
	C:\PROGRA~1\JETBRA~1\CLION2~1.4\bin\mingw\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/BattleBay_tool.dir/main.c.obj -MF CMakeFiles\BattleBay_tool.dir\main.c.obj.d -o CMakeFiles\BattleBay_tool.dir\main.c.obj -c C:\Users\Pierre-Luc\BattleBay_tool\main.c

CMakeFiles/BattleBay_tool.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/BattleBay_tool.dir/main.c.i"
	C:\PROGRA~1\JETBRA~1\CLION2~1.4\bin\mingw\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Pierre-Luc\BattleBay_tool\main.c > CMakeFiles\BattleBay_tool.dir\main.c.i

CMakeFiles/BattleBay_tool.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/BattleBay_tool.dir/main.c.s"
	C:\PROGRA~1\JETBRA~1\CLION2~1.4\bin\mingw\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Pierre-Luc\BattleBay_tool\main.c -o CMakeFiles\BattleBay_tool.dir\main.c.s

# Object files for target BattleBay_tool
BattleBay_tool_OBJECTS = \
"CMakeFiles/BattleBay_tool.dir/main.c.obj"

# External object files for target BattleBay_tool
BattleBay_tool_EXTERNAL_OBJECTS =

BattleBay_tool.exe: CMakeFiles/BattleBay_tool.dir/main.c.obj
BattleBay_tool.exe: CMakeFiles/BattleBay_tool.dir/build.make
BattleBay_tool.exe: CMakeFiles/BattleBay_tool.dir/linkLibs.rsp
BattleBay_tool.exe: CMakeFiles/BattleBay_tool.dir/objects1.rsp
BattleBay_tool.exe: CMakeFiles/BattleBay_tool.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable BattleBay_tool.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\BattleBay_tool.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/BattleBay_tool.dir/build: BattleBay_tool.exe
.PHONY : CMakeFiles/BattleBay_tool.dir/build

CMakeFiles/BattleBay_tool.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\BattleBay_tool.dir\cmake_clean.cmake
.PHONY : CMakeFiles/BattleBay_tool.dir/clean

CMakeFiles/BattleBay_tool.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Pierre-Luc\BattleBay_tool C:\Users\Pierre-Luc\BattleBay_tool C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug C:\Users\Pierre-Luc\BattleBay_tool\cmake-build-debug\CMakeFiles\BattleBay_tool.dir\DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/BattleBay_tool.dir/depend
