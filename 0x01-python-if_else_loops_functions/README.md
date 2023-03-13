 <h1 class="gap">0x01. Python - if/else, loops, functions</h1>
<h4>In a nutshell&hellip;</h4>
  <ul>


      <li>
        <strong>Auto QA review:</strong>
          0.0/160 mandatory
            &
            0.0/41 optional
      </li>
    <li>
      <strong>Altogether:</strong>
        &nbsp;<strong>0.0%</strong>
        <ul>
          <li>Mandatory: 0.0%</li>
            <li>Optional: 0.0%</li>
            <li>
              Calculation:&nbsp;
                  0.0%
                    + (0.0% * 0.0%)
              &nbsp;==&nbsp;<strong>0.0%</strong>
            </li>
        </ul>
    </li>
  </ul>
<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/jpjs5EnZTpBLLEremJYjPQ" title="More Control Flow Tools" target="_blank">More Control Flow Tools</a> (<em>Read until &ldquo;4.6. Defining Functions&rdquo; included</em>)</li>
<li><a href="/rltoken/F9n2AE-fpEPzt2PfBMGYAQ" title="IndentationError" target="_blank">IndentationError</a> </li>
<li><a href="/rltoken/ZdtRIAkFu8dMBT99DcFBNg" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="/rltoken/ElQgZYNHrLI7kV_ysEB1hQ" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="/rltoken/ElQgZYNHrLI7kV_ysEB1hQ" title="Learn to Program 2 : Looping" target="_blank">Learn to Program 2 : Looping</a> </li>
<li><a href="/rltoken/TuTTnEg_Rwn8U1g3PEsZmA" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle &ndash; Style Guide for Python Code</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/SdBJUMTPS5VW3cQNkhaeSg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>Why indentation is so important in Python</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use the <code>while</code> and <code>for</code> loops</li>
<li>How is Python&rsquo;s <code>for</code> different from <code>C</code>&lsquo;s?</li>
<li>How to use the <code>break</code> and <code>continues</code> statements</li>
<li>How to use <code>else</code> clauses on loops</li>
<li>What does the <code>pass</code> statement do, and when to use it</li>
<li>How to use <code>range</code></li>
<li>What is a function and how do you use functions</li>
<li>What does return a function that does not use any <code>return</code> statement</li>
<li>Scope of variables</li>
<li>What&rsquo;s a traceback</li>
<li>What are the arithmetic operators and how to use them</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>C Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89</li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don&rsquo;t have to push them to your repo (if you do we won&rsquo;t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don’t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<p><em>Note</em>: you do not need to understand lists yet.</p>
<h2 class="gap">Tasks</h2>
<h3 class="panel-title">
      0. Positive anything is better than negative nothing
    </h3>
<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>

<ul>
<li>You can find the source code <a href="/rltoken/rkvoXPA-lS3TAaemM9sChg" title="here" target="_blank">here</a></li>
<li>The variable <code>number</code> will store a different value every time you will run this program</li>
<li>You don&rsquo;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li>
<li>The output of the program should be:

<ul>
<li>The number, followed by

<ul>
<li>if the number is greater than 0: <code>is positive</code></li>
<li>if the number is 0: <code>is zero</code></li>
<li>if the number is less than 0: <code>is negative</code></li>
</ul></li>
<li>followed by a new line</li>
</ul></li>
</ul>

