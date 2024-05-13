# Day 03 - Python Bootcamp

### Exercise 00: Innocent Prank

 "Mobley, do you have an example money transfer form?"

 "I sure do. Look at the 'evilcorp.html' file in a shared folder."

 "Perfect. Remember, you can just run `python3 -m http.server` in a directory with this file to be able to test 
 our little prank in a browser. Just open http://127.0.0.1:8000/evilcorp.html and you'll see the form yourself. Then
 Elliot... brother, are you even listening?"

Elliot rotated his chair to show that he's interested.

 "So, you only have one shot at this. Your script will need to modify an actual HTML file on an Evil Corp's 
 server. The more people see the message that they are hacked the better."

Trenton immediately showed a script on her screen that had to be injected into a web page:

```
 <script>
        hacked = function() {
            alert('hacked');
        }
        window.addEventListener('load', 
          function() { 
            var f = document.querySelector("form");
            f.setAttribute("onsubmit", "hacked()");
          },
          false
        );
</script>
```

 "Let's call this operation... [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)!"

-----

You need to write a Python script 'exploit.py' that will do several things:

- First, it needs to read a file "evilcorp.html"
- Second, it should modify page title (in `<title>` tags) to be "Evil Corp - Stealing your money every day"
- Third, it should parse out the name of the user from the page (including the pronoun) and inject new tag `<h1>`
  into a `body` of a page, saying `<h1>Mr. Robot, you are hacked!</h1>`, where 'Mr. Robot' is a parsed pronoun
  and name.
- Fourth, it needs to inject a Trenton's script into a `body` of a page as well. If everything is okay, when
  the 'Send' button is pressed, you should see the word "hacked" appearing in an alert window.
- Finally, the link at the bottom of a page should now lead to "https://mrrobot.fandom.com/wiki/Fsociety" with 
  an actual name of the company on a page replaced with "Fsociety".

The new HTML file should be named "evilcorp_hacked.html" and placed in the same directory as the source
"evilcorp.html" file.


### Exercise 01: Cash Flow
After a while, Elliot turned his laptop on the table, showing the script. Mobley gave him a thumbs up and 
Trenton exchanged places with Darlene near the pinboard.

 "Well, this is a nice little distraction, but the actual attack will be happening in a different place.
 We know that Evil Corp is using [Redis](https://redis.io/) pubsub as a queue broker. But we only can deploy a
 script once, so..."

 "..So we need a test environment, I get it." Mobley flicked a chunk of popcorn and quickly caught it
 on the fly. "I'm on it."

-----

You need to write two scripts - `producer.py` and `consumer.py`.

Producer needs to generate JSON messages like this:

```
{
   "metadata": {
       "from": 1023461745,
       "to": 5738456434
   },
   "amount": 10000
}
```

and put them as a payload into a Redis pubsub queue. All account numbers ('from' and 'to') should 
consist of exactly 10 digits. Additional points can be earned if the code uses builtin `logging`
module (instead of `print` function) to write produced messages to stdout for manual testing.

Consumer should receive an argument with a list of account numbers like this:

`~$ python consumer.py -e 7134456234,3476371234`

where `-e` is a parameter receiving a list of bad guys' account numbers. When started, it should read
messages from a pubsub queue and print them to stdout on one line each. For accounts from the 
"bad guys' list" if they are specified as a receiver consumer should *swap* sender and receiver for
the transaction. But this should happend *only* in case "amount" is not negative.

For example, if producer generates three messages like these:

```
{"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

consumer started like `~$ python consumer.py -e 2222222222,4444444444` should print out:

```
{"metadata": {"from": 2222222222,"to": 1111111111},"amount": 10000}
{"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000}
{"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000}
```

Notice that only the first line was changed. Second one wasn't because "amount" was negative (even
though receiver is a bad guy). Third one wasn't changed because bad guy is a sender, not a receiver.


### Exercise 02: Deploy
 "Perfecto!" Darlene was enthusiastic. "Now all we need to do is write a deployment script."
 
 "I can do that!" Trenton had pretty good [Ansible](https://docs.ansible.com/ansible/latest/index.html) skills. 
 "Once Elliot is inside, all he has to do is install a bunch of packages on a server, copy over our
 exploit and consumer and run them!"

While she were talking, Elliot's fingers were running around on a keyboard, producing a 'todo list',
saving it into 'todo.yml'. Everything was ready.

-----

To complete this exercise, you don't need to actually know Ansible in details. It would be nice if
you could test your code through it, even though it's not strictly required. There is a list of
tasks that should be placed in a generated "deploy.yml" file in YAML format:

- Install packages
- Copy over files
- Run files on a remote server with a Python interpreter, specifying corresponding arguments

These tasks should be generated in Ansible notation (e.g. look [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html) for notation
on copying files). The script should be named 'gen_ansible.py'.

Thus, your code should convert Elliot's 'todo.yml' into 'deploy.yml' following this notation.