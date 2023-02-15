 $(document).ready(function (){
             var type = $("select option:selected").text()
            if (type == "Photographer") {
                $('#photography').show();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").hide();
            } else if (type == "Chef") {
                $('#photography').hide();
                $("#chef").show();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").hide();

            } else if (type == "Dressing Designer") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").show();
                $("#theme_decorator").hide();
                $("#venue").hide();

            } else if (type == "Theme Decorator") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").show();
                $("#venue").hide();

            } else if (type == "Venue") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").show();
            }

            $("select").change( function() {
             var type = $("select option:selected").text()
            if (type == "Photographer") {
                $('#photography').show();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").hide();
            } else if (type == "Chef") {
                $('#photography').hide();
                $("#chef").show();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").hide();

            } else if (type == "Dressing Designer") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").show();
                $("#theme_decorator").hide();
                $("#venue").hide();

            } else if (type == "Theme Decorator") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").show();
                $("#venue").hide();

            } else if (type == "Venue") {
                $('#photography').hide();
                $("#chef").hide();
                $("#dressing_designer").hide();
                $("#theme_decorator").hide();
                $("#venue").show();
            }
        } );

            function isNumber(value)
            {
               return (value.charCodeAt(0) >= 48 && value.charCodeAt(0) <= 57);
            }
            function validateEmail(email)
            {
                return email.match(/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
            };
            function validateURL(urlString){
	  	var urlPattern = new RegExp('^(https?:\\/\\/)?'+ // validate protocol
	    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // validate domain name
	    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // validate OR ip (v4) address
	    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // validate port and path
	    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // validate query string
	    '(\\#[-a-z\\d_]*)?$','i'); // validate fragment locator
	  return !!urlPattern.test(urlString);
	}

                $("#submit").on('click', function(){

                var formdata = $("#book").serializeArray();
                var data = {};
                var flag = false;
                var msg=""
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

                var selectedOption = $("#book select").val();
                var start, end,url;
                if(selectedOption == "Photographer")
                {
                    start = 7;
                    end = 10;
                    url = '/api/photographer';
                }
                else if(selectedOption == "Chef")
                {
                    start = 10;
                    end = 13;
                    url = '/api/chef';
                }
                else if(selectedOption == "Dressing Designer")
                {
                    start = 13;
                    end = 17;
                    url = '/api/designer';
                }
                else if(selectedOption == "Theme Decorator")
                {
                    start = 17;
                    end = 20;
                    url = '/api/decorator';
                }
                else if(selectedOption == "Venue")
                {
                    start = 20;
                    end = 23;
                    url = '/api/venue';
                }
                 $(formdata.slice(start,end)).each(function(index, obj){
                     if(obj.value=="")
                    {
                        flag = true;
                        msg = "All fields must be filled.";
                    }
                    if(obj.name=="portfolio")
                    {
                        if(!validateURL(obj.value))
                        {
                            flag = true;
                            msg = "Please enter valid URL for portfolio.";
                        }
                    }
                    data[obj.name] = obj.value;
                });
                if(flag)
                {
                    alert(msg);
                    return;
                }

                var jsonData = JSON.stringify(data)
                $.ajax({
                   url: '/api/service/login/'+data['email'],
                   type: 'GET',
                   success: function (response)
                   {
                       if(response.email == 'Not found')
                       {
                             $.ajax({
                    url: url,
                    type : "POST",
                    data : jsonData,
                    dataType : 'json',
                    contentType: "application/json; charset=utf-8",
                    success : function(result) {
                        if(result['msg']=="Account Created")
                        {
                            sessionStorage.setItem('email',data["email"]);
                            sessionStorage.setItem('type','service');
                            sessionStorage.setItem("loginName",data["name"]);
                            sessionStorage.setItem("mobile",data["mobileNo"]);
                            window.location.href="/bookev/service/profile";
                        }
                        else {
                            alert(result['msg']);
                        }
                    },
                    error: function(xhr, resp, text) {
                        console.log("Operation failed.");
                    }
                })
                       }
                       else
                       {
                           alert("Email already registered.");
                       }
                   }
                });

            });

         });