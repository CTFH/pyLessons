import java.io.*;

public class Converter {
	public static void main(String[] args) throws IOException{
		final String FROM = "SJIS";
		final String TO ="UTF8";
		if(args.length == 0) {
			System.out.println("実行時にファイル名を指定してください");
			return;
		}
		FileInputStream fis=new FileInputStream(args[0]);
		InputStreamReader isr=new InputStreamReader(fis,FROM);
		BufferedReader br=new BufferedReader(isr);

		FileOutputStream fos=new FileOutputStream("new_"+args[0]);
		OutputStreamWriter osw=new OutputStreamWriter(fos,TO);
		BufferedWriter bw=new BufferedWriter(osw);

		String line;
		while((line =br.readLine()) != null) {
			bw.write(line);
			bw.newLine();
		}
		br.close();
		bw.close();
	}
}
