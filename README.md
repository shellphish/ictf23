# iCTF 23

The 2023 iCTF is an educational challenge-based Capture The Flag competition focused on AI and Cybersecurity.
The 2023 iCTF is sponsored by the [NSF AI ACTION Institute](https://action.ucsb.edu), and it is organized by the Women in Computer Science (WiCS) at UCSB together with [Shellphish](http://www.shellphish.net).

The 2023 iCTF has two tracks, one for high school students and one for undergraudate students, hosted on different servers.
Each track has a set of challenges with a wide variety of difficulty.

Please see [ictf.cs.ucsb.edu](https://ictf.cs.ucsb.edu) for rules and registration procedures.
The infrastructure is hosted by [CTFd](https://CTFd.io).

## Challenges

Challenges are of two kinds:
1. Self-contained: The challenge is composed of a bundle of data, which contains all the information necessary to extract the flag.
2. Interactive, single component: The challenge provides some data (e.g., some code or a description pf the challenge), but the actual exploitation of the challenge requires connecting to a host at a specific port. The service is hosted in a docker container.
3. Interactive, multiple components: The challenge requires interaction with a complex system (e.g., a web server backed by a SQL database). The service is implemented as a composition of docker containers. Note: This format should be chosen only if strictly necessary, as the CTFd hosting system does not support multi-container deployments, and, therefore, challenges of this kind need to be deployed on a separate host, increasing the complexity of the infrastructure.

Examples of this challenges are in the repo under `challenges/samplelocal`, `challenges/sampleremote`, and `challenges/sampleweb`, respectively.

For any questions about challenge development please contact the administrators at [ictf-admin@googlegroups.com](mailto:ictf-admin@googlegroups.com).
