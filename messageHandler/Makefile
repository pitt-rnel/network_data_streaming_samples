CXX = clang++
RPCLIB_DIR = </PATH/TO/RPCLIB/>

MSG_DIR = .
MSG_HDR = .
MSG_OBJ = ./obj/$(CFG)/$(OS)-$(ARCH)-$(COMPILER)
MSG_PROG = messageHandler
MSG_SOURCES = $(wildcard $(MSG_DIR)/*.cpp)
MSG_INCLUDES = $(wildcard $(MSG_DIR)/*.h)
MSG_OBJECTS = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(notdir $(MSG_SOURCES)))
MSG_OUTPUT = $(BASE_DIR)/$(MSG_PROG)
MSG_FLAGS = -DLINUX -Wno-deprecated -std=c++17 -I$(RPCLIB_DIR)/include/ 
MSG_LDFLAGS = -L$(RPCLIB_DIR)/build -lrpc -lpthread
