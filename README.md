# iCTF23

The 2023 iCTF is a challenge-based Capture The Flag competition focused on AI and Cybersecurity.

The iCTF has a set of challenges with a wide variety of difficulty, and targets both high-school and undergraduate students.

The infrastructure is hosted by [CTFd](https://CTFd.io).

# Registration

Registration is performed through a Google form.
The competition only allows verified teams from educational institutions to participate.

The requirements are:
1. The team must be associated with an existing high school or university/college. A valid URL for the educational institution must be provided.
2. The team must identify a teacher/professor/lecturer who supervises the team. The team advisor is responsible for the ethical behavior of the team. The team adivsor must have a valid email address and a page within the website of the corresponding educational institution. An email will be sent to the advisor for verification.
3. Teams can be only all high-school students or all undergraduate students (i.e., there cannot be a team that mixes the two types of student).

# Challenges

Challenges are of two kinds:
1. Self-contained: The challenge is composed of a bundle of data, which contains all the information necessary to extract the flag.
2. Interactive, single component: The challenge provides some data (e.g., some code or a description), but the actual exploitation of the challenge requires connecting to a host at a specific port.
3. Interactive, multiple components: The challenge requires interaction with a complex system (e.g., a web server backed by a SQL database).

Examples of this challenges are in the repo under `challenges/samplelocal`, `challenges/sampleremote`, and `challenges/sampleweb`.
