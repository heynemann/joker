cmake_minimum_required (VERSION 2.6)
project (Joker)
list(APPEND CMAKE_CXX_FLAGS "-std=c++0x ${CMAKE_CXX_FLAGS} -g -lproxygenhttpserver -lfolly -lglog -lgflags -pthread")


set (PROJECT_BINARY_DIR ${PROJECT_BINARY_DIR}/bin)
set (PROJECT_SOURCE_DIR ${PROJECT_SOURCE_DIR}/src)

# The version number.
set (Joker_VERSION_MAJOR 1)
set (Joker_VERSION_MINOR 0)

include_directories ("${PROJECT_SOURCE_DIR}/handlers")
add_subdirectory (${PROJECT_SOURCE_DIR}/handlers)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/JokerConfig.h.in"
  "${PROJECT_BINARY_DIR}/JokerConfig.h"
)

# add the binary tree to the search path for include files
# so that we will find JokerConfig.h
include_directories("${PROJECT_BINARY_DIR}")

add_executable(Joker ${PROJECT_SOURCE_DIR}/server.cpp)
target_link_libraries (Joker handlers)

install (TARGETS Joker DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/JokerConfig.h" DESTINATION include)
