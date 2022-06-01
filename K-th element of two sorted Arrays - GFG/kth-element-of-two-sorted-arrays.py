#User function Template for python3
import sys
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n>m:
            return self.kthElement(arr2,arr1,m,n,k)
        l=max(0,k-m)
        r=min(k,n)
        
        inf=sys.maxsize
        
        while l<=r:
            cut1=l+(r-l)//2
            cut2=k-cut1
            
            l1=-inf if cut1==0 else arr1[cut1-1]
            l2=-inf if cut2==0 else arr2[cut2-1]
            r1=inf if cut1==n else arr1[cut1]
            r2=inf if cut2==m else arr2[cut2]
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            if l1>r2:
                r=cut1-1
            else:
                l=cut1+1
            
        
        
            
                
    
        
            
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends