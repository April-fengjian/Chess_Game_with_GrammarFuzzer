#include "rook.h"
using namespace std;
#include "square.h"
#include "checkerboard.h"
#include <vector>

Rook::Rook(string colour, Square *sq, Checkerboard *cb): 
  Piece(colour, sq, cb), moved{0} {
  value = 50;
  if (colour == "B") name = 'r';
  else if (colour == "W") name = 'R';
}

int Rook::getValue() const {
  return value;
}

char Rook::getname() const {
  return name;
}

void Rook::undo() { --moved; }

bool Rook::hasmoved() const {
  return moved;
}

bool Rook::can_move(Square *move) {
  if (cb->clearhorizontal(sq, move)) {
    return true;
  }
  if (cb->clearvertical(sq, move)) {
    return true;
  }
  return false;
}

void Rook::castling_move(Square *move) {
  move->setPiece(this);
  sq->setPiece(nullptr);
  sq->notifyObservers();
  ++moved;
  move->notifyObservers();
  sq = move;
}

