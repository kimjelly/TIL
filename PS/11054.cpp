#include <bits/stdc++.h>
using namespace std;

int a[1001] = {0};
int is[1001] = {0};
int ds[1001] = {0};

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);

    for (int i = 0; i < n; ++i) {
        int max_is = 0;
        int max_ds = 0;
        for (int j = 0; j < i; ++j) {
            // LIS
            if (a[i] > a[j])
                max_is = max(max_is, is[j]);
            // LDS in reverse = LIS
            if (a[n - 1 - i] > a[n - 1 - j])
                max_ds = max(max_ds, ds[n - 1 - j]);
        }
        is[i] = max_is + 1;
        ds[n - 1 - i] = max_ds + 1;
    }

    int ret = 0;
    for (int i = 0; i < n; ++i) {
        ret = max(ret, is[i] + ds[i]);
    }
    printf("%d\n", ret - 1);
}

/* is[i] = max length of LIS from A[0..i] (always contain A[0])
 * ds[i] = max length of LDS from A[i..n-1] (always contain A[n-1])
 * time = O(N^2), memory = O(N)
 */