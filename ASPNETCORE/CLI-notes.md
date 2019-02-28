# Resources
https://www.nuget.org/packages/dotnet-aspnet-codegenerator/
https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools

https://stackoverflow.com/questions/41450148/no-executables-found-matching-command-dotnet-aspnet-codegenerator

https://mattmillican.com/blog/aspnetcore-controller-scaffolding

adminer:
https://stackoverflow.com/questions/50097032/docker-compose-the-server-requested-authentication-method-unknown-to-the-clien

~/.zshrc

## Build and watch

```bash
export ASPNETCORE_Environment=Development
dotnet build
dotnet watch run

cd ClientApp
npm start 
```

## Compile and release
```
dotnet build "TodoList.csproj" -c Release -o ${PWD}/ap
dotnet publish "TodoList.csproj" -c Release -o ${PWD}/apptemp
cd apptemp
export ASPNETCORE_ENVIRONMENT=Production
dotnet TodoList.dll

export ASPNETCORE_ENVIRONMENT=Development
```

# Scaffolding

## New Api controlle from DbContext
To create a web api controller
```bash
dotnet aspnet-codegenerator --project . controller -api -name FooController -m Value -dc ValueContext
```

To create a razor scaffold with controller + pages
```bash
dotnet aspnet-codegenerator --project . controller -name HelloController -m Value -dc ValueContext
```
Or
```bash
dotnet aspnet-codegenerator --project . \
controller \
-api \
-name ValuesController \
-m Value \
-dc ValueContext \
-namespace PuppyBook.Controllers \
-outDir Controllers
```

## New React app
```
dotnet new react -n PuppyBook -o PuppyBook
```

## EF Core 

Migrations
```
dotnet ef migrations add InitialCreate
dotnet ef database update InitialCreate
```

## Azure

vm cli quickstart -
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-vm

https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?WT.mc_id=UI_empg

3:50
https://azure.microsoft.com/en-us/blog/low-priority-scale-sets/
https://azure.microsoft.com/en-us/pricing/calculator/#virtual-machines66ca9fa6-db99-4c3b-9813-906b0309f960
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/docker-machine

https://docs.microsoft.com/en-us/azure/virtual-machines/linux/docker-compose-quickstart
```
brew install azure-cli
az login

az vm create -n MyLinuxVM -g MyResourceGroup --image UbuntuLTS


sub=$(az account show --query "id" -o tsv)
docker-machine create -d azure \
    --azure-subscription-id $sub \
    --azure-ssh-user azureuser \
    --azure-open-port 80 \
    --azure-size "Standard_A1_v2" \
    myvm

```

## Azure CLI - make VM
```
az login
az account list --output table --all
az account set --subscription 8d9d6a48-8e68-445b-bf45-279dabb23bcb

az group create --name myResourceGroupVM --location eastus

"Standard_DS2_v2"

sub=$(az account show --query "id" -o tsv)

docker-machine create -d azure \
    --azure-subscription-id $sub \
    --azure-location "eastus" \
    --azure-ssh-user azureuser \
    --azure-open-port 80 \
    --azure-resource-group "again6" \
    --azure-size "Standard_B1s" \
    again6
    
deval myvm
dma ls
dma ip myvm
docker run -d -p 80:80 --restart=always nginx

d stop <containerid>

dc ps

docker run --name some-mysql \
-e MYSQL_ROOT_PASSWORD=my-secret-pw \
-e MYSQL_DATABASE=exampledb \
-e MYSQL_USER=user \
-e MYSQL_PASSWORD=pass \
-d mysql \
cmd --default-authentication-plugin=mysql_native_password


d run --name some-wordpress \
-p 80:80 \
-e WORDPRESS_DB_PASSWORD=my-secret-pw \ 
-e WORDPRESS_DB_USER=user
--link some-mysql:mysql \
-d wordpress 


```

# mysql + adminer
```yaml
version: '3.1'

services:

  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
       MYSQL_ROOT_PASSWORD: 'pass'
       MYSQL_DATABASE: 'db'
       MYSQL_USER: 'user'
       MYSQL_PASSWORD: 'pass'

  adminer:
    image: adminer
    depends_on:
      - db
    restart: always
    ports:
      - 8888:8080% 
```

## wordpress + adminer + mysql
```yaml
# Use root/example as user/password credentials

version: '3.1'

services:
  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
       MYSQL_ROOT_PASSWORD: 'pass'
       MYSQL_DATABASE: 'db'
       MYSQL_USER: 'user'
       MYSQL_PASSWORD: 'pass'
  wordpress:
    image: wordpress
    ports:
      - 9000:80
    links:
      - db:mysql
    depends_on:
      - db
    restart: always
    environment:
      WORDPRESS_DB_PASSWORD: 'pass' 
      WORDPRESS_DB_USER: 'user'
      WORDPRESS_DB_NAME: 'db'

  adminer:
    image: adminer
    depends_on:
      - db
    restart: always
    ports:
      - 8888:8080
```

## Azure VMs
```
The sizes available in the current region are: Standard_B1ms,Standard_B1s,Standard_B2ms,Standard_B2s,Standard_B4ms,Standard_B8ms,Standard_DS1_v2,Standard_DS2_v2,Standard_DS3_v2,Standard_DS4_v2,Standard_DS5_v2,Standard_DS11-1_v2,Standard_DS11_v2,Standard_DS12-1_v2,Standard_DS12-2_v2,Standard_DS12_v2,Standard_DS13-2_v2,Standard_DS13-4_v2,Standard_DS13_v2,Standard_DS14-4_v2,Standard_DS14-8_v2,Standard_DS14_v2,Standard_DS15_v2,Standard_DS2_v2_Promo,Standard_DS3_
```

# SSH
```bash
ssh-keygen -t rsa

# to remote
scp mylocalfile.txt myuser@mysite.com:~/mylocalfile.txt
# from remote
scp myuser@mysite.com:~/myremotefile.txt myremotefile.txt

# remove stale key from known_host
ssh-keygen -R <ip address>

# port forwarding via ssh
# do this from remote server
ssh -N -R 5901:localhost:5901 ME # where ME is your home address

ssh -i myprivatekey.pem root@1.2.3.4
```

Using the .ssh config files (~/.ssh/config)
--------------------------
1. Generate public & private ssh keys:
          `ssh-keygen -t rsa`
    Type in a name which will be put in `~/.ssh` directory

2. To bypass password prompt, you should add the `foo.pub` file to the `authorized_keys` file on the
server's `~/.ssh` directory. You can do a pipe via ssh:
    
    `cat mykey.pub | ssh myuser@mysite.com -p 123 'cat >> .ssh/authorized_keys' `

3. Add the publickey name to the `~/.ssh/config` file like this:

        Host bitbucket.org
          IdentityFile ~/.ssh/myprivatekeyfile # the leading spaces are important!
          Port 123

4. Verify and then SSH into the remote server. To check if your config is right type: `ssh -T git@github.com`
      
        ssh root@mysite.com
        or
        ssh mysite.com # if you setup the User setting in config

# Find and delete node_modules directory
```
find . -name 'node_modules' -type d -prune -exec rm -rf '{}' + 
```