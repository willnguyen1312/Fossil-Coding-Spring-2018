#include <bits/stdc++.h>

using namespace std;
int t, n, x;

bool cmp(int x, int y) {
	return y < x;
}

int main() {
	freopen("8.in", "r", stdin);
	freopen("8.out", "w", stdout);
	cin >> t;

	while (t--) {
		vector<int> v;
		vector<int> k;
		cin >> n;
		while(n--) {
			cin >> x;
			v.push_back(x);
			k.push_back(x);
		}

		map<int, int> h;
		
		sort(v.begin(), v.end(), cmp);

		if (v.size() == 0)
			continue;
		if (v.size() == 1) {
			cout << 1 <<  endl;
			continue;
		}

		int rnk = 1;

		for(int i = 0; i < v.size()-1; i++) {
			if(v[i] == v[i+1]) {
				h[v[i]] = rnk;
				h[v[i+1]] = rnk;
			} else {
				h[v[i]] = rnk;
				rnk = i+2;
				h[v[i+1]] = rnk;
			}
		}

		for(int i = 0; i < k.size(); i++) {
			cout << h[k[i]] << ' ';
		}
		cout << endl;
	}

	return 0;
}