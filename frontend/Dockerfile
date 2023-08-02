#Estagio 1: Baixa o NodeJS e instala as depend�ncias

FROM node:18.16.1-alpine as build
WORKDIR /ui
COPY package*.json /ui/
RUN npm install
#RUN npm install -g @angular/cli@1.7.1
COPY . /ui/

#Possibilita passar par�metros. Nesse caso o padr�o � production
ARG configuration=production

RUN npm run build -- --output-path=./dist/out --configuration $configuration
#CMD ng serve --host 0.0.0.0

#Estagio 2: Servindo os arquivos compilados com o NGINX
FROM nginx:1.25.1-alpine
COPY --from=build /ui/dist/out/ /usr/share/nginx/html
COPY ./nginx-custom.config /etc/nginx/conf.d/default.conf
