# ASPNet Unity Implementation for Creating a Server

## Table of Contents

1. Solution and Project Setup
2. Shared Library
3. Controller
4. Get Request
5. Post Request
6. From Query

---

## Solution and Project Setup

To begin we must create a solution file with Visual Studio (VS) which is where we will store all of our project files.

1. Create an empty solution. This is just a solution file with no other projects included. To create an empty solution you can use VS or something else like Jet Brains.

2. Create a new project inside of this solution. We are going to create an **ASP.NET Core** web application.

The **core** part of this definition is important as it allows the server to run on multiple platform (not just mac or windows).


<img align="right" src="https://github.com/Markay12/UnityLiveStreaming/blob/master/ASPnet/assets/readme/ASPNetCore.png" alt="drawing" style="margin-right: 20px" width="450"/>

The other version of ASP.NET is only used with Windows.

We are going to name this file _Server_.

## Shared Library

Data needs to be shared between the server and Unity. We do not want to duplicate models between the two. We want the server and Unity to communicate between each other to share the models. This is much less work for us in the end and creates a cleaner code file.

1. Create another project file as a _Class Library_. We are going to name this file _SharedLibrary_.

This library is going to be a project folder with all of our shared clases. These are the classes that are going to go back and forth between Unity and our server.

This server is going to use the restful API and will wait for the calls we will send to it. Therefore, it will just sit and wait for a request and then perform logic to later send out the data.

## Controller

The first file we are going to create is a PlayerController. This is as an example and you can change the controller to fit your needs.

Controller is very important here. This keyword must be included as this is going to be picked up and mapped. Therefore, we must include controller in our file name. 

1. Create a file named _PlayerController.cs_ inside the Controller directory. 

<img align="left" src="https://github.com/Markay12/UnityLiveStreaming/blob/master/ASPnet/assets/readme/DirectoryController.png" alt="drawing" style="margin-right: 20px" width="250"/>

When working on the code we need to make sure that we inherit from the ControllerBase so we can use the full controller functionality.

We will also want to use the APIController attribute along with creating our route. The route is created with `[Route("[controller]")]` placed at the top of our code.

1. We also need to make sure that we create a reference to the class file Player that we created in our SharedLibrary. This is done by including the reference in C# and also by binding the SharedLibrary to these files.

## Creating a Get Request

Now we can create our get request using ASP.NET. This is going to be our first method and will look like this:

```cs
[HttpGet]
public Player Get()
{

    var player = new Player(); //instantiate our object

    return player; //return the object

}
```

Our get request here is an end-point we can call with no payload where we can get data back from the server.

Now we can run the file and you should see your first output! This is going to open something call Swagger which is just the built in GUI for seeing those requests.

![Swagger Get Request Visual](https://github.com/Markay12/UnityLiveStreaming/blob/master/ASPnet/assets/readme/SwaggerGet.png)

From here we can access and execute to get the values of the Player script we wrote. This execution should give us an HTTP response of 200 that it worked and we will see the level and health attributes we set in the player class file.

![Get Output](https://github.com/Markay12/UnityLiveStreaming/blob/master/ASPnet/assets/readme/GetExecuteOutput.png)

## Creating a Post Request to the Server

Creating a post request is similar to the get request but now posts data to the server.

The code for this will look something like below. An example of how this would be used is when you want to create or update a resource on the server, such as adding a new record to a database or updating an existing record.

```cs
[HttpPost]
public Player Post(Player player)
{

    Console.WriteLine("Player has been added to the database");

    return Player;

}
```

We can now get information back about the player object that we are using. After we hit run we will see that we have now two end points that can be used. 

![Endpoints](https://github.com/Markay12/UnityLiveStreaming/blob/master/ASPnet/assets/readme/two_endpoints.png)

## From Query