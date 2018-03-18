#include <bits/stdc++.h>

using namespace std;
int x, y, n, test;
int main() {

	#ifndef ONLINE_JUDGE
	// freopen("5.in", "r", stdin);
	freopen("4.in", "w", stdout);
	#endif
	int test = 1000;
	cout << test << endl;

	while(test--) {
		cout << (x = rand() % 10 + 1) << ' ' << (y = rand() % 60 + 1) <<  ' ';
		n = rand() % 50 + 1;
 
		set<int> s;
		for(int i = 0; i <  n; i++) {
			int p = rand() % (60*24);
			s.insert(p);
		}
		cout << s.size() << endl;
		for(set<int> :: iterator it = s.begin(); it != s.end(); it++) {
			int p = *it;
			printf("%02d:%02d ", p/60, p%60);
		}
		cout << endl;
	}
}