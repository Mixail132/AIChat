FROM node:16-alpine AS local_build

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

CMD ["npm", "start"]

FROM nginx:alpine

#COPY --from=local_build /app/build /usr/share/nginx/html
#COPY --from=local_build /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css
COPY script.js /usr/share/nginx/html/script.js

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
