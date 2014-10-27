MODULES = randr.c brownian_motion.c

PROG = br_m

CDEFS = -std=c99 -Os 

LIBS = -lm

all:
	gcc $(MODULES) $(CDEFS) $(LIBS) -o $(PROG)
