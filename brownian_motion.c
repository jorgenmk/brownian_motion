#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "randr.h"
#include <time.h>

#define RUNS       100000
#define ST         100
#define MY         0.45
#define ITERATIONS 1000
#define VARIANCE   0.3
#define DELTA_T    1.0/ITERATIONS
#define BARRIER    15
#define M_El	   2.718281828459045235360287471352662498

int main(void)
{
    clock_t begin, end;
    srand(time(NULL));
    double standard_dist[ITERATIONS];
    int broken = 0;
    double st_next = ST;
    begin = clock();
    for (int j = 0; j < RUNS; j++)
    {
        st_next = ST;
        randr_array(standard_dist, ITERATIONS);
        for (int i = 0; i < ITERATIONS; i++)
        {
            st_next = st_next * pow(M_El, ((MY-pow((0.5*VARIANCE),2))*(DELTA_T)+(standard_dist[i]*sqrt(DELTA_T))));
            if (st_next < BARRIER)
            {
                broken += 1;
                break;
            }
        }
        //printf("st_next: %f\n", st_next);
    }
    end = clock();
    printf("Broke: %d/%d\n", broken, RUNS);
    printf("Rate: %f%%\n", (broken*100.0)/RUNS);
    printf("Time spent: %f\n", (double)(end-begin)/CLOCKS_PER_SEC);
    printf("Simulation/sec: %f\n", (double)RUNS/((end-begin)/CLOCKS_PER_SEC));
}

