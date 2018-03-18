#include <bits/stdc++.h>

using namespace std;
string s;
vector<int> v;
int t;

int main() {
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);
	cin >> t;
	while (t--) {
		cin >> s;
		v.clear();
		int n = s.size();

		for(int i = 0; i < n; i++) {
			v.push_back(s[i] - '0');
		}

		sort(v.begin(), v.end());

		for(int i = 0; i < n; i++) {
			if (v[i] != 0) {
				swap(v[i], v[0]);
				break;
			}
		}

		for(int i = 0; i < n; i++) {
			cout << v[i];
		}
		if (t) 
			cout << endl;
	}

	return 0;
}