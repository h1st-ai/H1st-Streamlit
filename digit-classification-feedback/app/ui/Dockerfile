
FROM node:12.17.0-alpine3.11 AS builder
ARG REACT_APP_BACKEND_URL
WORKDIR /app

COPY package*.json ./
COPY . .
RUN yarn
RUN yarn build

FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/build /usr/share/nginx/html
COPY --from=builder /app/build /usr/share/nginx/html/app

