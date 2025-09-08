# Базовый слой
FROM node:20-alpine AS base
WORKDIR /app


# ==== DEV target (vite dev server) ====
FROM base AS dev
COPY package.json package-lock.json* ./
RUN npm ci
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


# ==== BUILD target (FE build) ====
FROM base AS build
COPY package.json package-lock.json* ./
RUN npm ci
COPY . .
RUN npm run build


# ==== PROD target (nginx) ====
FROM nginx:1.27-alpine AS prod
# конфиг с проксированием /api → backend:8000
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]