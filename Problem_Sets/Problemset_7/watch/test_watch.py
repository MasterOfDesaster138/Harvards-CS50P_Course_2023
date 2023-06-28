##### HOW TO TEST: #####
"""Here’s how to test your code manually:

Run your program with python watch.py. 
Ensure your program prompts you for HTML, then copy/paste the below:
<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Press enter and your program should output https://youtu.be/xvFZjo5PgG0. 
Notice how, though the src attribute is prefixed with http://www.youtube.com/embed/, 
the resulting link is prefixed with https://youtu.be/.

Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Press enter and your program should still output https://youtu.be/xvFZjo5PgG0.

Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
Press enter and your program should output None. Notice how the src attribute doesn’t point to a YouTube link!

You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

check50 cs50/problems/2022/python/watch
Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. 
Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave.
"""

"""INSTRUCTIONS:
Implementieren Sie in einer Datei namens watch.py eine Funktion namens parse, die einen HTML-String als Eingabe erwartet, 
jede YouTube-URL extrahiert, die der Wert eines src-Attributs eines iframe-Elements darin ist, 
und ihr kürzeres, teilbares youtu.be Äquivalent als str zurückgibt. 
Erwarten Sie, dass eine solche URL in einem der folgenden Formate vorliegt. 
Nehmen Sie an, dass der Wert von src von doppelten Anführungszeichen umgeben sein wird. 
Und nehmen Sie an, dass die Eingabe nicht mehr als eine solche URL enthält. 
Wenn die Eingabe keine derartige URL enthält, wird None zurückgegeben."""

# Import the Libraries, Module and Functions we need for Testing
import pytest
from watch import parse


def test_parse_short_html():
    assert parse(r'<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == r'https://youtu.be/xvFZjo5PgG0'
    

def test_parse_long_html():
    html = r'<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(html) == r'https://youtu.be/xvFZjo5PgG0'
    
    
def test_parse_no_match():
    assert parse(r'<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None



