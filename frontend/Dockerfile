FROM node:20-alpine AS base

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install

FROM base AS development

COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

FROM base AS production

COPY . .

RUN npm install

RUN npm install -g serve

RUN npm run build

CMD [ "serve", "-s", "dist" ]

