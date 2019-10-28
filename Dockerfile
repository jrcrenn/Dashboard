FROM node:10
RUN mkdir -p /app
WORKDIR /app
COPY package.json /app
RUN npm install
RUN npm audit fix
COPY . /app
EXPOSE 8080
CMD ["npm", "start"]