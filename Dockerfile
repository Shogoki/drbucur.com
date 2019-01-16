FROM nginx
COPY ./output /usr/share/nginx/html
EXPOSE 80
