# CS50's Introduction to Programming with Python (CS50P) 2022 
# https://cs50.harvard.edu/python/2022/shorts/introduction/
# https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V
# https://youtu.be/OvKCESUCWII

"""
Week 0 - Functions and Variables
Week 1 - Conditionals
Week 2 - Loops
Week 3 - Exceptions
Week 4 - Libraries
Week 5 - Unit Tests
Week 6 - File I/O 
Week 7 - Regular Expressions
Week 8 - Object-Oriented Programming
Week 9 - Et Cetera
"""

"""
Transcription / Subtitles
1
00:00:24,000 --> 00:00:25,083
DAVID MALAN: Hello, world.

2
00:00:25,083 --> 00:00:28,410
My name is David Malan, and
this is CS50's Introduction

3
00:00:28,410 --> 00:00:29,880
to Programming with Python.

4
00:00:29,880 --> 00:00:33,720
Whereas CS50 itself is an introduction
to the intellectual enterprises

5
00:00:33,720 --> 00:00:35,880
of computer science and
the art of programming,

6
00:00:35,880 --> 00:00:40,210
this course is specifically focused
on programming in Python itself.

7
00:00:40,210 --> 00:00:42,210
At the beginning of the
course, we'll be focused

8
00:00:42,210 --> 00:00:45,570
on a topic in programming known as
functions and variables, mechanisms

9
00:00:45,570 --> 00:00:48,150
via which you can write code
that solves smaller problems,

10
00:00:48,150 --> 00:00:51,000
but you can compose those
smaller solutions into solutions

11
00:00:51,000 --> 00:00:52,530
to larger problems still.

12
00:00:52,530 --> 00:00:54,630
We'll then transition to
a look at conditionals,

13
00:00:54,630 --> 00:00:59,070
a way in code of expressing yourself
logically, to maybe do something

14
00:00:59,070 --> 00:01:02,340
if some question has an
answer of true, or not

15
00:01:02,340 --> 00:01:04,260
do something if the answer is false.

16
00:01:04,260 --> 00:01:06,240
We'll transition thereafter
to introducing you

17
00:01:06,240 --> 00:01:09,900
to loops, the ability, in code,
to do something again, and again,

18
00:01:09,900 --> 00:01:11,820
and again some number of times.

19
00:01:11,820 --> 00:01:14,280
We'll then transition to
something a little more technical,

20
00:01:14,280 --> 00:01:15,390
known as exceptions.

21
00:01:15,390 --> 00:01:18,353
Unfortunately, a lot can go wrong
when you're writing code, some of it

22
00:01:18,353 --> 00:01:20,520
your fault, some of it
perhaps someone else's fault.

23
00:01:20,520 --> 00:01:23,790
But you can write code defensively,
so to speak, and actually

24
00:01:23,790 --> 00:01:26,100
catch those kinds of
exceptions, those errors,

25
00:01:26,100 --> 00:01:29,310
and handle them properly so that
the users you're writing code for

26
00:01:29,310 --> 00:01:30,990
don't actually see the same.

27
00:01:30,990 --> 00:01:34,380
Thereafter, we'll take a look
at libraries, third-party code,

28
00:01:34,380 --> 00:01:37,470
written by other people, often,
or perhaps yourself in the past,

29
00:01:37,470 --> 00:01:40,040
that you can use and
reuse in your own projects

30
00:01:40,040 --> 00:01:42,960
so as to avoid reinventing
the wheel again and again.

31
00:01:42,960 --> 00:01:45,690
We'll look thereafter at
something called unit tests.

32
00:01:45,690 --> 00:01:49,530
It turns out, you'll actually
write code to test your own code.

33
00:01:49,530 --> 00:01:51,780
But you won't have to
write tests for your tests.

34
00:01:51,780 --> 00:01:55,240
Indeed, this is a best practice in
industry, writing tests for your code

35
00:01:55,240 --> 00:01:58,200
so that one, you can be sure that
your code today is, hopefully,

36
00:01:58,200 --> 00:02:00,490
if your tests are
correct, correct itself.

37
00:02:00,490 --> 00:02:04,320
But moreover, if you or someone else
modifies your code tomorrow, or down

38
00:02:04,320 --> 00:02:07,380
the line, you can rerun
those same tests to ensure

39
00:02:07,380 --> 00:02:10,850
that those new changes have not
broken anything about your own code.

40
00:02:10,850 --> 00:02:12,600
We'll then take a look
at something called

41
00:02:12,600 --> 00:02:15,780
File I/O, I/O for input
and output, the ability

42
00:02:15,780 --> 00:02:19,200
to not just store information
inside of a computer's memory,

43
00:02:19,200 --> 00:02:23,567
but rather save it persistently to
disk, so to speak, to files and folders.

44
00:02:23,567 --> 00:02:25,650
We'll then take a look at
another technique, known

45
00:02:25,650 --> 00:02:29,760
as regular expressions, whereby,
in Python, you can define patterns

46
00:02:29,760 --> 00:02:33,240
and you can validate data to make sure
the human typed something in as you

47
00:02:33,240 --> 00:02:33,910
expect.

48
00:02:33,910 --> 00:02:36,360
You can use regular expressions
to extract data, perhaps

49
00:02:36,360 --> 00:02:38,760
from some data set
you're trying to analyze.

50
00:02:38,760 --> 00:02:42,660
We'll then take a look, ultimately,
at object-oriented programming,

51
00:02:42,660 --> 00:02:46,530
a paradigm, a way of writing code,
whereby you can represent, in code,

52
00:02:46,530 --> 00:02:47,777
real-world entities.

53
00:02:47,777 --> 00:02:50,610
And this is in addition to other
paradigms of programming that we'll

54
00:02:50,610 --> 00:02:53,220
also explore, among them
procedural programming,

55
00:02:53,220 --> 00:02:55,440
where you write lots of
those functions, procedures

56
00:02:55,440 --> 00:02:58,110
really, top to bottom, to
solve problems step by step,

57
00:02:58,110 --> 00:03:01,053
and even something known as
functional programming, as well.

58
00:03:01,053 --> 00:03:02,970
And then at the very end
of the course will we

59
00:03:02,970 --> 00:03:06,270
equip you with all the more
tools for your toolkit.

60
00:03:06,270 --> 00:03:09,180
and additional building
blocks, additional vocabulary

61
00:03:09,180 --> 00:03:12,300
via which, after this same
course, you can go off on your own

62
00:03:12,300 --> 00:03:15,150
and either take other courses
or solve projects of your own,

63
00:03:15,150 --> 00:03:17,250
using all of these mechanisms.

64
00:03:17,250 --> 00:03:20,860
Now this course itself assumes
no prior programming background.

65
00:03:20,860 --> 00:03:23,610
So you don't have to have written
a single line of code in Python,

66
00:03:23,610 --> 00:03:25,150
or any language, yet.

67
00:03:25,150 --> 00:03:29,730
But this is also a course that you can
take before, during, or even after CS50

68
00:03:29,730 --> 00:03:33,000
itself, if you'd like to get
all the more versed with Python.

69
00:03:33,000 --> 00:03:35,700
Each week, via the courses
lectures, will we introduce you

70
00:03:35,700 --> 00:03:37,830
to any number of
concepts that we'll then

71
00:03:37,830 --> 00:03:41,070
drill down more deeply into in the
form of problem sets each week.

72
00:03:41,070 --> 00:03:43,470
That is, programming
projects that will enable

73
00:03:43,470 --> 00:03:47,460
you to apply some of those lessons
learned to problems of your very own.

74
00:03:47,460 --> 00:03:49,650
And by the end of the
course, you'll have

75
00:03:49,650 --> 00:03:53,190
solved so many problems that,
ideally, are representative

76
00:03:53,190 --> 00:03:55,930
of problems you'll eventually
encounter in the real world,

77
00:03:55,930 --> 00:03:58,680
whether you aspire to solve
code in the technical world

78
00:03:58,680 --> 00:04:01,440
or perhaps in the arts, the
humanities, the social sciences,

79
00:04:01,440 --> 00:04:03,210
the natural sciences, or beyond.

80
00:04:03,210 --> 00:04:06,570
You'll have, ultimately, the
vocabulary and the technical skills

81
00:04:06,570 --> 00:04:08,580
via which to approach the same.

82
00:04:08,580 --> 00:04:10,500
This, then, is CS50.

83
00:04:10,500 --> 00:04:15,470
And this is CS50's Introduction
to Programming with Python.

84
00:04:15,470 --> 00:04:17,000

"""
