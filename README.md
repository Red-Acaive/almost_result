# BA-Backend

## Backend Configuration(Docker)
> docker pull mysql  
> docker network create os-dev  
> docker run --name mysql --network os-dev -e MYSQL_ROOT_PASSWORD=dev -d -p 3306:3306 mysql
> docker compose up -d --build

## Uninstallation
> docker compose down