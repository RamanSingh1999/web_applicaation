# Use the Nginx image to serve the web application
FROM nginx:alpine

# Copy the static files to the Nginx web root
COPY . /usr/share/nginx/html

# Expose port 80 for the web server
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
