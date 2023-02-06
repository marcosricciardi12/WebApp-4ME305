cd backend
./install.sh
./boot.sh &
cd ..
cd frontend/angular
npm install
ng build --configuration=production
cd ..
cd ..
docker run -d -p 8080:80 -v $PWD/dist/client:/usr/share/nginx/html nginx:alpine
