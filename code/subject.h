#ifndef SUBJECT_H
#define SUBJECT_H
#include <vector>
#include <string>

class Piece;
class Observer;
class Subject {
  std::vector<Observer*> observers;
  public:
  //virtual ~Subject() {}
  void attach(Observer* o);
  void notifyObservers();
  virtual char getc() const = 0;
  virtual char getr() const = 0;
  virtual std::string getcolour() const = 0;
  virtual bool isoccupied() const = 0;
  virtual Piece* occupiedby() const = 0;
};


#endif

