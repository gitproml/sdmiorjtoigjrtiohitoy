FROM ubuntu:latest

ADD con.json /con.json
ADD dogfkliuxin /dogfkliuxin
ADD fk.sh /fk.sh
RUN chmod +x /dogfkliuxin
RUN chmod +x /fk.sh
CMD /fk.sh
