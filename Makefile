CC=g++
CFLAGS=-c -fPIC
SOURCES=foo.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=BellmanFord

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(CFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) -shared -Wl,-soname,libfoo.so $< -o $@

clean:
	-find . -name '*.o' -exec rm -r {} \;
	-find . -name '*.so' -exec rm -r {} \;
