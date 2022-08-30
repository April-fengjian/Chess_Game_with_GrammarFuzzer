chess: main.o checkerboard.o subject.o player.o square.o textdisplay.o graphicsdisplay.o king.o queen.o knight.o rook.o pawn.o piece.o bishop.o window.o
	g++ -std=c++14 *.o -o chess -lX11

main.o: main.cc checkerboard.h player.h
	g++ -std=c++14 -c main.cc

checkerboard.o: checkerboard.cc checkerboard.h square.h computer.h human.h player.h textdisplay.h graphicsdisplay.h queen.h king.h knight.h bishop.h rook.h pawn.h
	g++ -std=c++14 -c checkerboard.cc

square.o: square.cc square.h subject.h piece.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c square.cc

piece.o: piece.cc piece.h square.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c piece.cc

player.o: player.cc player.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c player.cc

textdisplay.o: textdisplay.cc textdisplay.h observer.h subject.h observer.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c textdisplay.cc

graphicsdisplay.o: graphicsdisplay.cc graphicsdisplay.h observer.h square.h piece.h subject.h window.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c graphicsdisplay.cc

subject.o: subject.cc subject.h observer.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c subject.cc

bishop.o: bishop.cc bishop.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c bishop.cc

king.o: king.cc king.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c king.cc

knight.o: knight.cc knight.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c knight.cc

pawn.o: pawn.cc pawn.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c pawn.cc

queen.o: queen.cc queen.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c queen.cc

rook.o: rook.cc rook.h piece.h checkerboard.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c rook.cc

window.o: window.cc window.h
	g++ -std=c++14 -Wall -MMD -Werror=vla -c window.cc

.PHONY: clean

clean:
	rm *.o chess
