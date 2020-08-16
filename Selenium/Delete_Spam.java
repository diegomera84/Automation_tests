import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.sikuli.basics.Settings;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Pattern;
import org.sikuli.script.Screen;
 
import static org.sikuli.script.Mouse.WHEEL_UP;
 
public class Delete_Spam_Gmail {
    public static void main(String[] args) throws FindFailed, InterruptedException {
        Screen screen = new Screen();
        Pattern pattern = new Pattern("/home/diego/Documents/SikuliX/Spam/recibidos.png");
        Pattern pattern2 = new Pattern("/home/diego/Documents/SikuliX/Spam/mas.png");
        Pattern pattern3 = new Pattern("/home/diego/Documents/SikuliX/Spam/menos.png");
        Pattern pattern4 = new Pattern("/home/diego/Documents/SikuliX/Spam/spam.png");
        Pattern pattern5 = new Pattern("/home/diego/Documents/SikuliX/Spam/selector.png");
        Pattern pattern6 = new Pattern("/home/diego/Documents/SikuliX/Spam/eliminar.png");
 
 
        System.setProperty("webdriver.gecko.driver","/home/diego/Documents/Sikuli/geckodriver");
        WebDriver driver = new FirefoxDriver();
 
        driver.get("http://gmail.com"); //There must be an open session
 
        screen.wheel(pattern, WHEEL_UP, 10); //Scroll until you see the "More"
        screen.click(pattern2);  //Click "Más"
        Settings.MoveMouseDelay = 2; //Wait 2 seconds
        screen.wheel(pattern3, WHEEL_UP, 10);  //Look for SPAM
        screen.click(pattern4);         //Click SPAM
        Settings.MoveMouseDelay = 1;    //Wait 1 seconds
        screen.click(pattern5);         //Click selector
        Settings.MoveMouseDelay = 1;    //Wait 1 seconds
        screen.click(pattern6);         //Click  "eliminar definitivamente"
        Settings.MoveMouseDelay = 1;    //Wait 1 seconds
        driver.close();                 //Close the Browser
 
    }
}