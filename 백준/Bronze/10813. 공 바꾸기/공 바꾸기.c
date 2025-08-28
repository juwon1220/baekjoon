#include <stdio.h>
#include <stdlib.h>
int main(void) {

	// 1 ~ N까지 바구니에
	// 1 ~ N번호가 적힌 공이 들어 있다!!
	int N, M;
	scanf("%d%d", &N, &M);

	int *array = (int *)calloc(N, sizeof(int));
	if (array == NULL) exit(1);
	
	for (int i = 0; i < N; i++) {
		array[i] = i + 1;
	}
	
	//for (int i = 0; i < N; i++) printf("%d ", array[i]);
	//printf("\n");

	for (int a = 0; a < M; a++)
	{
		int i, j;
		scanf("%d %d", &i, &j);

		int temp = array[i-1];
		array[i-1] = array[j-1];
		array[j-1] = temp;

		/*for (int i = 0; i < N; i++) printf("%d ", array[i]);
		printf("\n");*/
	}
	for (int i = 0; i < N; i++) printf("%d ", array[i]);
	printf("\n");

	free(array);


	return 0;
}