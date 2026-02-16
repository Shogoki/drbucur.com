FROM nginx:1.19.9
COPY ./output /usr/share/nginx/html
EXPOSE 80
