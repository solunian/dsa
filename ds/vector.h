#ifndef VECTOR_H
#define VECTOR_H

template <typename T>
class vector {
 private:
  int size;
  int length;
  T* arr;

  void resize(int new_size);

 public:
  vector();

  ~vector();

  int len() const;

  T& operator[](int i);

  T remove(int i);

  void insert(int i, const T& x);

  void append(const T& x);

  T pop();
};

// TEMPLATED IMPLEMENTATION WRITTEN BELOW!

#include <stdexcept>

const static int INITIAL_SIZE = 100;

template <typename T>
void vector<T>::resize(int new_size) {
  T* new_arr = new T[new_size];
  int smaller = (new_size < length) ? new_size : length;
  for (int i = 0; i < smaller; i++) {
    new_arr[i] = arr[i];
  }
  delete[] arr;
  arr = new_arr;
  size = new_size;
}

template <typename T>
vector<T>::vector() {
  size = INITIAL_SIZE;
  length = 0;
  arr = new T[INITIAL_SIZE];
}

template <typename T>
vector<T>::~vector() {
  delete[] arr;
}

template <typename T>
int vector<T>::len() const {
  return length;
}

template <typename T>
T& vector<T>::operator[](int i) {
  if (i < 0 || i >= length) {
    throw std::out_of_range("index i out of range");
  }

  return arr[i];
}

template <typename T>
T vector<T>::remove(int i) {
  if (i < 0 || i >= length) {
    throw std::out_of_range("index i out of range");
  }

  T removed = arr[i];
  for (int j = i + 1; j < length; j++) {
    arr[j - 1] = arr[j];
  }
  length--;

  return removed;
}

template <typename T>
void vector<T>::insert(int i, const T& x) {
  if (i < 0 || i > length) {  // can insert at i = len equiv to append(x)
    throw std::out_of_range("index i out of range");
  }

  if (length == size) {
    resize(size * 2);
  }

  for (int j = length; j > i; j--) {
    arr[j] = arr[j - 1];
  }
  arr[i] = x;
  length++;
}

template <typename T>
void vector<T>::append(const T& x) {
  insert(length, x);
}

template <typename T>
T vector<T>::pop() {
  return remove(length - 1);
}

#endif