Regular expressions
===================

Regular expressions support four things:
-> Identifiers
-> Modifiers
-> Whitespace characters
-> Flags

Identifiers
===========
Identifier      Description
\w              Matches alphanumeric characters, including underscore (_)
\W              Matches non-alphanumeric characters, excluding underscore (_)
\d              Matches a digit
\D              Matches a non-digit
\s              Matches a space
\S              Matches anything but a space
.               Matches a period (.)
\b              Matches any character except a new line

Modifiers
=========
Modifier        Description
^               Matches start of the string
$               Matches end of the string
?               Matches 0 or 1
*               Matches 0 or more
+               Matches 1 or more
|               Matches either or x/y
[ ]             Matches range
{x}             Amount of preceding code

Whitespace characters
=====================
Character       Description
\s              Space
\t              Tab
\n              New line
\e              Escape
\f              Form feed
\r              Return

Flags
=====
Flag            Description
re.IGNORECASE   Case-insensitive matching
re.DOTALL       Matches any character including new lines
re.MULTILINE    Multiline matching
Re.ASCII        Makes escape match only on ASCII characters
