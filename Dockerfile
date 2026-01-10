FROM nginx:1.21
COPY ./output /usr/share/nginx/html
EXPOSE 80
