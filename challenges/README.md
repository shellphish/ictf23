# Challenges
The challenges of this class follow the specification of the CTFd challenges, and are meant to be deployed using `ctfcli`.
See: https://docs.ctfd.io/docs/management/ctfcli/challenges/

## Sample Challenges

### `samplelocal`

This challenge is representative of a data-only service, in which a user has to download a file, which contains the flag (usually well-hidden).
This challenge does not use any containers.

### `sampleremote`

This challenge is representative of a remote access service, in which a user has to connect to a host and exploit a service to obtain the flag.
This challenge uses a single container.

### `sampleweb`

This challenge is representative of a web-based service, in which a user has to interact with a web application to obtain the flag.
This challenge uses multiple containers.
