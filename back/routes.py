from controllers.signin import Signin

client = {
    "signin":"/signin","view_func_signin":Signin.as_view("app_signin")
    "login":"/login","view_func_login":Login.as_view("app_login")
}