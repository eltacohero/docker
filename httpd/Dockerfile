FROM centos:latest

RUN yum update -y && yum install httpd -y
RUN /usr/sbin/httpd

WORKDIR /shared
