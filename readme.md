# API EvoCondo
### Desenvolvido em Django 
___
### Para rodar o Ambiente vitual e dependencias: 
###### Não Rodar no Pycharm(rodar na pasta raiz)

~~~
core\venv\Scripts\Activate
~~~

### Rodar Servidor
~~~
python manage.py runserver
~~~

## Auth
<details><summary>create new user</summary>
<p>

#### 
#### url: /auth/newuser/
~~~json
{
    "username": Str,
    "email": Str,
    "password": Str,
    "faceId": Int,
    "bithday": Date,
    "first_name": Str,
    "last_name": Str
}
~~~

</p>
</details>


<details><summary>change password</summary>
<p>

#### 
#### url: /auth/newpassword/
~~~json
{
    "username": Str,
    "password": Str,
}
~~~

</p>
</details>

<details><summary>Delete User</summary>
<p>

#### 
#### url: /auth/deleteuser/
~~~json
{
    "emploerNo": Int
}
~~~

</p>
</details>

<details><summary>Auth User</summary>
<p>

#### 
#### url: /auth/authuser/
~~~json
{
    "emploerNo": Int
}
~~~

</p>
</details>

<details><summary>isAuth User</summary>
<p>

#### 
#### url: /auth/authuser/
~~~json
{
    "emploerNo": Int
}
~~~

</p>
</details>

<details><summary>logOut User</summary>
<p>

#### 
#### url: /auth/authuser/
~~~json
{
    "emploerNo": Int
}
~~~

</p>
</details>
