#include <bits/stdc++.h>
using namespace std;

int D(int x) { return (2 * x) % 10000; }
int S(int x) { return (10000 + x - 1) % 10000; }
int L(int x) { return (x % 1000) * 10 + (x / 1000); }
int R(int x) { return (x % 10) * 1000 + (x / 10); }

// last number, last method
int visited[10001][2];

void f(int a, int b)
{
    memset(visited, -1, sizeof(visited));
    visited[a][0] = a;
    visited[a][1] = 0;

    char commands[6] = {' ', 'D', 'S', 'L', 'R'};

    queue<int> q;
    q.push(a);

    while (!q.empty()) {
        const int mid = q.front();
        q.pop();

        if (mid == b) {
            string res;
            while (!visited[b][1] == 0) {
                res.push_back(commands[visited[b][1]]);
                b = visited[b][0];
            }
            reverse(res.begin(), res.end());
            printf("%s\n", res.c_str());
            return;
        }

        auto trackAndEmplace = [&](int x, int c) {
            if (visited[x][0] == -1) {
                visited[x][0] = mid;
                visited[x][1] = c;
                q.push(x);
            }
        };
        trackAndEmplace(D(mid), 1);
        trackAndEmplace(S(mid), 2);
        trackAndEmplace(L(mid), 3);
        trackAndEmplace(R(mid), 4);
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--) {
        int a, b;
        scanf("%d %d", &a, &b);
        f(a, b);
    }
}