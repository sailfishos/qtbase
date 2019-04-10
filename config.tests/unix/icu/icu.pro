SOURCES = icu.cpp
CONFIG += console
CONFIG -= qt dylib
CONFIG += c++11

include($$PWD/../../../src/3rdparty/icu_dependency.pri)
