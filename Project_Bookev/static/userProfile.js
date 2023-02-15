        $(document).ready(function (){
            if(!sessionStorage.getItem('email'))
        {
            alert("You need to login to access this page.");
            window.location.href='/';
        }
            if(sessionStorage.getItem('email'))
            {
                $("#withoutLogin").hide();
            }
            else {
                $("#withLogin").hide();
            }
            $("#logout").on('click',function(){
                sessionStorage.clear();
                window.location.href='/';
            });

    });

        $(document.body).ready(function (e) {
                 $.ajax({type:"GET",
                     url:"/api/booking",
                     success: function(result){
                         myData = []
                         $(result).each(function (index,obj) {
                             if (obj.userMail == sessionStorage.getItem('email')) {
                                 myData.push(obj);
                             }
                         });
                         if(myData !=null || myData !=""){
                            table = $('#show').DataTable( {
                                data: myData ,destroy: true,
                                columns: [
                                    { data: 'serviceMail' },
                                    { data: 'date' },
                                    { data: 'charges' },




                                ]
                            } );
                        }

                  }});
                    $("#submit").on('click',function(){
            console.log("here");
            var formdata = $("#book").serializeArray();
            var data = {};
            var flag = false, msg="";
            $(formdata).each(function(index,obj){
                if(obj.value == "")
                {
                    flag = true;
                    msg = "All fields must be filled";
                }
                data[obj.name] = obj.value;
            });

            if(flag)
            {
                alert(msg);
                return;
            }

            $.ajax({
               url: '/api/service/login/'+data["serviceMail"],
               type: 'GET',
               success : function(response) {
                   if (response.email == 'Not found') {
                       flag = true;
                       msg = "Invalid email entered.";
                   }

               }
            });

            if(flag)
            {
                alert(msg);
                return;
            }
            data['userMail'] = sessionStorage.getItem('email');
            data = JSON.stringify(data);
            $.ajax({
                url: '/api/booking',
                type:'POST',
                data: data,
                success: function(){
                    alert("Feedback added!")
            }
            });
        });
        });



        $(document.body).ready(function (e) {
           $("#name").text(sessionStorage.getItem('loginName'));
            $("#email").text(sessionStorage.getItem('email'));
            $("#mobile").text(sessionStorage.getItem('mobile'));

            $("#submit").on('click',function(){

            var formdata = $("#book").serializeArray();
            var data = {};
            var flag = false, msg="";
            $(formdata).each(function(index,obj){
                if(obj.value == "")
                {
                    flag = true;
                    msg = "All fields must be filled";
                }
                data[obj.name] = obj.value;
            });

            if(flag)
            {
                alert(msg);
                return;
            }

            $.ajax({
               url: '/api/service/login/'+data["serviceMail"],
               type: 'GET',
               success : function(response) {
                    if (response['email'] != "Not found") {
                        data['userMail'] = sessionStorage.getItem('email');
            data = JSON.stringify(data);
            console.log(data);
            $.ajax({
                url: '/api/review',
                type:'POST',
                data: data,
                dataType : 'json',
                    contentType: "application/json; charset=utf-8",
                success: function(){
                    alert("Feedback added!")
                    window.location.href='/bookev/myProfile';
            }
            });
                   }
                    else
                        alert("Invalid Email entered.");

               }
            });
        });
        });

