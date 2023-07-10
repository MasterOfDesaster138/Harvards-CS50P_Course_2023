##### HOW TO TEST: #####
"""How to Test -> numb3rs.py
    Here’s how to test numb3rs.py manually:

    Run your program with python numb3rs.py.
    Ensure your program prompts you for an IPv4 address.
    Type 127.0.0.1, followed by Enter.
    Your validate function should return True.

    Run your program with python numb3rs.py.
    Type 255.255.255.255, followed by Enter.
    Your validate function should return True.

    Run your program with python numb3rs.py.
    Type 512.512.512.512, followed by Enter.
    Your validate function should return False.

    Run your program with python numb3rs.py.
    Type 1.2.3.1000, followed by Enter.
    Your validate function should return False.

    Run your program with python numb3rs.py.
    Type cat, followed by Enter.
    Your validate function should return False.

    How to Test -> test_numb3rs.py
    To test your tests, run pytest test_numb3rs.py.
    Try to use correct and incorrect versions of numb3rs.py
    to determine how well your tests spot errors:

    Ensure you have a correct version of numb3rs.py.
    Run your tests by executing pytest test_numb3rs.py.
    pytest should show that all of your tests have passed.

    Modify the validate function in the correct version of numb3rs.py.
    validate might, for example, only check whether the first byte of the IPv4 address is valid.
    Run your tests by executing pytest test_numb3rs.py. pytest should show that at least one of your tests has failed.
    Again modify the correct version of numb3rs.py.
    validate might, for example, mistakenly return True when the user inputs an incorrect IPv4 format.
    Run your tests by executing pytest test_numb3rs.py. pytest should show that at least one of your tests has failed.

    You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit.
    But be sure to test it yourself as well!

    --> check50 cs50/problems/2022/python/numb3rs
    Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected.
    Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave."""

""" German Instructions:
Eine IPv4-Adresse ist eine numerische Kennung, die ein Gerät (oder, im Fernsehen, ein Hacker) zur Kommunikation im Internet verwendet,
Sie ist vergleichbar mit einer Postadresse in der realen Welt und wird normalerweise in Punkt-Dezimal-Notation als #.#.#.# formatiert.
Jedes # sollte jedoch eine Zahl zwischen 0 und 255 einschließlich sein. Es genügt zu sagen, dass 275 nicht in diesem Bereich liegt!
Wenn doch nur NUMB3RS die Adresse in dieser Szene überprüft hätte!

Implementieren Sie in einer Datei namens numb3rs.py eine Funktion
namens validate, die eine IPv4-Adresse als Eingabe in Form eines str
erwartet und dann True bzw. False zurückgibt, wenn diese Eingabe eine gültige IPv4-Adresse ist oder nicht.

Strukturieren Sie numb3rs.py wie folgt, wobei Sie main gerne modifizieren und/oder andere Funktionen implementieren können, wie Sie es für richtig halten,
aber Sie dürfen keine anderen Bibliotheken importieren. Sie können, müssen aber nicht, re und/oder sys verwenden.


Entweder bevor oder nachdem Sie validate in numb3rs.py implementieren, implementieren Sie zusätzlich in einer Datei namens test_numb3rs.py
zwei oder mehr Funktionen, die zusammengenommen Ihre Implementierung von validate gründlich testen,
deren Namen jeweils mit test_ beginnen sollten, so dass Sie Ihre Tests mit ausführen können:
--> pytest test_numb3rs.py"""
"""HINWEISE:
Erinnern Sie sich daran, dass das Modul re über eine ganze Reihe von Funktionen verfügt,
gemäß docs.python.org/3/library/re.html, einschließlich der Suche.

Erinnern Sie sich, dass reguläre Ausdrücke eine ganze Reihe von Sonderzeichen unterstützen,
siehe docs.python.org/3/library/re.html#regular-expression-syntax.

Da Backslashes in regulären Ausdrücken fälschlicherweise für Escape-Sequenzen (wie \n) gehalten werden könnten,
ist es am besten, die rohe String-Notation von Python für reguläre Ausdrücke zu verwenden,
sonst warnt pytest mit DeprecationWarning: Ungültige Escape-Sequenz.
Genauso wie Format-Strings mit dem Präfix f versehen werden, werden auch Raw-Strings mit dem Präfix r versehen.
Verwenden Sie zum Beispiel statt "harvard\.edu" r "harvard\.edu".

Beachten Sie, dass re.search, wenn ein Muster mit "Erfassungsgruppen" (d.h. Klammern) übergeben wird,
ein "Match-Objekt" zurückgibt, gemäß docs.python.org/3/library/re.html#match-objects,

Wobei die Übereinstimmungen 1-indiziert sind, auf die Sie mit group einzeln zugreifen können,
per docs.python.org/3/library/re.html#re.Match.group,

oder kollektiv mit groups, per docs.python.org/3/library/re.html#re.Match.groups."""

import numb3rs

def test_valid_ipv4_address():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("10.0.0.0") == True
    assert numb3rs.validate("172.16.0.0") == True

def test_invalid_ipv4_address():
    assert numb3rs.validate("275.3.6.28") == False
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("10.0.0.256") == False

def test_empty_string():
    assert numb3rs.validate("") == False

def test_non_numeric_characters():
    assert numb3rs.validate("192.168.0.a") == False
    assert numb3rs.validate("10.0.0.") == False

def test_less_than_4_blocks():
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("10.0") == False

def test_more_than_4_blocks():
    assert numb3rs.validate("192.168.0.1.1") == False
    assert numb3rs.validate("10.0.0.0.0") == False

def test_number_out_of_range():
    assert numb3rs.validate("192.168.0.256") == False
    assert numb3rs.validate("10.0.0.-1") == False



