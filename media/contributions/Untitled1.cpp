#include <stdio.h>
#include <stdlib.h>

int bit_return(int a, int loc) // Bit returned at location
{
  int buf = a & 1<<loc;
  if (buf == 0)
    return 0;
  else
    return 1;
}

int main()
{
  int a = 289642; // Represent 'a' in binary
  int i = 0;
  for (i = 31; i>=0; i--)
  {
    printf("%d",bit_return(a,i));
  }
  return 0;
}
