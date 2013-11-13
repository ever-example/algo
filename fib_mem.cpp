#include <iostream>
#include <vector>

using namespace std;

int fib(int n);

int main() {

	int n;
	cout << "Enter which Fib. # to compute for: ";
	cin >> n;

	cout << "The number you entered was: " << n << endl;
	cout << "The corresponding Fib. is: " << fib(n) << endl;
}

int fib(int n) {
	static std::vector<int> fibs;
	int num;
	if (n < fibs.size()) {
		return fibs.at(n-1);
	} else if (n <= 2) {
		num = 1;
	} else {
		num = fib(n-1) + fib(n-2);
	}
	fibs.push_back(num);
	return num;
}
