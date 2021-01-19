
# mega-link-checker

## Dependencies:
* Python 3.5+
* pip install sys
* pip install requests

---

## mega.py

A basic tool that checks if a MEGA link is still online or not.

### Usage:

```
python mega.py links.txt
```
where 'links.txt' is a file located in your current working directory containing a MEGA link on each line.

Alternatively, you can just use curl:
```
sudo curl --silent --data-ascii '[{"a":"g", "g":1, "ssl":0, "p":"'CODE'"}]' https://eu.api.mega.co.nz/cs
```
where CODE is the unique hash from your MEGA link.