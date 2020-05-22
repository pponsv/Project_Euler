/* A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are: 

012   021   102   120   201   210 

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? */

/* Este método es de fuerza bruta porque me hacía ilusión aprender a crear permutaciones */

#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

void vprint(vector <int> const &a) {
   for(unsigned i=0; i < a.size(); i++)
      cout << a.at(i);
   cout << endl;
}

int main() {
	vector<int> nums{0,1,2,3,4,5,6,7,8,9};
	int n = 1;
	while (n<1000000) {
		n += 1;
		for (int i=nums.size()-1;i>=0;i--) {
			if (nums[i] > nums[i-1]) {
				for (int j=nums.size()-1;j>i-1;j--) {
					if (nums[i-1] < nums[j]) {
						swap(nums[i-1],nums[j]);
						reverse(begin(nums) + i,end(nums));
						break;
					}
				}
				break;
			}
		}
	}
	vprint(nums);
}


