import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class WebDriverBasic {

	public static void main(String[] args) throws Exception {
		WebDriver driver;
		String username = System.getenv("SAUCE_USERNAME");
		String accessKey = System.getenv("SAUCE_ACCESS_KEY");
	
		DesiredCapabilities capabilities = new DesiredCapabilities();
		capabilities.setCapability("platform", "Windows 8");
		capabilities.setCapability("browserName", "Chrome");
		capabilities.setCapability("version", "37");
		capabilities.setCapability("name", "Basic Java WebDriver Test");

		// print out some environment variables, for funs
		String[] envVars = {"SAUCE_USERNAME", "SUPER_HAPPY_FUN_VAR", "BUILD_NUMBER", "BUILD_ID"};

		for (String v : envVars) {
			String output = System.getenv(v) || "";
			System.out.println(v + " : " );
		}

		driver = new RemoteWebDriver(new URL("http://"+username+":"+accessKey+"@ondemand.saucelabs.com:80/wd/hub"), capabilities);
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        
        driver.get("http://www.amazon.com/");
        
		driver.quit();
        System.out.println("Done! View this test on your dashboard at https://saucelabs.com/tests");
	}
}
