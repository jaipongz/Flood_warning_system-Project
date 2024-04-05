FROM node:alpine
#get baseImage

WORKDIR /code

COPY . /code/

RUN npm install

EXPOSE 8000

CMD [ "npm", "start"]