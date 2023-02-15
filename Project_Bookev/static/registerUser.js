    $(document).ready(function(){
        // click on button submit
        $("#submit").on('click', function(){
            // send ajax
            var formdata = $("#book").serializeArray();
            var data = {};

            function isNumber(value)
            {
               return (value.charCodeAt(0) >= 48 && value.charCodeAt(0) <= 57);
            }
            function validateEmail(email)
            {
                return email.match(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
            };
            var flag = false;
                var msg="";
            $(formdata.slice(0,5)).each(function(index, obj){
                if(obj.value=="")
                    {
                        flag = true;
                        msg = "All fields must be filled.";
                    }
                    if(obj.name == "cnic")
                    {
                        if(obj.value.length != 13) {
                            msg = "CNIC Length should be 13."
                            flag = true;
                        }
                        for(let i = 0; i < obj.value.length; i++)
                        {
                            if(!(isNumber(obj.value.charAt(i))))
                            {
                                msg="CNIC should contain only digits."
                                flag = true;
                            }
                        }
                    }
                    if(obj.name == "mobileNo")
                    {
                        for(let i = 0; i < obj.value.length; i++)
                        {
                            if(!(isNumber(obj.value.charAt(i))) && obj.value.charAt(i) != '+' && obj.value.charAt(i) != '-')
                            {
                                console.log(i);
                                msg="Invalid Mobile Number!"
                                flag = true;
                            }
                        }
                    }
                    if(obj.name == "email")
                    {
                        if(!validateEmail(obj.value))
                        {
                             msg="Invalid Email!"
                            flag = true;
                        }
                    }
                    if(obj.name == "password")
                    {
                        let capital=false, small = false, special = false, digit = false;
                        for(let i = 0; i < obj.value.length; i++)
                        {
                            if(obj.value.charCodeAt(i) >= '0'.charCodeAt(0) && obj.value.charCodeAt(i) <= '9'.charCodeAt(0))
                            {
                                digit = true;
                            }
                            else if(obj.value.charCodeAt(i) >= 'a'.charCodeAt(0) && obj.value.charCodeAt(i) <= 'z'.charCodeAt(0))
                            {
                                small = true;
                            }
                            else if(obj.value.charCodeAt(i) >= 'A'.charCodeAt(0) && obj.value.charCodeAt(i) <= 'Z'.charCodeAt(0))
                            {
                                capital = true;
                            }
                            else
                            {
                                special = true;
                            }
                        }
                        if(!capital || !small || !digit || !special)
                        {
                            msg = "Your password must contain atleast one uppercase alphabet, one lowercase alphabet, one digit and one special character.";
                            flag = true;
                        }
                    }
                data[obj.name] = obj.value;
            });
            $(formdata.slice(5,6)).each(function(index, obj) {
                    if(obj.value != data['password'])
                    {
                        msg="Password doesn't match.";
                        flag = true;
                    }
                });
            if(flag)
                {
                    alert(msg);
                    return;
                }
            var JSONdata =JSON.stringify(data)
            $.ajax({
                url: '/api/user', // url where to submit the request
                type : "POST", // type of action POST || GET
                data : JSONdata, // post data || get data
                dataType : 'json',
                contentType: "application/json; charset=utf-8",
                    success : function(result) {
                        if(result['msg']=="Account Created")
                        {
                            sessionStorage.setItem('email',data["email"]);
                            sessionStorage.setItem('loginName',data["name"]);
                            sessionStorage.setItem('mobile',data["mobileNo"]);
                            sessionStorage.setItem('type','user');
                            window.location.href="/";
                        }
                        else {
                            alert(result['msg']);
                        }
                    },
                    error: function(xhr, resp, text) {
                        console.log("Operation failed.");
                    }
            })

        });
    });