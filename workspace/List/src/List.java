/*
 *  List class
 *    
 *  A List is an ordered collection of any kind of Object.
 * 
 *  Operations:
 *     AddToEnd    Add a given object to the end of the list.
 *     Print       Print (to standard output) the objects in the list in order,
 *                 enclosed in square brackets, separated by spaces.
 */
class List {
  private static final int INIT_LEN = 10;
  private Object [] items;  // the actual items
  private int numItems;     // the number of items currently in the list
  private int currentObject;
  
  /*
   * constructor: initialize the list to be empty
   */
  public List()
  {
    items = new Object [INIT_LEN];
    numItems = 0;
    currentObject = 0;
  }

  /*
   * AddToEnd
   *
   * Given: Object ob
   * Do:    Add ob to the end of the list.
   */
  public void AddToEnd(Object ob)
  {
	  if(numItems == items.length)
	  {
		  Object [] temp = new Object[items.length];
		  for(int i=0; i < items.length; ++i)
		  {
			  temp[i] = items[i];
		  }
		  
		  items = new Object[items.length * 2];
		  
		  for(int i=0; i < temp.length; ++i)
		  {
			  items[i] = temp[i];
		  }
	  }
	  
	  items[numItems++] = ob;
  }
  
  /*
   * Print
   *
   * Print (to standard output) the objects in the list in order, enclosed in
   * square brackets, separated by spaces.
   */
  public void Print()
  {
	  if(items.length == 0)
	  {
		  System.out.println("[]");
		  return;
	  }
	  
	  System.out.print("[");
	  for(int i=0; i < numItems - 1; ++i)
	  {
		  System.out.print(items[i] + " ");
	  }
	  System.out.print(items[numItems - 1]);
	  System.out.print("]");
  }
  
  public void firstElement()
  {
	  currentObject = 0;
  }
  
  public Object nextElement()
  {
	  return items[currentObject++];
  }
  
  public boolean hasMoreElements()
  {
	  if(items.length == 0 || (currentObject >= numItems))
	  {
		  return false;
	  }
	  else
	  {
		  return true;
	  }
  }
}