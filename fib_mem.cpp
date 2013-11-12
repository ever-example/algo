#include <iostream>
#include <vector>

using namespace std;

int fib(int n);
std::vector<int> fibs;

int main() {

	int n;
	cout << "Enter which Fib. # to compute for" << endl;
	cin >> n;

	cout << "The number you entered was: " << n << endl;
	cout << "The corresponding Fib. is: " << fib(n) << endl;
}

int fib(int n) {
	if (n <= 2) {
		return 1;
	} else if (n < fibs.size()) {
		return fibs.at(n);
	} else {
		int num = fibs.at(n-1) + fibs.at(n-2);
		return num;
	}
}
