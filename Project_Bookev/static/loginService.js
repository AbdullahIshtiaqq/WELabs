$(document).ready(function(){
$("#bookSubmit").on('click',function (){
        var formdata = $("#book").serializeArray();
        var email = formdata[0]["value"];
       $.ajax({
           url:'/api/service/login/'+ email,
           type: 'GET',
           success:function (response){
               console.log(typeof(response));
                if(response.email == "Not found")
                {
                    alert("Email does not exist.");
                }
                else
                {
                    if(response.password != formdata[1]["value"])
                    {
                        alert("Invalid Password Entered.");
                    }
                    else
                    {
                        sessionStorage.setItem("email",email);
                        sessionStorage.setItem("type","service");
                        sessionStorage.setItem("loginName",response.name);
                        sessionStorage.setItem("mobile",response.mobileNo);
                        window.location.href='/bookev/service/profile';
                    }
                }
           }
       }) ;
    });
});