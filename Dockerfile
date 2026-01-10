FROM nginx:1.21.6
COPY ./output /usr/share/nginx/html
EXPOSE 80
