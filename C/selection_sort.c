#include <stdio.h>
#include <stdlib.h>

#define N 1000

int main(void) {
	int arr[N];
	int i, j, t;
	for (i = 0; i < N; i++) arr[i] = rand();
	
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (arr[i] > arr[j]) {
				t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}
	
	return 0;
}
