# Syntax Highlighting in Python

______

## Code to format

This blog is how to use Python to enable syntax highlighting in a markdown code snippet. The result is HTML/CSS that can be used and displayed on a site. In fact, this is the solution I'm using for this website. 

Take the code block below as an example. As of now there is no syntax highlighting. 

```
if __name__ == '__main__':
    print('hello world!')
```


#### Requirements
```
pip install markdown2
pip install Pygments
```

After installing these two packages, we will create a python file named `test.py`.

This snippet imports the markdown2 package, and uses it to convert the read md file (as a string), and write its contents as a HTML file.

```python
# test.py

import markdown2

with open("test.md","r") as f:
    text = f.read()

page =  markdown2.markdown(text,extras=['fenced-code-blocks', 'code-friendly']) 

with open('test.html', 'w') as output_file:
        output_file.write(page)
```

The result of this script can be seen below:

```html
<!-- test.html -->

<div class="codehilite">
    <pre>
        <span>
        </span>
        <code>
            <span class="k">if</span> 
            <span class="vm">__name__</span> 
            <span class="o">==</span>
             <span class="s1">&#39;__main__&#39;</span>
             <span class="p">:</span>
            <span class="nb">print</span>
            <span class="p">(</span>
            <span class="s1">&#39;hello world!&#39;</span>
            <span class="p">)</span>
        </code>
    </pre>
</div>
```

However, when previewing this file in your browser, it will still appear to not have any syntax highlighting. This is due to a key component being missin - CSS. This is where the python module `pygmentize` comes into use.

Open a terminal instance and enter the following commmand:

```bash
pygmentize -S default -f html > test.css
```

This will create a file called `test.css`. Some of its contents can be seen below (there's a lot of lines).

```css
/* test.css */

pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: #eee; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.hll { background-color: #ffffcc }
.c { color: #3D7B7B; font-style: italic } /* Comment */
.err { border: 1px solid #FF0000 } /* Error */
.k { color: #008000; font-weight: bold } /* Keyword */
.o { color: #666666 } /* Operator */
.ch { color: #3D7B7B; font-style: italic } /* Comment.Hashbang */
/* 
    etc.
*/
```

Next, all we need to do is add this file `test.css` to our HTML file `test.html`.

```html
<!-- test.html -->

<link rel="stylesheet" href="test.css">

<div class="codehilite">
    <pre>
        <span>
        </span>
        <code>
            <span class="k">if</span> 
            <span class="vm">__name__</span> 
            <span class="o">==</span>
             <span class="s1">&#39;__main__&#39;</span>
             <span class="p">:</span>
            <span class="nb">print</span>
            <span class="p">(</span>
            <span class="s1">&#39;hello world!&#39;</span>
            <span class="p">)</span>
        </code>
    </pre>
</div>
```

Now when we reload the HTML file, it should have syntax highlighting!

```python
if __name__ == '__main__':
    print('hello world!')
```