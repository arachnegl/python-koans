============
Python Koans
============

Python Koans is an interactive tutorial for learning the Python programming
language by making tests pass.

Most tests are *fixed* by filling the missing parts of assert functions. Eg:

    self.assertEqual(__, 1+2)

which can be fixed by replacing the __ part with the appropriate code:

    self.assertEqual(3, 1+2)

Occasionally you will encounter some failing tests that are already filled out.
In these cases you will need to finish implementing some code to progress. For
example, there is an exercise for writing some code that will tell you if a
triangle is equilateral, isosceles or scalene.

As well as being a great way to learn some Python, it is also a good way to get
a taste of Test Driven Development (TDD).


Downloading Python Koans
------------------------

Python Koans is available through git on Github:

    http://github.com/arachnegl/python-koans

You download the source as a zip/gz/bz2.


Installing Python
-----------------

You can download Python from here:

    http://www.python.org/download

After installing Python make sure the folder containing the python executable
is in the system path. In other words, you need to be able to be able to run
Python from a command console. 

`python3` or `python.exe` depending on the operating system. 

If you have problems, this may help:

    http://www.python.org/about/gettingstarted


Getting Started
---------------

From a unix terminal or windows command prompt go to the python
koans folder and run::

    python3 contemplate_koans.py

Example using Python 3 with windows, fire up the command shell (cmd.exe) 
and run this:

.. image:: http://i442.photobucket.com/albums/qq150/gregmalcolm/GettingStarted.png

Apparently a test failed::

    AssertionError: False is not True

It also tells me exactly where the problem in, its an assert on line 12
of .\\koans\\about_asserts.py. This one is easy, just change False to True to
make the test pass.

Sooner or later you will likely encounter tests where you are not sure what the
expected value should be. For example::

    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()
        self.assertEqual(__, isinstance(fido, object))

This is where the Python Command Line can come in handy. In this case I can
fire up the command line, recreate the scenario and run queries:

.. image:: http://i442.photobucket.com/albums/qq150/gregmalcolm/DebuggingPython.png


Testing specific koans
======================

Running a whole test case::

  $ python3 contemplate_koans.py about_strings

Running a single test::

  $ python3 contemplate_koans.py about_strings.AboutStrings.test_triple_quoted_strings_need_less_escaping


Acknowledgments
---------------

Most of this is lifted from Greg Malcom:

    http://github.com/gregmalcolm/python_koans

I highly recommend completing Malcom's Koans once you have completed these.

I chose not to fork as I wanted a version suitable for students of a non
programming background.

