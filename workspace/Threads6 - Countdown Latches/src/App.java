import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Processor implements Runnable
{
	private CountDownLatch latch;
	
	public Processor(CountDownLatch latch)
	{
		this.latch = latch;
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("Started.");
		
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		latch.countDown();
	}
	
}

public class App {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final int init_count = 4;
		final int pool_size = 4;
		CountDownLatch latch = new CountDownLatch(init_count);
		ExecutorService executor = Executors.newFixedThreadPool(pool_size);
		
		for(int i=0; i<pool_size; i++)
		{
			executor.submit(new Processor(latch));
		}
		
		try {
			latch.await();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Completed.");
	}

}
