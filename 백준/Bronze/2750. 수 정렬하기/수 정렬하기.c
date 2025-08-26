#include <stdio.h>
void bubble_sort(int *pa, int size);
void print_array(int *pa, int size);
void swap(int *pa, int *pb);
int main(void) {
	int N;
	scanf("%d", &N);

	int array[N];

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
	}
	/*int array[5] = { 79, 2, 34, 55, 10 };
	bubble_sort(array, 5);
	print_array(array, 5);*/

	
	bubble_sort(array, N);
	print_array(array, N);

	return 0;
}
void bubble_sort(int *pa, int size)
{	// 오름차순 정렬 : 오른쪽으로 갈수록 커져야 한다
	// 인접한 두 요소 비교해서
	// 만약, 왼쪽이 더 크면 오른쪽 값과 치환
	int *po = pa;

	// 내가 짠 코드
	for (int i = size; i > 0; i--)
	{
		for (int j = 0; j < i-1; j++)
		{
			if (pa[j] > pa[j + 1])
			{
				swap(pa + j, pa + j + 1);
			}
		}
	}





	//// w. 교수님
	//// step.1
	//if (*(pa + 0) > *(pa + 1))
	//{
	//	swap(pa + 0, pa + 1);
	//}
	//if (*(pa + 1) > *(pa + 2))
	//{
	//	swap(pa + 0, pa + 1);
	//}
	//// 이렇게 4번 진행하면 가장 오른쪽이 가장 큰 값이 될 겁니다
	//// => for문
	//for (int i = 0; i < size - 1; i++)
	//{
	//	if (*(pa + i) > *(pa + i + 1))
	//	{
	//		swap(pa + i, pa + i + 1);
	//	}
	//}

	//// step.2
	//for (int i = 0; i < size - 2; i++)
	//{
	//	if (*(pa + i) > *(pa + i + 1))
	//	{
	//		swap(pa + i, pa + i + 1);
	//	}
	//}
	//
	//// step.3
	//for (int i = 0; i < size - 3; i++)
	//{
	//	if (*(pa + i) > *(pa + i + 1))
	//	{
	//		swap(pa + i, pa + i + 1);
	//	}
	//}

	//// 반복 되니깐 for문으로~
	//for (int j = 1; j < size; j++)
	//{
	//	for (int i = 0; i < size - j; i++)
	//	{
	//		if (*(pa + i) > *(pa + i + 1))
	//		{
	//			swap(pa + i, pa + i + 1);
	//		}
	//	}
	//}

}

void print_array(int *pa, int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", pa[i]);
	}
	printf("\n");
}

void swap(int *pa, int *pb)
{
	int temp;
	temp = *pa;
	*pa = *pb;
	*pb = temp;
}