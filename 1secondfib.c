#include <iostream>
#include <time.h>

time_t current_time = time(NULL) ;

unsigned int n;
long long n1 = 0;
long long n2 = 1;

int j = 1;


int main()
{
  while (current_time + 1 >=   time(NULL))
  {
    n = n1 + n2;
    n1 = n2 ;
    n2 = n ;
    j++ ;
  
  }
  std::cout << "the" << j << "'th number is " << n <<".\n";
  
  std::cout <<"validity check, these numbers divided should say about 1.7  " << n << "/" << n1 << " \n";
}

