Simple Versioning
=================

the idea is based on Semantic Versioning 2.0.0
but simpler and more flexible.


Summary
-------

Given a version number MAJOR.MINOR.PATCH(.BUILD), increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible
   manner, and
3. PATCH version when you make backwards-compatible bug fixes.

ans use
4. BUILD number when you need it.

The additional build number can be used for pre-release and
extended versions if needed.
Also simpler formats without a PATCH or MINOR version are allowed.
Release version examples: 22, 1.14, 1.25.1, 1.2.2.1
Pre-release version examples: 0.1, 1.0.1, 1.1.0.1
Development version indicator examples: 1.0, 1.1.0, 1.2.2.0
(Is also a pre-release but the preferred way is to use it only as an in
development indicator.)


Introduction
------------

The idea is base on Semantic Versioning and provides another solution to
handle versions in software projects and libraries.
It provides a simpler way to handle versioning and also a way with more
options to version schemes. It shows the right way and advice to the preferred
solution.

I call this system "Simple Versioning." Under this scheme, version numbers
and the way they change convey meaning about the underlying code and what has
been modified from one version to the next.


Simple Versioning Specification
-------------------------------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1. Software using Simple Versioning SHOULD declare a public API. This API
could be declared in the code itself or exist strictly in documentation.
However it is done, it SHOULD be precise and comprehensive.

2. A normal version number MUST take the form X.Y.Z where X, Y, and Z are
non-negative integers, and MUST NOT contain leading zeros. X is the
major version, Y is the minor version, and Z is the patch version.
Each element MUST increase numerically. For instance: 1.9.1 -> 1.10.1 -> 1.11.1.

3. Once a versioned package has been released, the contents of that version
MUST NOT be modified. Any modifications MUST be released as a new version.

4. Major version zero (0.y.z) is for initial development. Anything MAY change
at any time. The public API SHOULD NOT be considered stable. A minor version
zero (1.0.z) is for pre-releases of a major version. A patch version of zero
(1.1.0) is a development version, or simple a marker for the start of the next
development.

5. Version 1.1.1 defines the public API. The way in which the version number
is incremented after this release is dependent on this public API and how it
changes.

6. Patch version Z (x.y.Z) MUST be incremented if only backwards
compatible bug fixes are introduced. A bug fix is defined as an internal
change that fixes incorrect behavior.

7. Minor version Y (x.Y.z) MUST be incremented if new, backwards
compatible functionality is introduced to the public API. It MUST be
incremented if any public API functionality is marked as deprecated. It MAY be
incremented if substantial new functionality or improvements are introduced
within the private code. It MAY include patch level changes. Patch version
MUST be reset to 1 when minor version is incremented.

8. Major version X (X.y.z | X > 0) MUST be incremented if any backwards
incompatible changes are introduced to the public API. It MAY also include minor
and patch level changes. Patch and minor version MUST be reset to 1 when major
version is incremented.

9. A pre-release or development version is indicated by setting either one ore
more of major, minor or patch to zero (x.y.z | x = 0 | y = 0 | z = 0).
Ex.: 0.1.1, 1.0.1, 1.1.0, 1.1.0.12
A trailing zero should be used to mark a development versions.
For pre-releases normally the next to last version number is set to zero.

10. Precedence refers to how versions are compared to each other when ordered.
Precedence MUST be calculated by separating the version into parts, normally
major, minor, patch and additional build number.
For comparison the version is split up into a tuple and the number is converted
to a positive integer.
Precedence is determined by the first difference when
comparing each of these identifiers from left to right as follows: Major, minor,
patch and build versions are always compared numerically.
Example: 1.1.1 < 2.1.1 < 2.2.1 < 2.2.2.
If different version schemes are compared the missing part is not assumed to be
zero or one. They cannot compare equal and are compared part by part if the
parts are equal the longer version scheme wins.
Ex: 1.1 < 1.1.0, 1.1 != 1.1.0, 1.1 != 1.1.1

11. If you don't need or want the API guarantees and another versioning scheme
as the promoted default Major.Minor.Patch fits better to your solutions, you
can do that. As example if you want to do year based versions with counting
the release number in the year, do it so. (2017.1, 2017.2, ...)
But name it only simple versioning compatible if it mets the specifications
of the numbering and the following definition.


