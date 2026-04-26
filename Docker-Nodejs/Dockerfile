# Use official Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json .

# Install dependencies (none here, but good practice)
RUN npm install

# Copy app code
COPY . .

# Expose port
EXPOSE 3000

# Start app
CMD ["node", "app.js"]