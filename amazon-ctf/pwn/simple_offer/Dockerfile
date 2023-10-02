FROM --platform=linux/amd64 ubuntu:23.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt install libc6

RUN useradd -ms /bin/sh bof
WORKDIR /home/bof

COPY ./bof ./
COPY ./flag.txt ./

RUN chown -R root:bof /home/bof && \
    chmod 750 /home/bof && \
    chmod 550 /home/bof/bof && \
    chown root:bof /home/bof/flag.txt && \
    chmod 440 /home/bof/flag.txt

EXPOSE 1234

CMD ["socat", "-T60", "TCP-LISTEN:1234,reuseaddr,fork,su=bof","EXEC:/home/bof/bof"]
