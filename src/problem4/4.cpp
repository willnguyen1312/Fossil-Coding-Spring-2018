#include <bits/stdc++.h>

using namespace std;
int t, n, x, y;

int main() {
	freopen("4.in", "r", stdin);
	freopen("4.out", "w", stdout);
	cin >> t;

	while (t--) {
		cin >> x >> y >> n;
		std::vector<int> v;
		bool ok = false;

		for(int i = 0; i < n; i++) {
			int hour, minu;

			scanf("%2d:%2d ", &hour, &minu);
			int p = hour*60 + minu;
			v.push_back(p);
		}

		if (x == 1) {
			printf("%02d:%02d\n", v[0]/60, v[0]%60);
			continue;
		}

		for(int i = 1; i < v.size(); i++) {
			int k = i - x + 1;
			if (k >= 0 && v[i] - v[k] < y) {
				printf("%02d:%02d\n", v[i]/60, v[i]%60);
				ok = true;
				break;
			}
		}

		if (!ok) {
			cout << "can not wake!" << endl;
		}
	}

	return 0;
}