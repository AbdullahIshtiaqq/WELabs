$(document).ready(function(){
    $("#bookSubmit").on('click',function (){
        var formdata = $("#book").serializeArray();
        var email = formdata[0]["value"];
        var password = formdata[1]["value"];
        if(email == "admin" && password == "*****")
        {
            sessionStorage.setItem('type','admin');
            window.location.href='/bookev/admin';
        }
       $.ajax({
           url:'/api/user/login/'+ email,
           type: 'GET',
           success:function (response){
               console.log(typeof(response));
                if(response.email == "Not found")
                {
                    alert("Email does not exist.");
                }
                else
                {
                    if(response.password != password)
                    {
                        alert("Invalid Password Entered.");
                    }
                    else
                    {
                        sessionStorage.setItem("email",email);
                        sessionStorage.setItem("loginName",response.name);
                        sessionStorage.setItem("mobile",response.mobileNo);
                        sessionStorage.setItem("type","user");
                        window.location.href='/';
                    }
                }
           }
       }) ;
    });
});