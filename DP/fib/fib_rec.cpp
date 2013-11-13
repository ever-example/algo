#include <iostream>

using namespace std;
int fib(int n);

int main() {

	int n;
	cout << "Enter which Fib. # to compute: " << endl;
	cin >> n;
	
	cout << "The number you entered was: " << n << endl;
	cout << "The corresponding Fib. is: " << fib(n) << endl;
}

int fib(int n) {
	if (n <= 2) return 1;
	else {
		int num = fib(n - 1) + fib(n - 2);
		return num;
	}
}
