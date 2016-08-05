# InstantAlert
InstantAlert/Mkulima app, a very simple Flask web app,For sending messages(alerts) to farmers.
The app is integrated with AfricasTalking API for this functionality.

######INTERGRATING FLASK WEB APP WITH API
Application Programming Interface (API) is a set of routines, protocols, and tools for building software applications. It specifies how software components should interact and APIs are used when programming graphical user interface (GUI) components.

##How to use AfricasTalking API
**You need your AfricasTalking username and APIKey**

*To get AfricasTalking Username*

1.Create an account with AfricasTalking.Username is sent to your email.

*To get APIKey*

1.LogIn.

2.Go to settings.Select My APIKey.

3.Enter your valid password.

4.Generate your APIkey.

5.Save it for later use.

*Sending message using Python.

1.Go to SMS.

2.Select your programming language(I used python).

3.Use the code snippet it shows how to send SMS messaged using AT API.
    -The code  uses python gateway class AfricasTalkingGateway.py

4.A 'sendMessage.py' function would look like this.

    # Import the helper gateway class

**from AfricasTalkingGateway import AfricasTalkingGateway,AfricasTalkingGatewayException**

**def sendMessage(code):**

    # Specify your login credentials

    **username = "username"**

    **apikey   = "APIKey"**

    # Specify the numbers that you want to send to in a comma-separated list

    # Please ensure you include the country code (+254 for Kenya)

    **to      = "+2547xxxxxxxx"**

    # And of course we want our recipients to know what we really do
   
    #message = str(code)

    **message = "Hey yo using AfricasTalking API"**

    # Create a new instance of our awesome gateway class

    **gateway = AfricasTalkingGateway(username, apikey)**

    # Any gateway errors will be captured by our custom Exception class below, 

    # so wrap the call in a try-catch block


