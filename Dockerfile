FROM node:18

WORKDIR /app

COPY package*.json ./

# Clear npm cache
RUN npm cache clean --force

# Install dependencies
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
