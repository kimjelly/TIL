#include <bits/stdc++.h>
using namespace std;

int a[10001] = {0};
int dp[3][2] = {0};

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) 
        scanf("%d", &a[i]);
    int d = 1;
    dp[0][d] = 0;
    dp[1][d] = a[1];
    dp[2][d] = 0;

    for (int i = 2; i <= n; ++i) {
        d = !d;
        dp[0][d] = max(max(dp[0][!d], dp[1][!d]), dp[2][!d]);
        dp[1][d] = dp[0][!d] + a[i];
        dp[2][d] = dp[1][!d] + a[i];
    }

    printf("%d\n", max(max(dp[0][d], dp[1][d]), dp[2][d]));
}

/* 답 안 보고 직접 풀었음
 * dp[0], dp[1], dp[2]는 각각 몇 칸 떨어졌는지를 나타냄
 *
 * 더 좋은 방법이 있을까?
 * - 어차피 이전 상태만 본다면 scanf로 입력 받으면서 해결 가능
 * - dp[3][2]가 아니라 dp[3] + 임시변수 하나로 표현 가능
 */