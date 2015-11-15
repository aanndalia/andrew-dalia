
/* Adapter class that uses inheritance */
public class ConsoleLogWriter2 extends ConsoleWriter implements LogWriter {

	@Override
	public void out(String text) {
		// TODO Auto-generated method stub
		writeConsole(text);
	}

}
