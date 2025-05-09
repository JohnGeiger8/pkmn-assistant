# frontend/Dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build --prod

FROM nginx:stable-alpine
COPY --from=builder /app/dist/pkmn-assistant-ui /usr/share/nginx/html
