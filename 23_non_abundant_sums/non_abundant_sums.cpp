/* Encontrar la suma de todos los números naturales que no pueden ser escritos como suma de números abundantes */

#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int sumdivisors (int n) {
	int suma = 0;
	/* cout << sqrt(n) << endl; */
	for (int i=1;i<=sqrt(n);i++) {
		if (n%i == 0) {
			suma += i + n/i;
			if (i == sqrt(n)) {
				suma -= i;
			}
		}
	}
	return suma - n;
}

bool isabundant (int n) {
	return (sumdivisors(n) > n);
}

vector<int> abundants (int max) {
	vector<int> abs = {};
	for (int i=1;i<max;i++) {
		if (isabundant(i)) {
			abs.push_back(i);
		}
	}
	return abs;
}

void vprint(vector <int> const &a) {
   for(unsigned i=0; i < a.size(); i++)
      cout << a.at(i) << ' ';
   cout << endl;
}

int main () {
	int max = 28124;
	vector<int> abs = abundants(max);
	vector<int> numbers = {};
	for (int i = 0;i<28124;i++) {
		numbers.push_back(i);
	}
	for (unsigned i=0; i<abs.size();i++) {
		for (unsigned j=0; j<abs.size(); j++) {
			int tmp = abs[i]+abs[j];
			if (tmp > max) {
				break;
			}
			numbers[tmp] = 0;
		}
	}
	int suma = 0;
	for (auto& n : numbers) {
    	suma += n;
	}
	cout << suma << endl;	
}

