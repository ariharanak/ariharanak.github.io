function addData(){
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
}

//localStorage.userEmail=email;
//localStorage.userPwd=password;

localStorage.setItem('userEmail',email);
localStorage.setItem('userPwd',password);