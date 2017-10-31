Simple Versioning
=================

This is version 17.10 of the specification. (Versioning date based YY.M)

The idea is based on Semantic Versioning but simpler and more flexible.
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

Additionally there are two build numbers.

4. BUILD number
5. ADDBUILD number (additional build number)

A pre-release or development release is indicated by having at least
one number of a version part set to zero.

The additional build numbers can be used for pre-release, development and
extended versions if needed.

Also simpler formats without a PATCH or BUILD numbers are allowed.
Release version examples: 1.14, 1.25.1, 1.2.2.1, 1.2.2.1.2
Pre-release version examples: 0.1, 1.0.1, 1.1.0.1, 1.2.3.0.1
Development version indicator examples: 1.0, 1.1.0, 1.2.2.0
(Is also a pre-release but the preferred way is to use it only as an in
development indicator.)

As an alternative date based release numbers as 2017.1 or 17.1 are also
valid. Also something like YY.M.D like 17.3.1 for the release at the
date 2017/03/01 is also valid.
Only recommendation is to specify the exact versioning scheme in the
documentation.


Simple rules:

- A version string has minimum one dot and up to four (1-4 ".")
- Only numbers, numbers are equal or greater than zero (n >= 0)
- Pre-releases are indicated by having at least one zero number. (n == 0)
- Comparison is done by splitting the version string in a tuple of numbers
  and comparing the tuples.


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
(M.N) and up to major, minor, patch, build and additional build version number
(M.N.P.B.A).

2. The most common scheme is M.N.P where M, N, and P are
non-negative integers, and MUST NOT contain leading zeros. M is the
major version, N is the minor version, and P is the patch version.
Each element MUST increase numerically. For instance: 1.9.1 -> 1.10.1 -> 1.11.1.
The API and feature garanties are the same as for Semantic Versioning 2.0.0.

3. Once a versioned package has been released, the contents of that version
MUST NOT be modified. Any modifications MUST be released as a new version.

4. Major version zero (0.N.P) is for initial development. Anything MAY change
at any time. The public API SHOULD NOT be considered stable. A minor version
zero (1.0.P) is for pre-releases of a major version. A patch version of zero
(1.1.0) is a development version, or simple a marker for the start of the next
development.

5. A pre-release or development version is indicated by setting either one ore
more of major, minor, patch, build or additional build to zero
Ex.: 0.1.1, 1.0.1, 1.1.0, 1.1.0.12, 1.2.4.0.16
A trailing zero should be used to mark a development versions.
(1.1.0, development after version 1.1)
For pre-releases normally the next to last version number is set to zero.
(1.0.5, pre-release for 1.1)

6. Precedence refers to how versions are compared to each other when ordered.
Precedence MUST be calculated by separating the version into parts, normally
major, minor, patch and additional build numbers.
For comparison the version is split up into a tuple and the number is converted
to a positive integer.
Precedence is determined by the first difference when
comparing each of these identifiers from left to right as follows: Major, minor,
patch and build numbers are always compared numerically.
Example: 1.1.1 < 2.1.1 < 2.2.1 < 2.2.2.
If different version schemes are compared the missing part is not assumed to be
zero or one. They cannot compare equal and are compared part by part if the
parts are equal the longer version scheme wins.
Ex: 1.1 < 1.1.0, 1.1 != 1.1.0, 1.1 != 1.1.1

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
                             | <major> "." <minor> "." <patch> "." <build>
                             | <major> "." <minor> "." <patch> "." <build> "." <addbuild>

    <major> ::= <numeric identifier>

    <minor> ::= <numeric identifier>

    <patch> ::= <numeric identifier>

    <build> ::= <numeric identifier>

    <addbuild> ::= <numeric identifier>

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
Every part is simply a number and a pre-release is indicated by
setting one or more numbers to zero.
Simple to understand simple to detect and implement programatically.

For really simple projects it allows also to have simpler schemes and
omit parts. Also if someone wants to do date based releases it can be done
with this scheme.


FAQ
---

**How should I deal with revisions in the 0.y.z initial development phase?**

The simplest thing to do is start your initial development release at 0.1
and then increment the minor version for each subsequent release.

**How do I know when to release 1.1?**

If your software is being used in production, it should probably already be
1.1. If you have a stable API on which users have come to depend, you should
be 1.1. If you're worrying a lot about backwards compatibility, you should
probably already be 1.1.

**Doesn't this discourage rapid development and fast iteration?**

Major version zero is all about rapid development. If you're changing the API
every day you should either still be in version 0.N or on a separate
development branch working on the next major version.


**Does Simple Versioning have a size limit on the version string?**

No, but use good judgment. A 255 character version string is probably overkill,
for example. Also, specific systems may impose their own limits on the size of
the string.


**Is there a difference between a pre-release and development version?**

Not really, it is more a convention to never do a pre-release with a version
that ends with zero (1.0.0) instead use it only to mark internal development
and also count pre-release starting from 1 as last number.

**Is there a simple way to indicate a release version?**

