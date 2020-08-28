# Twitter API Setup

To collect Twitter data, we're going to work with the [Twitter API](https://developer.twitter.com/en/docs/basics/getting-started) and [twarc](https://github.com/DocNow/twarc), a Python package for collecting Twitter data through the Twitter API. To access the Twitter API, we first need to:

**1.** Apply for a Twitter developer account

**2.** Create a Twitter application

The developer account will allow us to create an application, which will eventually get us a series of API keys and tokens, which we can then use to access Twitter data.

According to Twitter, the reason for this somewhat drawn-out application process is to "prevent abuse of the Twitter platform" and "better understand and serve our developer community."

After getting our API keys, we then need to

**3.** Install twarc

**4.** Configure/set up twarc

**5.** Download the twarc repository

The following instructions will guide you through each part of this 5-step process.

## 1. Apply for a Twitter Developer Account


**1.** First navigate to [Twitter's "Apply for access" web page](https://developer.twitter.com/en/apply-for-access.html) and select "Apply for a developer account."

<img src="../images/Twitter/apply-for-access.png" width=100%>

**2.** If you already have a Twitter account, you'll be asked to log in with your account username and password. If you don't already have a Twitter account, you'll be asked to sign up for one.


**3.** After you've logged in, Twitter will ask: "What is your primary reason for using Twitter developer tools?" Because we're collecting data for our class "Introduction to Cultural Analytics," you can select "Doing academic research" or "Student."

<img src="../images/Twitter/developer-primary-reason.png" width=100%>

**4.** The next page of the application will ask: "This is you, right?" Confirm that your Twitter username and email are correct, select your country of residence (United States), and come up with a name for your application. It doesn't matter which name you choose. I'd suggest using your first name.

**5.** Then Twitter will ask: "How will you use the Twitter API or Twitter data?"

<img src="../images/Twitter/twitter-use-explanation.png" width=100%>


**In English, please describe how you plan to use Twitter data and/or APIs. For students and teachers, please include the name of the school, the name of the instructor and the course number (i

**Are you planning to analyze Twitter data?**


**Will your app use Tweet, Retweet, like, follow, or Direct Message functionality?**


**Do you plan to display Tweets or aggregate data about Twitter content outside of Twitter?**


**Will your product, service or analysis make Twitter content or derived information available to a government entity? In general, schools, colleges, and universities do not fall under this category.**



**6.** Review your application and accept [Twitter's Developer Agreement](https://developer.twitter.com/en/developer-terms/agreement-and-policy). Before accepting the agreement, however, briefly read through it and remember to note down one thing that surprises you about the terms in for HW 6. 

<img src="../images/Twitter/developer-agreement.png" width=100%>

**7.** Verify your email.

<img src="../images/Twitter/developer-success.png" width=100%>

## 2. Create an Application

Once you confirm your email address, you'll be taken to your developer account home page, where you can now create an app. 

<img src="../images/Twitter/app-home-page.png" width=100%>

**1.** Select "Create an app."

<img src="../images/Twitter/create-app.png" width=100%>

**2.** Now you have to fill out another application! Don't fret. We need to create an app to collect Twitter data, but many of the questions here are geared toward other kinds of Twitter apps, and we can skip them.

Below are suggested responses:

**App name (required)**

(Choose a name. Again, it doesn't matter which name you choose. First name will suffice.)

**Application description (required)** 

This app will be used to collect, curate, and analyze datasets related to culture and the humanities.

**Website URL (required)**

https://melaniewalsh.github.io/Intro-Cultural-Analytics

**You can skip Callback URLs, Terms of Service URL, Privacy Policy URL, Organization name, and Organization website URL.**

**Tell us how this app will be used (required)**

I will be using this app for a class called "Introduction to Cultural Analytics" (INFO 1350), which is being taught at Cornell University by Prof. Melanie Walsh. We will be collecting, curating, and analyzing datasets related to culture and the humanities. I plan to collect tweets about different subjects, to contextualize them, and to possibly share them as tweet IDs.

Then select "Create."

**3.** You've successfully created an app! Now select the "Keys and tokens" tab of your application home page. You will be able to see your unique "Consumer API key" and "Consumer API secret key." You will also need to generate your own "Access token & access token secret." 

<img src="../images/Twitter/keys-and-tokens.png" width=100%>

Write down your consumer key, consumer secret, access token, and access token secret in a safe location. Treat these keys and tokens like you would a password. (For more information about how and why to protect your keys and tokens, see ["Securing keys and access tokens"](https://developer.twitter.com/en/docs/basics/authentication/guides/securing-keys-and-tokens).) You will need to use your consumer key, consumer secret, access token, and access token secret to access Twitter's API through twarc.

## 3. Install twarc

Now we're going to install the Python and command line tool twarc, which you can find hosted on this GitHub page with installation and usage instructions: [https://github.com/DocNow/twarc](https://github.com/DocNow/twarc)

To install twarc, simply run the following on the command line:

!pip install twarc

!twarc version

## 4. Configure/Set up Twarc

Now that twarc is installed on our computers, we need to set it up so that we can collect Twitter data with this tool. We need to submit and save our Twitter API keys into twarc.

There are two options for configuring twarc.

### Option 1 — Configure Twarc From the Command Line

To configure twarc, open up your Terminal or PowerShell and copy and paste `twarc configure` into your command line.

!twarc configure

Twarc will prompt you to copy and paste in your Twitter consumer key and Twitter consumer secret. Then it will ask you to visit a URL to authorize access to the Twitter account that is associated with your API keys.

Please enter your Twitter application credentials from apps.twitter.com:

consumer key:

consumer secret:

Please log into Twitter and visit this URL in your browser:

https://api.twitter.com/oauth/authorize?oauth_token=UNIQUE-TOKEN

<img src="../images/Twitter/Twitter-authorize.png" width=100%>


Once you click "Authorize App", you will be redirected to the URL that is associated with your  API keys (likely our course website). You need to carefully inspect this URL because it actually contains the PIN that you need for the last step of twarc configuration. The URL will look something like this:

`https://melaniewalsh.github.io/Intro-Cultural-Analytics/oauthtoken=YOUR-UNIQUE-TOKEN&oauthverifier=THIS-IS-THE-DISPLAYED-PIN-YOU-NEED`

You need to copy and paste the part after `oauthverifier=` into the prompt at the command line:

After you have authorized the application please enter the displayed PIN:

If the PIN works, then you will get a happy successs message. Make sure to copy and paste this message into HW 6.

The credentials for mellymeldubs have been saved to your configuration file at /Users/melaniewalsh/.twarc

✨ ✨ ✨  Happy twarcing! ✨ ✨ ✨

### Option 2 — Configure Twarc in This Notebook

Copy your [API keys](https://developer.twitter.com/en/apps) and paste them into the quotation marks below. Also type in your Twitter handle without the @ symbol.

twitter_handle = ""
consumer_key= ""
consumer_secret = ""
access_token = ""
access_token_secret= ""

Then run the two cells below:

configuration = f"""[{twitter_handle}]
consumer_key={consumer_key}
consumer_secret = {consumer_secret}
access_token = {access_token}
access_token_secret= {access_token_secret}
"""

import os
config_filename = os.path.join(os.path.expanduser("~"), ".twarc")
with open(config_filename, "w") as file_object:
    file_object.write(configuration)

To test whether twarc has been properly configured, run a sample search and see if Twitter data gets returned:

!twarc search "something incredibly obscure"

## 5. Download the Twarc Repository 

Finally, we also need to download the twarc repository from GitHub, because there are a few things in it that aren't included in the version of twarc that's installed through pip. To download the repository, run:

!git clone https://github.com/DocNow/twarc.git

If Git isn't working for some reason, you can also download the repository as a zip file: https://github.com/DocNow/twarc/archive/master.zip