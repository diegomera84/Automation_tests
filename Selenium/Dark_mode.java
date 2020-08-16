package com.autentia.sikulix;
 
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.sikuli.basics.Settings;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Pattern;
import org.sikuli.script.Screen;
 
public class Sikuli {
public static void main(String[] args) throws FindFailed, InterruptedException {
 
//First we create a Screen object to interact with the screen
Screen screen = new Screen();
//Next we generate a pattern for each image with which we are going to interact
// in our case with the image I ACCEPT, to accept Cookies and the image of the
// light bulb to switch to dark mode.
Pattern pattern = new Pattern("/home/diego/Documents/Images/acepto.png"); 
Pattern pattern2 = new Pattern("/home/diego/Documents/Images/bombilla.png");
 
//Create WebDriver for Chrome
System.setProperty("webdriver.chrome.driver","/home/diego/Documents/Sikuli/chromedriver");
WebDriver driver = new ChromeDriver();
 
//access website
driver.get("https://finofilipino.org/");
System.out.println(driver.getTitle());
System.out.println(driver.getCurrentUrl());
System.out.println(driver.getPageSource());
//click on the first pattern, the image of ACCEPT
screen.click(pattern);
Settings.MoveMouseDelay = 3; //wait 3 seconds
//double click on the image of the light bulb, pattern 2 and switch to dark mode.
screen.doubleClick(pattern2);
   }
}