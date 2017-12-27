Simple Versioning
=================

This is version 17.12 of the specification. (Versioning date based YY.M)

The idea is based on Semantic Versioning but simpler.
Or as an alternative on CalVer calendar based versioning.


Summary
-------

The normal version scheme for a release is the same as for
Semantic Versioning.
Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible
   manner, and
3. PATCH version when you make backwards-compatible bug fixes.

Additionally there are pre release markers (optional).

A pre release marker is separated with an additional dot "."
then the marker optional another dot "." and a number.
Following pre release markers are allowed:

. "a", for alpha releases.
. "b", for beta releases.
. "c", for release candidates.

The prerelease marker can be translated to a number to compare
the release tuple. In this case it translates to:
"a" ->   -6
"b" ->   -5
"c" ->   -4

To compare releases split the version string by ".", convert the
first three to an integer the forth as a hex number to an integer
and the fifth to an integer. Recalculate the forth with the following
formula "-16+x" where x is the forth value converted from hex.
If the PATCH version is missed it is asumeed to be zero "0".

To compare versions the version string is converted to a tuple
of five fields containing only integer.
For example::

    1.0.0 -> (1,0,0,0,0)
    1.0 -> (1,0,0.0,0)
    1.1.0.a.1 -> (1,1,0,-6,1)
    1.1.a.2 -> (1,1,0,-6,2)
    2.4.1.c.1 -> (2,4,1,-4,1)
    1.2.0.a -> (1,2,0,-6, 0)

If the forth field is < 0 then it is a pre release.

Also simpler formats without a PATCH number is allowed.
Release version examples: 1.14, 1.25.1.
Pre-release version examples: 0.1.a.0, 1.1.0.a.1, 1.0.0.c.3

As an alternative date based release numbers as 2017.1 or 17.1 are also
valid. Also something like YY.M.D like 17.3.1 for the release at the
date 2017/03/01 is also valid.
Only recommendation is to specify the exact versioning scheme in the
documentation.


Simple rules:

- A version string has minimum one dot and up to four (1-4 ".")
- Only numbers and the letters "a", "b", "c".
- Pre-releases are indicated by having one of the letters "a", "b", "c" in it.
- Comparison is done by splitting the version string in a tuple of numbers
  and comparing the tuples. Letters are converted as specified.


Introduction
------------

The idea is base on Semantic Versioning and provides another solution to
handle versions in software projects and libraries.
It provides a simpler way to handle versioning and is also more flexible.

I call this system "Simple Versioning." Under this scheme, version numbers
and the way they change convey meaning about the underlying code and what has
been modified from one version to the next.


Simple Versioning Specification
-------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1. A simple version has as a minimum a major and a minor version number
(M.N) and up to major, minor, patch, and a pre release specifier (Letter.Count)
(M.N.P.L.C).

2. The most common scheme is M.N.P where M, N, and P are
non-negative integers, and MUST NOT contain leading zeros. M is the
major version, N is the minor version, and P is the patch version.
Each element MUST increase numerically. For instance: 1.9.1 -> 1.10.1 -> 1.11.1.
The API and feature garanties are the same as for Semantic Versioning 2.0.0.

3. Once a versioned package has been released, the contents of that version
MUST NOT be modified. Any modifications MUST be released as a new version.

4. Major version zero (0.N.P) is for initial development. Anything MAY change
at any time. The public API SHOULD NOT be considered stable.

5. A pre-release version is indicated by appending
one of the letters "a" for alpha release, "b" for beta release or "c" for a
release canditato and a optional number to the version string.
Ex.: 1.1.1.a.1, 1.0.1.b.2, 1.1.0.c.1, 1.2.c.1, 1.1.1.a
The letters are converted to values for comparison as specified.
"a" to -6, "b" to -5 and "c" to -4.

6. Precedence refers to how versions are compared to each other when ordered.
Precedence MUST be calculated by separating the version into parts, normally
major, minor, patch and additional pre release numbers.
For comparison the first part of a version (up to a pre release indicator)
is split up into a tuple and the number is converted to a positive integer.
Missing numbers are considered to be zero.
Precedence is determined by the first difference when
comparing each of these identifiers from left to right as follows: Major, minor,
patch are always compared numerically.
Example: 1.1.1 < 2.1.1 < 2.2.1 < 2.2.2.
If different version schemes are compared the missing part is assumed to be
zero.

