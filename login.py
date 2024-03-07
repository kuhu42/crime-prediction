<!-- myapp/templates/myapp/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>
<style>
body {
margin: 0;
padding: 0;
font-family: 'Arial', sans-serif;
background-color: #34495E ; /* Set your background color here */
display: flex;
align-items: center;
justify-content: center;
height: 100vh;
}
.login-container {
background-color: #ffffff;
padding: 30px;
border-radius: 8px;
box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
text-align: center;
animation: fadeInUp 0.8s ease-in-out;
}
h2 {
color: #333333;
font-size: 24px;
margin-bottom: 20px;
}
label {
display: block;
margin-top: 15px;
font-size: 16px;
color: #555555;
}
input {
width: 100%;
padding: 12px;
margin-top: 8px;
margin-bottom: 20px;
border: 1px solid #cccccc;
border-radius: 4px;
box-sizing: border-box;
font-size: 16px;
}
input[type="submit"] {
background-color: #5D6D7E ;
color: white;
cursor: pointer;
font-size: 18px;
}
input[type="submit"]:hover {
background-color: #45a049;
}
@keyframes fadeInUp {
0% {
opacity: 0;
transform: translateY(20px);
}
100% {
opacity: 1;
transform: translateY(0);
}
}
</style>
</head>
<body>
<div class="login-container">
<h2>Welcome Back!</h2>
{% if error %}
<p style="color: red;">{{ error }}</p>
{% endif %}
<form action="{% url 'login' %}" method="post">
{% csrf_token %}
<label for="username">Username:</label>
<input type="text" id="username" name="username" required>
<label for="password">Password:</label>
<input type="password" id="password" name="password" required>
<input type="submit" value="Login">
</form>
</div>
</body>
</html>
