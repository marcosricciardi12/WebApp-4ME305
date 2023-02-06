cd backend
./install.sh
./boot.sh &
cd ..
cd frontend/angular
npm install
ng build --configuration=production
docker run -d -p 8080:80 -v $PWD/dist/client:/usr/share/nginx/html nginx:alpine
cd ..
cd ..
