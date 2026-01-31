#include "vector.h"
#include <iostream>

int main() {
  vector<int> arr;
  for (int i = 0; i < 10; i++) {
    arr.append(i);
  }

  std::cout << arr.pop();
  arr.remove(2);

  for (int i = 0; i < arr.len(); i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;
}