Backus–Naur Form Grammar for Simple Versions
--------------------------------------------

    <valid simple version> ::= <major>
		                     | <major> "." <minor>
		                     | <major> "." <minor> "." <patch>
		                     | <major> "." <minor> "." <patch> "." <build>

    <major> ::= <numeric identifier>

    <minor> ::= <numeric identifier>

    <patch> ::= <numeric identifier>

    <build> ::= <numeric identifier>

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
the complicated pre-release and build specifiers. Every part is simply a
number and a pre-release is indicated by setting one number to zero.
Simple to understand simple to detect and implement programatically.

For really simple projects it allows also to have simpler schemes and
omit parts. Also if someone wants to do date based releases it can be done
with this scheme.


FAQ
---

### How should I deal with revisions in the 0.y.z initial development phase?

The simplest thing to do is start your initial development release at 0.1.1
and then increment the minor version for each subsequent release.

### How do I know when to release 1.1.1?

If your software is being used in production, it should probably already be
1.1.1. If you have a stable API on which users have come to depend, you should
be 1.1.1. If you're worrying a lot about backwards compatibility, you should
probably already be 1.1.1.

### Doesn't this discourage rapid development and fast iteration?

Major version zero is all about rapid development. If you're changing the API
every day you should either still be in version 0.y.z or on a separate
development branch working on the next major version.

### If even the tiniest backwards incompatible changes to the public API require a major version bump, won't I end up at version 42.1.1 very rapidly?

This is a question of responsible development and foresight. Incompatible
changes should not be introduced lightly to software that has a lot of
dependent code. The cost that must be incurred to upgrade can be significant.
Having to bump major versions to release incompatible changes means you'll
think through the impact of your changes, and evaluate the cost/benefit ratio
involved.

### Does Simple Versioning have a size limit on the version string?

No, but use good judgment. A 255 character version string is probably overkill,
for example. Also, specific systems may impose their own limits on the size of
the string.


### Is there a difference between a pre-release and development version?

Not really, it is more a convention to never do a pre-release with a version
that ends with zero (1.0.0) instead use it only to mark internal development
and also count pre-release starting from 1 as last number.

### Is there a simple way to indicate a release version?

Yes a real simple one. Every number must be >0 to indicate a release.
For example if you split up the version string by "." convert every part to an
integer and every integer is bigger than zero.

In pseudo code:

version_tuple = split("1.1.1", ".")
is_release = all(version_tuple)
(zero integer is considered false other true)

A pre-release or development release is simply:
is_pre_release = not is_release

### I need to do pre-release for a patch version is this possible?

Yes, use the additional buld number to extend your version.
Something like 1.4.0.1 for your first pre-release to the final patch release of
1.4.1.

### Is it good practice to change version schemes often?

No, please decide a version scheme at start of your project and don't change it
then. So if you decide with a two digits version scheme like 25.1 and not do
patch release, stick with it.

### Are more version parts then four allowed?

No, version have up to four parts not more. A version 1.2.3.4.5 is not allowed.
This is simply to limit it in length. Keep in mind you can increment the numbers
to really high values if you want. So there is not really a limit in the amount
of versions.

### I am not comfortable to increase the length of parts for pre-releases?

If you don't want to change your version scheme to get the additional build
number for pre-releases of patches you must stick by doing only pre-releases
for a major version. Or have only one pre-release for a minor one.
In most cases this is enough if you release early and often and do small
minor releases with not to much new features.
You can also skip some numbers and to pre-release with 1.2.0, 1.3.0, 1.4.0
and a release with 1.4.1.


### I really want to have fancy pre-release or other build specifiers?

Hmm, this is about simple versioning avoiding this kind of stuff.
So please use another version scheme that solves your needs.
All this complicated specifiers are against the main goal of the this
spec. But please think some minutes about it, your users and everyone else
will be happy if you choose the simple to understand solution.


About
-----

The Simple Versioning specification is authored by Wolfgang Langner.
The main goal is to keep it simple also in implementation and for
version comparison.


License
-------

Creative Commons - CC BY 3.0
http://creativecommons.org/licenses/by/3.0/
