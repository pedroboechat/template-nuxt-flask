FROM node:16-bullseye

COPY package.json /usr

WORKDIR /usr

ENV PATH /usr/node_modules/.bin:$PATH

RUN npm install

COPY . /usr/app

WORKDIR /usr/app