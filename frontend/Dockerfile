FROM node:20-alpine AS base

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install

FROM base AS development

COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