7. If you don't need or want the API guarantees and another versioning scheme
as the promoted default Major.Minor.Patch fits better to your solutions, you
can do that. As example if you want to do year based versions with counting
the release number in the year, just do it. (2017.1, 2017.2, ...)
But name it only simple versioning compatible if it mets the specifications
of the numbering and the following definition.


Backus–Naur Form Grammar for Simple Versions
--------------------------------------------

::

    <valid simple version> ::= <major> "." <minor>
                             | <major> "." <minor> "." <patch>
                             | <major> "." <minor> "." <patch> "." <letter>
                             | <major> "." <minor> "." <patch> "." <letter> "." <count>

    <major> ::= <numeric identifier>

    <minor> ::= <numeric identifier>

    <patch> ::= <numeric identifier>

    <letter> ::= "a" | "b" | "c"

    <count> ::= <numeric identifier>

    <numeric identifier> ::= "0"
                           | <positive digit>
                           | <positive digit> <digits>

    <digits> ::= <digit>
               | <digit> <digits>

    <digit> ::= "0"
              | <positive digit>

    <positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"



Why Use Simple Versioning?
--------------------------

The basic idea is the same as for Semantic Versioning but eliminates
the complicated alphanumeric pre-release and build specifiers.
Here are only three pre-release specifieers allowed.

For really simple projects it allows also to have simpler schemes and
omit parts. Also if someone wants to do date based releases it can be done
with this scheme.


FAQ
---

**How should I deal with revisions in the 0.y.z initial development phase?**

The simplest thing to do is start your initial development release at 0.1
and then increment the minor version for each subsequent release.

**How do I know when to release 1.0?**

If your software is being used in production, it should probably already be
1.0. If you have a stable API on which users have come to depend, you should
be 1.0. If you're worrying a lot about backwards compatibility, you should
probably already be 1.0.

**Doesn't this discourage rapid development and fast iteration?**

Major version zero is all about rapid development. If you're changing the API
every day you should either still be in version 0.N or on a separate
development branch working on the next major version.


**Does Simple Versioning have a size limit on the version string?**

No, but use good judgment. A 255 character version string is probably overkill,
for example. Also, specific systems may impose their own limits on the size of
the string.


**Is there a difference between a pre-release and development version?**

A development version is simply a pre-release and the advice is to use
the letter "a" as indicator.

**Is there a simple way to indicate a release version?**

Yes, if there is no pre-release letter in the version string.

**Is it good practice to change release version schemes often?**

No, please decide a version scheme for your releases at start of your project
and don't change it then.
So if you decide with a two digits version scheme like 25.1 and not do
patch release, stick with it. 

**Are simple digit versions allowed?**

No, the minimum is to have to number parts, ex: 1.1
A simple version with a single number, ex: 12 is not allowed.
This is to visually mark it with a "." that it is something about a version.


**I really want to have fancy pre-release or other build specifiers?**

Hmm, this is about Simple Versioning avoiding this kind of stuff.
So please use another version scheme that solves your needs.
All this complicated specifiers are against the main goal of the this
spec. But please think some minutes about it, your users and everyone else
will be happy if you choose the simple to understand solution.


**What is a development version?**

A development version is simply a convention. It is also a pre release
at alpha level. Use ".a.0" as development version indicator.


**Can I use the length of version numbers as indicator?**

Yes you can if your your count for a pre-release is not optionl.
So a pre-release version if split is longer than three.
You can also do this by simply counting dot's.


About
-----

The Simple Versioning specification is authored by Wolfgang Langner.
The main goal is to keep it simple also in implementation and for
version comparison.
It is simple to detect pre-release version.
It contains advice for the most common version scheme based on Semantic Versioning.


License
-------

Creative Commons - CC BY 3.0
http://creativecommons.org/licenses/by/3.0/
