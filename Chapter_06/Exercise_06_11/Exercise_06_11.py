"""
11. Personal Web Page Generator
Write a program that asks the user for his or her name, then asks the user to enter a sentence
 that describes himself or herself. Here is an example of the program’s screen:
Enter your name: Julie Taylor Enter
Describe yourself: I am a computer science major, a member of the
Jazz club, and I hope to work as a mobile app developer after I
graduate. Enter
Once the user has entered the requested input, the program should create an HTML file,
containing the input, for a simple Web page. Here is an example of the HTML content,
using the sample input previously shown:
<html>
<head>
</head>
<body>
 <center>
 <h1>Julie Taylor</h1>
 </center>
 <hr />
 I am a computer science major, a member of the Jazz club,
 and I hope to work as a mobile app developer after I graduate.
 <hr />
</body>
</html>


@author Sharaf Qeshta
"""


def main():
    try:
        username = input("Enter your name: ")
        description = input("Describe yourself: ")
        file = open(f"{username}.html", "w")

        file.write("<html>")
        file.write("<head>")
        file.write("</head>")
        file.write("<body>")
        file.write("<center>")
        file.write(f"<h1>{username}</h1>")
        file.write("</center>")
        file.write("<hr>")
        file.write(description)
        file.write("<hr>")
        file.write("</body>")
        file.write("</html>")
    except Exception as error:
        print(error)


main()
