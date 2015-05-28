package com.yourcompany;

import com.saucelabs.common.SauceOnDemandAuthentication;
import com.saucelabs.common.SauceOnDemandSessionIdProvider;
import com.saucelabs.common.Utils;
import com.saucelabs.saucerest.SauceREST;

import org.json.JSONException;
import org.json.JSONObject;
import org.junit.rules.TestWatcher;
import org.junit.runner.Description;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * {@link TestWatcher} subclass that will mark a Sauce OnDemand job as passed or failed depending on the result
 * of the test case being executed.
 *
 * @author see {@link github} for original
 * @author Ross Rowe - modifications to use {@link SauceOnDemandAuthentication}
 */
public class SauceOnDemandTestWatcher2 extends TestWatcher {

    /**
     * The underlying {@link com.saucelabs.common.SauceOnDemandSessionIdProvider} instance which contains the Selenium session id.  This is typically
     * the unit test being executed.
     */
    private final SauceOnDemandSessionIdProvider sessionIdProvider;

    /**
     * The instance of the Sauce OnDemand Java REST API client.
     */
    private final SauceREST sauceREST;

    /**
     * Boolean indicating whether to print the log messages to the stdout.
     */
    private boolean verboseMode = true;

    /**
     * @param sessionIdProvider
     */
    public SauceOnDemandTestWatcher2(SauceOnDemandSessionIdProvider sessionIdProvider) {
        this(sessionIdProvider, new SauceOnDemandAuthentication());
    }

    public SauceOnDemandTestWatcher2(SauceOnDemandSessionIdProvider sessionIdProvider, boolean verboseMode) {
        this(sessionIdProvider, new SauceOnDemandAuthentication(), verboseMode);
    }

    /**
     * @param sessionIdProvider
     * @param authentication
     */
    public SauceOnDemandTestWatcher2(SauceOnDemandSessionIdProvider sessionIdProvider, SauceOnDemandAuthentication authentication) {
        this(sessionIdProvider,
                authentication.getUsername(),
                authentication.getAccessKey(), true);
    }

    /**
     * @param sessionIdProvider
     * @param authentication
     */
    public SauceOnDemandTestWatcher2(SauceOnDemandSessionIdProvider sessionIdProvider, SauceOnDemandAuthentication authentication, boolean verboseMode) {
        this(sessionIdProvider,
                authentication.getUsername(),
                authentication.getAccessKey(),
                verboseMode);
    }

    /**
     * @param sessionIdProvider
     * @param username
     * @param accessKey
     */
    public SauceOnDemandTestWatcher2(SauceOnDemandSessionIdProvider sessionIdProvider, final String username, final String accessKey, boolean verboseMode) {
        this.sessionIdProvider = sessionIdProvider;
        sauceREST = new SauceREST(username, accessKey);
        this.verboseMode = verboseMode;
    }

    /**
     * Invoked if the unit test passes without error or failure.  Invokes the Sauce REST API to mark the Sauce Job
     * as 'passed'.
     *
     * @param description not used
     */
    protected void succeeded(Description description) {
        if (sessionIdProvider.getSessionId() != null) {
            //log the session id to the system out
            printSessionId(description);
            Map<String, Object> updates = new HashMap<String, Object>();
            updates.put("passed", true);
            
            // Allison's modifications:
            // this will set the test name to something like: com.yourcompany.SampleSauceTest amazon[1]
            
            updates.put("name", description.getClassName() + " " + description.getMethodName());
            
            // end Allison's modifications
            
            Utils.addBuildNumberToUpdate(updates);
            sauceREST.updateJobInfo(sessionIdProvider.getSessionId(), updates);
        }
    }

    private void printSessionId(Description description) {
        if (verboseMode) {
            String message = String.format("SauceOnDemandSessionID=%1$s job-name=%2$s.%3$s", sessionIdProvider.getSessionId(), description.getClassName(), description.getMethodName());
            System.out.println(message);
        }
    }

    /**
     * Invoked if the unit test either throws an error or fails.  Invokes the Sauce REST API to mark the Sauce Job
     * as 'failed'.
     *
     * @param e           not used
     * @param description not used
     */
    protected void failed(Throwable e, Description description) {
        if (sessionIdProvider != null && sessionIdProvider.getSessionId() != null) {
            printSessionId(description);
            Map<String, Object> updates = new HashMap<String, Object>();
            updates.put("passed", false);
            
            // Allison's modifications:
            // this will set the test name to something like: com.yourcompany.SampleSauceTest amazon[1]
            updates.put("name", description.getClassName() + " " + description.getMethodName());
            try {
            	// this will set the custom data field to something like:
            	// {"failure":"org.junit.ComparisonFailure: expected:<A[A]mazon.com: Online Sh...> but was:<A[]mazon.com: Online Sh...>"}
            	updates.put("custom-data", new JSONObject().put("failure", e.toString()));
            } catch(JSONException ex) {
            	System.out.println("Encountered JSONException while setting custom-data.");
            	ex.printStackTrace();
            }
            // end Allison's modifications
            
            Utils.addBuildNumberToUpdate(updates);
            sauceREST.updateJobInfo(sessionIdProvider.getSessionId(), updates);

            if (verboseMode) {
                // get, and print to StdOut, the link to the job
                String authLink = sauceREST.getPublicJobLink(sessionIdProvider.getSessionId());
                System.out.println("Job link: " + authLink);
            }
        }
    }


}