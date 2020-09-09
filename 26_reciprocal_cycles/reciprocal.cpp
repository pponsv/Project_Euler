/* *Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. */
#include <bits/stdc++.h> 
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

string div(int n) {
	bool end = false;
	string div = "0.";
	int rem = 10;
	for (int i=0;i<1000;i++) {
		int app = rem/n;
		rem = 10*(rem % n);
		/* cout << app << " " << rem << endl; */
		div.append(to_string(app));
	}
	return div;
}

int len_subs(int num) {
	string s = div(num);
	int s_len = s.length();
	int len = 0;
	for (int i = 0; i < s_len; i++) {
		for (int j = i+1; j < s_len; j++) {
			if (s[i] == s[j]) {
				string s_b = s.substr(i,j-i);
				string s_t = s.substr(j,j-i);
				/* cout << s_b << s_t << endl; */
				if (s.substr(i,j-i) == s.substr(j,j-i)) {
					len = max(len,j-i);
					if (s_b == s.substr(j+j-i,j-i)) {
						break;}
				}
			}		
		}
	}
	return len;
}

int main(void) {
	int len = 0;
	int N = 0;
	int nlen = 0;
	for (int n = 2; n<1000; n++) {
	/* cout << div(n) << endl; */
		nlen = len_subs(n);
		if (nlen > len) {
			N = n;
			len = nlen;
		}
		cout << N << ' ' << len << endl;
	}
	cout << div(N) << endl;
	/* cout << len_subs(7); */
	
}

