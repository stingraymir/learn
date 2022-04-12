# convert to python code
"""
function f(A){
  if (A.length < 2)
    return A.length;
    
  let best = 1;
  let bestLower = 1;
  let bestHigher = 1;
  
  for (let i=1; i<A.length; i++){
    if (A[i] == A[i-1]){
      bestLower = bestLower + 1;
      bestHigher = bestHigher + 1;
    
    } else if (A[i] - 1 == A[i-1]){
      bestLower = 1 + bestHigher;
      bestHigher = 1;
    
    } else if (A[i] + 1 == A[i-1]){
      bestHigher = 1 + bestLower;
      bestLower = 1;
    
    } else {
      bestLower = 1;
      bestHigher = 1;
    }

    best = Math.max(best, bestLower, bestHigher);
  }
  
  return best;
}
"""

def f(A):
    if len(A) < 2:
        return len(A)
    best = 1
    bestLower = 1
    bestHigher = 1
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            bestLower = bestLower + 1
            bestHigher = bestHigher + 1
        elif A[i] - 1 == A[i-1]:
            bestLower = 1 + bestHigher
            bestHigher = 1
        elif A[i] + 1 == A[i-1]:
            bestHigher = 1 + bestLower
            bestLower = 1
        else:
            bestLower = 1
            bestHigher = 1
        best = max(best, bestLower, bestHigher)
    return best

    


