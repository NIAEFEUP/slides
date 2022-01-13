FROM node:16-bullseye-slim 

WORKDIR /HateCss/website/
COPY src/ ./src/
COPY public/ ./public/
COPY package.json ./ 
RUN npm install  

EXPOSE 3000
CMD ["npm", "start"]

# to run 
# docker run -p 3000:3000 -v (pwd)/src/:/HateCss/website/src/ docker-workshop
