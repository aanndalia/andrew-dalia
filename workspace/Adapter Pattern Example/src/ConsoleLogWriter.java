/* Adapter class that uses composition.
 * Implements client interface LogWriter and
 * Composes of using the alternative interface ConsoleWriter (the adaptee) */
public class ConsoleLogWriter implements LogWriter{

	private ConsoleWriter consoleWriter;
	
	public ConsoleLogWriter() {
		this.consoleWriter = new ConsoleWriter();
	}
	
	@Override
	public void out(String text) {
		consoleWriter.writeConsole(text);
	}

}
