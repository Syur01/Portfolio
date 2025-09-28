FROM node:20-alpine

WORKDIR /home/app

COPY . .

RUN npm install
RUN npm install -g @angular/cli@19

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0"]
