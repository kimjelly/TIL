#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;    

    set<pair<int, string>> s;
    scanf("%d\n", &n);

    char str[50];

    for (int i = 0; i < n; ++i) {
        scanf("%s", str);
        s.emplace(strlen(str), str);
    }

    for (const auto& p : s) {
        puts(p.second.data());
    }
}
