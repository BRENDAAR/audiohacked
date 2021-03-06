import java.lang.String;
import java.lang.Integer;

public class Ring0DataStore
{
	/* store the Network base port number for the nodes */
	public static int netport_base = 9130;
	
	/* store the base name of the input file */
	public static String infile_name = new String("input-file-");
	
	/* store the base name of the output file */
	public static String outfile_name = new String("output-file-");

	/* store the base name of the output file */
	public static String statusfile_name = new String("status-file-");
	
	/* store the maximum THT byte count of a frame */
	public static Integer tht_byte_count = new Integer(400);
}

