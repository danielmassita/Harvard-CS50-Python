# https://cs50.harvard.edu/python/2022/shorts/style/
# https://www.youtube.com/watch?v=m8K66w_VMcU

pip install black
pip install pylint

# "Readability counts"
# "A style guide is about consistency. Consistency with this style guide is important.
# Consistency within a project is more important. Consistency within one module or
# function is the most important.

"""
[MUSIC PLAYING] DAVID MALAN: All right, this is CS50's introduction to programming with Python. My name is David Malan, and this is our look at style. Now, up until now, we've been writing code that's hopefully at least correct. That is, the code does what you intended to do. And hopefully, it's also well designed, that is, you're using relatively few lines of code to achieve some goal while still ensuring that it's readable. You're perhaps using functions that save you the trouble of reinventing wheels, so to speak. 

But it's possible that your code isn't necessarily manifesting the best style as well, which is another form of quality that you can ascribe to some code. Now style, or the right type of style to use, is rather subjective, and it depends typically on the programmer, on the company, on the course, or on the language that you're actually using. 

But within the Python community, it turns out that there's some pretty regimented standards that most all python Programmers adhere to, or rather, are expected to adhere to, because this particular language and community has tried to codify some of their preferences for how your code should look in the form of something called PEP 8. So a PEP or P-E-P-- Python enhancement proposal-- is a set of proposals that the community within the world of Python typically generate to not only propose new ideas, but also to codify, ultimately, certain standards. 

And PEP 8 happens to be such a proposal that standardized, or rather tried to standardize, what our code should look like-- that is to say, it's quite possible to write code that's not only correct, it might even be well designed, but it's just really a mess. And it just doesn't look very good. It's not very pretty. It's therefore harder to read. It's harder for others to read. And therefore, it's just not as maintainable. And any time you make something harder to read or less maintainable, you're just increasing the probability, dare say down the line, of introducing bugs. 

So it's a good thing for your code to be properly formatted, just like in the world of writing emails or essays or books or documents or beyond. It tends to be good practice to capitalize certain words, at least in English, use good punctuation, use paragraph breaks and the like. So even if you're relatively new to programming, at least in English or your own human language, odds are you've had quite a bit of practice with writing language in the human world that also just looks good as well. 

Well, what does it mean to look good in the world of programming code? Well, let me propose that if you look at PEP 8 itself, which is available on the internet via this address here, it turns out that it tries to standardize a number of details that would be manifest in your own code once you've written a number of lines. And the overarching premise of PEP 8, and really the notion of style in the Python community especially, is that "readability counts." 

And typically, languages-- Python among them-- come with what's generally known as a style guide. A style guide, not unlike PEP 8, is some kind of guide-- a document, either printed or perhaps internet based-- that just tries to standardize what everyone's code should look like. So a course that you're taking might have its own style guide. A company you're working for might have its own style guide. You, down the road as a professional programmer, might have your own style guide for your own code. 

But within the Python community, they've tried generally to standardize for the most part a lot of these details. And ultimately-- quote, unquote too-- a style guide is about consistency, consistency with this style guide, in the context of Python is important. Consistency within a project is more important. And consistency within one module or function is the most important. So that is to say, these aren't necessarily hard and fast rules, but rather guidelines that should guide the design of your own code. 

Now, how do you go about designing, or how do you go about styling your code well? Well, it boils down to things like this and many more-- indentation, using consistent indentation. Now, in some languages, it doesn't strictly have to be there, when you indent one line of code under another, or it could be one space, or two spaces, three spaces, or four-- maybe even eight, or an actual tab. In the world of Python, they tried to put an end to this debate and they prescribed that we all just agree to use four spaces consistently. 

Tabs versus spaces-- no tabs, spaces instead. And indeed, typically in something like VS Code, when you hit Tab on your keyboard, depending on how the program is configured, it should generally convert even things like tabs to individual spaces, like four. What about maximum line length? Your code tends to get less and less readable the longer and longer your lines of code get, especially if they start to scroll over the screen. 

So Python too tries to standardize what the maximum line length is. You just shouldn't go past a certain number of characters to the right of your screen. Blank lines-- using some number of blank lines, for instance, between blocks of code, perhaps among comments also just lends itself to making your code more readable. Why? Because it's not just a wall of text, a wall of code that you or other programmers have to see by adding in blank lines. 

And whitespace, more generally, can make it a little easier to wrap your mind around what's going on. And then imports-- even something like this, when you're importing this library or that, or this module or package, Python too prescribes just how and where you should generally put those lines of code that say import or from. And Python, via PEP 8, also prescribes any number of details as well. And 

These aren't details that we necessarily preach along the way, but rather practice as we write each of these examples in class. And it turns out, too, that as you see more and more code, well, you just get accustomed to the certain rules of proposals like these. So how do you go about, though, checking if your code is in conformance with something like PEP 8, or a style guide more generally? 

Well, you can certainly read the style guide itself and then look at your own code, and compare the two left and right. And decide, oh, I need to fix this and this other thing in my own code. But there's also tools, being programmers, that can help us solve these problems as well. And one of the most popular in the world of Python is a program called pylint, which is an example of what's generally known as a linter, which is a program that rather statically analyzes. 

That is-- reads your code top to bottom, left to right, and tries to figure out if there are potentially mistakes therein, or at least inconsistencies with something like a prescribed style guide. This is something that you can install via the usual ways, using something like pip. And its documentation is here. But it turns out there's other tools out there as well that are perhaps a little less noisy than pylint. 

It turns out if you run pylint on most of the programs you've written thus far, odds are you're going to be overwhelmed with just how many things you apparently did wrong stylistically, even though your code may very well be both correct and well designed. So a little less noisy, at least initially, might be this program here, that's the de facto standard within the Python community for formatting your code for you. 

Pycodestyle, formerly known as PEP 8-- a program as well-- is a program that you can not only run on your computer, documented at this URL here, it will actually take care of the process of reformatting your code for you if it's a bit messy. That is, if the style of your code, your indentation and blank lines and other details as well, are not in accordance with the style guide, something like pycodestyle will just fix it for you. 

But another one, an alternative nowadays that's actually gaining steam, that's perhaps even more popular nowadays, quite simply called black. And black is a program that you too can install with pip here, and it's documented at this URL. And the etymology of the name black is actually an allusion to Henry Ford, who invented cars way back when, and only sold quite a few black models of the same. And indeed, he's generally known as saying a quote along these lines, any customer can have a car painted any color that he wants, so long that it is black. 

So if you think about that for a moment, it's not quite a choice. And indeed, that's the spirit of this particular formatter called black, which is that it's opinionated, more so than others. With a lot of these formatters that exist out there, you tend to-- or your company tends to, or your course tends to configure them with certain rules. So there might be different ways to do indentation. There might be different ways to do imports or blank lines, and different companies and different people might reasonably disagree, and therefore have their own style guide here, their own style guide there. 

And it just tends to waste a lot of time, is the thinking, if all of us don't even agree on some of these basics. So this particular formatter, called black, is opinionated in the sense that it just makes a lot of these decisions for you. And if you don't like the way black is formatting your code, tough-- tough, that's the way it's going to do it. And this is a trend, perhaps now, at least within the Python community, of quibbling a little less over these stylistic details so that you and I can ultimately focus all the more on writing good code and solving actual problems. 

And let's go ahead and do just this. Let me go ahead and open up vscode here, where in advance I've created a program called students.py, whose purpose in life is just to create at the top of this program a dictionary containing key value pairs, the keys of which are the names of some students, the values of which are the houses at Hogwarts in which they live, and then I've just got a for loop here that iterates over each of those students, printing out for now each of their names. 

You can imagine certainly doing more with the values as well, but for now, this is a simple program. But it's already manifesting poor style, arguably-- certainly inconsistent with PEP 8 itself. And I know this from just experience, eyeballing it, and realizing, wow, this is not a good thing that this first line of code goes completely off my own screen. Feels like it's probably a little long-- and I'm going to have to scroll to even see what's going on. 

And this one's more subtle, but if you look at line three here, even though I've indented technically sufficiently-- so long as my code is indented underneath the for loop, and any subsequent indentation, if I had more lines of code, were similarly indented, the code would work. And it would be correct. But it just does not accord with PEP 8, which prescribes again, four spaces of indentation at each level. 

So how can I go about fixing this? Well, if I've already installed one of these formatters, for instance, something like black, I could literally just do this with my terminal window. I'm going to run the command black, space, students.py, and hit enter. And voila, you'll see that the students.py file has been automatically reformatted. And at the top of my file, I have now a dictionary-- same dictionary as before, but just so much more readable. 

Not only does it not wrap around to the edge of the screen, you can also see each of the key values pairs one line at a time. And you can see that it lends itself to even adding more down the road. It turns out it's not incorrect to have a final trailing comma like this, even though it's not strictly necessary here on the new line six. Why? Well, Padma in Ravenclaw is the very last student in this particular dictionary. 

But just in case, as is often the case, I might go in and start adding more key value pairs later. A common source of mistake is to accidentally forget that, oh, I didn't have a comma there previously. And here I am, adding more key value pairs. So that is the kind of detail that black not only fixes for you, but again, has an opinion on as well. 

So moving forward, as you write code of your own, it's good to get ingrained into you some of the lessons of and some of the guidelines in a style guide like PEP 8, but know that there's tools, be pycodestyle, or black, or something else altogether, that you can use as a programmer to help you focus more on correctness, more on design, more on solving actual problems, while still ensuring that your code is now automatically formatted as well. 
"""
