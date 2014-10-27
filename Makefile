MODULES = randr.c brownian_motion.c

PROG = br_m

CFLAGS = -std=c99 -O3 -Wall

LIBS = -lm

all:
	gcc $(MODULES) $(CFLAGS) $(LIBS) -o $(PROG)
