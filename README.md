<h3 align="center">PDF GENERATOR</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> An application that generates a pdf file based on (unfortunetelly) handmade pattern and then send an email with that pdf file
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
<!-- - [Deployment](#deployment) -->

## 🧐 About <a name = "about"></a>

Project created to automate generating pdf files based on api data and then send this file through mail. Created for a buisness usage.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

First you need to build a docker image using included Dockerfile and docker-compose<br>

```
docker-compose up --build
```

Then you need to type in your enviroment variables in docker compose:

```js
version: '3'
services:
  app:
    build:
      context: .  # Path to the Dockerfile directory
    ports:
      - "5000:5000"
    environment:
      - API_KEY=SuPeRSeCrEtApIKeY12345
      - SENDER_EMAIL=user@mail.com
      - EMAIL_PASSWORD=SuPeRSeCrEtPaSsWoRd
      - SMPT_SERVER=smtp.service.com
      - SMPT_SERVER_PORT=587
```

You can also modify a template to your use but you have to do it manually in:

### ./pdf_creator/pdf_creator.py

#### and

### ./pdf_creator/style.py

<!-- ### Installing

THERE WILL BE A DOCKER INSTALATION INSTRUCTION

Say what the step will be

```
Give the example
```

And repeat

```
until finished
``` -->

## 🎈 Usage <a name="usage"></a>

### JSON MUST INCLUDE THIS FIELDS:

```json
{
    "recipient_email":"",   #Email address of message recipient
    "user_email":"",    # Mail of person who send the mail. Used to send BCC message to sender.
    "user_company":"",  # Company that send the email. Implemented options: 'bowim'/'passat'.
    "user_fullname":"", # Full name of person who sends the email.
    "user_phone":"",    # Mobile phone number of person who sends the email.
    "city" : "",        # City name. Used on pdf file in the left corner
    "date" : "",        # Date that will be used on pdf file
    "order_No" : "",
    "course_No": "",
    "route":"",
    "loadings":"",
    "unloadings":"",
    "comments" : "",
    "price":"",
    "currency":"",      # Currency that is used in pdf file in format like "PLN", "EUR".
    "driver":"",        # Driver's full name
    "carrier_details":"",
    "ordering_person_details":"",
    "route_documents":""
}
```

### To change footer:

./send_mail/details.py

### To change template:

./pdf_creator/pdf_creator.py
./pdf_creator/style.py

### Usage in postman:

1. Select POST method and type your ip address eg. 10.0.0.1:5000
2. Add api key "X-API-KEY" to authorize
3. Add "Content-Type":"application/json" in headers
4. Pass a correct formated json to body

### Usage in access VB:

#### 1. Using VB.NET(eg. .NET app):

```VB
Imports System.Net.Http
Imports System.Threading.Tasks

Module Program
    Sub Main()
        Task.Run(Async Function() Await SendRequest()).Wait()
    End Sub

    Async Function SendRequest() As Task
        Dim client As New HttpClient()

        ' Set the API key header
        client.DefaultRequestHeaders.Add("Content-Type", "application/json")
        client.DefaultRequestHeaders.Add("X-API-KEY", "your_secret_api_key")

        ' Make the POST request
        Dim response As HttpResponseMessage = Await client.PostAsync("http://localhost:5000/send_email")

        ' Read and display the response
        Dim responseString As String = Await response.Content.ReadAsStringAsync()
        Console.WriteLine(responseString)
    End Function
End Module
```

#### 2. Using VBA (eg. Excel or Access):

##### - Using WinHttpRequest:

```VB
Sub SendRequest()
    Dim http As Object
    Set http = CreateObject("WinHttp.WinHttpRequest.5.1")

    ' Open the request
    http.Open "POST", "http://localhost:5000/send_email", False

    ' Set the API key header
    http.SetRequestHeader "Content-Type", "application/json"
    http.setRequestHeader "X-API-KEY", "your_secret_api_key"
    ' Send the request
    http.Send

    ' Display the response
    MsgBox http.responseText
End Sub
```

##### - Using XMLHTTP:

```VB
Sub SendRequest()
    Dim xmlhttp As Object
    Set xmlhttp = CreateObject("MSXML2.XMLHTTP")

    ' Open the request
    xmlhttp.Open "POST", "http://localhost:5000/send_email", False

    ' Set the API key header
    xmlhttp.setRequestHeader "Content-Type", "application/json"
    xmlhttp.setRequestHeader "X-API-KEY", "your_secret_api_key"


    ' Send the request
    xmlhttp.Send

    ' Display the response
    MsgBox xmlhttp.responseText
End Sub
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/)

## ✍️ Authors <a name = "authors"></a>

- [@Kubatoja](https://github.com/Kubatoja) - Jakub Błaszczyk
