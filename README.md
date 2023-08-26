# iCTF23

The 2023 iCTF is a challenge-based Capture The Flag competition focused on AI and Cybersecurity.
The iCTF has a set of challenges that cover the skillset range of both high-school and undergraduate students.
The infrastructure is composed of a registration system and of a gamebot, which is based on [CTFd](https://github.com/CTFd/).

# Registration

This competition only allows verified teams from educational institutions to participate.

The requirements are:
1. The team is associated with an existing high school or university/college. A valid URL for the educational institution must be provided.
2. The team must identify a teacher/professor/lecturer that supervises the team and who is responsible for the ethical behavior of the team. The team adivsor must have a valid email address and a page within the website of the corresponding educational institution. An email will be sent to the advisor for verification.
3. Teams can be only all high-school students or all undergraduate students (i.e., there cannot be a team that mixes the two types of student).

# Challenges

Challenges are of two kinds:
1. Self-contained: The challenge is composed of a bundle of data, which contains all the information necessary to extract the flag.
2. Interactive: The challenge provides some data (e.g., some code or a description), but the actual exploitation of the challenge requires connecting to a host at a specific port.

Examples of this challenges are in the repo under `challenges\localtest` and `challenges\remotetest`.
