
# mega-link-checker

## Dependencies:
* Python 3.5+
* pip install sys
* pip install requests

---

## mega.py

A basic tool that checks if a MEGA link is still online or not.
Deletes the links that are offline if the '-d' argumet is given.

### Usage:

```
python mega.py "links.txt"
```

which simply lists if the links are online or not.

```
python mega.py -d "links.txt"
```

which lists if the links are online or not and deletes the offline ones from the original text file.

The path given can be an absolute path or a relative path.


Alternatively, you can check the status of a single link using:
```
sudo curl --silent --data-ascii '[{"a":"g", "g":1, "ssl":0, "p":"'CODE'"}]' https://eu.api.mega.co.nz/cs
```
where CODE is the unique id from your MEGA link 
(ex. ABcD1E2F for https://mega.nz/folder/ABcD1E2F#WSv_Y1PWjQs1QbYBbyhjfw)