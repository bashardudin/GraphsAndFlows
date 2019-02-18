#####################
Conventions and Rules
#####################

This page lists the conventions and rules to follow when coding in Python for
the *algorithmics* course, dispensed to first and second year students at
**EPITA**.

Any convention not found here is replaced by its Python
`PEP8`_ counterpart. Conventions for *docstrings* are to follow `PEP257`_ and
`Google conventions`_.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP257: https://www.python.org/dev/peps/pep-0257/
.. _Google conventions: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


************
Coding Style
************


Naming Conventions
==================

Naming conventions follow either the *UPPERCASE*, *lowercase*, *CamelCase* or
the *snake_case convention*, depending on named objects.

  * **Files and directories**: follow the *lowercase* convention.
  * **Functions and methods**: follow a light version of the *snake_case*
    convention.
  * **Variables, class instances and class attributes**: follow the *function
    convention*.
  * **Classes**: follow the *CamelCase* convention.
  * **Constants**: are expected to be in *UPPERCASE_SNAKE*.
  * **Auxiliary functions**: name of auxiliary function of function `name`, in
    charge of step or task `step` takes the form `__[name]_[step]`.

.. hint:: Function names should be all lowercase while kept short and explicit.
   Separate words by underscores if necessary to improve readability.

Punctuation and Spacing Conventions
===================================

This section puts some emphasis on rules and conventions extracted from `PEP8`_,
concerning syntactically correct options on code spacing and punctuation.

  * **Indentation** is to be given by 4 *spaces*.
  * There are no spaces before **commas** and **colons**, there is a
    space after a comma and a new line after a colon.
  * There is one space before an equality sign and one after it. Exception
    is made for default assignments in functions' parameters; there are no
    spaces neither before nor after the equality sign in that case.
  * There is one space before a binary operator and one after it.
  * There is no space after an opening **parenthesis** nor before a closing
    one. There is no space before an opening parenthesis when enclosing a
    function's list of parameters.
  * Same conventions hold for **brackets** and **braces**. There is no space
    before an opening **bracket** or **brace** when used to specify a key.
  * There are at least two spaces before inline **comments**.

.. caution:: You're advised to configure your IDE or text editor to
   automatically replace *any tab* character by 4 *spaces*.


***********************************************
Forbidden Functions, Keywords and Coding Habits
***********************************************

Any Python function or keyword not explicitly allowed in this document is
**FORBIDDEN**, exception made of progress stages below.
Hereafter is a list of most common forbidden functions and keywords.

  * ``break`` and ``continue`` are absolutely forbidden instructions. More
    generally, any abusive use of flow breaking instructions (including ``return``
    instruction) is forbidden.
  * *lambda* functions are not allowed (as not needed at our level).
  * The course focus is **algorithmics**. No explicit use of object oriented
    programming on students' side is expected nor allowed.
  * Power (or exponentiation) operator ``**`` is not allowed.


***************
Progress Stages
***************

This the list of progress stages any algorithmics student goes through during
first year. Each stage comes with its privileges: the use of previously
forbidden built-in functions and keywords.

Stage 1
=======

  * some arithmetic operators: ``+``, ``-``, ``//``,
    ``%``, ``/``
  * ``def`` for functions
  * ``if``, ``elif`` and ``else`` clauses
  * ``while`` loops

Stage 2
=======

  * ``list`` objects
  * ``list.append`` method
  * ``list.pop`` method without any argument
  * ``len`` function on *list* objects
  * ``for`` loops
  * ``range`` function, within for loops and in its three variants

Stage 3
=======

  * ``list.insert`` and ``list.pop`` methods

Stage 4
=======

  * the ``is`` keyword, **now mandatory while testing against None value**
  * flow-breaking ``return`` instruction, **only** for marginal cases to keep
    loop bodies simpler

Stage 5
=======

  * ternaries
  * list initialization using syntax ``[val] * nb``
  * object coercion into boolean
  * sets and dictionaries
  * list comprehensions
  * deep copy, via ``copy.deepcopy``
