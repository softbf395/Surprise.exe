cmake_minimum_required(VERSION 3.10)
project(SurpriseApp)

add_executable(app_exe main.cpp)

# Add custom command to encode the executable after build
add_custom_command(TARGET app_exe POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:app_exe> ${CMAKE_BINARY_DIR}/app.exe
    COMMAND python ${CMAKE_SOURCE_DIR}/encoder.py ${CMAKE_BINARY_DIR}/app.exe ${CMAKE_BINARY_DIR}/encoded.exe
    COMMAND python ${CMAKE_SOURCE_DIR}/add_hint.py ${CMAKE_BINARY_DIR}/encoded.exe
)