Yes a real simple one. Every number must be >0 to indicate a release.
For example if you split up the version string by "." convert every part to an
integer and every integer is bigger than zero.

In pseudo code:

version_tuple = split("1.1.1", ".")
is_release = all(version_tuple)
(zero integer is considered false other true)

A pre-release or development release is simply:
is_pre_release = not is_release

**I need to do pre-release for a minor version is this possible?**

Yes, use the build number to extend your version.
Something like 1.4.0.1 for your first pre-release to the final minor release of
1.5.

**I need to do pre-release for a patch version is this possible?**

Yes, use the additional build numbers to extend your version.
Something like 1.4.2.0.1 for your first pre-release to the final patch
release of 1.4.3.

**I don't do pre-releases is a zero number still useful for me?**

Yes it is. Use a trailing zero as your internal development marker so
development after a release is visible in the version number.
For example after the release of the version 2.5.2 set your version
to 2.6.0 to mark it as development for the next major version 2.6.1.


**Is it good practice to change release version schemes often?**

No, please decide a version scheme for your releases at start of your project
and don't change it then.
So if you decide with a two digits version scheme like 25.1 and not do
patch release, stick with it. But it is ok for pre-releases to use additional
build numbers.
So for release you use a version scheme and for your pre-releases you use
another version scheme. This is totally fine.

**Are more version parts then five allowed?**

No, version have up to five parts not more. A version 1.2.3.4.5.6 is not allowed.
This is simply to limit it in length. Keep in mind you can increment the numbers
to really high values if you want. So there is not really a limit in the amount
of versions.

**Are simple digit versions allowed?**

No, the minimum is to have to number parts, ex: 1.1
A simple version with a single number, ex: 12 is not allowed.
This is to visually mark it with a "." that it is something about a version.

**I am not comfortable to increase the length of parts for pre-releases?**

If you don't want to change your version scheme to get the additional build
number for pre-releases of patches you must stick by doing only pre-releases
for a major version.
In most cases this is enough if you release early and often and do small
minor releases with not to much new features.

In this case your release flow is::

  0.1.1 - initial development
  1.0.1 - first pre-release
  1.1.1 - first major release
  1.1.2 - patch release
  1.2.0 - development for next minor release
  1.2.1 - minor release
  2.0.0 - development for next major release
  2.0.1 - first pre-release for next major
  2.0.2 - second pre-release for next major
  2.1.1 - second major release

You can also skip some numbers and do development pre-release with
1.2.0, 1.3.0, 1.4.0 and a release with 1.4.1.


**I really want to have fancy pre-release or other build specifiers?**

Hmm, this is about Simple Versioning avoiding this kind of stuff.
So please use another version scheme that solves your needs.
All this complicated specifiers are against the main goal of the this
spec. But please think some minutes about it, your users and everyone else
will be happy if you choose the simple to understand solution.


**I need a really simple workflow for my versions is this possible?**

Yes, in this case you mostly use a major and minor version number and
a patch only if needed.

Simple release workflow::

  0.1 - initial development
  1.0 - pre-release for first major
  1.1 - First major version
  1.1.0 - internal development version
  1.2 - second release with first minor additions
  1.2.0 - internal development
  1.2.1 - patch for 1.2
  1.2.2 - next patch for 1.2
  1.3 - third release
  1.4 - forth release
  2.0 - pre-release for next major
  2.1 - next major release

Even simpler is to do no patch release and use the trailing zero only
as a internal development marker.


**What is a development version?**

A development version is simply a convention and is indicated by a
trailing zero (1.1.0). Advice is to not do a pre-release of such a version.
It can be very useful to visually mark the internal development version.
After a release simply append ".0" to the version to mark it now I start
the next development cycle. Before the next release remove it and increment
the version numbers.

For example::

  1.1.1 was first release now append ".0" as a marker
  1.1.1.0 for development of next release cycle
  1.1.2 do the patch release
  1.1.2.0 development marker
  1.2.1 next minor version

In this case no pre-releases are done and the trailing zero is only used
internally to visually mark a development version.
If this is checked into a source control system it is clear this is a
development branch and not for release.


**I am in fear to do something wrong?**

Keep calm, to meet the spec not much must be done.
Everything from 0.1 to 1.1.1.1.1 or higher positive numbers is good.
Keep two things in mind. At a minimum one point and up to four points
between the numbers, numbers are zero or a positive number.
Thats it in simple words.


**Can I use the length of version numbers as indicator?**

Yes you can but the main rule for pre-releases and zero still apply.
You can make your own more restrictive conventions and do
checks in a CI build system about the length.
Something like for a release three version numbers are enforced to avoid
a pre-release with a development indicator.
Or something like a release has three numbers and a pre-release has
five numbers.
You can also do this by simply counting dot's.


About
-----

The Simple Versioning specification is authored by Wolfgang Langner.
The main goal is to keep it simple also in implementation and for
version comparison.
It is simple to detect a development or pre-release version.
It contains advice for the most common version scheme based on Semantic Versioning.


License
-------

Creative Commons - CC BY 3.0
http://creativecommons.org/licenses/by/3.0/
