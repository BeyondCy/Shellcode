#include <stdint.h>
#include <stdio.h>
#include <unistd.h>
#include <iostream>

using namespace std;

//Coded By B3mB4m
//Credits for blog.badtrace.com
//I just convert it C to C++ :)


int main(void){
	uint64_t rdtsc, rdtsc2;
	unsigned eax, edx,total=0;

	for (int i = 0; i < 10; ++i){
		__asm__ volatile("rdtsc" : "=a" (eax), "=d" (edx));
		rdtsc  = ((unsigned long long)eax) | (((unsigned long long)edx) << 32);
		__asm__ volatile("rdtsc" : "=a" (eax), "=d" (edx));
		rdtsc2  = ((unsigned long long)eax) | (((unsigned long long)edx) << 32);
		cout << "Avarage : " <<  rdtsc2-rdtsc << endl;
		total += rdtsc2-rdtsc;
	}cout << "Total avarage : " << total / 10 << endl;
	if (total > 200)
		cout << "VM Detected" << endl;
	else
		cout << "VM Not Present" << endl;	
	
}
