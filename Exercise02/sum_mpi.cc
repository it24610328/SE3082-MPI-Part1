#include <cstdio>
#include <cstdlib>
#include <mpi.h>
int main(void)
{
    int rank, size;
    MPI_Init(NULL, NULL);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // IT24610328 - Ex2 - Added N and per process range split
    const long long N = 10000000;
    long long chunk = N / size;
    long long start = rank * chunk + 1;
    long long end = (rank == size - 1) ? N : start + chunk - 1;

    // IT24610328 - Ex2 - Added barrier and timer
    MPI_Barrier(MPI_COMM_WORLD);
    double t0 = MPI_Wtime();

    // IT24610328 - Ex2 - Added local sum over own range
    long long local = 0, total = 0;
    for (long long i = start; i <= end; i++)
        local += i;

    // IT24610328 - Ex2 - Added reduce of local sums to rank 0
    MPI_Reduce(&local, &total, 1, MPI_LONG_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    double t1 = MPI_Wtime();
    if (rank == 0) {
        printf("Processes = %d\n", size);
        printf("Sum = %lld (expected 50000005000000)\n", total);
        printf("Time = %f seconds\n", t1 - t0);
    }
    MPI_Finalize();
}
