def bucketsort( A ):
  code = hashing( A )
  buckets = [list() for _ in range( code[1] )]
  for i in A:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )
  for bucket in buckets:
    insertionsort( bucket )
  ndx = 0
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      A[ndx] = v
      ndx += 1
import math
def hashing( A ):
  m = A[0]
  for i in range( 1, len( A ) ):
    if ( m < A[i] ):
      m = A[i]
  result = [m, int( math.sqrt( len( A ) ) )]
  return result
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )
s=list(map(int,input().split()))
S=subsets(s)
print(S)
