import java.io.IOException;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
//import IOException


public class App {

	public static void main(String[] args) {
		
		ExecutorService executor = Executors.newCachedThreadPool();
		
		Future<Integer> future = executor.submit(new Callable<Integer>(){

			@Override
			public Integer call() throws Exception {
				Random random = new Random();
				
				int duration = random.nextInt(4000);
				if(duration > 2000){
					throw new IOException("Slept for too long");
				}
				System.out.println("Starting.");
				
				Thread.sleep(duration);
				
				System.out.println("Finished.");
				
				return duration;
			}
			
		});
		
		executor.shutdown();
		
		try {
			System.out.println("Future value is: " + future.get());
		} catch (InterruptedException e) {
			e.printStackTrace();
		} catch (ExecutionException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
			System.out.println(e);
		}
	}

}
