
# Set the minimum version of CMake that's required 
cmake_minimum_required(VERSION 3.12)

# make sure the source and binary directories are different
# this is here to prevent so-called "in-source" builds where the root directory of the source
# is also the root directory of the build
get_filename_component(srcdir "${CMAKE_SOURCE_DIR}" REALPATH)
get_filename_component(bindir "${CMAKE_BINARY_DIR}" REALPATH)
if ("${srcdir}" STREQUAL "${bindir}")
  message(FATAL_ERROR "No support for in-source builds.")
endif()

# Set the project name
project(framework-testbench LANGUAGES CXX)

# Load additional macros used by this project. 
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# Load the BuildMacros module. If loaded correctly, the variable 
# 'build_macros_found' will be set to the path of the module.  Otherwise, it
# is set to NOTFOUND.
include(BuildMacros RESULT_VARIABLE build_macros_found)

# If an install location hasn't been set via CMAKE_INSTALL_PREFIX, set it to 
# a reasonable default ($PWD/install).  
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX $ENV{HOME}/.local CACHE PATH "" FORCE)
  message(STATUS "Install directory set to ${CMAKE_INSTALL_PREFIX}")
endif()

# If a user is building outside of a Docker or Singularity environment, 
# warn them. 
if (NOT EXISTS /.dockerenv AND NOT EXISTS /singularity)
  message(WARNING "You are not inside a container; you may be working in an untested environment.")
endif()

# Set the python installation path
set(PYTHON_PACKAGE_NAME LDMX)

# Set the default release type to "Debug". If a release type is specified 
# at the command line, it's respected.
set(default_build_type "Debug")
if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
 message(STATUS "Setting build type to '${default_build_type}' as none was specified.")
 set(CMAKE_BUILD_TYPE "${default_build_type}" CACHE STRING "Choose the type of build." FORCE)
endif()

# Clear any variables cached during previous configuration cycles. 
clear_cache_variables()

# Start by building all of the classes needed for building the event bus and 
# ROOT dictionary. This is on by forcing the global "BUILD_EVENT_ONLY" option
# here.
set(BUILD_EVENT_ONLY ON CACHE BOOL "Build the SimCore library." FORCE)

add_subdirectory(Bench ${CMAKE_BINARY_DIR}/BenchEvent)

# Once the event libraries have been built, turn off the global option. 
set(BUILD_EVENT_ONLY OFF CACHE BOOL "Build the SimCore library." FORCE)

# The framework has all the backend code needed to run all processors.
add_subdirectory(Framework)

# This module contains all detector service related code.  Needed by recon. 
add_subdirectory(Bench)
