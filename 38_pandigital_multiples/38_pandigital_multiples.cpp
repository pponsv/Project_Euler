#include <iostream>
#include <string>
#include <unordered_set>
#include <sstream>
#include <math.h>

using namespace std;

const string numbers = "123456789";
unordered_set <char> nums(begin(numbers), end(numbers));

bool is_pandigital (int n) {
	string strn = to_string(n);
	unordered_set <char> str_set(begin(strn), end(strn));
	bool result;
	if (str_set == nums) {
		result = true;
	}
	else {
		result = false;
	}
	return result;
}

int concat_nine (int N) {
	string concat = "";
	int n = 1;
	int conc = 0;
	while (concat.length() < 9) {
		concat.append(to_string(n*N));
		n++;
	}
	if (concat.length() == 9) {
		conc = stoi(concat);
		if (is_pandigital(conc) == false) {
			conc = 0;
		}
	}
	return conc;
}


int main () {
	int max_concat = 0;
	for (int i = 9999; i > 0; i--) {
		max_concat = max(max_concat,concat_nine(i));
	}
	cout << max_concat << endl;
}

