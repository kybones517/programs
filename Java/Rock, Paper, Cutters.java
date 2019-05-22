import java.util.Random;
import java.util.Scanner; 
class Main {
  public static void main(String[] args){
    Random r = new Random();
		Scanner sc = new Scanner(System.in); 
  String tools[] = new String[] {"Paper","Rock","Cutters"};
 int t = r.nextInt(tools.length);

   String tool = tools[t];   
   System.out.println(tool);
	 System.out.println("Input:");
	 String input = sc.nextLine();


  }
}
