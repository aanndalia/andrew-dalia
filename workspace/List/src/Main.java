
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List list = new List();
		
		list.AddToEnd(1);
		list.AddToEnd(2);
		list.AddToEnd(3);
		
		list.Print();
		System.out.println();
		// now iterate through the list, printing each item
	    list.firstElement();
	    while (list.hasMoreElements()) 
	    {
	        //String tmp = (String)list.nextElement();
	    	Object tmp = list.nextElement();
	        System.out.println(tmp);
	    }
	}

}
