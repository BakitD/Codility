

int solution(int A[], int B[], int N) {
    int counter = 0;
    int last;
    if (N > 0) {
        counter = 1;
        last = B[0];
        for (int i = 0; i < N; i++) {
            if (A[i] > last) {
                last = B[i];
                counter++;
            }
        }
    }
    return counter;
}