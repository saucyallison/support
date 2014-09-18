import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

public class WebDriverBasic {

	public static void main(String[] args) throws Exception {
		WebDriver driver;
	
		DesiredCapabilities capabilities = new DesiredCapabilities();
		capabilities.setCapability("platform", "Windows 8");
		capabilities.setCapability("browserName", "Chrome");
		capabilities.setCapability("version", "36");
		capabilities.setCapability("name", "Basic Java WebDriver Test");

		driver = new RemoteWebDriver(new URL("http://awilbur:3fad902d-fb2e-4350-9689-b4100aba43a4@ondemand.saucelabs.com:80/wd/hub"), capabilities);
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        
        driver.get("http://www.amazon.com/");
        
		driver.quit();
        System.out.println("Done! View this test on your dashboard at https://saucelabs.com/tests");
	}
}