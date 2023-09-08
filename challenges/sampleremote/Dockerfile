FROM gcc

RUN apt-get update -y \
    && apt-get install --no-install-recommends -y xinetd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY ./src/flag.txt /flag.txt
RUN chmod 644 /flag.txt

RUN useradd -u 31337 -ms /bin/bash challenge
# Prevents the user from writing to the home directory
RUN chown root:root /home/challenge
RUN chmod 755 /home/challenge

# Source files
COPY src /home/challenge/src
# Read-only files
COPY ro /home/challenge/ro
# Writeable files
COPY rw /home/challenge/rw
RUN chown challenge:challenge /home/challenge/rw
RUN chmod 755 /home/challenge/rw

# Creates the application
COPY Makefile /home/challenge/Makefile
WORKDIR /home/challenge
RUN make

# Install the service
RUN mv /home/challenge/src/xinetd.conf /etc/xinetd.d/sampleremote

# The port this leaves on
EXPOSE 7631
CMD ["/usr/sbin/xinetd", "-dontfork"]
