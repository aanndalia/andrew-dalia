
public class Test {

	public static int[] NonZeros( int [] A )
	{
		int length = A.length;
		int new_length = 0;
		for(int i=0; i < length; ++i)
		{
			if(A[i] != 0)
			{				
				new_length++;
			}			
		}
		
		int nA[] = new int[new_length];
		int nidx = 0;
		for(int i=0; i < length; ++i)
		{
			if(A[i] != 0)
			{				
				nA[nidx++] = A[i];
			}			
		}
		
		return nA;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr1[] = {0,1,2,3,2};
		System.out.print("passed ");
		for(int i = 0; i < arr1.length; ++i)
		{
			System.out.print(arr1[i] + " ");
		}
		System.out.println();
		System.out.print("got back ");
		int ret[] = NonZeros(arr1);
		for(int i = 0; i < ret.length; ++i)
		{
			System.out.print(ret[i] + " ");
		}
	}

}
