
# mega-link-checker

## Dependencies:
* Python 3.5+
* pip install sys
* pip install requests

* A .txt file with ALL your MEGA links to be checked (line separated).

---

## mega.py

A basic tool that checks if MEGA links are still online or not.
<br>
Are you the type of person who has thousands of MEGA links all stored in a .txt file? Then this is for you!

### Usage:

```
python mega.py "links.txt"
```

which simply lists if the links are online or not.

OR

```
python mega.py -d "links.txt"
```

which lists if the links are online or not AND **deletes** the offline ones from the original .txt file.

<em>Important: Please be careful with this one as this will irreversibly overwrite your .txt file.</em>

(In both cases, the path given can be an absolute path or a relative path.)

---


Alternatively, you can check the status of a single link using:
```
sudo curl --silent --data-ascii '[{"a":"g", "g":1, "ssl":0, "p":"'CODE'"}]' https://eu.api.mega.co.nz/cs
```
where CODE is the unique id from your MEGA link 
(ex. ABcD1E2F for https://mega.nz/folder/ABcD1E2F#WSv_Y1POjQs1QbYBbyhjfw)